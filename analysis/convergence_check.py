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
print("Starting ubar convergence analysis")
print("=" * 60)

# Load Data
print("\n[1/4] Initializing BudgetIO...")
init_start = time.perf_counter()
sim = pio.BudgetIO("Data/Empty_Domains/20PCT", padeops=True, runid=3)
init_time = time.perf_counter() - init_start
print(f"✓ BudgetIO initialized in {init_time:.2f}s")

# Set up timesteps
print("\n[2/4] Setting up timestep list...")
tids = list(range(0, 10919, 100))
print(f"✓ Timesteps to load: {len(tids)}")
print(f"  Range: tid {tids[0]} to {tids[-1]}")

# Set up figure and colors
print("\n[3/4] Setting up figure and loading data...")
fig, ax = plt.subplots(1, 1, figsize=(7, 6))
colors = cmc.batlow(np.linspace(0, 1, len(tids)))
print(f"✓ Figure created")
print(f"  Processing {len(tids)} timesteps...\n")

# Stream load and plot
load_start = time.perf_counter()
for k, tid in enumerate(tids):
    iter_start = time.perf_counter()

    data = sim.slice(budget_terms=["ubar"], tidx=tid)
    print(f"tid={tid}, ubar shape={data['ubar'].shape}")
    ubar_avg = data["ubar"].mean(axis=(0, 2))  # average over x and z → shape (nz,)

    ax.plot(sim.y, ubar_avg, color=colors[k], lw=0.8)

    iter_time = time.perf_counter() - iter_start
    progress = (k + 1) / len(tids) * 100
    print(f"  [{k+1:3d}/{len(tids):3d}] tid={tid:6d} ({progress:5.1f}%) - {iter_time:.3f}s")

total_load_time = time.perf_counter() - load_start
avg_time_per_step = total_load_time / len(tids)
print(f"\n✓ All data loaded and plotted")
print(f"  Total loading time: {total_load_time:.2f}s")
print(f"  Average per timestep: {avg_time_per_step:.3f}s")

# Labels, colorbar, title
print("\n[4/4] Finalizing plot...")
ax.set(xlabel="x", ylabel="ubar", title="Ubar Streamwise Profile Convergence (20PCT)")
ax.grid(True, alpha=0.3)

sm = mpl.cm.ScalarMappable(cmap=cmc.batlow,
                            norm=mpl.colors.Normalize(vmin=tids[0], vmax=tids[-1]))
sm.set_array([])

fig.subplots_adjust(right=0.88)
cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])
fig.colorbar(sm, cax=cbar_ax, label="tid")

plt.suptitle("Mean Streamwise Velocity Profile Convergence — 20PCT", fontsize=13)

# Save
save_start = time.perf_counter()
plt.savefig("20PCT_ubar_profilex_convergence.png", dpi=300, bbox_inches="tight")
save_time = time.perf_counter() - save_start
print(f"✓ Figure saved as '20PCT_ubar_profilex_convergence.png' ({save_time:.2f}s)")

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

