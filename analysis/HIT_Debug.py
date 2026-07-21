"""
HIT_Combined_Diagnostics.py (NO BUDGET FILES VERSION - COMBINED FIELD PLOTS - FIXED)

Uses padeopsIO's native imshow() for proper visualization while combining plots.
"""

import numpy as np
import padeopsIO as pio
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.colors import Normalize
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

CONFIGS = [
    {
        "label": "CTP_4_TI_8_UNB",
        "path": "Data/HIT_Turbines/CTP_4/TI_8/UNB",
        "runid": 3,
    },
]

cfg = CONFIGS[0]

# The single list of tidx values used for both diagnostics
TIDX_LIST = [10000, 15000, 25000, 30000, 31000, 40000, 45000, 50000, 55000]

# Timesteps to use for computing time-averaged means
TIME_AVERAGING_TIDX_LIST = [10000, 15000, 25000, 30000, 31000, 40000, 45000, 50000, 55000]

# Controller shutdown timestep, for reference lines on the plots.
SHUTDOWN_TIMESTEP = 30118

# x-locations where to extract TI values
REGIONS = {
    "HIT": 68.75,
    "at_disk": 5.0,
    "downstream": 6.0,
    "upstream": 2.5,
}

# x-y plane location (z-coordinate) used for the field slice images
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
# COMPUTE TIME-AVERAGED FIELDS
# ============================================================
def compute_time_averaged_fields(sim, tidx_list, field_names=("u", "v", "w")):
    """
    Compute time-averaged velocity fields from instantaneous snapshots.
    
    Parameters
    ----------
    sim : BudgetIO
        Simulation object
    tidx_list : list
        List of timestep indices to average over
    field_names : tuple
        Velocity components ("u", "v", "w")
    
    Returns
    -------
    dict
        Keys: field names, values: 3D arrays (time-averaged fields)
    """
    print(f"\nComputing time-averaged fields from {len(tidx_list)} timesteps...")
    
    time_averaged_fields = {}
    
    for field in field_names:
        field_sum = None
        
        for tidx in tidx_list:
            try:
                field_data = np.asarray(sim.slice(field_terms=field, tidx=tidx)[field])
                
                if field_sum is None:
                    field_sum = field_data.copy()
                else:
                    field_sum += field_data
                    
            except Exception as e:
                print(f"  Warning: Could not load {field} at tidx={tidx}: {e}")
                continue
        
        if field_sum is not None:
            time_averaged_fields[field] = field_sum / len(tidx_list)
            print(f"  ✓ {field}: mean = {np.mean(time_averaged_fields[field]):.6f}")
        else:
            print(f"  ✗ Failed to compute time average for {field}")
    
    return time_averaged_fields


# ============================================================
# TI CALCULATION (without budget files)
# ============================================================
def compute_TI_at_locations(sim, tidx, x_locations, time_averaged_fields, 
                            field_names=("u", "v", "w")):
    """
    Compute Turbulence Intensity at specified x-locations.
    """
    
    results = {}
    
    try:
        # Load INSTANTANEOUS 3D fields at this tidx
        u_inst = np.asarray(sim.slice(field_terms="u", tidx=tidx)["u"])
        v_inst = np.asarray(sim.slice(field_terms="v", tidx=tidx)["v"])
        w_inst = np.asarray(sim.slice(field_terms="w", tidx=tidx)["w"])
        
        # Use pre-computed time-averaged fields
        ubar = time_averaged_fields["u"]
        vbar = time_averaged_fields["v"]
        wbar = time_averaged_fields["w"]
        
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
            
            # Average over y-z
            urms = np.mean(rms_magnitude)
            
            # Mean speed at this location (from time-averaged fields)
            mean_u = np.mean(ubar_slice)
            mean_v = np.mean(vbar_slice)
            mean_w = np.mean(wbar_slice)
            mean_speed = np.sqrt(mean_u**2 + mean_v**2 + mean_w**2)
            
            # TI as percentage
            if mean_speed != 0:
                ti = (urms / mean_speed) * 100
            else:
                ti = np.nan
            
            results[region_name] = {
                "ti": ti,
                "urms": urms,
                "mean_speed": mean_speed,
                "mean_u": mean_u,
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
# FIELD SLICE IMAGES (COMBINED WITH PADEOPSIO IMSHOW)
# ============================================================
def plot_field_slices_combined(sim, tidx_list, field_terms, zlim, save_dir, label):
    """
    Create combined field slice plots for all timesteps optimized for PowerPoint slides.
    
    Figure size is landscape oriented with proper proportions for 3x3 grid.
    """
    saved = []
    
    for field in field_terms:
        print(f"\n  Creating combined plot for field={field}...")
        
        # First pass: load all data objects
        data_objects = []
        valid_tidx = []
        
        for tidx in tidx_list:
            try:
                data = sim.slice(field_terms=[field], zlim=zlim, tidx=tidx)
                data_objects.append(data)
                valid_tidx.append(tidx)
            except Exception as e:
                print(f"    Warning: Could not load {field} at tidx={tidx}: {e}")
                continue
        
        if not data_objects:
            print(f"    ✗ Failed to load any data for field={field}")
            continue
        
        # Get raw numpy arrays to compute global min/max for normalization
        raw_arrays = [np.asarray(d[field]) for d in data_objects]
        global_min = np.min([np.min(arr) for arr in raw_arrays])
        global_max = np.max([np.max(arr) for arr in raw_arrays])
        norm = plt.Normalize(vmin=global_min, vmax=global_max)
        
        # Determine grid layout (3 columns)
        n_plots = len(data_objects)
        n_cols = 3
        n_rows = int(np.ceil(n_plots / n_cols))
        
        # Landscape PowerPoint proportions: wider than tall
        # 16:9 aspect ratio maintained but scaled for 3x3 grid
        figsize = (16, 10)  # Width x Height - landscape oriented
        
        fig, axes = plt.subplots(
            n_rows, n_cols, 
            figsize=figsize,
            constrained_layout=False
        )
        
        # Flatten axes array for easier iteration
        if n_plots == 1:
            axes = np.array([axes])
        else:
            axes = axes.flatten()
        
        # Track image objects for colorbar
        images = []
        
        # Plot each field slice using padeopsIO's imshow
        for idx, (data_obj, tidx, ax) in enumerate(zip(data_objects, valid_tidx, axes)):
            # Use padeopsIO's native imshow
            data_obj[field].imshow(ax=ax)
            
            ax.set_title(f"tidx={tidx}", fontweight="bold", fontsize=14)
            ax.set_xlabel("x/D", fontsize=11, fontweight="bold")
            ax.set_ylabel("y/D", fontsize=11, fontweight="bold")
            ax.tick_params(labelsize=9)
            
            # Get the image artist
            im = ax.get_images()[0]
            
            # Apply normalization and colormap
            im.set_norm(norm)
            im.set_cmap("viridis")
            
            images.append(im)
            
            # Remove the individual colorbar that padeopsIO creates
            for cbar_ax in list(fig.axes):
                if cbar_ax != ax and hasattr(cbar_ax, 'colorbar'):
                    cbar_ax.remove()
        
        # Remove all existing colorbar axes
        axes_to_remove = [ax for ax in fig.axes[n_rows*n_cols:]]
        for ax in axes_to_remove:
            ax.remove()
        
        # Hide unused subplots
        for idx in range(len(data_objects), len(axes)):
            axes[idx].set_visible(False)
        
        # Add single colorbar on the right side
        cbar_ax = fig.add_axes([0.93, 0.15, 0.015, 0.70])
        cbar = fig.colorbar(images[0], cax=cbar_ax)
        cbar.set_label(f"{field} velocity", fontweight="bold", fontsize=12)
        cbar.ax.tick_params(labelsize=9)
        
        # Tight layout with minimal spacing
        plt.subplots_adjust(left=0.05, right=0.92, top=0.92, bottom=0.06, 
                           hspace=0.28, wspace=0.18)
        
        # Title with global min/max info
        fig.suptitle(
            f"{label}: {field}-velocity field (z={zlim}) | "
            f"Range: [{global_min:.6f}, {global_max:.6f}]",
            fontsize=16, fontweight="bold", y=0.98
        )
        
        # Save figure with high DPI for quality
        fname = save_dir / f"{label}_{field}_slices_combined.png"
        plt.savefig(fname, dpi=150, bbox_inches="tight")
        plt.close(fig)
        saved.append(fname)
        print(f"    ✓ Saved: {fname}")
    
    return saved

# ============================================================
# MAIN EXECUTION
# ============================================================

# Step 1: Compute time-averaged fields once
time_averaged_fields = compute_time_averaged_fields(
    sim, 
    tidx_list=TIME_AVERAGING_TIDX_LIST,
    field_names=("u", "v", "w")
)

if not all(key in time_averaged_fields for key in ["u", "v", "w"]):
    print("ERROR: Could not compute all time-averaged fields. Exiting.")
    exit(1)

# Step 2: Process each timestep for TI calculations
ti_results = {region: [] for region in REGIONS}
urms_results = {region: [] for region in REGIONS}
mean_speed_results = {region: [] for region in REGIONS}
mean_u_results = {region: [] for region in REGIONS}

print(f"\nProcessing {len(TIDX_LIST)} timesteps for {cfg['label']}...")
for i, tidx in enumerate(TIDX_LIST):
    print(f"[{i+1}/{len(TIDX_LIST)}] tidx={tidx}")

    # Compute TI at all regions
    data = compute_TI_at_locations(
        sim, 
        tidx=tidx, 
        x_locations=REGIONS,
        time_averaged_fields=time_averaged_fields
    )
    
    for region_name in REGIONS:
        ti_results[region_name].append(data[region_name]["ti"])
        urms_results[region_name].append(data[region_name]["urms"])
        mean_speed_results[region_name].append(data[region_name]["mean_speed"])
        mean_u_results[region_name].append(data[region_name]["mean_u"])

# Step 3: Create combined field slice plots
print(f"\nGenerating combined field slice plots...")
plot_field_slices_combined(
    sim, 
    tidx_list=TIDX_LIST,
    field_terms=FIELD_TERMS,
    zlim=FIELD_SLICE_Z,
    save_dir=FIELD_DIR,
    label=cfg["label"]
)

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
ax.set_ylabel("Mean Speed", fontweight="bold")
ax.set_title(f"{cfg['label']}: Mean Speed", fontweight="bold")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.ticklabel_format(axis="y", useOffset=False, style="plain")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.7f"))

line_plot_path = OUTPUT_DIR / f"{cfg['label']}_TI_timeseries_no_budget.png"
plt.savefig(line_plot_path, dpi=150, bbox_inches="tight")
plt.close(fig)

print("\n" + "=" * 60)
print(f"Done. Outputs for {cfg['label']}:")
print(f"  Line plot:    {line_plot_path}")
print(f"  Field plots:  {FIELD_DIR}/ (combined per field)")
print("=" * 60)

# Print sample values for debugging
print("\n" + "=" * 60)
print("Sample TI values:")
print("=" * 60)
for region in REGIONS:
    print(f"{region:15} at tidx=20000: TI = {ti_results[region][6]:6.2f}%")