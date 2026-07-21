import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, Polygon
import matplotlib.patheffects as path_effects
import numpy as np
from padeopsIO import turbine
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# Set matplotlib to use proper font rendering
plt.rcParams['mathtext.fontset'] = 'dejavusans'

# ============================================================================
# CONFIGURATION
# ============================================================================
SIM_CONFIGS = [
    # CTP = 2
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_2/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="10%", TI="3%",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_2/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="20%", TI="3%",  marker="o"),

    # CTP = 4
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_4/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="10%", TI="3%",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_4/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="20%", TI="3%",  marker="o"),

    # CTP = 6
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_6/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="10%", TI="3%",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_6/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="20%", TI="3%",  marker="o"),

    # CTP = 8
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_8/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="10%", TI="3%",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_8/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="20%", TI="3%",  marker="o"),

    # CTP = 10
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_10/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=10, blockage="10%", TI="3%",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Filter/CTP_10/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=10, blockage="20%", TI="3%",  marker="o"),
]

# Bin-averaging factor for time series plots (decimation). Averages every
# BIN_SIZE consecutive raw points into one plotted point, to cut down the
# number of points drawn and make line style / markers distinguishable.
BIN_SIZE = 150

# Smaller bin size for the by-CTP subplot version to show more detail
BIN_SIZE_BY_CTP = 50
X_KE_FLUX = 5.0
# Window size for computing rolling standard deviation (in raw samples)
# Set to None to disable rolling std, or set to a value like 50-200
ROLLING_STD_WINDOW = 100

# Linestyle by TI level, used in the COMBINED (all-sims) plot, where marker
# encodes CTP and linestyle encodes TI.
TI_LINESTYLES = {
    "3%":  "solid",
    "8%":  "dashed",
    "12%": "dotted",
}

# Marker by TI level, used in the BY-CTP subplot plots. Each subplot only
# contains one CTP value, so a CTP-based marker would be identical across
# every line in that panel and add no information. Marker instead encodes
# TI there (color still encodes blockage, linestyle stays solid for all).
TI_MARKERS = {
    "3%":  "o",
    "8%":  "s",
    "12%": "^",
}

# Maps a time-series key to its precomputed time-averaged scalar key, so we
# can draw a horizontal reference line showing the converged mean on top of
# each raw/binned time series.
SERIES_MEAN_KEY = {
    "a_series": "a_mean",
    "cp_series": "cp",
    "ct_series": "ct",
}

LES_DATA_PATH = "0turb_les.csv"
UBM_DATA_PATH = "UBM_Model.csv"
# Maps a scalar plot's `key` to the matching column name in each reference dataset
LES_KEY_MAP = {"cp": "cp", "ct": "ct", "a_mean": "a", "cp_direct": "cp", "ct_direct": "ct"}
UBM_KEY_MAP = {"cp": "Cp", "ct": "Ct", "a_mean": "an", "cp_direct": "Cp", "ct_direct": "Ct"}

# ============================================================================
# MAGMA COLORMAP - blockage-based colors
# ============================================================================
def get_blockage_colors():
    """Return a dict mapping blockage percentages to pink and darker orange colors."""
    return {
        "10%": "#9B4F7F",      # Pink/purple
        "20%": "#D97706",      # Darker orange
    }

BLOCKAGE_COLORMAP = get_blockage_colors()

# ============================================================================
# HELPERS — internal / computation
# ============================================================================

def load_sim(cfg):
    """Load empty and turbine BudgetIO objects for one config."""
    sim_e = pio.BudgetIO(cfg["path"], padeops=True, runid=cfg["runid_e"])
    sim_t = pio.BudgetIO(cfg["path"], padeops=True, runid=cfg["runid_t"],
                         normalize_origin="turbine")
    return sim_e, sim_t


def get_uinf(sim_t):
    """Inflow velocity: scalar mean over the upstream (x = -5D) hub-height slice."""
    return float(sim_t.slice(field_terms=["u"], xlim=-5, zlim=0)["u"].mean())

def compute_ke_flux_empty(sim_e, x_target=X_KE_FLUX):
    """
    Advective kinetic energy flux through a y-z plane at x=x_target in the
    EMPTY domain (no turbine), using time-averaged budget fields (ubar,
    vbar, wbar) rather than instantaneous snapshots.

    Returns
    -------
    ke_flux_density : float, mean KE flux per unit area at x_target [vel^3]
    ke_flux_total   : float, KE flux integrated over the y-z plane [vel^3 * area]
    """
    view = sim_e.slice(budget_terms=["ubar", "vbar", "wbar"], xlim=x_target)
    ubar = np.asarray(view["ubar"], dtype=np.float64)
    vbar = np.asarray(view["vbar"], dtype=np.float64)
    wbar = np.asarray(view["wbar"], dtype=np.float64)

    ke_flux_field = 0.5 * (ubar * ubar + vbar * vbar + wbar * wbar) * ubar
    ke_flux_density = float(np.mean(ke_flux_field))

    y = np.asarray(sim_e.y, dtype=np.float64)
    z = np.asarray(sim_e.z, dtype=np.float64)
    dy = float(y[1] - y[0])
    dz = float(z[1] - z[0])
    ke_flux_total = float(np.sum(ke_flux_field) * dy * dz)

    return ke_flux_density, ke_flux_total
def compute_cp_ct_timeseries(sim_t):
    """
    Compute time series and time-averaged Cp, Ct, and induction factor for one simulation.
    ...
    Returns
    -------
    cp, ct : scalar floats (time-averaged from second half only)
    a_series, cp_series, ct_series : numpy arrays (second half of all data)
    uinf : scalar float (inflow velocity)
    ud_mean : scalar float (time-averaged disk velocity, second half only)
    """
    uinf = get_uinf(sim_t)
    ud = np.asarray(sim_t.read_turb_uvel("all", steady=False))
    ctp = float(sim_t.ta[0].ct)
    print(ctp)

    # Take only the second half of all data
    n = len(ud)
    second_half_idx = n // 2
    ud = ud[second_half_idx:]

    # Compute time series
    a_series = 1.0 - (ud / uinf)
    cp_series = ctp * ((1.0 - a_series) ** 3)
    ct_series = ctp * ((1.0 - a_series) ** 2)

    # Compute time-averaged scalars
    cp = float(np.mean(cp_series))
    ct = float(np.mean(ct_series))
    ud_mean = float(np.mean(ud))

    return cp, ct, a_series, cp_series, ct_series, uinf, ud_mean
def compute_thrust_power_timeseries(sim_t):
    """
    Compute time series and time-averaged thrust coefficient (Ct) and power
    coefficient (Cp) DIRECTLY from disk velocity and turbine power output —
    independent of the induction-factor (a) formulation used elsewhere.

    Thrust = 2*(pi/4)*ud*(uinf - ud)
    Ct     = Thrust / (0.5*(pi/4)*uinf^2)
    Cp     = Power  / (0.5*(pi/4)*uinf^3)

    Returns
    -------
    ct_direct, cp_direct : scalar floats (time-averaged, second half only)
    thrust_series, ct_direct_series, power_series, cp_direct_series : numpy arrays (second half)
    """
    uinf = get_uinf(sim_t)
    ud = np.asarray(sim_t.read_turb_uvel("all", steady=False))
    power = np.asarray(sim_t.read_turb_power("all", turb=1, steady=False))

    # Guard against slightly mismatched sample counts between the two reads
    n = min(len(ud), len(power))
    ud = ud[:n]
    power = power[:n]

    second_half_idx = n // 2
    ud = ud[second_half_idx:]
    power = power[second_half_idx:]

    rotor_area = np.pi / 4.0  # D = 1

    thrust_series = 2.0 * rotor_area * ud * (uinf - ud)
    ct_direct_series = thrust_series / (0.5 * rotor_area * uinf ** 2)
    power_series = power
    cp_direct_series = power_series / (0.5 * rotor_area * uinf ** 3)

    ct_direct = float(np.mean(ct_direct_series))
    cp_direct = float(np.mean(cp_direct_series))

    return ct_direct, cp_direct, thrust_series, ct_direct_series, power_series, cp_direct_series

def compute_rolling_std(series, window):
    """
    Compute rolling standard deviation of a series.

    Parameters
    ----------
    series : numpy array
        Input time series
    window : int
        Window size for rolling computation

    Returns
    -------
    numpy array
        Rolling std dev (same length as input, padded with NaN at edges)
    """
    if window is None or window <= 1:
        return np.zeros_like(series)

    std_series = np.full_like(series, np.nan, dtype=float)
    half_window = window // 2

    for i in range(len(series)):
        start = max(0, i - half_window)
        end = min(len(series), i + half_window + 1)
        std_series[i] = np.std(series[start:end])

    return std_series


def compute_global_y_extent(results, D=1.0):
    """Return (y_min, y_max) in x/D units of the widest domain across all sims."""
    y_min_global = np.inf
    y_max_global = -np.inf
    for r in results:
        view = r["sim_t"].slice(field_terms=["u"], zlim=0)
        u_data = view["u"]
        y = np.array(u_data.y) / D if hasattr(u_data, 'y') else np.arange(u_data.shape[0]) / D
        y_min_global = min(y_min_global, y.min())
        y_max_global = max(y_max_global, y.max())
    return y_min_global, y_max_global

def compute_classical_line(key):
    """
    Classical actuator-disk momentum theory using a fixed a_line range.
    Limited so that Ctp does not exceed 10.

    Ct  = 4a(1-a)
    Cp  = 4a(1-a)^2
    a   = a
    Ctp = 4a/(1-a)   (blockage-independent, so there's only ever one line)

    The "_direct" keys (ct_direct, cp_direct) are computed via a different
    method (from ud/power rather than induction factor) but should
    theoretically collapse onto the same classical curve, so they're mapped
    to their base key here.
    """
    key_map = {"ct_direct": "ct", "cp_direct": "cp"}  # NEW
    key = key_map.get(key, key)                        # NEW

    # Solve for a when ctp = 10: 10 = 4a/(1-a) => a = 10/14 ≈ 0.714
    a_max = 10.0 / 14.0  # This gives ctp_line = 10
    a_line = np.linspace(0, a_max, 100)
    ctp_line = 4 * a_line / (1 - a_line)

    # Ensure ctp_line doesn't exceed 10 due to numerical precision
    ctp_line = np.minimum(ctp_line, 10.0)

    if key == "cp":
        y_line = 4 * a_line * (1 - a_line) ** 2
    elif key == "ct":
        y_line = 4 * a_line * (1 - a_line)
    elif key == "a_mean":
        y_line = a_line
    else:
        return None, None

    return ctp_line, y_line

def _unique_values(results, key):
    """Return values of results[key] in first-seen order, deduplicated."""
    seen = []
    for r in results:
        if r[key] not in seen:
            seen.append(r[key])
    return seen


def _bin_average(series, bin_size):
    """Average consecutive non-overlapping chunks of `bin_size` samples."""
    n_bins = len(series) // bin_size
    if n_bins == 0:
        return series.copy()
    trimmed = series[: n_bins * bin_size]
    return trimmed.reshape(n_bins, bin_size).mean(axis=1)


def _bin_aggregate_std(series, bin_size):
    """
    Aggregate standard deviation from raw series into binned values.
    For each bin, compute the std of the raw points in that bin.
    """
    n_bins = len(series) // bin_size
    if n_bins == 0:
        return np.array([np.std(series)])
    trimmed = series[: n_bins * bin_size]
    binned_std = trimmed.reshape(n_bins, bin_size).std(axis=1)
    return binned_std


# ============================================================================
# HELPERS — plotting
# ============================================================================

def plot_velocity_field_with_patches(sim_t, label, ctp, ax, D=1.0, hub_height=0, include_cbar=True, global_y_range=None):
    """
    Render the hub-height streamwise velocity field with patches for boundaries and turbine.

    Parameters
    ----------
    sim_t : BudgetIO
        Turbine simulation object
    label : str
        Plot label
    ctp : float
        Thrust coefficient
    ax : matplotlib axis
        Axis to plot on
    D : float
        Rotor diameter (default 1.0)
    hub_height : float
        Hub height z-coordinate (default 0)
    include_cbar : bool
        Whether to add a colorbar (default True)
    global_y_range : tuple of (y_min, y_max), optional
        Widest domain extent across the whole sweep (x/D units). If this
        sim's domain is narrower, the gap out to global_y_range is hatched.
        If None, no hatching is drawn.
    """
    view = sim_t.slice(field_terms=["u"], zlim=hub_height)
    u_data = view["u"]

    x = np.array(u_data.x) / D if hasattr(u_data, 'x') else np.arange(u_data.shape[1]) / D
    y = np.array(u_data.y) / D if hasattr(u_data, 'y') else np.arange(u_data.shape[0]) / D
    u_values = np.array(u_data).T

    X, Y = np.meshgrid(x, y)

    cf = ax.contourf(X, Y, u_values, levels=20, cmap='RdYlBu_r', extend='both')

    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    y_center = (y_min + y_max) / 2

    # Hatch the gap between this domain and the global extent if provided
    if global_y_range is not None:
        g_y_min, g_y_max = global_y_range
        if y_max < g_y_max - 1e-9:
            boundary_top = Rectangle((x_min, y_max), x_max - x_min, g_y_max - y_max,
                                    linewidth=0, facecolor='gray', hatch='///', alpha=0.4, zorder=1)
            ax.add_patch(boundary_top)
        if y_min > g_y_min + 1e-9:
            boundary_bottom = Rectangle((x_min, g_y_min), x_max - x_min, y_min - g_y_min,
                                       linewidth=0, facecolor='gray', hatch='///', alpha=0.4, zorder=1)
            ax.add_patch(boundary_bottom)
        ax.set_ylim(g_y_min, g_y_max)

    # Turbine rotor
    rotor = Rectangle((-0.05, y_center - D/2), 0.1, D,
                      linewidth=2, edgecolor='white', facecolor='white', alpha=0.9, zorder=3)
    ax.add_patch(rotor)

    if include_cbar:
        cbar = plt.colorbar(cf, ax=ax, label='u/U_inf (-)',
                           pad=0.01, fraction=0.032, aspect=22)
        cbar.ax.tick_params(labelsize=10)
        cbar.set_label('u/U_inf (-)', fontsize=11, fontweight='bold')

    ax.set_xlabel('x/D (-)', fontsize=12, fontweight='bold')
    ax.set_ylabel('y/D (-)', fontsize=12, fontweight='bold')
    ax.set_title(f'{label} - $\\mathbf{{C\'_T}}$ = {ctp}', fontsize=13, fontweight='bold')
    ax.tick_params(axis='both', labelsize=10)
    ax.set_aspect('equal')
    ax.grid(False)

    return cf


def plot_velocity_field_stacked(sim_t_list, label_list, ctp, ax_list, D=1.0, hub_height=0, global_y_range=None):
    """
    Plot multiple velocity fields stacked vertically.
    10% plot shows full domain. 20% plot has grey rectangles on sides showing domain difference.
    Uses global_y_range if provided; otherwise computes from the pair.
    """
    all_u_data = []
    view_list = []
    x_ranges = []
    y_ranges = []

    for sim_t in sim_t_list:
        view = sim_t.slice(field_terms=["u"], zlim=hub_height)
        view_list.append(view)
        u_data = view["u"]
        all_u_data.append(np.array(u_data).T)

        x = np.array(u_data.x) / D if hasattr(u_data, 'x') else np.arange(u_data.shape[1]) / D
        y = np.array(u_data.y) / D if hasattr(u_data, 'y') else np.arange(u_data.shape[0]) / D
        x_ranges.append((x.min(), x.max()))
        y_ranges.append((y.min(), y.max()))

    u_min = min(np.min(u) for u in all_u_data)
    u_max = max(np.max(u) for u in all_u_data)

    # Find which is 10% and which is 20%
    is_first_10 = "10%" in label_list[0]
    if is_first_10:
        x_lim_10 = x_ranges[0]
        x_lim_20 = x_ranges[1]
    else:
        x_lim_10 = x_ranges[1]
        x_lim_20 = x_ranges[0]

    # Use 10% domain as the reference (typically wider)
    x_lim = x_lim_10

    # Use global_y_range if provided; otherwise use local pair's range
    if global_y_range is not None:
        y_lim = global_y_range
    else:
        y_lim = (min(yr[0] for yr in y_ranges), max(yr[1] for yr in y_ranges))

    cfs = []
    for idx, (ax, label) in enumerate(zip(ax_list, label_list)):
        view = view_list[idx]
        u_data = view["u"]

        x = np.array(u_data.x) / D if hasattr(u_data, 'x') else np.arange(u_data.shape[1]) / D
        y = np.array(u_data.y) / D if hasattr(u_data, 'y') else np.arange(u_data.shape[0]) / D
        u_values = all_u_data[idx]

        X, Y = np.meshgrid(x, y)

        cf = ax.contourf(X, Y, u_values, levels=20, cmap='RdYlBu_r',
                        vmin=u_min, vmax=u_max, extend='both')

        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)

        x_min, x_max = x_lim
        y_min, y_max = y_lim
        y_center = (y_min + y_max) / 2

        # Hatch the gap between this sim's domain and the global extent
        y_sim_min, y_sim_max = y_ranges[idx]

        if y_sim_max < y_max - 1e-9:
            boundary_top = Rectangle((x_min, y_sim_max), x_max - x_min, y_max - y_sim_max,
                                    linewidth=0, facecolor='gray', hatch='///', alpha=0.4, zorder=1)
            ax.add_patch(boundary_top)

        if y_sim_min > y_min + 1e-9:
            boundary_bottom = Rectangle((x_min, y_min), x_max - x_min, y_sim_min - y_min,
                                       linewidth=0, facecolor='gray', hatch='///', alpha=0.4, zorder=1)
            ax.add_patch(boundary_bottom)

        # Grey rectangles for 20% case ONLY (shows x-domain difference)
        is_20_percent = "20%" in label
        if is_20_percent:
            # Get the 20% domain range
            x_20_min, x_20_max = x_lim_20

            # Left side grey rectangle
            if x_20_min > x_min:
                left_rect = Rectangle((x_min, y_lim[0]), x_20_min - x_min,
                                     y_lim[1] - y_lim[0],
                                     linewidth=0, facecolor='gray', alpha=0.3, zorder=2)
                ax.add_patch(left_rect)

            # Right side grey rectangle
            if x_20_max < x_max:
                right_rect = Rectangle((x_20_max, y_lim[0]), x_max - x_20_max,
                                      y_lim[1] - y_lim[0],
                                      linewidth=0, facecolor='gray', alpha=0.3, zorder=2)
                ax.add_patch(right_rect)

        # Turbine rotor
        rotor = Rectangle((-0.05, y_center - D/2), 0.1, D,
                         linewidth=2, edgecolor='white', facecolor='white', alpha=0.9, zorder=3)
        ax.add_patch(rotor)

        ax.set_xlabel('x/D (-)', fontsize=9, fontweight='bold')
        ax.set_ylabel('y/D (-)', fontsize=9, fontweight='bold')
        ax.set_title(f'{label} - $\\mathbf{{C\'_T}}$ = {ctp}', fontsize=10, fontweight='bold')
        ax.tick_params(axis='both', labelsize=7)
        ax.set_aspect('equal')
        ax.grid(False)

        cfs.append(cf)

    # Single colorbar at the end, positioned properly with shorter height
    cbar = plt.colorbar(cfs[-1], ax=ax_list, label='u/U_inf (-)',
                       pad=0.02, fraction=0.028, aspect=30, shrink=0.5)
    cbar.ax.tick_params(labelsize=7)
    cbar.set_label('u/U_inf (-)', fontsize=8, fontweight='bold')

    return cfs

def save_scalar_plot_with_lines(results, key, xlabel, ylabel, title, savepath,
                                 figsize=(7.5, 5), ncol=2, ylim=None,
                                 les_df=None, ubm_df=None, blockage_colors=None,
                                 show_classical=True):
    """
    Plot scalar values (Cp, Ct, a) vs CTP with MARKERS ONLY (no connecting lines).
    Each unique label gets its own marker style with blockage-based color.
    Optionally overlays LES reference data (points), the UBM model (dotted line),
    and classical momentum theory (dashed line, sampled over full range).
    """
    key_std = key + "_std"

    fig, ax = plt.subplots(figsize=figsize)

    label_groups = {}
    for r in results:
        label = r["label"]
        if label not in label_groups:
            label_groups[label] = []
        label_groups[label].append(r)

    seen_labels = set()
    for label, group in label_groups.items():
        group = sorted(group, key=lambda r: r["CTP"])

        x_vals = np.array([r["CTP"] for r in group])
        y_vals = np.array([r[key] for r in group])
        y_stds = np.array([r[key_std] for r in group])

        # Get blockage-based color from BLOCKAGE_COLORMAP
        blockage = group[0]["blockage"]
        color = BLOCKAGE_COLORMAP.get(blockage, "black")
        marker = group[0]["marker"]
        ti = group[0]["TI"]
        
        # Adjust marker size based on TI level (3% TI gets smaller markers)
        if ti == "3%":
            marker_size = 40
        else:
            marker_size = 70

        # Remove lines, plot MARKERS ONLY
        if label not in seen_labels:
            ax.scatter(x_vals, y_vals, color=color, marker=marker, s=marker_size, 
                      edgecolors='black', linewidths=1.5, label=label, alpha=0.85, zorder=5)
            seen_labels.add(label)
        else:
            ax.scatter(x_vals, y_vals, color=color, marker=marker, s=marker_size,
                      edgecolors='black', linewidths=1.5, alpha=0.85, zorder=5)

        # Std dev bands still present
        ax.fill_between(x_vals, y_vals - y_stds, y_vals + y_stds,
                        color=color, alpha=0.15, edgecolor="none", label=None)

    # --- LES reference data (points only) ---
    if les_df is not None and key in LES_KEY_MAP:
        les_col = LES_KEY_MAP[key]
        for beta_val, group in les_df.groupby("beta"):
            blockage_label = f"{int(round(beta_val * 100))}%"
            color = BLOCKAGE_COLORMAP.get(blockage_label, "black")
            group_sorted = group.sort_values("ctp")
            ax.scatter(group_sorted["ctp"], group_sorted[les_col],
                       color=color, marker="x", s=40, linewidths=2.2,
                       label=f"LES, {blockage_label} Blocked, 0% TI", zorder=5)

    # --- UBM model (DOTTED line) ---
    if ubm_df is not None and key in UBM_KEY_MAP:
        ubm_col = UBM_KEY_MAP[key]
        for beta_val, group in ubm_df.groupby("beta"):
            blockage_label = f"{int(round(beta_val * 100))}%"
            color = BLOCKAGE_COLORMAP.get(blockage_label, "black")
            group_sorted = group.sort_values("Ctp")
            ax.plot(group_sorted["Ctp"], group_sorted[ubm_col],
                   color=color, linestyle=":", linewidth=2.0,
                   label=f"UBM, {blockage_label} Blocked", zorder=4)

    # --- Classical momentum theory (dashed line, full range) ---
    if show_classical:
        ctp_line, y_line = compute_classical_line(key)
        if ctp_line is not None:
            ax.plot(ctp_line, y_line, color="gray", linestyle="--", linewidth=1.5,
                   label="Classical Momentum Theory", zorder=3)

    ax.set_xlabel(xlabel, fontsize=11, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.tick_params(axis='both', labelsize=9)
    
    # Set x-axis limit to 10 for C'_T
    ax.set_xlim(0, 10.5)
    
    # Move legend outside graph area
    ax.legend(fontsize=10, loc="center left", bbox_to_anchor=(1.0, 0.5), 
              framealpha=0.95, ncol=1)
    ax.grid(True, alpha=0.4, linestyle="--")

    if ylim is not None:
        y_data_max = max(r[key] + r[key_std] for r in results)
        top = max(ylim[1], y_data_max * 1.03)
        ax.set_ylim(ylim[0], top)
        ax.autoscale(enable=False)

    fig.subplots_adjust(left=0.12, right=0.75, top=0.93, bottom=0.12)
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath}")


def _by_ctp_style_kwargs(r):
    """For the by-CTP subplot version: color -> blockage, marker -> TI."""
    return dict(
        color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"),
        linestyle="dashed",
        linewidth=1.2,
        alpha=0.85,
        marker=TI_MARKERS.get(r["TI"], "o"),
        markersize=5,
        markevery=10,
        markerfacecolor="none",
        markeredgewidth=1.0,
    )


def _combined_style_kwargs(r):
    """For the combined all-sims plot: color -> blockage, linestyle -> TI, marker -> CTP."""
    return dict(
        color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"),
        linestyle=TI_LINESTYLES.get(r["TI"], "solid"),
        linewidth=0.6,
        alpha=0.6,
        marker=r["marker"],
        markersize=4,
        markevery=15,
        markerfacecolor="none",
        markeredgewidth=0.8,
    )


def save_timeseries_by_ctp(results, ylabel, key, title_base, savepath_base,
                            bin_size=BIN_SIZE, figsize=(11, 5.5)):
    """
    Plot decimated (bin-averaged) time series grouped by CTP, saving a
    SEPARATE standalone figure for each CTP value (rather than stacking all
    CTPs into one multi-panel figure). Each series uses its own full length
    (second half of all data). A dotted horizontal line marks the
    time-averaged mean for each series, if available via SERIES_MEAN_KEY.

    Output filenames are derived from savepath_base by inserting the CTP
    value before the extension, e.g. "./All_a_timeseries.png" ->
    "./All_a_timeseries_CTP2.png", "./All_a_timeseries_CTP4.png", etc.
    """
    ctps = _unique_values(results, "CTP")
    mean_key = SERIES_MEAN_KEY.get(key)
    base_path = Path(savepath_base)

    for ctp in ctps:
        subs = [r for r in results if r["CTP"] == ctp]

        fig, ax = plt.subplots(figsize=figsize)

        seen_labels = set()
        for r in subs:
            series = r[key]
            series_binned = _bin_average(series, bin_size)
            x_binned = np.arange(len(series_binned)) * bin_size

            style = _by_ctp_style_kwargs(r)
            label = r["label"]

            if label not in seen_labels:
                ax.plot(x_binned, series_binned, label=label, **style)
                seen_labels.add(label)
            else:
                ax.plot(x_binned, series_binned, **style)

            # Mean reference line, so convergence is easy to judge at a glance
            if mean_key is not None:
                ax.axhline(r[mean_key], color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"), 
                           linestyle=":", linewidth=1.5, alpha=0.7, zorder=0)

            if key in ["cp_series", "ct_series"] and ROLLING_STD_WINDOW is not None:
                std_series = compute_rolling_std(series, ROLLING_STD_WINDOW)
                std_binned = _bin_aggregate_std(std_series, bin_size)

                ax.fill_between(
                    x_binned[: len(std_binned)],
                    series_binned - std_binned,
                    series_binned + std_binned,
                    color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"),
                    alpha=0.15,
                    edgecolor="none",
                    label=None
                )

        ax.set_xlabel("Time Step (post-spinup)", fontsize=10, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=10, fontweight='bold')
        ax.set_title(f"{title_base} - $\\mathbf{{C\'_T}}$ = {ctp}\n(Bin-Averaged, every {bin_size} steps)",
                    fontsize=12, fontweight='bold')
        ax.tick_params(axis='both', labelsize=9)
        ax.legend(fontsize=9, loc="best", framealpha=0.95, ncol=2)
        ax.grid(True, alpha=0.3, linestyle="--")

        fig.subplots_adjust(left=0.11, right=0.96, top=0.87, bottom=0.13)

        savepath = base_path.parent / f"{base_path.stem}_CTP{ctp}{base_path.suffix}"
        fig.savefig(savepath, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {savepath}")


def save_timeseries_combined(results, ylabel, key, title, savepath,
                             bin_size=BIN_SIZE, figsize=(13, 8), ncol=3):
    """
    Single combined plot with every simulation overlaid.
    Each series uses its own full length (second half of all data).
    A faint dotted horizontal line marks each series' time-averaged mean.
    """
    fig, ax = plt.subplots(figsize=figsize)

    mean_key = SERIES_MEAN_KEY.get(key)

    for r in results:
        series = r[key]
        series_binned = _bin_average(series, bin_size)
        x_binned = np.arange(len(series_binned)) * bin_size

        style = _combined_style_kwargs(r)
        label = f"$\\mathbf{{C\'_T}}$={r['CTP']}, {r['label']}"
        ax.plot(x_binned, series_binned, label=label, **style)

        # Mean reference line (kept faint since this plot already has many series)
        if mean_key is not None:
            ax.axhline(r[mean_key], color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"), 
                       linestyle=":", linewidth=1.0, alpha=0.5, zorder=0)

        if key in ["cp_series", "ct_series"] and ROLLING_STD_WINDOW is not None:
            std_series = compute_rolling_std(series, ROLLING_STD_WINDOW)
            std_binned = _bin_aggregate_std(std_series, bin_size)

            ax.fill_between(
                x_binned[: len(std_binned)],
                series_binned - std_binned,
                series_binned + std_binned,
                color=BLOCKAGE_COLORMAP.get(r["blockage"], "black"),
                alpha=0.08,
                edgecolor="none",
                label=None
            )

    ax.set_xlabel("Time Step (post-spinup)",
                 fontsize=10, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=10, fontweight='bold')
    ax.set_title(f"{title}\n(Bin-Averaged every {bin_size} steps - linestyle = TI, marker = $\\mathbf{{C\'_T}}$, color = blockage)\nShaded bands represent temporal std dev (±1 std); dotted lines mark series means",
                fontsize=11, fontweight='bold')
    ax.tick_params(axis='both', labelsize=8)
    ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(1.01, 1.0),
             framealpha=0.95, ncol=ncol)
    ax.grid(True, alpha=0.3, linestyle="--")
    fig.subplots_adjust(left=0.09, right=0.78, top=0.86, bottom=0.10)
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath}")


def save_velocity_fields_master(results, savepath, global_y_range=None, figsize=None):
    """
    Create a master subplot figure showing all velocity fields.

    Parameters
    ----------
    results : list of dict
        Results list with sim_t keys
    savepath : str
        Output path
    global_y_range : tuple of (y_min, y_max), optional
        Global y extent to use for hatching gaps. If None, computed from results.
    figsize : tuple, optional
        Figure size
    """
    n_sims = len(results)
    n_cols = 4
    n_rows = (n_sims + n_cols - 1) // n_cols

    if figsize is None:
        figsize = (4.5 * n_cols, 3.5 * n_rows)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)

    if n_rows == 1 and n_cols == 1:
        axes = np.array([[axes]])
    elif n_rows == 1 or n_cols == 1:
        axes = axes.reshape(n_rows, n_cols)

    # Compute u_min/max and global y extent once
    all_u_data = []
    all_y = []
    for r in results:
        view = r["sim_t"].slice(field_terms=["u"], zlim=0)
        u_data = view["u"]
        all_u_data.append(np.array(u_data).T)
        all_y.append(np.array(u_data.y) if hasattr(u_data, 'y') else np.arange(u_data.shape[0]))

    u_min = min(np.min(u) for u in all_u_data)
    u_max = max(np.max(u) for u in all_u_data)

    if global_y_range is None:
        y_min_global = min(y.min() for y in all_y)
        y_max_global = max(y.max() for y in all_y)
    else:
        y_min_global, y_max_global = global_y_range

    # Plot each simulation
    for idx, r in enumerate(results):
        row = idx // n_cols
        col = idx % n_cols
        ax = axes[row, col]

        view = r["sim_t"].slice(field_terms=["u"], zlim=0)
        u_data = view["u"]

        x = np.array(u_data.x) if hasattr(u_data, 'x') else np.arange(u_data.shape[1])
        y = all_y[idx]
        u_values = all_u_data[idx]

        X, Y = np.meshgrid(x, y)

        cf = ax.contourf(X, Y, u_values, levels=20, cmap='RdYlBu_r',
                        vmin=u_min, vmax=u_max, extend='both')

        x_min, x_max = x.min(), x.max()
        y_min, y_max = y.min(), y.max()

        # Hatch the gap between this domain and the global extent
        if y_max < y_max_global - 1e-9:
            ax.add_patch(Rectangle((x_min, y_max), x_max - x_min, y_max_global - y_max,
                                    linewidth=0, facecolor='gray', hatch='///', alpha=0.4))
        if y_min > y_min_global + 1e-9:
            ax.add_patch(Rectangle((x_min, y_min_global), x_max - x_min, y_min - y_min_global,
                                    linewidth=0, facecolor='gray', hatch='///', alpha=0.4))

        ax.set_ylim(y_min_global, y_max_global)

        # Turbine rotor (assuming 0 hub height, D=1.0)
        rotor = Rectangle((-0.05, -0.5), 0.1, 1.0,
                         linewidth=2, edgecolor='white', facecolor='white', alpha=0.9)
        ax.add_patch(rotor)

        ax.set_title(f"{r['label']} - $\\mathbf{{C\'_T}}$ = {r['CTP']}", fontsize=9, fontweight='bold')
        ax.set_xlabel('x/D (-)', fontsize=8, fontweight='bold')
        ax.set_ylabel('y/D (-)', fontsize=8, fontweight='bold')
        ax.tick_params(axis='both', labelsize=7)
        ax.set_aspect('equal')
        ax.grid(False)

    # Hide unused subplots
    for idx in range(n_sims, n_rows * n_cols):
        row = idx // n_cols
        col = idx % n_cols
        axes[row, col].set_visible(False)

    cbar_ax = fig.add_axes([0.915, 0.2, 0.008, 0.6])
    cbar = plt.colorbar(cf, cax=cbar_ax, label='u/U_inf (-)')
    cbar.ax.tick_params(labelsize=6)
    cbar.set_label('u/U_inf (-)', fontsize=7, fontweight='bold')

    fig.suptitle("Hub-Height Streamwise Velocity - All Simulations",
                 fontsize=13, fontweight='bold', y=0.995)
    fig.subplots_adjust(left=0.06, right=0.91, top=0.94, bottom=0.06, wspace=0.25, hspace=0.4)
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath}")


def tag(s):
    """Strip % for use in filenames."""
    return s.replace("%", "")


# ============================================================================
# MAIN
# ============================================================================

results = []
for cfg in SIM_CONFIGS:
    print(f"Loading: $\\mathbf{{C\'_T}}$={cfg['CTP']}  {cfg['label']}")
    sim_e, sim_t = load_sim(cfg)
    cp, ct, a_series, cp_series, ct_series, uinf, ud_mean = compute_cp_ct_timeseries(sim_t)

    # NEW: direct thrust/power based coefficients
    ct_direct, cp_direct, thrust_series, ct_direct_series, power_series, cp_direct_series = compute_thrust_power_timeseries(sim_t)

    ke_flux_density, ke_flux_total = compute_ke_flux_empty(sim_e, x_target=X_KE_FLUX)
    print(f"    KE flux (empty domain) at x={X_KE_FLUX}: density={ke_flux_density:.6e}, total={ke_flux_total:.6e}")

    results.append({
        **cfg,
        "sim_t": sim_t,
        "cp": cp,
        "ct": ct,
        "a_series": a_series,
        "cp_series": cp_series,
        "ct_series": ct_series,
        "uinf": uinf,
        "ud_mean": ud_mean,
        "ke_flux_density_x5": ke_flux_density,
        "ke_flux_total_x5": ke_flux_total,
        # NEW
        "thrust_series": thrust_series,
        "ct_direct_series": ct_direct_series,
        "power_series": power_series,
        "cp_direct_series": cp_direct_series,
    })

les_df = pd.read_csv(LES_DATA_PATH)
ubm_df = pd.read_csv(UBM_DATA_PATH)

ctps      = _unique_values(results, "CTP")
ti_levels = _unique_values(results, "TI")

print("\nRecalculating mean values and std devs from post-spinup data...")
for r in results:
    a_data = r["a_series"]
    cp_data = r["cp_series"]
    ct_data = r["ct_series"]

    r["a_mean"] = float(np.mean(a_data))
    r["cp"] = float(np.mean(cp_data))
    r["ct"] = float(np.mean(ct_data))
    r["cp_mean_a"] = r["CTP"] * (1.0 - r["a_mean"])**3
    r["ct_mean_a"] = r["CTP"] * (1.0 - r["a_mean"])**2
    r["a_mean_std"] = float(np.std(a_data))
    r["cp_std"] = float(np.std(cp_data))
    r["ct_std"] = float(np.std(ct_data))
    r["cp_mean_a_std"] = 0.0
    r["ct_mean_a_std"] = 0.0

    # NEW: direct thrust/power coefficients
    r["ct_direct"] = float(np.mean(r["ct_direct_series"]))
    r["cp_direct"] = float(np.mean(r["cp_direct_series"]))
    r["ct_direct_std"] = float(np.std(r["ct_direct_series"]))
    r["cp_direct_std"] = float(np.std(r["cp_direct_series"]))
    r["thrust_mean"] = float(np.mean(r["thrust_series"]))
    r["power_mean"] = float(np.mean(r["power_series"]))

    print(
        f"  {r['label']:30s} (n={len(a_data):6d} steps) -> "
        f"a = {r['a_mean']:.4f}±{r['a_mean_std']:.4f}, "
        f"$\\mathbf{{C_P}}$ = {r['cp']:.4f} (mean-a: {r['cp_mean_a']:.4f}) ± {r['cp_std']:.4f}, "
        f"$\\mathbf{{C_T}}$ = {r['ct']:.4f} (mean-a: {r['ct_mean_a']:.4f}) ± {r['ct_std']:.4f}, "
        f"$\\mathbf{{C_P,direct}}$ = {r['cp_direct']:.4f}±{r['cp_direct_std']:.4f}, "  # NEW
        f"$\\mathbf{{C_T,direct}}$ = {r['ct_direct']:.4f}±{r['ct_direct_std']:.4f}"    # NEW
    )

def save_time_averaged_csv(results, savepath="./Time_Averaged_Summary.csv"):
    """
    Save time-averaged uinf, ud, a, ct, and cp for each simulation to a CSV,
    with one row per simulation, organized by CTP and TI level.
    """
    rows = []
    for r in results:
        rows.append({
            "CTP": r["CTP"],
            "TI": r["TI"],
            "blockage": r["blockage"],
            "label": r["label"],
            "uinf": r["uinf"],
            "ud": r["ud_mean"],
            "a": r["a_mean"],
            "a_std": r["a_mean_std"],
            "ct": r["ct"],
            "ct_std": r["ct_std"],
            "cp": r["cp"],
            "cp_std": r["cp_std"],
            "ke_flux_density_x5": r["ke_flux_density_x5"],  # NEW
            "ke_flux_total_x5": r["ke_flux_total_x5"],       # NEW
        })

    df = pd.DataFrame(rows)
    df = df.sort_values(["CTP", "TI", "blockage"]).reset_index(drop=True)
    df.to_csv(savepath, index=False)
    print(f"  Saved: {savepath}")

print("\nAll simulations loaded!")

save_time_averaged_csv(results, "./Time_Averaged_Summary.csv")

# Compute global y extent once for all velocity field plots
GLOBAL_Y_RANGE = compute_global_y_extent(results)
print(f"\nGlobal y-extent across all sims: [{GLOBAL_Y_RANGE[0]:.4f}, {GLOBAL_Y_RANGE[1]:.4f}] (normalized)")

print("\nGenerating velocity field plots with patches...")
for ctp in ctps:
    for ti in ti_levels:
        subs = [r for r in results if r["CTP"] == ctp and r["TI"] == ti]
        if not subs:
            continue

        if len(subs) == 2:
            fig = plt.figure(figsize=(7.5, 4))
            gs = fig.add_gridspec(2, 1, hspace=0.3)
            axes = [fig.add_subplot(gs[0]), fig.add_subplot(gs[1])]
            labels = [r["label"] for r in subs]
            sim_list = [r["sim_t"] for r in subs]
            plot_velocity_field_stacked(sim_list, labels, ctp, axes,
                                       global_y_range=GLOBAL_Y_RANGE)
            fig.suptitle(f"Hub-Height Streamwise Velocity - {ti} TI, $\\mathbf{{C\'_T}}$ = {ctp}",
                         fontsize=11, fontweight='bold', y=0.98)
            fig.subplots_adjust(left=0.12, right=0.85, top=0.92, bottom=0.10, hspace=0.3)
        else:
            fig, axes = plt.subplots(1, len(subs), figsize=(7.5, 5))
            if len(subs) == 1:
                axes = [axes]
            for ax, r in zip(axes, subs):
                plot_velocity_field_with_patches(r["sim_t"], r["label"], ctp, ax,
                                                 global_y_range=GLOBAL_Y_RANGE)
            fig.suptitle(f"Hub-Height Streamwise Velocity - {ti} TI, $\\mathbf{{C\'_T}}$ = {ctp}",
                         fontsize=12, fontweight='bold')
            fig.subplots_adjust(left=0.12, right=0.95, top=0.93, bottom=0.12)

        savepath = f"./CTP{ctp}_{tag(ti)}TI_u.png"
        fig.savefig(savepath, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {savepath}")

print("\nGenerating master velocity field subplot...")
save_velocity_fields_master(results, "./All_Velocity_Fields.png", global_y_range=GLOBAL_Y_RANGE)
print("Master velocity field subplot complete!")

print("Velocity field plots complete!")

print("\nGenerating scalar comparison plots with markers and std dev bands...")

save_scalar_plot_with_lines(
    results,
    key="cp",
    xlabel="$\\mathbf{{C\'_T}}$ (-)", ylabel="$\\mathbf{{C_P}}$ (-)",
    title="$\\mathbf{{C_P}}$ vs $\\mathbf{{C\'_T}}$ - All Configurations",
    ylim=(0, 1.4),
    savepath="./All_Cp_vs_CTP_f.png",
    les_df=les_df, ubm_df=ubm_df, blockage_colors=BLOCKAGE_COLORMAP,
)

save_scalar_plot_with_lines(
    results,
    key="ct",
    xlabel="$\\mathbf{{C\'_T}}$ (-)", ylabel="$\\mathbf{{C_T}}$ (-)",
    title="$\\mathbf{{C_T}}$ vs $\\mathbf{{C\'_T}}$ - All Configurations",
    ylim=(0, 2.2),
    savepath="./All_Ct_vs_CTP_f.png",
    les_df=les_df, ubm_df=ubm_df, blockage_colors=BLOCKAGE_COLORMAP,
)

save_scalar_plot_with_lines(
    results,
    key="a_mean",
    xlabel="$\\mathbf{{C\'_T}}$ (-)", ylabel="Induction Factor (a) (-)",
    title="Induction Factor vs $\\mathbf{{C\'_T}}$ - All Configurations",
    ylim=(0, 0.8),
    savepath="./All_a_vs_CTP_f.png",
    les_df=les_df, ubm_df=ubm_df, blockage_colors=BLOCKAGE_COLORMAP,
)

print("Scalar plots complete!")

print("\nGenerating direct thrust/power coefficient scalar plots...")

save_scalar_plot_with_lines(
    results,
    key="cp_direct",
    xlabel="$\\mathbf{{C\'_T}}$ (-)", ylabel="$\\mathbf{{C_P}}$, direct (-)",
    title="Power Coefficient (Direct from $u_d$, $P$) vs $\\mathbf{{C\'_T}}$ - All Configurations",
    ylim=(0, 1.4),
    savepath="./All_Cp_direct_vs_CTP_f.png",
    les_df=les_df, ubm_df=ubm_df, blockage_colors=BLOCKAGE_COLORMAP,
)

save_scalar_plot_with_lines(
    results,
    key="ct_direct",
    xlabel="$\\mathbf{{C\'_T}}$ (-)", ylabel="$\\mathbf{{C_T}}$, direct (-)",
    title="Thrust Coefficient (Direct from $u_d$, $u_\\infty$) vs $\\mathbf{{C\'_T}}$ - All Configurations",
    ylim=(0, 2.2),
    savepath="./All_Ct_direct_vs_CTP_f.png",
    les_df=les_df, ubm_df=ubm_df, blockage_colors=BLOCKAGE_COLORMAP,
)

print("Direct thrust/power coefficient scalar plots complete!")

print("\nGenerating time series plots (post-spinup, bin-averaged)...")
print(f"Using rolling std window: {ROLLING_STD_WINDOW}")

save_timeseries_by_ctp(
    results,
    ylabel="Induction Factor (a) (-)",
    key="a_series",
    title_base="Induction Factor Time Series",
    savepath_base="./All_a_timeseries.png",
    bin_size=BIN_SIZE_BY_CTP,
)

save_timeseries_by_ctp(
    results,
    ylabel="$\\mathbf{{C_P}}$ (-)",
    key="cp_series",
    title_base="$\\mathbf{{C_P}}$ Time Series",
    savepath_base="./All_cp_timeseries.png",
    bin_size=BIN_SIZE_BY_CTP,
)

save_timeseries_by_ctp(
    results,
    ylabel="$\\mathbf{{C_T}}$ (-)",
    key="ct_series",
    title_base="$\\mathbf{{C_T}}$ Time Series",
    savepath_base="./All_ct_timeseries.png",
    bin_size=BIN_SIZE_BY_CTP,
)
print("Time series plots (by $\\mathbf{{C\'_T}}$) complete!")

print("\nGenerating combined all-simulation time series plots...")
save_timeseries_combined(
    results,
    ylabel="Induction Factor (a) (-)",
    key="a_series",
    title="Induction Factor Time Series - All Simulations",
    savepath="./All_Sims_a_timeseries.png",
)

save_timeseries_combined(
    results,
    ylabel="$\\mathbf{{C_P}}$ (-)",
    key="cp_series",
    title="$\\mathbf{{C_P}}$ Time Series - All Simulations",
    savepath="./All_Sims_cp_timeseries.png",
)

save_timeseries_combined(
    results,
    ylabel="$\\mathbf{{C_T}}$ (-)",
    key="ct_series",
    title="$\\mathbf{{C_T}}$ Time Series - All Simulations",
    savepath="./All_Sims_ct_timeseries.png",
)
print("Combined plots complete!")

print("\nAll analysis complete!")