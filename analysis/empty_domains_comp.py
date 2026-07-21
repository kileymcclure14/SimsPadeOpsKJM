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

# **TARGET X LOCATION FOR TEMPORAL EVALUATION**
X_EVAL = 4.0

# **USE BUDGETS IN THE LAST 10,000 TIMESTEPS**
MAX_TIMESTEPS = 10000

SIM_CONFIGS = [

    # CTP = 2
    dict(path="Data/HIT_AD/CTP_2/TI_3/10PCT", runid=2, CTP="2", blockage="10%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_2/TI_3/20PCT", runid=2, CTP="2", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_2/TI_6/10PCT", runid=2, CTP="2", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_2/TI_6/20PCT", runid=2, CTP="2", blockage="20%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_2/TI_10/10PCT", runid=2, CTP="2", blockage="10%", TI="10%", color="green"),
    #dict(path="Data/HIT_AD/CTP_2/TI_10/20PCT", runid=2, CTP="2", blockage="20%", TI="10%", color="green"),

    # CTP = 4
    dict(path="Data/HIT_AD/CTP_4/TI_3/10PCT", runid=2, CTP="4", blockage="10%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_4/TI_3/20PCT", runid=2, CTP="4", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_4/TI_6/10PCT", runid=2, CTP="4", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_4/TI_6/20PCT", runid=2, CTP="4", blockage="20%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_4/TI_10/10PCT", runid=2, CTP="4", blockage="10%", TI="10%", color="green"),
    #dict(path="Data/HIT_AD/CTP_4/TI_10/20PCT", runid=2, CTP="4", blockage="20%", TI="10%", color="green"),

    # CTP = 6
    dict(path="Data/HIT_AD/CTP_6/TI_3/10PCT", runid=2, CTP="6", blockage="10%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_6/TI_3/20PCT", runid=2, CTP="6", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_6/TI_6/10PCT", runid=2, CTP="6", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_6/TI_6/20PCT", runid=2, CTP="6", blockage="20%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_6/TI_10/10PCT", runid=2, CTP="6", blockage="10%", TI="10%", color="green"),
    #dict(path="Data/HIT_AD/CTP_6/TI_10/20PCT", runid=2, CTP="6", blockage="20%", TI="10%", color="green"),

    # CTP = 8
    dict(path="Data/HIT_AD/CTP_8/TI_3/10PCT", runid=2, CTP="8", blockage="10%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_8/TI_3/20PCT", runid=2, CTP="8", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_8/TI_6/10PCT", runid=2, CTP="8", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_8/TI_6/20PCT", runid=2, CTP="8", blockage="20%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_8/TI_10/10PCT", runid=2, CTP="8", blockage="10%", TI="10%", color="green"),
    #dict(path="Data/HIT_AD/CTP_8/TI_10/20PCT", runid=2, CTP="8", blockage="20%", TI="10%", color="green"),

    # CTP = 10
    dict(path="Data/HIT_AD/CTP_10/TI_3/10PCT", runid=2, CTP="10", blockage="10%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_10/TI_3/20PCT", runid=2, CTP="10", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_10/TI_6/10PCT", runid=2, CTP="10", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_10/TI_6/20PCT", runid=2, CTP="10", blockage="20%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_10/TI_10/10PCT", runid=2, CTP="10", blockage="10%", TI="10%", color="green"),
    #dict(path="Data/HIT_AD/CTP_10/TI_10/20PCT", runid=2, CTP="10", blockage="20%", TI="10%", color="green"),
]

# ============================================================================
# HELPERS — computation
# ============================================================================

def get_all_tidx(path, runid):
    """Find all available tidx values for budget files in a given run."""
    sim_dir = Path(path)
    budget_files = list(sim_dir.glob(f"Run{runid:02d}_budget0_term01_t*.s3D"))

    if not budget_files:
        raise FileNotFoundError(f"No budget files found for Run{runid:02d} at {path}")

    tidxs = []
    for f in budget_files:
        match = re.search(r"_t(\d+)_", f.name)
        if match:
            tidxs.append(int(match.group(1)))

    if not tidxs:
        raise FileNotFoundError(f"Could not parse tidx from budget filenames at {path}")

    tidxs = sorted(set(tidxs))
    return tidxs


def get_selected_tidx(path, runid, max_timesteps=MAX_TIMESTEPS):
    """
    Get budget timesteps that fall within the last max_timesteps of the simulation.
    
    This finds the maximum tidx available, then selects all budget timesteps
    that occurred in the last max_timesteps (i.e., tidx >= max_tidx - max_timesteps).
    
    Parameters
    ----------
    path : str
        Simulation directory path
    runid : int
        Run ID
    max_timesteps : int
        Number of most recent timesteps to consider
    
    Returns
    -------
    list
        Selected tidx values that fall within the last max_timesteps
    """
    all_tidxs = get_all_tidx(path, runid)
    
    if len(all_tidxs) == 0:
        raise ValueError("No budget timesteps found")
    
    # Determine the window: last max_timesteps
    max_tidx = max(all_tidxs)
    min_tidx_window = max_tidx - max_timesteps
    
    # Filter budgets that fall within this window
    selected = [tidx for tidx in all_tidxs if tidx >= min_tidx_window]
    
    return selected


def get_latest_tidx(path, runid):
    """Find the latest available tidx for budget files in a given run."""
    return get_all_tidx(path, runid)[-1]


def compute_TI(u, v, w, ubar, vbar, wbar):
    """
    Compute turbulence intensity (%) averaged over y and z.

    TI is computed as:
        u_rms = sqrt((u'^2 + v'^2 + w'^2) / 3)
        mean_speed = sqrt(ubar^2 + vbar^2 + wbar^2)
        TI = (u_rms / mean_speed) * 100  [%]
    """
    uprime = u - ubar
    vprime = v - vbar
    wprime = w - wbar

    urms_3d     = np.sqrt((uprime**2 + vprime**2 + wprime**2) / 3)
    barspeed_3d = np.sqrt(ubar**2 + vbar**2 + wbar**2)

    urms     = np.mean(urms_3d,     axis=(1, 2))
    barspeed = np.mean(barspeed_3d, axis=(1, 2))

    return np.where(barspeed != 0, (urms / barspeed) * 100, np.nan)


def find_closest_x_index(x_array, x_target):
    """
    Find the index of the closest x value in the array to the target x.
    
    Parameters
    ----------
    x_array : numpy array
        Array of x coordinates
    x_target : float
        Target x coordinate (e.g., 4.0 for turbine location)
    
    Returns
    -------
    int
        Index of closest x value
    """
    return np.argmin(np.abs(x_array - x_target))


def _unique_values(results, key):
    """Return unique values of results[key] in first-seen order."""
    seen = []
    for r in results:
        if r[key] not in seen:
            seen.append(r[key])
    return seen


def tag(s):
    """Strip % from string for use in filenames."""
    return s.replace("%", "")


def find_ti_data_file(path, blockage):
    """
    Find the ti_data.npz file for a given simulation path and blockage level.
    
    Searches for ti_data.npz in the blockage directory.
    """
    ti_file = Path(path) / "ti_data.npz"
    if ti_file.exists():
        return ti_file
    else:
        return None


# ============================================================================
# MAIN
# ============================================================================

print("=" * 80)
print("LOADING SIMULATIONS AND CREATING SUBPLOTS")
print("=" * 80)
print(f"Using data from the last {MAX_TIMESTEPS} timesteps for:")
print(f"  - Mean TI spatial profile (subplot 2)")
print(f"  - Mean TI_factor (subplot 1)")
print(f"  - Mean TI% at x={X_EVAL} (subplot 4)")
print(f"Temporal TI evaluation location: x = {X_EVAL}")

# Load all data
results = []
ti_data_all = {}  # Store TI_factor and TIDX data by (CTP, blockage)
ti_temporal_data = {}  # Store TI evolution over time for each domain

for idx, cfg in enumerate(SIM_CONFIGS, 1):
    print(f"\n[{idx}/{len(SIM_CONFIGS)}] CTP={cfg['CTP']}, {cfg['blockage']} blocked, {cfg['TI']} TI, runid={cfg['runid']}")
    
    try:
        # Get budget timesteps in the last MAX_TIMESTEPS window
        selected_tidxs = get_selected_tidx(cfg["path"], cfg["runid"], max_timesteps=MAX_TIMESTEPS)
        all_tidxs = get_all_tidx(cfg["path"], cfg["runid"])
        max_tidx = max(all_tidxs)
        min_window = max_tidx - MAX_TIMESTEPS
        print(f"  → Total timesteps in simulation: up to tidx={max_tidx}")
        print(f"  → Last {MAX_TIMESTEPS} timesteps window: tidx >= {min_window}")
        print(f"  → Found {len(selected_tidxs)} budget files in this window (tidx: {selected_tidxs[0]} to {selected_tidxs[-1]})")
    except FileNotFoundError as e:
        print(f"  ⚠ SKIPPED: {e}")
        continue

    try:
        # Load and average data across selected budget timesteps
        # *** ALL DATA COMES FROM THE LAST 10,000 TIMESTEPS ***
        sim = pio.BudgetIO(cfg["path"], padeops=True, runid=cfg["runid"])
        
        ti_arrays = []
        ti_temporal_dict = {"tidx": [], "ti_at_x4": []}  # Store temporal data at x=X_EVAL
        x_coord = None
        x_index_4 = None
        
        # Load each selected budget timestep (all within last MAX_TIMESTEPS)
        for tidx_idx, tidx in enumerate(selected_tidxs):
            if tidx_idx % max(1, len(selected_tidxs) // 10) == 0:  # Progress update every 10%
                print(f"    Loading timestep {tidx_idx+1}/{len(selected_tidxs)} (tidx={tidx})")
            
            ubar = np.asarray(sim.slice(budget_terms="ubar", tidx=tidx)["ubar"])
            vbar = np.asarray(sim.slice(budget_terms="vbar", tidx=tidx)["vbar"])
            wbar = np.asarray(sim.slice(budget_terms="wbar", tidx=tidx)["wbar"])

            u    = np.asarray(sim.slice(field_terms="u", tidx=tidx)["u"])
            v    = np.asarray(sim.slice(field_terms="v", tidx=tidx)["v"])
            w    = np.asarray(sim.slice(field_terms="w", tidx=tidx)["w"])

            TI_data = compute_TI(u, v, w, ubar, vbar, wbar)
            ti_arrays.append(TI_data)
            
            # Store x coordinate on first timestep
            if x_coord is None:
                x_coord = np.copy(sim.x)
                # PASS X_EVAL TO find_closest_x_index() ← X=4 USED HERE
                x_index_4 = find_closest_x_index(x_coord, x_target=X_EVAL)
                x_at_index = x_coord[x_index_4]
                print(f"    → Found x={x_at_index:.4f} closest to target x={X_EVAL} at index {x_index_4}")
            
            # Extract TI value at x=X_EVAL (x=4)
            ti_at_x_eval = TI_data[x_index_4]
            ti_temporal_dict["tidx"].append(tidx)
            ti_temporal_dict["ti_at_x4"].append(ti_at_x_eval)
            
        
        # Time-average the TI values across the last MAX_TIMESTEPS
        # *** THIS IS THE MEAN TI PROFILE PLOTTED IN SUBPLOT 2 ***
        ti_arrays = np.array(ti_arrays)
        TI_data_avg = np.nanmean(ti_arrays, axis=0)

        results.append({
            **cfg,
            "x": x_coord,
            "ti_arr": TI_data_avg,  # Mean TI profile from last MAX_TIMESTEPS
            "ti_temporal": ti_temporal_dict,  # Store temporal evolution at x=X_EVAL
            "selected_tidxs": selected_tidxs,  # These are all in the last MAX_TIMESTEPS window
            "x_index_4": x_index_4,
            "max_tidx": max_tidx,
            "min_window": min_window,
            "num_spatial_samples": len(selected_tidxs),  # Number of timesteps averaged for spatial profile
        })

        # Store temporal data by (CTP, blockage, TI%)
        temporal_key = (cfg["CTP"], cfg["blockage"], cfg["TI"])
        ti_temporal_data[temporal_key] = ti_temporal_dict

        print(f"  ✓ Loaded and time-averaged successfully over {len(selected_tidxs)} timesteps")
        print(f"    - Mean TI profile (spatial average from last {MAX_TIMESTEPS} timesteps): {np.nanmean(TI_data_avg):.3f}%")
        print(f"    - Mean TI at x={X_EVAL}: {np.nanmean(np.array(ti_temporal_dict['ti_at_x4'])):.3f}%")

        del sim, u, v, w, ubar, vbar, wbar, ti_arrays

    except Exception as e:
        print(f"  ⚠ ERROR loading data: {e}")
        import traceback
        traceback.print_exc()
        continue

    # Try to load TI_factor data (only once per blockage level)
    try:
        ti_file = find_ti_data_file(cfg["path"], cfg["blockage"])
        if ti_file and (cfg["CTP"], cfg["blockage"]) not in ti_data_all:
            data = np.load(ti_file)
            tidx_data = data["TIDX"]
            ti_fact_data = data["TI_fact"]
            
            # Get the window from the first matching result
            matching_result = next((r for r in results if r["CTP"] == cfg["CTP"] and r["blockage"] == cfg["blockage"]), None)
            if matching_result:
                min_window = matching_result["min_window"]
                
                # Handle mismatched array lengths
                if len(tidx_data) != len(ti_fact_data):
                    min_len = min(len(tidx_data), len(ti_fact_data))
                    tidx_data = tidx_data[:min_len]
                    ti_fact_data = ti_fact_data[:min_len]
                
                # *** FILTER TO ONLY TIMESTEPS IN THE LAST MAX_TIMESTEPS WINDOW ***
                # This ensures mean TI_factor uses the same window as mean TI profile
                window_mask = tidx_data >= min_window
                tidx_data_filtered = tidx_data[window_mask]
                ti_fact_data_filtered = ti_fact_data[window_mask]
                
                # Remove any NaN or inf values
                valid_mask = ~(np.isnan(ti_fact_data_filtered) | np.isinf(ti_fact_data_filtered) | 
                              np.isnan(tidx_data_filtered) | np.isinf(tidx_data_filtered))
                tidx_data_filtered = tidx_data_filtered[valid_mask]
                ti_fact_data_filtered = ti_fact_data_filtered[valid_mask]
                
                # Calculate mean of TI_fact from LAST MAX_TIMESTEPS only
                # *** THIS IS THE MEAN SHOWN IN SUBPLOT 1 ***
                mean_ti_fact = float(np.mean(ti_fact_data_filtered)) if len(ti_fact_data_filtered) > 0 else np.nan
                
                # Store both filtered (for plotting) and full (for reference) data
                ti_data_all[(cfg["CTP"], cfg["blockage"])] = {
                    "TIDX": tidx_data_filtered,
                    "TI_fact": ti_fact_data_filtered,
                    "mean_ti_fact": mean_ti_fact,
                    "num_factor_samples": len(ti_fact_data_filtered),
                }
                print(f"  ✓ Loaded TI_factor data from {ti_file}")
                print(f"    - Found {len(ti_fact_data_filtered)} TI_fact values in window (tidx >= {min_window})")
                print(f"    - Mean TI_fact (from last {MAX_TIMESTEPS} timesteps): {mean_ti_fact:.4f}")
    except Exception as e:
        print(f"  ⚠ ERROR loading TI_factor data: {e}")


print("\n" + "=" * 80)
print(f"LOADED DATA SUMMARY")
print("=" * 80)
print(f"Total results: {len(results)}")
print(f"TI_factor files loaded: {len(ti_data_all)}")
print(f"Temporal TI data loaded: {len(ti_temporal_data)}")

# Show statistics on how many timesteps were averaged
print("\nData compilation from last MAX_TIMESTEPS window:")
print(f"{'Config':<40} {'Spatial Samples':<20} {'TI_factor Samples':<20}")
print("-" * 80)
for r in results:
    num_spatial = r.get("num_spatial_samples", 0)
    config_str = f"CTP={r['CTP']}, {r['blockage']}, {r['TI']}"
    ti_factor_key = (r["CTP"], r["blockage"])
    num_factor = ti_data_all.get(ti_factor_key, {}).get("num_factor_samples", "N/A")
    print(f"{config_str:<40} {num_spatial:<20} {str(num_factor):<20}")


# ============================================================================
# PLOTTING - CREATE SUBPLOTS FOR EACH (CTP, BLOCKAGE, TI%) COMBINATION
# ============================================================================

print("\n" + "=" * 80)
print("CREATING SUBPLOTS FOR EACH (CTP, BLOCKAGE, TI%) COMBINATION")
print("=" * 80)

# Get unique combinations
ctps = sorted(set([cfg["CTP"] for cfg in SIM_CONFIGS]))
blockages = sorted(set([cfg["blockage"] for cfg in SIM_CONFIGS]))
ti_levels = sorted(set([cfg["TI"] for cfg in SIM_CONFIGS]))

print(f"CTPs: {ctps}")
print(f"Blockages: {blockages}")
print(f"TI Levels: {ti_levels}")
print(f"\nTotal combinations to generate: {len(ctps) * len(blockages) * len(ti_levels)}")

subplot_count = 0

for ctp in ctps:
    for blockage in blockages:
        for ti_level in ti_levels:
            # Get result for this (CTP, blockage, TI%) combo
            matching_result = None
            for r in results:
                if r["CTP"] == ctp and r["blockage"] == blockage and r["TI"] == ti_level:
                    matching_result = r
                    break
            
            if matching_result is None:
                continue
            
            # Get TI_factor data (based on CTP and blockage only, not TI)
            ti_factor_key = (ctp, blockage)
            has_ti_factor = ti_factor_key in ti_data_all
            
            subplot_count += 1
            print(f"\n[{subplot_count}] Creating subplot for CTP={ctp}, {blockage}, {ti_level}...")
            
            # Create figure with 2x3 subplots (6 total)
            fig, axes = plt.subplots(2, 3, figsize=(20, 10))
            fig.suptitle(f"CTP={ctp}, {blockage} Blocked, {ti_level} TI\n(Time-Averaged over {len(matching_result['selected_tidxs'])} budget timesteps from last {MAX_TIMESTEPS})", 
                         fontsize=14, fontweight='bold')
            
            # ========== ROW 1: SPATIAL PROFILES ==========
            
            # --- Subplot 1: TI_factor vs TIDX with Mean Line (from last MAX_TIMESTEPS) ---
            ax1 = axes[0, 0]
            if has_ti_factor:
                ti_data = ti_data_all[ti_factor_key]
                tidx = ti_data["TIDX"]
                ti_fact = ti_data["TI_fact"]
                mean_ti_fact = ti_data["mean_ti_fact"]
                
                if len(tidx) > 0:
                    # Plot TI_factor time series (only from last MAX_TIMESTEPS window)
                    ax1.plot(tidx, ti_fact, '-', color='steelblue', linewidth=2, label='TI Factor (last 10k tidx)')
                    
                    # Add horizontal line for mean (calculated from last MAX_TIMESTEPS)
                    ax1.axhline(y=mean_ti_fact, color='red', linestyle='--', linewidth=2.5, 
                               alpha=0.7, label=f'Mean TI_fact = {mean_ti_fact:.4f}')
                    
                    ax1.set_xlabel("Time Index (TIDX)")
                    ax1.set_ylabel("TI Factor")
                    ax1.set_title("TI Factor Evolution (last 10k tidx)")
                    ax1.legend(fontsize=10, loc='best')
                    ax1.grid(True, alpha=0.3)
                else:
                    ax1.text(0.5, 0.5, "No valid TI_factor data\n(all NaN/Inf)", ha='center', va='center', transform=ax1.transAxes)
                    ax1.set_title("TI Factor Evolution")
            else:
                ax1.text(0.5, 0.5, "No TI_factor data", ha='center', va='center', transform=ax1.transAxes)
                ax1.set_title("TI Factor Evolution")
            
            # --- Subplot 2: Mean TI Profile (Spatial) - from last MAX_TIMESTEPS ---
            ax2 = axes[0, 1]
            if matching_result is not None:
                color = matching_result["color"]
                ax2.plot(matching_result["x"], matching_result["ti_arr"], 
                        color=color, linewidth=2.5, marker='o', markersize=5, markevery=10, label=f"{blockage}")
                
                # Mark the location x=X_EVAL with a vertical line
                x_at_eval = matching_result["x"][matching_result["x_index_4"]]
                ax2.axvline(x=x_at_eval, color='red', linestyle='--', linewidth=2, alpha=0.6, label=f'Eval at x={x_at_eval:.2f}')
                
                ax2.set_xlabel("x/D")
                ax2.set_ylabel("Mean TI (%)")
                ax2.set_title(f"Mean TI Profile vs x/D (from last {MAX_TIMESTEPS})")
                ax2.legend()
                ax2.grid(True, alpha=0.3)
            else:
                ax2.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax2.transAxes)
                ax2.set_title(f"Mean TI Profile vs x/D (from last {MAX_TIMESTEPS})")
            
            # --- Subplot 3: Spatial Statistics ---
            ax3 = axes[0, 2]
            if matching_result is not None:
                ti_arr = matching_result["ti_arr"]
                spatial_stats_text = (
                    f"Spatial Statistics (x-direction):\n"
                    f"(from last {MAX_TIMESTEPS} timesteps)\n\n"
                    f"Mean TI: {np.mean(ti_arr):.4f}%\n"
                    f"Std Dev: {np.std(ti_arr):.4f}%\n"
                    f"Min: {np.min(ti_arr):.4f}%\n"
                    f"Max: {np.max(ti_arr):.4f}%\n"
                    f"Range: {np.max(ti_arr) - np.min(ti_arr):.4f}%\n"
                    f"n_points: {len(ti_arr)}"
                )
                ax3.text(0.5, 0.5, spatial_stats_text, ha='center', va='center', 
                        transform=ax3.transAxes, fontfamily='monospace', fontsize=11,
                        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
                ax3.axis('off')
                ax3.set_title("Spatial Statistics")
            else:
                ax3.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax3.transAxes)
                ax3.set_title("Spatial Statistics")
            
            # ========== ROW 2: TEMPORAL EVOLUTION ==========
            
            # --- Subplot 4: TI vs Time (at x=X_EVAL) with Mean Line ---
            ax4 = axes[1, 0]
            temporal_key = (ctp, blockage, ti_level)
            if temporal_key in ti_temporal_data:
                temporal = ti_temporal_data[temporal_key]
                ti_values = np.array(temporal["ti_at_x4"])
                mean_ti_at_x4 = np.mean(ti_values)
                
                ax4.plot(temporal["tidx"], temporal["ti_at_x4"], 'o-', 
                        color=matching_result["color"], linewidth=2.5, markersize=7, alpha=0.7, label='TI at x=4.0')
                
                # Add horizontal line for mean TI (from last MAX_TIMESTEPS)
                ax4.axhline(y=mean_ti_at_x4, color='red', linestyle='--', linewidth=2.5, 
                           alpha=0.7, label=f'Mean TI% = {mean_ti_at_x4:.4f}')
                
                ax4.set_xlabel("Time Index (TIDX)")
                ax4.set_ylabel(f"TI at x={X_EVAL} (%)")
                ax4.set_title(f"TI vs Time (evaluated at x={X_EVAL})")
                ax4.legend(fontsize=10, loc='best')
                ax4.grid(True, alpha=0.3)
            else:
                ax4.text(0.5, 0.5, "No temporal data", ha='center', va='center', transform=ax4.transAxes)
                ax4.set_title(f"TI vs Time (at x={X_EVAL})")
            
            # --- Subplot 5: Temporal Std Dev / Variability (at x=X_EVAL)
            ax5 = axes[1, 1]
            if temporal_key in ti_temporal_data:
                temporal = ti_temporal_data[temporal_key]
                ti_array = np.array(temporal["ti_at_x4"])
                
                # Compute rolling standard deviation
                window = max(3, len(ti_array) // 20)  # Adaptive window: ~5% of data
                if len(ti_array) > window:
                    rolling_std = np.array([np.std(ti_array[max(0, i-window):i+window+1]) 
                                           for i in range(len(ti_array))])
                    ax5.plot(temporal["tidx"], rolling_std, 's-', 
                            color=matching_result["color"], linewidth=2, markersize=6, alpha=0.7)
                    ax5.set_xlabel("Time Index (TIDX)")
                    ax5.set_ylabel("Rolling Std Dev (%)")
                    ax5.set_title(f"TI Temporal Variability at x={X_EVAL} (Rolling Std Dev, window={window})")
                    ax5.grid(True, alpha=0.3)
                else:
                    ax5.text(0.5, 0.5, "Insufficient data\nfor std dev", ha='center', va='center', transform=ax5.transAxes)
                    ax5.set_title(f"TI Temporal Variability at x={X_EVAL}")
            else:
                ax5.text(0.5, 0.5, "No temporal data", ha='center', va='center', transform=ax5.transAxes)
                ax5.set_title(f"TI Temporal Variability at x={X_EVAL}")
            
            # --- Subplot 6: Temporal Statistics Summary (at x=X_EVAL)
            ax6 = axes[1, 2]
            if temporal_key in ti_temporal_data:
                temporal = ti_temporal_data[temporal_key]
                ti_array = np.array(temporal["ti_at_x4"])
                
                temporal_stats_text = (
                    f"Temporal Statistics (at x={X_EVAL}):\n"
                    f"(from last {MAX_TIMESTEPS} timesteps)\n\n"
                    f"Mean TI: {np.mean(ti_array):.4f}%\n"
                    f"Std Dev: {np.std(ti_array):.4f}%\n"
                    f"Min: {np.min(ti_array):.4f}%\n"
                    f"Max: {np.max(ti_array):.4f}%\n"
                    f"Range: {np.max(ti_array) - np.min(ti_array):.4f}%\n"
                    f"n_samples: {len(ti_array)}"
                )
                ax6.text(0.5, 0.5, temporal_stats_text, ha='center', va='center', 
                        transform=ax6.transAxes, fontfamily='monospace', fontsize=11,
                        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
                ax6.axis('off')
                ax6.set_title(f"Temporal Statistics at x={X_EVAL}")
            else:
                ax6.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax6.transAxes)
                ax6.set_title(f"Temporal Statistics at x={X_EVAL}")
            
            fig.tight_layout()
            
            # Save figure with unique name for each combination
            savepath = f"./subplot_CTP{ctp}_{tag(blockage)}_{tag(ti_level)}.png"
            fig.savefig(savepath, dpi=300, bbox_inches="tight")
            print(f"  ✓ Saved: {savepath}")
            plt.close(fig)

print("\n" + "=" * 80)
print(f"✓ ALL {subplot_count} SUBPLOTS GENERATED SUCCESSFULLY!")
print("=" * 80)