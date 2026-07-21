"""
HIT_Combined_Diagnostics.py (FULLY CORRECTED)

Now computes Turbulence Intensity (TI) exactly like Code 2:
- Loads full 3D fields (not just y-z slices)
- Computes fluctuations relative to time-averaged means
- Averages RMS magnitude over y-z at each x-location to get TI
- Extracts values at specified x-locations
"""

import numpy as np
import padeopsIO as pio
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

CONFIGS = [
    {
        "label": "CTP_4_TI_3_UNB",
        "path": "Data/HIT_Turbines/CTP_4/TI_3/UNB",
        "runid": 3,
    },
]

cfg = CONFIGS[0]

# The single list of tidx values used for BOTH the line-plot points and
# the field slice images. Edit freely.
TIDX_LIST = [10000, 20000, 25000, 29000, 30000, 40000, 50000, 60000, 63000]

# Controller shutdown timestep, for reference lines on the plots.
SHUTDOWN_TIMESTEP = 23971

# x-locations (in absolute coordinates) where to extract TI values
REGIONS = {
    "HIT": 23.6,
    "at_disk": 5.0,
    "downstream": 6.0,
    "upstream": 2.5,
}

# x-y plane location (z-coordinate) used for the field slice images —
# hub-height plan view
FIELD_SLICE_Z = 0
FIELD_TERMS = ["u"]  # fields to render as images

OUTPUT_DIR = Path("output") / cfg["label"]
FIELD_DIR = OUTPUT_DIR / "field_slices"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FIELD_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD SIMULATION (once)
# ============================================================
print(f"Loading simulation: {cfg['label']} ({cfg['path']})")
sim = pio.BudgetIO(
    cfg["path"],
    padeops=True,
    runid=cfg["runid"],
    normalize_origin="turbine",
)


# ============================================================
# TI CALCULATION (matches Code 2 exactly)
# ============================================================
def compute_TI_at_locations(sim, tidx, x_locations, field_names=("u", "v", "w")):
    """
    Compute Turbulence Intensity at specified x-locations.
    
    Matches Code 2's methodology exactly:
    1. Load full 3D instantaneous and time-averaged velocity fields
    2. Compute fluctuations: u' = u_inst - ubar_time_averaged
    3. Compute RMS magnitude: sqrt((u'^2 + v'^2 + w'^2) / 3) at each point
    4. Average RMS over y-z at each x-location
    5. Normalize by mean speed to get TI (%)
    
    Parameters
    ----------
    sim : BudgetIO
        Simulation object
    tidx : int
        Timestep index
    x_locations : dict
        Dict of {region_name: x_coord}
    field_names : tuple
        Velocity components ("u", "v", "w")
    
    Returns
    -------
    dict
        Keys: region names, values: dict with "ti", "urms", "mean_speed"
    """
    
    results = {}
    
    try:
        # Load FULL 3D instantaneous fields
        u_inst = np.asarray(sim.slice(field_terms="u", tidx=tidx)["u"])
        v_inst = np.asarray(sim.slice(field_terms="v", tidx=tidx)["v"])
        w_inst = np.asarray(sim.slice(field_terms="w", tidx=tidx)["w"])
        
        # Load FULL 3D time-averaged fields
        ubar = np.asarray(sim.slice(budget_terms="ubar", tidx=tidx)["ubar"])
        vbar = np.asarray(sim.slice(budget_terms="vbar", tidx=tidx)["vbar"])
        wbar = np.asarray(sim.slice(budget_terms="wbar", tidx=tidx)["wbar"])
        
        # Get x-coordinates
        x_coords = np.asarray(sim.x)
        
        # For each requested x-location, find nearest index and extract TI
        for region_name, x_loc in x_locations.items():
            # Find nearest x-index
            x_idx = np.argmin(np.abs(x_coords - x_loc))
            
            # Extract y-z slice at this x
            u_slice = u_inst[x_idx, :, :]
            v_slice = v_inst[x_idx, :, :]
            w_slice = w_inst[x_idx, :, :]
            
            ubar_slice = ubar[x_idx, :, :]
            vbar_slice = vbar[x_idx, :, :]
            wbar_slice = wbar[x_idx, :, :]
            
            # Compute fluctuations
            uprime = u_slice - ubar_slice
            vprime = v_slice - vbar_slice
            wprime = w_slice - wbar_slice
            
            # RMS magnitude at each point
            rms_magnitude = np.sqrt((uprime**2 + vprime**2 + wprime**2) / 3.0)
            
            # Average over y-z (matching Code 2's axis=(1,2) averaging)
            urms = np.mean(rms_magnitude)
            
            # Mean speed at this location
            mean_speed = np.sqrt(
                np.mean(ubar_slice)**2 + 
                np.mean(vbar_slice)**2 + 
                np.mean(wbar_slice)**2
            )
            
            # TI as percentage
            if mean_speed != 0:
                ti = (urms / mean_speed) * 100
            else:
                ti = np.nan
            
            results[region_name] = {
                "ti": ti,
                "urms": urms,
                "mean_speed": mean_speed,
                "mean_u": np.mean(ubar_slice),
                "success": True,
            }
    
    except Exception as e:
        print(f"    Error computing TI at tidx={tidx}: {e}")
        for region_name in x_locations:
            results[region_name] = {
                "ti": np.nan,
                "urms": np.nan,
                "mean_speed": np.nan,
                "mean_u": np.nan,
                "success": False,
            }
    
    return results


# ============================================================
# FIELD SLICE IMAGE
# ============================================================
def plot_field_slice(sim, tidx, field_terms, zlim, save_dir, label):
    """
    Renders and saves a field slice image (x-y plane at fixed z).
    """
    saved = []
    for field in field_terms:
        try:
            data = sim.slice(field_terms=[field], zlim=zlim, tidx=tidx)
            fig, ax = plt.subplots(figsize=(8, 5))
            data[field].imshow(ax=ax)
            ax.set_title(f"{label} | field={field} | tidx={tidx}")
            fname = save_dir / f"{label}_{field}_tidx{tidx}.png"
            plt.savefig(fname, dpi=150, bbox_inches="tight")
            plt.close(fig)
            saved.append(fname)
        except Exception as e:
            print(f"    Field plot failed at tidx={tidx}, field={field}: {e}")
    return saved


# ============================================================
# MAIN LOOP
# ============================================================
ti_results = {region: [] for region in REGIONS}
urms_results = {region: [] for region in REGIONS}
mean_speed_results = {region: [] for region in REGIONS}
mean_u_results = {region: [] for region in REGIONS}

print(f"\nProcessing {len(TIDX_LIST)} timesteps for {cfg['label']}...")
for i, tidx in enumerate(TIDX_LIST):
    print(f"[{i+1}/{len(TIDX_LIST)}] tidx={tidx}")

    # --- Compute TI at all regions ---
    data = compute_TI_at_locations(sim, tidx=tidx, x_locations=REGIONS)
    
    for region_name in REGIONS:
        ti_results[region_name].append(data[region_name]["ti"])
        urms_results[region_name].append(data[region_name]["urms"])
        mean_speed_results[region_name].append(data[region_name]["mean_speed"])
        mean_u_results[region_name].append(data[region_name]["mean_u"])

    # --- Field slice image ---
    plot_field_slice(sim, tidx, FIELD_TERMS, FIELD_SLICE_Z, FIELD_DIR, cfg["label"])

# Convert to arrays
tidx_arr = np.array(TIDX_LIST)
for region in REGIONS:
    ti_results[region] = np.array(ti_results[region])
    urms_results[region] = np.array(urms_results[region])
    mean_speed_results[region] = np.array(mean_speed_results[region])
    mean_u_results[region] = np.array(mean_u_results[region])


# ============================================================
# LINE PLOTS: TI + Mean Speed
# ============================================================
colors = {"HIT": "red", "at_disk": "blue", "downstream": "green", "upstream": "orange"}
region_labels = {name: f"{name} (x={x_loc:g})" for name, x_loc in REGIONS.items()}

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), constrained_layout=True)

for _ax in axes:
    _ax.set_box_aspect(0.75)

# TI (%)
ax = axes[0]
for region_name in REGIONS:
    vals = ti_results[region_name]
    valid = ~np.isnan(vals)
    if np.any(valid):
        ax.plot(tidx_arr[valid], vals[valid], marker="o", linewidth=2, markersize=7,
                 label=region_labels[region_name], color=colors[region_name], alpha=0.85)
if SHUTDOWN_TIMESTEP is not None and tidx_arr.min() <= SHUTDOWN_TIMESTEP <= tidx_arr.max():
    ax.axvline(SHUTDOWN_TIMESTEP, color="black", linestyle="--", linewidth=2, label="Shutdown")
ax.set_xlabel("Timestep", fontweight="bold")
ax.set_ylabel("Turbulence Intensity (%)", fontweight="bold")
ax.set_title(f"{cfg['label']}: Turbulence Intensity (TI)", fontweight="bold")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Mean Speed
ax = axes[1]
for region_name in REGIONS:
    vals = mean_speed_results[region_name]
    valid = ~np.isnan(vals)
    if np.any(valid):
        ax.plot(tidx_arr[valid], vals[valid], marker="s", linewidth=2, markersize=7,
                 label=region_labels[region_name], color=colors[region_name], alpha=0.85)
if SHUTDOWN_TIMESTEP is not None and tidx_arr.min() <= SHUTDOWN_TIMESTEP <= tidx_arr.max():
    ax.axvline(SHUTDOWN_TIMESTEP, color="black", linestyle="--", linewidth=2, label="Shutdown")
ax.set_xlabel("Timestep", fontweight="bold")
ax.set_ylabel("Mean Speed (time-averaged)", fontweight="bold")
ax.set_title(f"{cfg['label']}: Mean Speed", fontweight="bold")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.ticklabel_format(axis="y", useOffset=False, style="plain")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.7f"))

line_plot_path = OUTPUT_DIR / f"{cfg['label']}_TI_timeseries.png"
plt.savefig(line_plot_path, dpi=150, bbox_inches="tight")
plt.close(fig)

print("\n" + "=" * 60)
print(f"Done. Outputs for {cfg['label']}:")
print(f"  Line plot:    {line_plot_path}")
print(f"  Field images: {FIELD_DIR}/ ({len(TIDX_LIST)} timesteps x {len(FIELD_TERMS)} fields)")
print("=" * 60)

# Print sample values for debugging
print("\n" + "=" * 60)
print("Sample TI values (should be ~6-14% to match Code 2):")
print("=" * 60)
for region in REGIONS:
    print(f"{region:15} at tidx=20000: TI = {ti_results[region][6]:6.2f}%")