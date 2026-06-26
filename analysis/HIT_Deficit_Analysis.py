import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np


# ============================================================================
# CONFIGURATION
# ============================================================================
# KEEP YOUR SIM_CONFIGS EXACTLY AS YOU POSTED
SIM_CONFIGS = [
     # CTP = 2
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_2/TI_3/10PCT",  runid_t=3, CTP="2", blockage="10%", TI="3%"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_2/TI_3/20PCT",  runid_t=3, CTP="2", blockage="20%", TI="3%"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_2/TI_8/10PCT",  runid_t=3, CTP="2", blockage="10%", TI="8%"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_2/TI_8/20PCT",  runid_t=3, CTP="2", blockage="20%", TI="8%"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_2/TI_12/10PCT", runid_t=3, CTP="2", blockage="10%", TI="12%"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_2/TI_12/20PCT", runid_t=3, CTP="2", blockage="20%", TI="12%"),

    # CTP = 4
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_4/TI_3/10PCT",  runid_t=3, CTP="4", blockage="10%", TI="3%"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_4/TI_3/20PCT",  runid_t=3, CTP="4", blockage="20%", TI="3%"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_4/TI_8/10PCT",  runid_t=3, CTP="4", blockage="10%", TI="8%"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_4/TI_8/20PCT",  runid_t=3, CTP="4", blockage="20%", TI="8%"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_4/TI_12/10PCT", runid_t=3, CTP="4", blockage="10%", TI="12%"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_4/TI_12/20PCT", runid_t=3, CTP="4", blockage="20%", TI="12%"),

    # CTP = 6
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_6/TI_3/10PCT",  runid_t=3, CTP="6", blockage="10%", TI="3%"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_6/TI_3/20PCT",  runid_t=3, CTP="6", blockage="20%", TI="3%"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_6/TI_8/10PCT",  runid_t=3, CTP="6", blockage="10%", TI="8%"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_6/TI_8/20PCT",  runid_t=3, CTP="6", blockage="20%", TI="8%"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_6/TI_12/10PCT", runid_t=3, CTP="6", blockage="10%", TI="12%"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_6/TI_12/20PCT", runid_t=3, CTP="6", blockage="20%", TI="12%"),

    # CTP = 8
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_8/TI_3/10PCT",  runid_t=3, CTP="8", blockage="10%", TI="3%"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_8/TI_3/20PCT",  runid_t=3, CTP="8", blockage="20%", TI="3%"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_8/TI_8/10PCT",  runid_t=3, CTP="8", blockage="10%", TI="8%"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_8/TI_8/20PCT",  runid_t=3, CTP="8", blockage="20%", TI="8%"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_8/TI_12/10PCT", runid_t=3, CTP="8", blockage="10%", TI="12%"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_8/TI_12/20PCT", runid_t=3, CTP="8", blockage="20%", TI="12%"),

    # CTP = 10
    dict(label="10% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_10/TI_3/10PCT",  runid_t=3, CTP="10", blockage="10%", TI="3%"),
    dict(label="20% Blocked, 3% TI",  path="Data/HIT_Turbines/CTP_10/TI_3/20PCT",  runid_t=3, CTP="10", blockage="20%", TI="3%"),
    dict(label="10% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_10/TI_8/10PCT",  runid_t=3, CTP="10", blockage="10%", TI="8%"),
    dict(label="20% Blocked, 8% TI",  path="Data/HIT_Turbines/CTP_10/TI_8/20PCT",  runid_t=3, CTP="10", blockage="20%", TI="8%"),
    dict(label="10% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_10/TI_12/10PCT", runid_t=3, CTP="10", blockage="10%", TI="12%"),
    dict(label="20% Blocked, 12% TI", path="Data/HIT_Turbines/CTP_10/TI_12/20PCT", runid_t=3, CTP="10", blockage="20%", TI="12%"),
]

# ============================================================================
# HELPERS
# ============================================================================

def load_deficit(cfg):
    return pio.DeficitIO(
        cfg["path"], padeops=True, runid=cfg["runid_t"], normalize_origin="turbine"
    )


def _unique_values(results, key):
    seen = []
    for r in results:
        if r[key] not in seen:
            seen.append(r[key])
    return seen


def tag(s):
    return s.replace("%", "")


def get_data_range(deficit, term, zlim=0):
    try:
        deficit.read_budgets(budget_terms=[term], overwrite=False)
        view = deficit.slice(budget_terms=[term], zlim=zlim)
        data = view[term].values
        return np.nanmin(data), np.nanmax(data)
    except Exception:
        return None, None


def fmt_range(vmin, vmax):
    if vmin is None or vmax is None:
        return "N/A"
    return f"[{vmin:.4f}, {vmax:.4f}]"


def plot_deficit_field(deficit, term, zlim=0, label="", ax=None, cmap="RdBu_r", vmin=None, vmax=None):
    """
    IMPORTANT:
    - Uses view[term].imshow(...) to preserve your original field view.
    - Removes any auto-created tiny colorbar axes immediately.
    """
    try:
        deficit.read_budgets(budget_terms=[term], overwrite=False)
        view = deficit.slice(budget_terms=[term], zlim=zlim)

        # Track axes count before plotting (in case backend auto-adds cbar axes)
        n_before = len(ax.figure.axes)

        # Keep your original plotting path (preserves view/orientation/domain behavior)
        im = view[term].imshow(ax=ax, cmap=cmap, vmin=vmin, vmax=vmax)

        # Remove any auto-created axes (tiny horizontal bars)
        if len(ax.figure.axes) > n_before:
            for extra_ax in ax.figure.axes[n_before:]:
                if extra_ax is not ax:
                    extra_ax.remove()

        ax.set_title(label, fontsize=11, fontweight="bold", pad=8)
        ax.set_xlabel("y", fontsize=9)
        ax.set_ylabel("x", fontsize=9)
        ax.tick_params(labelsize=8)
        return im

    except Exception as e:
        print(f"      ERROR {term}: {type(e).__name__}: {e}")
        ax.text(
            0.5, 0.5, f"Data not\navailable\n({type(e).__name__})",
            ha="center", va="center", transform=ax.transAxes, fontsize=9
        )
        ax.set_title(label, fontsize=11, fontweight="bold", pad=8)
        ax.set_xlabel("y", fontsize=9)
        ax.set_ylabel("x", fontsize=9)
        return None


def plot_deficit_velocity_components(deficit, label, ax_array, zlim=0, cmap="RdBu_r", vmin_dict=None, vmax_dict=None):
    components = [("delta_u", "ΔU"), ("delta_v", "ΔV"), ("delta_w", "ΔW")]
    images = []
    for ax, (term, term_label) in zip(ax_array, components):
        vmin = vmin_dict[term] if vmin_dict else None
        vmax = vmax_dict[term] if vmax_dict else None
        im = plot_deficit_field(
            deficit, term, zlim=zlim, label=f"{label}\n{term_label}",
            ax=ax, cmap=cmap, vmin=vmin, vmax=vmax
        )
        images.append(im)
    return images


# ============================================================================
# MAIN
# ============================================================================

# Load all simulations
results = []
for cfg in SIM_CONFIGS:
    print(f"Loading: CTP={cfg['CTP']}  {cfg['label']}")
    try:
        deficit = load_deficit(cfg)
        results.append({**cfg, "deficit": deficit})
    except Exception as e:
        print(f"  ERROR loading {cfg['label']}: {e}")

ctps = _unique_values(results, "CTP")
ti_levels = _unique_values(results, "TI")
blockages = _unique_values(results, "blockage")

print(f"\nLoaded {len(results)} simulations")
print(f"CTPs: {ctps}")
print(f"TI levels: {ti_levels}")
print(f"Blockages: {blockages}\n")

print("Generating deficit velocity field plots...\n")

for ctp in ctps:
    for ti in ti_levels:
        subs = [r for r in results if r["CTP"] == ctp and r["TI"] == ti]
        if not subs:
            continue

        subs_sorted = sorted(subs, key=lambda x: int(x["blockage"].rstrip("%")))
        n_blockages = len(subs_sorted)

        print(f"Processing: CTP={ctp}, TI={ti}")
        print("  Calculating data ranges...")

        terms = ["delta_u", "delta_v", "delta_w"]
        labels = ["ΔU", "ΔV", "ΔW"]

        # Global per-term range across blockages (shared scale per column)
        vmin_dict = {t: np.inf for t in terms}
        vmax_dict = {t: -np.inf for t in terms}

        for r in subs_sorted:
            for t in terms:
                dmin, dmax = get_data_range(r["deficit"], t, zlim=0)
                if dmin is not None:
                    vmin_dict[t] = min(vmin_dict[t], dmin)
                    vmax_dict[t] = max(vmax_dict[t], dmax)

        for t in terms:
            if np.isinf(vmin_dict[t]) or np.isinf(vmax_dict[t]):
                vmin_dict[t] = None
                vmax_dict[t] = None

        print(
            f"  Data ranges: "
            f"U={fmt_range(vmin_dict['delta_u'], vmax_dict['delta_u'])}, "
            f"V={fmt_range(vmin_dict['delta_v'], vmax_dict['delta_v'])}, "
            f"W={fmt_range(vmin_dict['delta_w'], vmax_dict['delta_w'])}"
        )

        fig_height = 3.7 * n_blockages + 1
        fig, axes = plt.subplots(n_blockages, 3, figsize=(18, fig_height), constrained_layout=False)

        if n_blockages == 1:
            axes = axes.reshape(1, -1)

        # Plot rows
        for row_idx, r in enumerate(subs_sorted):
            print(f"    Processing blockage: {r['blockage']}")
            plot_deficit_velocity_components(
                r["deficit"],
                r["blockage"],
                axes[row_idx, :],
                zlim=0,
                cmap="RdBu_r",
                vmin_dict=vmin_dict,
                vmax_dict=vmax_dict
            )

        # Defensive cleanup: remove any non-main axes before shared colorbars
        main_axes = set(axes.ravel())
        for a in list(fig.axes):
            if a not in main_axes:
                fig.delaxes(a)

        # One shared vertical normalized colorbar per column
        for col_idx, (term, cbar_label) in enumerate(zip(terms, labels)):
            if vmin_dict[term] is None:
                continue

            norm = plt.Normalize(vmin=vmin_dict[term], vmax=vmax_dict[term])
            sm = plt.cm.ScalarMappable(norm=norm, cmap="RdBu_r")
            sm.set_array([])

            cbar = fig.colorbar(
                sm,
                ax=axes[:, col_idx],  # shared across all rows in this column
                orientation="vertical",
                fraction=0.035,
                pad=0.02
            )
            cbar.set_label(cbar_label, fontsize=10, fontweight="bold")
            cbar.ax.tick_params(labelsize=8)

        fig.suptitle(
            f"Velocity Deficits at Hub Height — CTP = {ctp}, TI = {ti} (Comparison by Blockage)",
            fontsize=14, fontweight="bold", y=0.995
        )

        plt.subplots_adjust(left=0.07, right=0.90, top=0.92, bottom=0.08, hspace=0.55, wspace=0.35)

        outname = f"./Deficit_CTP{ctp}_{tag(ti)}TI_Blockage_Comparison.png"
        fig.savefig(outname, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"  ✓ Saved: {outname}\n")

print("=" * 80)
print("ALL DEFICIT PLOTS COMPLETE!")
print("=" * 80)