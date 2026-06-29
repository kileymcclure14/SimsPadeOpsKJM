import analysis_utils as au
from pathlib import Path
import os
import math
import re
import padeopsIO as pio
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine


# ============================================================================
# CONFIGURATION
# ============================================================================
SIM_CONFIGS = [
    dict(path="Data/HIT_Turbines/CTP_2/TI_3/UNB", runid=3, CTP="2", blockage="0.005%", TI="3%", color="black"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_3/10PCT",  runid=3, CTP="2", blockage="10%", TI="3%",  color="blue"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_3/20PCT",  runid=3, CTP="2", blockage="20%", TI="3%",  color="red"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_8/UNB", runid=3, CTP="2", blockage="1%", TI="8%", color="brown"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_8/10PCT",  runid=3, CTP="2", blockage="0.005%", TI="8%",  color="orange"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_8/20PCT",  runid=3, CTP="2", blockage="20%", TI="8%",  color="green"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_12/UNB", runid=3, CTP="2", blockage="0.005%", TI="12%", color="gray"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_12/10PCT", runid=3, CTP="2", blockage="10%", TI="12%", color="cyan"),
    dict(path="Data/HIT_Turbines/CTP_2/TI_12/20PCT", runid=3, CTP="2", blockage="20%", TI="12%", color="magenta"),

    # CTP = 4
    dict(path="Data/HIT_Turbines/CTP_4/TI_3/UNB", runid=3, CTP="4", blockage="0.005%", TI="3%", color="black"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_3/10PCT",  runid=3, CTP="4", blockage="10%", TI="3%",  color="blue"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_3/20PCT",  runid=3, CTP="4", blockage="20%", TI="3%",  color="red"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_8/UNB", runid=3, CTP="4", blockage="0.005%", TI="8%", color="brown"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_8/10PCT",  runid=3, CTP="4", blockage="10%", TI="8%",  color="orange"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_8/20PCT",  runid=3, CTP="4", blockage="20%", TI="8%",  color="green"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_12/UNB", runid=3, CTP="4", blockage="0.005%", TI="12%", color="gray"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_12/10PCT", runid=3, CTP="4", blockage="10%", TI="12%", color="cyan"),
    dict(path="Data/HIT_Turbines/CTP_4/TI_12/20PCT", runid=3, CTP="4", blockage="20%", TI="12%", color="magenta"),

    # CTP = 6
    dict(path="Data/HIT_Turbines/CTP_6/TI_3/UNB", runid=3, CTP="6", blockage="0.005%", TI="3%", color="black"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_3/10PCT",  runid=3, CTP="6", blockage="10%", TI="3%",  color="blue"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_3/20PCT",  runid=3, CTP="6", blockage="20%", TI="3%",  color="red"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_8/UNB", runid=3, CTP="6", blockage="0.005%", TI="8%", color="brown"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_8/10PCT",  runid=3, CTP="6", blockage="10%", TI="8%",  color="orange"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_8/20PCT",  runid=3, CTP="6", blockage="20%", TI="8%",  color="green"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_12/UNB", runid=3, CTP="6", blockage="0.005%", TI="12%", color="gray"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_12/10PCT", runid=3, CTP="6", blockage="10%", TI="12%", color="cyan"),
    dict(path="Data/HIT_Turbines/CTP_6/TI_12/20PCT", runid=3, CTP="6", blockage="20%", TI="12%", color="magenta"),

    # CTP = 8
    dict(path="Data/HIT_Turbines/CTP_8/TI_3/UNB", runid=3, CTP="8", blockage="0.005%", TI="3%", color="black"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_3/10PCT",  runid=3, CTP="8", blockage="10%", TI="3%",  color="blue"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_3/20PCT",  runid=3, CTP="8", blockage="20%", TI="3%",  color="red"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_8/UNB", runid=3, CTP="8", blockage="0.005%", TI="8%", color="brown"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_8/10PCT",  runid=3, CTP="8", blockage="10%", TI="8%",  color="orange"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_8/20PCT",  runid=3, CTP="8", blockage="20%", TI="8%",  color="green"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_12/UNB", runid=3, CTP="8", blockage="0.005%", TI="12%", color="gray"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_12/10PCT", runid=3, CTP="8", blockage="10%", TI="12%", color="cyan"),
    dict(path="Data/HIT_Turbines/CTP_8/TI_12/20PCT", runid=3, CTP="8", blockage="20%", TI="12%", color="magenta"),

    # CTP = 10
    dict(path="Data/HIT_Turbines/CTP_10/TI_3/UNB", runid=3, CTP="10", blockage="0.005%", TI="3%", color="black"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_3/10PCT",  runid=3, CTP="10", blockage="10%", TI="3%",  color="blue"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_3/20PCT",  runid=3, CTP="10", blockage="20%", TI="3%",  color="red"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_8/UNB", runid=3, CTP="10", blockage="0.005%", TI="8%", color="brown"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_8/10PCT",  runid=3, CTP="10", blockage="10%", TI="8%",  color="orange"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_8/20PCT",  runid=3, CTP="10", blockage="20%", TI="8%",  color="green"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_12/UNB", runid=3, CTP="10", blockage="0.005%", TI="12%", color="gray"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_12/10PCT", runid=3, CTP="10", blockage="10%", TI="12%", color="cyan"),
    dict(path="Data/HIT_Turbines/CTP_10/TI_12/20PCT", runid=3, CTP="10", blockage="20%", TI="12%", color="magenta"),
]


# ============================================================================
# HELPERS — computation
# ============================================================================

def get_latest_tidx(path, runid):
    """
    Find the latest available tidx for budget files in a given run.

    Scans the simulation directory for budget files matching the pattern:
    Run{runid:02d}_budget0_term01_t*.s3D

    Extracts time indices from filenames and returns the latest one.

    Parameters
    ----------
    path : str
        Path to the simulation directory
    runid : int
        Run ID (will be zero-padded to 2 digits)

    Returns
    -------
    int
        Latest available time index

    Raises
    ------
    FileNotFoundError
        If no budget files found or tidx cannot be parsed from filenames
    """
    sim_dir = Path(path)

    budget_files = list(sim_dir.glob(f"Run{runid:02d}_budget0_term01_t*.s3D"))

    if not budget_files:
        raise FileNotFoundError(
            f"No budget files found for Run{runid:02d} at {path}"
        )

    tidxs = []
    for f in budget_files:
        match = re.search(r"_t(\d+)_", f.name)
        if match:
            tidxs.append(int(match.group(1)))

    if not tidxs:
        raise FileNotFoundError(
            f"Could not parse tidx from budget filenames at {path}"
        )

    tidxs = sorted(set(tidxs))
    return tidxs[-1]


def compute_TI(u, v, w, ubar, vbar, wbar):
    """
    Compute turbulence intensity (%) averaged over y and z.

    TI is computed as:
        u_rms = sqrt((u'^2 + v'^2 + w'^2) / 3)
        mean_speed = sqrt(ubar^2 + vbar^2 + wbar^2)
        TI = (u_rms / mean_speed) * 100  [%]

    Computed at each x location by averaging over y and z.

    Parameters
    ----------
    u, v, w : ndarray
        Velocity components (shape: nx, ny, nz)
    ubar, vbar, wbar : ndarray
        Mean velocity components (shape: nx, ny, nz)

    Returns
    -------
    TI : 1-D array along x
        Turbulence intensity [%]
    """
    uprime = u - ubar
    vprime = v - vbar
    wprime = w - wbar

    urms_3d     = np.sqrt((uprime**2 + vprime**2 + wprime**2) / 3)
    barspeed_3d = np.sqrt(ubar**2 + vbar**2 + wbar**2)

    urms     = np.mean(urms_3d,     axis=(1, 2))
    barspeed = np.mean(barspeed_3d, axis=(1, 2))

    return np.where(barspeed != 0, (urms / barspeed) * 100, np.nan)


def _unique_values(results, key):
    """
    Return unique values of results[key] in first-seen order.

    Parameters
    ----------
    results : list of dict
        List of result dictionaries
    key : str
        Dictionary key to extract unique values from

    Returns
    -------
    list
        Unique values in order of first appearance
    """
    seen = []
    for r in results:
        if r[key] not in seen:
            seen.append(r[key])
    return seen


def tag(s):
    """
    Strip % from string for use in filenames.

    Parameters
    ----------
    s : str
        Input string

    Returns
    -------
    str
        String with '%' removed
    """
    return s.replace("%", "")


# ============================================================================
# HELPERS — plotting
# ============================================================================

def save_TI_plot(ax_data, title, savepath, figsize=(10, 6)):
    """
    Generic turbulence intensity comparison plot.

    Parameters
    ----------
    ax_data : list of tuple
        List of (x_array, ti_arr, cfg_dict) tuples where:
        - x_array: x coordinates
        - ti_arr: turbulence intensity values
        - cfg_dict: config dict with 'label' and 'color' keys
    title : str
        Plot title
    savepath : str
        Path to save figure
    figsize : tuple, optional
        Figure size (default: (10, 6))
    """
    fig, ax = plt.subplots(figsize=figsize)

    for x, ti_arr, cfg in ax_data:
        ax.plot(x, ti_arr, label=cfg["label"], color=cfg["color"])

    ax.set_xlabel("x/D")
    ax.set_ylabel("Turbulence Intensity (%)")
    ax.set_title(title)
    ax.legend()
    ax.grid()
    fig.tight_layout()
    fig.savefig(savepath, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: {savepath}")


# ============================================================================
# MAIN
# ============================================================================

print("=" * 80)
print("LOADING SIMULATIONS AND COMPUTING TURBULENCE INTENSITY")
print("=" * 80)

# --- Load all simulations and compute TI ---
results = []
skipped = 0
loaded = 0

for idx, cfg in enumerate(SIM_CONFIGS, 1):
    print(f"\n[{idx}/{len(SIM_CONFIGS)}] CTP={cfg['CTP']}, {cfg['blockage']} blocked, {cfg['TI']} TI")

    try:
        tidx = get_latest_tidx(cfg["path"], cfg["runid"])
        print(f"  → Found tidx={tidx}")
    except FileNotFoundError as e:
        print(f"  ⚠ SKIPPED: {e}")
        skipped += 1
        continue

    try:
        sim  = pio.BudgetIO(cfg["path"], padeops=True, runid=cfg["runid"])

        # Load mean velocities
        ubar = np.asarray(sim.slice(budget_terms="ubar", tidx=tidx)["ubar"])
        vbar = np.asarray(sim.slice(budget_terms="vbar", tidx=tidx)["vbar"])
        wbar = np.asarray(sim.slice(budget_terms="wbar", tidx=tidx)["wbar"])

        # Load instantaneous velocities
        u    = np.asarray(sim.slice(field_terms="u", tidx=tidx)["u"])
        v    = np.asarray(sim.slice(field_terms="v", tidx=tidx)["v"])
        w    = np.asarray(sim.slice(field_terms="w", tidx=tidx)["w"])

        # Compute turbulence intensity
        TI   = compute_TI(u, v, w, ubar, vbar, wbar)

        # Store result — note: "TI" (string label from cfg) is preserved via **cfg;
        # the computed array is stored separately as "ti_arr" to avoid collision.
        results.append({
            **cfg,
            "label":  f"{cfg['blockage']} Blockage, {cfg['TI']} TI, CTP={cfg['CTP']}",
            "x":      np.copy(sim.x),
            "ti_arr": TI,
        })

        print(f"  ✓ Loaded successfully")
        print(f"    - Grid shape: {u.shape}")
        print(f"    - TI range: {np.nanmin(TI):.3f}% - {np.nanmax(TI):.3f}%")
        print(f"    - TI mean: {np.nanmean(TI):.3f}%")

        loaded += 1

        del sim, u, v, w, ubar, vbar, wbar

    except Exception as e:
        print(f"  ⚠ ERROR loading data: {e}")
        skipped += 1
        continue


# --- Summary ---
print("\n" + "=" * 80)
print(f"LOADING SUMMARY: {loaded} loaded, {skipped} skipped, {len(SIM_CONFIGS)} total")
print("=" * 80)

if not results:
    print("No data loaded! Exiting.")
    exit(1)

# Extract unique parameter values
ctps      = _unique_values(results, "CTP")
ti_levels = _unique_values(results, "TI")       # "TI" is the string label, e.g. "3%"
blockages = _unique_values(results, "blockage")

print(f"CTP values: {ctps}")
print(f"TI levels: {ti_levels}")
print(f"Blockage ratios: {blockages}")
print()


# ============================================================================
# PLOTTING
# ============================================================================

print("=" * 80)
print("GENERATING PLOTS")
print("=" * 80)

# --- Plot 1: by (CTP, TI) — one line per blockage level ---
print("\n[Plot Set 1] By (CTP, TI) — one line per blockage level")
plot_count = 0
for ctp in ctps:
    for ti in ti_levels:
        subs = [r for r in results if r["CTP"] == ctp and r["TI"] == ti]
        if not subs:
            continue
        ax_data = [(r["x"], r["ti_arr"], {**r, "label": f"{r['blockage']} Blockage"})
                   for r in subs]
        save_TI_plot(
            ax_data,
            title=f"Turbulence Intensity vs x/D — {ti} TI, CTP = {ctp}",
            savepath=f"./TI_{tag(ti)}pct_CTP{ctp}_turbine.png",
        )
        plot_count += 1

print(f"  → Generated {plot_count} plots")


# --- Plot 2: by (CTP, blockage) — one line per TI level ---
print("\n[Plot Set 2] By (CTP, blockage) — one line per TI level")
plot_count = 0
for ctp in ctps:
    for blockage in blockages:
        subs = [r for r in results if r["CTP"] == ctp and r["blockage"] == blockage]
        if not subs:
            continue
        ax_data = [(r["x"], r["ti_arr"], {**r, "label": f"{r['TI']} TI"}) for r in subs]
        save_TI_plot(
            ax_data,
            title=f"Turbulence Intensity vs x/D — {blockage} Blocked, CTP = {ctp}",
            savepath=f"./TI_{tag(blockage)}pct_CTP{ctp}_turbine.png",
        )
        plot_count += 1

print(f"  → Generated {plot_count} plots")


# --- Plot 3: all cases together, one panel per CTP ---
print("\n[Plot Set 3] All cases per CTP")
plot_count = 0
for ctp in ctps:
    subs = [r for r in results if r["CTP"] == ctp]
    if not subs:
        continue
    ax_data = [(r["x"], r["ti_arr"], r) for r in subs]
    save_TI_plot(
        ax_data,
        title=f"Turbulence Intensity vs x/D — All Cases, CTP = {ctp}",
        savepath=f"./TI_all_CTP{ctp}_turbine.png",
        figsize=(14, 8),
    )
    plot_count += 1

print(f"  → Generated {plot_count} plots")

print("\n" + "=" * 80)
print("✓ ALL PLOTS GENERATED SUCCESSFULLY!")
print("=" * 80)