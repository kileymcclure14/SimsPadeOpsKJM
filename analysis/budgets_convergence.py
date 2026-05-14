import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc

data_path = Path(au.DATA_PATH)

# Load Data
sim = pio.BudgetIO("Data/Empty_Domains/Spinups/10PCT_Restart", padeops=True, runid=4)

# Get Velocities
tids = range(750000, 999990, 10000)
all_t = sim.unique_times()

valid_tids = [(i, tid) for i, tid in enumerate(tids) if i < len(all_t)]

for i, tid in valid_tids:
    data_ubar = sim.slice(budget_terms=["ubar"], ylim=1.4, zlim=1.4, tidx=tid)
    data_vbar = sim.slice(budget_terms=["vbar"], ylim=1.4, zlim=1.4, tidx=tid)
    data_wbar = sim.slice(budget_terms=["wbar"], ylim=1.4, zlim=1.4, tidx=tid)

    globals()[f"ubar_{tid}"] = np.array(data_ubar["ubar"])
    globals()[f"vbar_{tid}"] = np.array(data_vbar["vbar"])
    globals()[f"wbar_{tid}"] = np.array(data_wbar["wbar"])
    print(f"Loaded data for tid={tid} (index {i})")



fig, axes = plt.subplots(1, 3, figsize=(16, 5))

colors = cmc.batlow(np.linspace(0, 1, len(valid_tids)))

for k, (i, tid) in enumerate(valid_tids):
    axes[0].plot(sim.x, globals()[f"ubar_{tid}"].squeeze(), color=colors[k], lw=0.8)
    axes[1].plot(sim.x, globals()[f"vbar_{tid}"].squeeze(), color=colors[k], lw=0.8)
    axes[2].plot(sim.x, globals()[f"wbar_{tid}"].squeeze(), color=colors[k], lw=0.8)

axes[0].set(xlabel="x", ylabel="ubar", title="Ubar Convergence (10% Blocked Spinup)")
axes[1].set(xlabel="x", ylabel="vbar", title="Vbar Convergence (10% Blocked Spinup)")
axes[2].set(xlabel="x", ylabel="wbar", title="Wbar Convergence (10% Blocked Spinup)")

for ax in axes:
    ax.grid(True, alpha=0.3)

sm = mpl.cm.ScalarMappable(cmap="cmc.batlow", norm=mpl.colors.Normalize(vmin=valid_tids[0][1], vmax=valid_tids[-1][1]))
sm.set_array([])

fig.subplots_adjust(top=0.88, right=0.88, wspace=0.3)
cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])
fig.colorbar(sm, cax=cbar_ax, label="tid")

plt.suptitle("Mean Velocity Profiles Convergence in 10% Blocked Spinup", fontsize=16)
plt.savefig("10pct_blocked_spinup_convergence.png", dpi=300, bbox_inches="tight")
plt.close()