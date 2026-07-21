from pathlib import Path
import re
import traceback
import numpy as np
import matplotlib.pyplot as plt
import padeopsIO as pio

# ============================================================================
# CONFIGURATION
# ============================================================================

X_EVAL = 4.0
MAX_TIMESTEPS = 10000

SIM_CONFIGS = [
    # CTP = 2
    # dict(path="Data/HIT_AD/CTP_2/TI_3/10PCT", runid=2, CTP="2", blockage="10%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_2/TI_3/20PCT", runid=2, CTP="2", blockage="20%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_2/TI_6/10PCT", runid=2, CTP="2", blockage="10%", TI="6%", color="orange"),
    dict(path="Data/HIT_AD/CTP_2/TI_6/20PCT", runid=2, CTP="2", blockage="20%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_2/TI_10/10PCT", runid=2, CTP="2", blockage="10%", TI="10%", color="green"),
    # dict(path="Data/HIT_AD/CTP_2/TI_10/20PCT", runid=2, CTP="2", blockage="20%", TI="10%", color="green"),

    # CTP = 4
    # dict(path="Data/HIT_AD/CTP_4/TI_3/10PCT", runid=2, CTP="4", blockage="10%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_4/TI_3/20PCT", runid=2, CTP="4", blockage="20%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_4/TI_6/10PCT", runid=2, CTP="4", blockage="10%", TI="6%", color="orange"),
    dict(path="Data/HIT_AD/CTP_4/TI_6/20PCT", runid=2, CTP="4", blockage="20%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_4/TI_10/10PCT", runid=2, CTP="4", blockage="10%", TI="10%", color="green"),
    # dict(path="Data/HIT_AD/CTP_4/TI_10/20PCT", runid=2, CTP="4", blockage="20%", TI="10%", color="green"),

    # CTP = 6
    # dict(path="Data/HIT_AD/CTP_6/TI_3/10PCT", runid=2, CTP="6", blockage="10%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_6/TI_3/20PCT", runid=2, CTP="6", blockage="20%", TI="3%", color="brown"),
    dict(path="Data/HIT_AD/CTP_6/TI_6/10PCT", runid=2, CTP="6", blockage="10%", TI="6%", color="orange"),
    dict(path="Data/HIT_AD/CTP_6/TI_6/20PCT", runid=2, CTP="6", blockage="20%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_6/TI_10/10PCT", runid=2, CTP="6", blockage="10%", TI="10%", color="green"),
    # dict(path="Data/HIT_AD/CTP_6/TI_10/20PCT", runid=2, CTP="6", blockage="20%", TI="10%", color="green"),

    # CTP = 8
    # dict(path="Data/HIT_AD/CTP_8/TI_3/10PCT", runid=2, CTP="8", blockage="10%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_8/TI_3/20PCT", runid=2, CTP="8", blockage="20%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_8/TI_6/10PCT", runid=2, CTP="8", blockage="10%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_8/TI_6/20PCT", runid=2, CTP="8", blockage="20%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_8/TI_10/10PCT", runid=2, CTP="8", blockage="10%", TI="10%", color="green"),
    # dict(path="Data/HIT_AD/CTP_8/TI_10/20PCT", runid=2, CTP="8", blockage="20%", TI="10%", color="green"),

    # CTP = 10
    # dict(path="Data/HIT_AD/CTP_10/TI_3/10PCT", runid=2, CTP="10", blockage="10%", TI="3%", color="brown"),
    # dict(path="Data/HIT_AD/CTP_10/TI_3/20PCT", runid=2, CTP="10", blockage="20%", TI="3%", color="brown"),
    #dict(path="Data/HIT_AD/CTP_10/TI_6/10PCT", runid=2, CTP="10", blockage="10%", TI="6%", color="orange"),
    #dict(path="Data/HIT_AD/CTP_10/TI_6/20PCT", runid=2, CTP="10", blockage="20%", TI="6%", color="orange"),
    # dict(path="Data/HIT_AD/CTP_10/TI_10/10PCT", runid=2, CTP="10", blockage="10%", TI="10%", color="green"),
    # dict(path="Data/HIT_AD/CTP_10/TI_10/20PCT", runid=2, CTP="10", blockage="20%", TI="10%", color="green"),
]

_TIDX_PATTERN = re.compile(r"_t(\d+)_")


# ============================================================================
# HELPERS
# ============================================================================

def get_all_tidx(path, runid):
    sim_dir = Path(path)
    budget_files = sim_dir.glob(f"Run{runid:02d}_budget0_term01_t*.s3D")

    tidxs = []
    for f in budget_files:
        match = _TIDX_PATTERN.search(f.name)
        if match:
            tidxs.append(int(match.group(1)))

    if not tidxs:
        raise FileNotFoundError(f"No budget files found for Run{runid:02d} at {path}")

    return sorted(set(tidxs))


def get_selected_tidx(path, runid, max_timesteps=MAX_TIMESTEPS):
    all_tidxs = get_all_tidx(path, runid)
    return all_tidxs[-max_timesteps:]


def compute_TI(u, v, w, ubar, vbar, wbar):
    uprime = u - ubar
    vprime = v - vbar
    wprime = w - wbar

    urms_3d = np.sqrt((uprime * uprime + vprime * vprime + wprime * wprime) / 3.0)
    barspeed_3d = np.sqrt(ubar * ubar + vbar * vbar + wbar * wbar)

    urms = np.mean(urms_3d, axis=(1, 2))
    barspeed = np.mean(barspeed_3d, axis=(1, 2))

    ti = np.full_like(urms, np.nan, dtype=np.float64)
    mask = barspeed != 0
    ti[mask] = (urms[mask] / barspeed[mask]) * 100.0
    return ti


def find_closest_x_index(x_array, x_target):
    return int(np.argmin(np.abs(x_array - x_target)))


def tag(s):
    return s.replace("%", "")


def find_ti_data_file(path, blockage):
    ti_file = Path(path) / "ti_data.npz"
    return ti_file if ti_file.exists() else None


def rolling_std_fast(x, window):
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    if n == 0:
        return np.array([], dtype=np.float64)
    if window < 2:
        return np.zeros(n, dtype=np.float64)

    kernel = np.ones(window, dtype=np.float64) / window
    mean = np.convolve(x, kernel, mode="same")
    mean_sq = np.convolve(x * x, kernel, mode="same")
    var = np.maximum(mean_sq - mean * mean, 0.0)
    return np.sqrt(var)


def load_slice_term(sim, term, tidx, is_budget):
    if is_budget:
        return np.asarray(sim.slice(budget_terms=term, tidx=tidx)[term], dtype=np.float32)
    return np.asarray(sim.slice(field_terms=term, tidx=tidx)[term], dtype=np.float32)


def summarize_array(arr):
    arr = np.asarray(arr, dtype=np.float64)
    return {
        "mean": float(np.nanmean(arr)),
        "std": float(np.nanstd(arr)),
        "min": float(np.nanmin(arr)),
        "max": float(np.nanmax(arr)),
        "range": float(np.nanmax(arr) - np.nanmin(arr)),
        "n": int(arr.size),
    }


# ============================================================================
# MAIN LOADING
# ============================================================================

print("=" * 80)
print("LOADING SIMULATIONS AND CREATING SUBPLOTS")
print("=" * 80)
print(f"Using last {MAX_TIMESTEPS} timesteps for all simulations")
print(f"Temporal TI evaluation location: x = {X_EVAL}")

results = []
results_map = {}
ti_data_all = {}
ti_temporal_data = {}

for idx, cfg in enumerate(SIM_CONFIGS, 1):
    print(
        f"\n[{idx}/{len(SIM_CONFIGS)}] CTP={cfg['CTP']}, {cfg['blockage']} blocked, "
        f"{cfg['TI']} TI, runid={cfg['runid']}"
    )

    try:
        selected_tidxs = get_selected_tidx(cfg["path"], cfg["runid"], max_timesteps=MAX_TIMESTEPS)
        print(f"  -> Using last {len(selected_tidxs)} timesteps (from {selected_tidxs[0]} to {selected_tidxs[-1]})")
    except FileNotFoundError as e:
        print(f"  SKIPPED: {e}")
        continue

    try:
        sim = pio.BudgetIO(cfg["path"], padeops=True, runid=cfg["runid"])

        x_coord = None
        x_index_eval = None
        ti_sum = None
        ti_count = None
        temporal_tidx = []
        temporal_ti = []
        progress_step = max(1, len(selected_tidxs) // 10)

        for tidx_idx, tidx in enumerate(selected_tidxs):
            if tidx_idx % progress_step == 0:
                print(f"    Loading timestep {tidx_idx + 1}/{len(selected_tidxs)} (tidx={tidx})")

            ubar = load_slice_term(sim, "ubar", tidx, is_budget=True)
            vbar = load_slice_term(sim, "vbar", tidx, is_budget=True)
            wbar = load_slice_term(sim, "wbar", tidx, is_budget=True)
            u = load_slice_term(sim, "u", tidx, is_budget=False)
            v = load_slice_term(sim, "v", tidx, is_budget=False)
            w = load_slice_term(sim, "w", tidx, is_budget=False)

            ti_profile = compute_TI(u, v, w, ubar, vbar, wbar)

            if x_coord is None:
                x_coord = np.asarray(sim.x, dtype=np.float64).copy()
                x_index_eval = find_closest_x_index(x_coord, x_target=X_EVAL)
                print(
                    f"    -> Found x={x_coord[x_index_eval]:.4f} closest to target "
                    f"x={X_EVAL} at index {x_index_eval}"
                )

            if ti_sum is None:
                ti_sum = np.nan_to_num(ti_profile, nan=0.0)
                ti_count = np.isfinite(ti_profile).astype(np.int32)
            else:
                ti_sum += np.nan_to_num(ti_profile, nan=0.0)
                ti_count += np.isfinite(ti_profile)

            temporal_tidx.append(tidx)
            temporal_ti.append(float(ti_profile[x_index_eval]))

            del ubar, vbar, wbar, u, v, w, ti_profile

        TI_data_avg = np.divide(
            ti_sum,
            ti_count,
            out=np.full_like(ti_sum, np.nan, dtype=np.float64),
            where=ti_count > 0,
        )

        temporal_dict = {
            "tidx": np.asarray(temporal_tidx, dtype=np.int64),
            "ti_at_x4": np.asarray(temporal_ti, dtype=np.float64),
        }

        result = {
            **cfg,
            "x": x_coord,
            "ti_arr": TI_data_avg,
            "ti_temporal": temporal_dict,
            "selected_tidxs": selected_tidxs,
            "x_index_4": x_index_eval,
        }
        results.append(result)
        results_map[(cfg["CTP"], cfg["blockage"], cfg["TI"])] = result

        temporal_key = (cfg["CTP"], cfg["blockage"], cfg["TI"])
        ti_temporal_data[temporal_key] = temporal_dict

        print(f"  Loaded and time-averaged successfully over {len(selected_tidxs)} timesteps")
        print(f"    - TI mean (spatial average): {np.nanmean(TI_data_avg):.3f}%")
        print(f"    - TI at x={X_EVAL}: {np.nanmean(temporal_dict['ti_at_x4']):.3f}%")

        del sim, ti_sum, ti_count, temporal_tidx, temporal_ti

    except Exception as e:
        print(f"  ERROR loading data: {e}")
        traceback.print_exc()
        continue

    try:
        ti_file = find_ti_data_file(cfg["path"], cfg["blockage"])
        key = (cfg["CTP"], cfg["blockage"])
        if ti_file and key not in ti_data_all:
            data = np.load(ti_file)
            tidx_data = np.asarray(data["TIDX"], dtype=np.float64)
            ti_fact_data = np.asarray(data["TI_fact"], dtype=np.float64)

            min_len = min(len(tidx_data), len(ti_fact_data))
            tidx_data = tidx_data[:min_len]
            ti_fact_data = ti_fact_data[:min_len]

            valid_mask = np.isfinite(tidx_data) & np.isfinite(ti_fact_data)
            tidx_data = tidx_data[valid_mask]
            ti_fact_data = ti_fact_data[valid_mask]

            mean_ti_fact = float(np.mean(ti_fact_data)) if ti_fact_data.size > 0 else np.nan

            ti_data_all[key] = {
                "TIDX": tidx_data,
                "TI_fact": ti_fact_data,
                "mean_ti_fact": mean_ti_fact,
            }
            print(f"  Loaded TI_factor data from {ti_file} (mean TI_fact = {mean_ti_fact:.4f})")
    except Exception as e:
        print(f"  ERROR loading TI_factor data: {e}")


print("\n" + "=" * 80)
print("LOADED DATA SUMMARY")
print("=" * 80)
print(f"Total results: {len(results)}")
print(f"TI_factor files loaded: {len(ti_data_all)}")
print(f"Temporal TI data loaded: {len(ti_temporal_data)}")

print("\nTimesteps averaged per simulation:")
for r in results:
    print(f"  CTP={r['CTP']}, {r['blockage']}, {r['TI']}: {len(r['selected_tidxs'])} timesteps")


# ============================================================================
# PLOTTING
# ============================================================================

print("\n" + "=" * 80)
print("CREATING SUBPLOTS FOR EACH (CTP, BLOCKAGE, TI%) COMBINATION")
print("=" * 80)

ctps = sorted({cfg["CTP"] for cfg in SIM_CONFIGS}, key=float)
blockages = sorted({cfg["blockage"] for cfg in SIM_CONFIGS}, key=lambda s: float(s.replace('%', '')))
ti_levels = sorted({cfg["TI"] for cfg in SIM_CONFIGS}, key=lambda s: float(s.replace('%', '')))

print(f"CTPs: {ctps}")
print(f"Blockages: {blockages}")
print(f"TI Levels: {ti_levels}")
print(f"\nTotal combinations to generate: {len(ctps) * len(blockages) * len(ti_levels)}")

subplot_count = 0

for ctp in ctps:
    for blockage in blockages:
        for ti_level in ti_levels:
            matching_result = results_map.get((ctp, blockage, ti_level))
            if matching_result is None:
                continue

            ti_factor_key = (ctp, blockage)
            has_ti_factor = ti_factor_key in ti_data_all
            temporal_key = (ctp, blockage, ti_level)

            subplot_count += 1
            print(f"\n[{subplot_count}] Creating subplot for CTP={ctp}, {blockage}, {ti_level}...")

            fig, axes = plt.subplots(2, 3, figsize=(20, 10))
            fig.suptitle(
                f"CTP={ctp}, {blockage} Blocked, {ti_level} TI\n"
                f"(Time-Averaged over {len(matching_result['selected_tidxs'])} budget timesteps)",
                fontsize=14,
                fontweight="bold",
            )

            ax1, ax2, ax3 = axes[0, 0], axes[0, 1], axes[0, 2]
            ax4, ax5, ax6 = axes[1, 0], axes[1, 1], axes[1, 2]

            if has_ti_factor:
                ti_data = ti_data_all[ti_factor_key]
                tidx = ti_data["TIDX"]
                ti_fact = ti_data["TI_fact"]
                mean_ti_fact = ti_data["mean_ti_fact"]

                if tidx.size > 0:
                    ax1.plot(tidx, ti_fact, '-', color='steelblue', linewidth=2, label='TI Factor')
                    ax1.axhline(
                        y=mean_ti_fact,
                        color='red',
                        linestyle='--',
                        linewidth=2.5,
                        alpha=0.7,
                        label=f'Mean TI_fact = {mean_ti_fact:.4f}',
                    )
                    ax1.set_xlabel("Time Index (TIDX)")
                    ax1.set_ylabel("TI Factor")
                    ax1.set_title("TI Factor Evolution")
                    ax1.legend(fontsize=10, loc='best')
                    ax1.grid(True, alpha=0.3)
                else:
                    ax1.text(0.5, 0.5, "No valid TI_factor data\n(all NaN/Inf)", ha='center', va='center', transform=ax1.transAxes)
                    ax1.set_title("TI Factor Evolution")
            else:
                ax1.text(0.5, 0.5, "No TI_factor data", ha='center', va='center', transform=ax1.transAxes)
                ax1.set_title("TI Factor Evolution")

            color = matching_result["color"]
            x = matching_result["x"]
            ti_arr = matching_result["ti_arr"]
            x_at_eval = x[matching_result["x_index_4"]]

            ax2.plot(x, ti_arr, color=color, linewidth=2.5, marker='o', markersize=5, markevery=max(1, len(x) // 20), label=f"{blockage}")
            ax2.axvline(x=x_at_eval, color='red', linestyle='--', linewidth=2, alpha=0.6, label=f'Eval at x={x_at_eval:.2f}')
            ax2.set_xlabel("x/D")
            ax2.set_ylabel("Mean TI (%)")
            ax2.set_title("Mean TI Profile vs x/D")
            ax2.legend()
            ax2.grid(True, alpha=0.3)

            spatial_stats = summarize_array(ti_arr)
            spatial_stats_text = (
                f"Spatial Statistics (x-direction):\n\n"
                f"Mean TI: {spatial_stats['mean']:.4f}%\n"
                f"Std Dev: {spatial_stats['std']:.4f}%\n"
                f"Min: {spatial_stats['min']:.4f}%\n"
                f"Max: {spatial_stats['max']:.4f}%\n"
                f"Range: {spatial_stats['range']:.4f}%\n"
                f"n_points: {spatial_stats['n']}"
            )
            ax3.text(
                0.5,
                0.5,
                spatial_stats_text,
                ha='center',
                va='center',
                transform=ax3.transAxes,
                fontfamily='monospace',
                fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
            )
            ax3.axis('off')
            ax3.set_title("Spatial Statistics")

            if temporal_key in ti_temporal_data:
                temporal = ti_temporal_data[temporal_key]
                tidx_vals = temporal["tidx"]
                ti_array = temporal["ti_at_x4"]

                ax4.plot(tidx_vals, ti_array, 'o-', color=color, linewidth=2.0, markersize=4, alpha=0.7)
                ax4.set_xlabel("Time Index (TIDX)")
                ax4.set_ylabel(f"TI at x={X_EVAL} (%)")
                ax4.set_title(f"TI vs Time (evaluated at x={X_EVAL})")
                ax4.grid(True, alpha=0.3)

                window = max(3, len(ti_array) // 20)
                rolling_std = rolling_std_fast(ti_array, window)
                ax5.plot(tidx_vals, rolling_std, '-', color=color, linewidth=2, alpha=0.8)
                ax5.set_xlabel("Time Index (TIDX)")
                ax5.set_ylabel("Rolling Std Dev (%)")
                ax5.set_title(f"TI Temporal Variability at x={X_EVAL} (window={window})")
                ax5.grid(True, alpha=0.3)

                temporal_stats = summarize_array(ti_array)
                temporal_stats_text = (
                    f"Temporal Statistics (at x={X_EVAL}):\n\n"
                    f"Mean TI: {temporal_stats['mean']:.4f}%\n"
                    f"Std Dev: {temporal_stats['std']:.4f}%\n"
                    f"Min: {temporal_stats['min']:.4f}%\n"
                    f"Max: {temporal_stats['max']:.4f}%\n"
                    f"Range: {temporal_stats['range']:.4f}%\n"
                    f"n_samples: {temporal_stats['n']}"
                )
                ax6.text(
                    0.5,
                    0.5,
                    temporal_stats_text,
                    ha='center',
                    va='center',
                    transform=ax6.transAxes,
                    fontfamily='monospace',
                    fontsize=11,
                    bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
                )
                ax6.axis('off')
                ax6.set_title(f"Temporal Statistics at x={X_EVAL}")
            else:
                ax4.text(0.5, 0.5, "No temporal data", ha='center', va='center', transform=ax4.transAxes)
                ax4.set_title(f"TI vs Time (at x={X_EVAL})")
                ax5.text(0.5, 0.5, "No temporal data", ha='center', va='center', transform=ax5.transAxes)
                ax5.set_title(f"TI Temporal Variability at x={X_EVAL}")
                ax6.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax6.transAxes)
                ax6.set_title(f"Temporal Statistics at x={X_EVAL}")

            fig.tight_layout()
            savepath = f"./subplot_CTP{ctp}_{tag(blockage)}_{tag(ti_level)}.png"
            fig.savefig(savepath, dpi=300, bbox_inches="tight")
            print(f"  Saved: {savepath}")
            plt.close(fig)

print("\n" + "=" * 80)
print(f"ALL {subplot_count} SUBPLOTS GENERATED SUCCESSFULLY!")
print("=" * 80)