import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc
import time

data_path = Path(au.DATA_PATH)

print("=" * 60)
print("Starting velocity convergence analysis")
print("=" * 60)

# Load Data
print("\n[1/4] Initializing BudgetIO...")
init_start = time.perf_counter()
sim = pio.BudgetIO("Data/Filtered_Spinups/10PCT", padeops=True, runid=1)
init_time = time.perf_counter() - init_start
print(f"✓ BudgetIO initialized in {init_time:.2f}s")

# Get Velocities - no all_t check
print("\n[2/4] Setting up timestep list...")
tids = list(range(800000, 990000, 10000))
print(f"✓ Timesteps to load: {len(tids)}")
print(f"  Range: tid {tids[0]} to {tids[-1]}")

# Set up figure and colors
print("\n[3/4] Setting up figure and loading data...")
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
colors = cmc.batlow(np.linspace(0, 1, len(tids)))
print(f"✓ Figure created")
print(f"  Processing {len(tids)} timesteps...\n")

# Stream load and plot
load_start = time.perf_counter()
for k, tid in enumerate(tids):
    iter_start = time.perf_counter()
    
    # Load all three velocity components at once
    data = sim.slice(budget_terms=["ubar", "vbar", "wbar"], 
                    ylim=1.4, zlim=1.4, tidx=tid)
    
    # Plot and immediately discard
    axes[0].plot(sim.x, data["ubar"].squeeze(), color=colors[k], lw=0.8)
    axes[1].plot(sim.x, data["vbar"].squeeze(), color=colors[k], lw=0.8)
    axes[2].plot(sim.x, data["wbar"].squeeze(), color=colors[k], lw=0.8)
    
    iter_time = time.perf_counter() - iter_start
    progress = (k + 1) / len(tids) * 100
    
    print(f"  [{k+1:3d}/{len(tids):3d}] tid={tid:6d} ({progress:5.1f}%) - {iter_time:.3f}s")

total_load_time = time.perf_counter() - load_start
avg_time_per_step = total_load_time / len(tids)
print(f"\n✓ All data loaded and plotted")
print(f"  Total loading time: {total_load_time:.2f}s")
print(f"  Average per timestep: {avg_time_per_step:.3f}s")

# Set labels and titles
print("\n[4/4] Finalizing plot...")
axes[0].set(xlabel="x", ylabel="ubar", title="Ubar Convergence (10% Blocked Spinup)")
axes[1].set(xlabel="x", ylabel="vbar", title="Vbar Convergence (10% Blocked Spinup)")
axes[2].set(xlabel="x", ylabel="wbar", title="Wbar Convergence (10% Blocked Spinup)")

for ax in axes:
    ax.grid(True, alpha=0.3)

sm = mpl.cm.ScalarMappable(cmap="cmc.batlow", 
                           norm=mpl.colors.Normalize(vmin=tids[0], vmax=tids[-1]))
sm.set_array([])

fig.subplots_adjust(top=0.88, right=0.88, wspace=0.3)
cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])
fig.colorbar(sm, cax=cbar_ax, label="tid")

plt.suptitle("Mean Velocity Profiles Convergence in 10% Blocked Spinup", fontsize=16)

# Save
save_start = time.perf_counter()
plt.savefig("10PCT_filterspin_convergence.png", dpi=300, bbox_inches="tight")
save_time = time.perf_counter() - save_start
print(f"✓ Figure saved as '10PCT_filterspin_convergence.png' ({save_time:.2f}s)")

plt.close()

# Final summary
total_time = time.perf_counter() - init_start
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"BudgetIO initialization:  {init_time:7.2f}s")
print(f"Data loading & plotting:  {total_load_time:7.2f}s ({avg_time_per_step:.3f}s/step)")
print(f"Figure saving:            {save_time:7.2f}s")
print(f"TOTAL TIME:               {total_time:7.2f}s")
print("=" * 60)
print("✓ Done!")