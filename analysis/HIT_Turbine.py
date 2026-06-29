import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine


# ============================================================================
# CONFIGURATION
# ============================================================================
SIM_CONFIGS = [
    # CTP = 2
    dict(label="Unblocked, 3% TI", path="Data/HIT_Turbines/CTP_2/TI_3/UNB", runid_e=2, runid_t=3, CTP=2, blockage="0.005%", TI="3%", color="black", marker="o"),
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_2/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="10%", TI="3%",  color="blue",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_2/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="20%", TI="3%",  color="red",   marker="o"),
    dict(label="Unblocked, 8% TI", path="Data/HIT_Turbines/CTP_2/TI_8/UNB", runid_e=2, runid_t=3, CTP=2, blockage="0.005%", TI="8%", color="black", marker="s"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_2/TI_8/10PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="10%", TI="8%",  color="blue",  marker="s"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_2/TI_8/20PCT",  runid_e=2, runid_t=3, CTP=2,  blockage="20%", TI="8%",  color="red",   marker="s"),
    dict(label="Unblocked, 12% TI", path="Data/HIT_Turbines/CTP_2/TI_12/UNB", runid_e=2, runid_t=3, CTP=2, blockage="0.005%", TI="12%", color="black", marker="^"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_2/TI_12/10PCT", runid_e=2, runid_t=3, CTP=2,  blockage="10%", TI="12%", color="blue",  marker="^"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_2/TI_12/20PCT", runid_e=2, runid_t=3, CTP=2,  blockage="20%", TI="12%", color="red",   marker="^"),

    # CTP = 4
    dict(label="Unblocked, 3% TI", path="Data/HIT_Turbines/CTP_4/TI_3/UNB", runid_e=2, runid_t=3, CTP=4, blockage="0.005%", TI="3%", color="black", marker="o"),
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_4/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="10%", TI="3%",  color="blue",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_4/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="20%", TI="3%",  color="red",   marker="o"),
    dict(label="Unblocked, 8% TI", path="Data/HIT_Turbines/CTP_4/TI_8/UNB", runid_e=2, runid_t=3, CTP=4, blockage="0.005%", TI="8%", color="black", marker="s"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_4/TI_8/10PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="10%", TI="8%",  color="blue",  marker="s"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_4/TI_8/20PCT",  runid_e=2, runid_t=3, CTP=4,  blockage="20%", TI="8%",  color="red",   marker="s"),
    dict(label="Unblocked, 12% TI", path="Data/HIT_Turbines/CTP_4/TI_12/UNB", runid_e=2, runid_t=3, CTP=4, blockage="0.005%", TI="12%", color="black", marker="^"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_4/TI_12/10PCT", runid_e=2, runid_t=3, CTP=4,  blockage="10%", TI="12%", color="blue",  marker="^"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_4/TI_12/20PCT", runid_e=2, runid_t=3, CTP=4,  blockage="20%", TI="12%", color="red",   marker="^"),

    # CTP = 6
    dict(label="Unblocked, 3% TI", path="Data/HIT_Turbines/CTP_6/TI_3/UNB", runid_e=2, runid_t=3, CTP=6, blockage="0.005%", TI="3%", color="black", marker="o"),
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_6/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="10%", TI="3%",  color="blue",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_6/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="20%", TI="3%",  color="red",   marker="o")
    dict(label="Unblocked, 8% TI", path="Data/HIT_Turbines/CTP_6/TI_8/UNB", runid_e=2, runid_t=3, CTP=6, blockage="0.005%", TI="8%", color="black", marker="s"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_6/TI_8/10PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="10%", TI="8%",  color="blue",  marker="s"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_6/TI_8/20PCT",  runid_e=2, runid_t=3, CTP=6,  blockage="20%", TI="8%",  color="red",   marker="s"),
    dict(label="Unblocked, 12% TI", path="Data/HIT_Turbines/CTP_6/TI_12/UNB", runid_e=2, runid_t=3, CTP=6, blockage="0.005%", TI="12%", color="black", marker="^"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_6/TI_12/10PCT", runid_e=2, runid_t=3, CTP=6,  blockage="10%", TI="12%", color="blue",  marker="^"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_6/TI_12/20PCT", runid_e=2, runid_t=3, CTP=6,  blockage="20%", TI="12%", color="red",   marker="^"),

    # CTP = 8
    dict(label="Unblocked, 3% TI", path="Data/HIT_Turbines/CTP_8/TI_3/UNB", runid_e=2, runid_t=3, CTP=8, blockage="0.005%", TI="3%", color="black", marker="o"),
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_8/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="10%", TI="3%",  color="blue",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_8/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="20%", TI="3%",  color="red",   marker="o"),
    dict(label="Unblocked, 8% TI", path="Data/HIT_Turbines/CTP_8/TI_8/UNB", runid_e=2, runid_t=3, CTP=8, blockage="0.005%", TI="8%", color="black", marker="s"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_8/TI_8/10PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="10%", TI="8%",  color="blue",  marker="s"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_8/TI_8/20PCT",  runid_e=2, runid_t=3, CTP=8,  blockage="20%", TI="8%",  color="red",   marker="s"),
    dict(label="Unblocked, 12% TI", path="Data/HIT_Turbines/CTP_8/TI_12/UNB", runid_e=2, runid_t=3, CTP=8, blockage="0.005%", TI="12%", color="black", marker="^"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_8/TI_12/10PCT", runid_e=2, runid_t=3, CTP=8,  blockage="10%", TI="12%", color="blue",  marker="^"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_8/TI_12/20PCT", runid_e=2, runid_t=3, CTP=8,  blockage="20%", TI="12%", color="red",   marker="^"),

    # CTP = 10
    dict(label="Unblocked, 3% TI", path="Data/HIT_Turbines/CTP_10/TI_3/UNB", runid_e=2, runid_t=3, CTP=10, blockage="0.005%", TI="3%", color="black", marker="o"),
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_10/TI_3/10PCT",  runid_e=2, runid_t=3, CTP=10, blockage="10%", TI="3%",  color="blue",  marker="o"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_10/TI_3/20PCT",  runid_e=2, runid_t=3, CTP=10, blockage="20%", TI="3%",  color="red",   marker="o"),
    dict(label="Unblocked, 8% TI", path="Data/HIT_Turbines/CTP_10/TI_8/UNB", runid_e=2, runid_t=3, CTP=10, blockage="0.005%", TI="8%", color="black", marker="s"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_10/TI_8/10PCT",  runid_e=2, runid_t=3, CTP=10, blockage="10%", TI="8%",  color="blue",  marker="s"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_10/TI_8/20PCT",  runid_e=2, runid_t=3, CTP=10, blockage="20%", TI="8%",  color="red",   marker="s"),
    dict(label="Unblocked, 12% TI", path="Data/HIT_Turbines/CTP_10/TI_12/UNB", runid_e=2, runid_t=3, CTP=10, blockage="0.005%", TI="12%", color="black", marker="^"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_10/TI_12/10PCT", runid_e=2, runid_t=3, CTP=10, blockage="10%", TI="12%", color="blue",  marker="^"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_10/TI_12/20PCT", runid_e=2, runid_t=3, CTP=10, blockage="20%", TI="12%", color="red",   marker="^"),
]

# Fraction of the time series to discard as spinup (0.5 = discard first half).
SPINUP_FRACTION = 0.5

# Bin-averaging factor for time series plots (decimation). Averages every
# BIN_SIZE consecutive raw points into one plotted point, to cut down the
# number of points drawn and make line style / markers distinguishable.
BIN_SIZE = 150

# Smaller bin size for the by-CTP subplot version to show more detail
BIN_SIZE_BY_CTP = 50

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
    """Inflow velocity: scalar mean over the upstream (x = -1D) hub-height slice."""
    return float(sim_t.slice(field_terms=["u"], xlim=-1, zlim=0)["u"].mean())


def compute_cp_ct_timeseries(sim_t, spinup_fraction=SPINUP_FRACTION):
    """
    Compute time series and time-averaged Cp, Ct, and induction factor for one simulation.
    Uses the formulas:
        a = 1 - (ud / uinf)
        cp = ctp * (1 - a)^3
        ct = ctp * (1 - a)^2

    Parameters
    ----------
    sim_t : BudgetIO object
        Turbine simulation
    spinup_fraction : float
        Fraction of time series to discard as spinup

    Returns
    -------
    cp, ct : scalar floats (time-averaged)
    a_series, cp_series, ct_series : numpy arrays (time series after spinup)
    """
    uinf = get_uinf(sim_t)
    ud = np.asarray(sim_t.read_turb_uvel("all", steady=False))
    ctp = float(sim_t.ta[0].ct)

    # Discard spinup transient
    n = len(ud)
    spinup_idx = int(spinup_fraction * n)
    ud = ud[spinup_idx:]

    # Compute time series
    a_series = 1.0 - (ud / uinf)
    cp_series = ctp * ((1.0 - a_series) ** 3)
    ct_series = ctp * ((1.0 - a_series) ** 2)

    # Compute time-averaged scalars
    cp = float(np.mean(cp_series))
    ct = float(np.mean(ct_series))

    return cp, ct, a_series, cp_series, ct_series


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


# ============================================================================
# HELPERS — plotting
# ============================================================================

def plot_velocity_field(sim_t, label, ax):
    """Render the hub-height streamwise velocity field onto ax."""
    view = sim_t.slice(field_terms=["u"], zlim=0)
    view["u"].imshow(ax=ax)
    ax.set_title(label, fontsize=12, fontweight="bold")


def _marker_kwargs(cfg, label=None, color=None):
    return dict(
        label=label if label is not None else cfg["label"],
        color=color if color is not None else cfg["color"],
        marker=cfg["marker"],
        markersize=8,
        markeredgewidth=1.5,
        markerfacecolor="none",
        linestyle="none",
    )


def save_scalar_plot(ax_data, xlabel, ylabel, title, savepath,
                     figsize=(12, 7), ncol=2):
    """
    Generic scatter plot for all configurations.

    ax_data : list of (x_value, y_value, cfg_dict, label_override, color_override)
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Group by label so each unique series gets one legend entry
    seen_labels = {}
    for x, y, cfg, label, color in ax_data:
        key = (label, color, cfg["marker"])
        kwargs = _marker_kwargs(cfg, label=label, color=color)
        if key in seen_labels:
            kwargs.pop("label")
            ax.plot(x, y, **kwargs)
        else:
            seen_labels[key] = True
            ax.plot(x, y, **kwargs)

    ax.set_xlabel(xlabel, fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=12, fontweight="bold")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.legend(fontsize=11, loc="best", framealpha=0.95, ncol=ncol)
    ax.grid(True, alpha=0.4, linestyle="--")
    fig.tight_layout()
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath}")


def _by_ctp_style_kwargs(r):
    """For the by-CTP subplot version: color -> blockage, marker -> TI
    (linestyle stays solid for all, since within one CTP panel the only
    two things distinguishing a line are blockage and TI)."""
    return dict(
        color=r["color"],
        linestyle="solid",
        linewidth=0.6,
        alpha=0.85,
        marker=TI_MARKERS.get(r["TI"], "o"),
        markersize=5,
        markevery=10,
        markerfacecolor="none",
        markeredgewidth=1.0,
    )


def _combined_style_kwargs(r):
    """For the combined all-sims plot: color -> blockage, linestyle -> TI,
    marker -> CTP (from cfg). Thinner/lighter lines and sparser markers
    than the by-CTP version, since up to 30 series overlap on one axes."""
    return dict(
        color=r["color"],
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
                            n_common, bin_size=BIN_SIZE, figsize=(14, 10)):
    """
    Plot decimated (bin-averaged) time series grouped by CTP in subplots.
    Every series uses its LAST `n_common` raw samples (i.e. the most
    settled, longest-time-averaged tail of each run), so all panels span
    the same duration and are directly comparable without truncating
    longer runs down to only their earliest, possibly less-converged
    post-spinup samples.

    results : list of result dicts
    ylabel : y-axis label
    key : key in result dict ('a_series', 'cp_series', or 'ct_series')
    title_base : base title string
    savepath_base : base path without extension
    n_common : number of raw (pre-binning) samples to keep from each series
    bin_size : number of raw samples averaged into each plotted point
    """
    ctps = _unique_values(results, "CTP")
    n_ctp = len(ctps)

    fig, axes = plt.subplots(n_ctp, 1, figsize=figsize, sharex=True)
    if n_ctp == 1:
        axes = [axes]

    # Shared x-axis: time relative to the end of the (common) window, so
    # every line's window represents "the last n_common steps" regardless
    # of how much longer its full run actually was.
    x_binned = np.arange(n_common // bin_size) * bin_size

    for idx, ctp in enumerate(ctps):
        ax = axes[idx]
        subs = [r for r in results if r["CTP"] == ctp]

        seen_labels = set()
        for r in subs:
            series = r[key][-n_common:]
            series_binned = _bin_average(series, bin_size)
            style = _by_ctp_style_kwargs(r)
            label = r["label"]

            if label not in seen_labels:
                ax.plot(x_binned[: len(series_binned)], series_binned,
                       label=label, **style)
                seen_labels.add(label)
            else:
                ax.plot(x_binned[: len(series_binned)], series_binned, **style)

        ax.set_ylabel(ylabel, fontsize=11, fontweight="bold")
        ax.set_title(f"{title_base} — CTP = {ctp}", fontsize=12, fontweight="bold")
        ax.legend(fontsize=9, loc="best", framealpha=0.95, ncol=2)
        ax.grid(True, alpha=0.3, linestyle="--")

    axes[-1].set_xlabel("Time Step (last common window, after spinup)",
                        fontsize=12, fontweight="bold")
    fig.suptitle(f"{title_base} (Bin-Averaged, every {bin_size} steps)",
                 fontsize=14, fontweight="bold", y=0.995)
    fig.tight_layout()
    fig.savefig(savepath_base, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath_base}")


def save_timeseries_combined(results, ylabel, key, title, savepath,
                             n_common, bin_size=BIN_SIZE, figsize=(16, 9), ncol=3):
    """
    Single combined plot with every simulation overlaid:
    color = blockage, linestyle = TI (solid/dashed/dotted),
    marker = CTP (from cfg). Every series uses its LAST `n_common` raw
    samples (most settled tail of each run) so all lines span the same
    duration. Lines are thinner and more transparent than the by-CTP
    version, since up to 30 series overlap on one axes.
    """
    fig, ax = plt.subplots(figsize=figsize)
    x_binned = np.arange(n_common // bin_size) * bin_size

    for r in results:
        series = r[key][-n_common:]
        series_binned = _bin_average(series, bin_size)
        style = _combined_style_kwargs(r)
        label = f"CTP={r['CTP']}, {r['label']}"
        ax.plot(x_binned[: len(series_binned)], series_binned,
               label=label, **style)

    ax.set_xlabel("Time Step (last common window, after spinup)",
                 fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=12, fontweight="bold")
    ax.set_title(f"{title}\n(Bin-Averaged every {bin_size} steps — "
                f"linestyle = TI, marker = CTP, color = blockage)",
                fontsize=13, fontweight="bold")
    ax.legend(fontsize=7.5, loc="upper left", bbox_to_anchor=(1.01, 1.0),
             framealpha=0.95, ncol=ncol)
    ax.grid(True, alpha=0.3, linestyle="--")
    fig.tight_layout()
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {savepath}")


def tag(s):
    """Strip % for use in filenames, e.g. '10%' -> '10', '3%' -> '3'."""
    return s.replace("%", "")


# ============================================================================
# MAIN
# ============================================================================

# --- Load all simulations and compute Cp / Ct time series ---
results = []
for cfg in SIM_CONFIGS:
    print(f"Loading: CTP={cfg['CTP']}  {cfg['label']}")
    sim_e, sim_t = load_sim(cfg)
    cp, ct, a_series, cp_series, ct_series = compute_cp_ct_timeseries(sim_t)
    results.append({
        **cfg,
        "sim_t": sim_t,
        "cp": cp,
        "ct": ct,
        "a_series": a_series,
        "cp_series": cp_series,
        "ct_series": ct_series,
    })

ctps      = _unique_values(results, "CTP")
ti_levels = _unique_values(results, "TI")

# Every simulation may have a different post-spinup length (different total
# run length, or different SPINUP_FRACTION cutoff in raw samples). Truncate
# every series to the shortest one so all time series plots share the same
# x-range and are directly comparable without truncating longer runs down 
# to only their earliest, possibly less-converged post-spinup samples.
n_common = min(len(r["a_series"]) for r in results)
print(f"\nCommon post-spinup length across all sims: {n_common} steps "
     f"(shortest run determines this)")

# --- Recalculate mean values (a, cp, ct) from the truncated data range ---
print("\nRecalculating mean values from truncated data range...")
for r in results:
    # Truncate each series to the common length
    a_truncated = r["a_series"][:n_common]
    cp_truncated = r["cp_series"][:n_common]
    ct_truncated = r["ct_series"][:n_common]
    
    # Compute mean values from truncated range
    r["a_mean"] = float(np.mean(a_truncated))
    r["cp"] = float(np.mean(cp_truncated))
    r["ct"] = float(np.mean(ct_truncated))
    
    print(f"  {r['label']:30s} -> a = {r['a_mean']:.4f},  "
          f"Cp = {r['cp']:.4f},  Ct = {r['ct']:.4f}")

print("\nAll simulations loaded!")

# --- Velocity field plots: one figure per (CTP, TI) ---
print("\nGenerating velocity field plots...")
for ctp in ctps:
    for ti in ti_levels:
        subs = [r for r in results if r["CTP"] == ctp and r["TI"] == ti]
        if not subs:
            continue
        fig, axes = plt.subplots(1, len(subs), figsize=(7 * len(subs), 5))
        if len(subs) == 1:
            axes = [axes]
        for ax, r in zip(axes, subs):
            plot_velocity_field(r["sim_t"], r["label"], ax)
        fig.suptitle(f"Final Streamwise Velocity — {ti} TI, CTP = {ctp}",
                     fontsize=14, fontweight="bold")
        fig.tight_layout()
        savepath = f"./CTP{ctp}_{tag(ti)}TI_u.png"
        fig.savefig(savepath, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved: {savepath}")
print("Velocity field plots complete!")

# --- Cp and Ct vs CTP: all configurations on one figure ---
print("\nGenerating scalar comparison plots...")
for qty, key in [("Cp", "cp"), ("Ct", "ct")]:
    ax_data = [(r["CTP"], r[key], r, r["label"], r["color"]) for r in results]
    save_scalar_plot(
        ax_data,
        xlabel="CTP", ylabel=qty,
        title=f"{qty} vs CTP — All Configurations",
        savepath=f"./All_{qty}_vs_CTP.png",
    )
print("Scalar plots complete!")

# --- Time series plots by CTP: Cp, Ct, and induction factor ---
print("\nGenerating time series plots (grouped by CTP, bin-averaged, "
     "truncated to common length)...")
save_timeseries_by_ctp(
    results,
    ylabel="Induction Factor (a)",
    key="a_series",
    title_base="Induction Factor Time Series",
    savepath_base="./All_a_timeseries.png",
    n_common=n_common,
    bin_size=BIN_SIZE_BY_CTP,
)

save_timeseries_by_ctp(
    results,
    ylabel="Cp",
    key="cp_series",
    title_base="Cp Time Series",
    savepath_base="./All_cp_timeseries.png",
    n_common=n_common,
    bin_size=BIN_SIZE_BY_CTP,
)

save_timeseries_by_ctp(
    results,
    ylabel="Ct",
    key="ct_series",
    title_base="Ct Time Series",
    savepath_base="./All_ct_timeseries.png",
    n_common=n_common,
    bin_size=BIN_SIZE_BY_CTP,
)
print("Time series plots (by CTP) complete!")

# --- Combined plots: every simulation overlaid on one figure ---
print("\nGenerating combined all-simulation time series plots...")
save_timeseries_combined(
    results,
    ylabel="Induction Factor (a)",
    key="a_series",
    title="Induction Factor Time Series — All Simulations",
    savepath="./All_Sims_a_timeseries.png",
    n_common=n_common,
)

save_timeseries_combined(
    results,
    ylabel="Cp",
    key="cp_series",
    title="Cp Time Series — All Simulations",
    savepath="./All_Sims_cp_timeseries.png",
    n_common=n_common,
)

save_timeseries_combined(
    results,
    ylabel="Ct",
    key="ct_series",
    title="Ct Time Series — All Simulations",
    savepath="./All_Sims_ct_timeseries.png",
    n_common=n_common,
)
print("Combined plots complete!")

print("\nAll analysis complete!")