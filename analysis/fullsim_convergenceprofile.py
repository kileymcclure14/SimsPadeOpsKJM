import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc
import time

print("=" * 60)
print("Streamwise Velocity Profile at Multiple Times")
print("=" * 60)

print("\n[1/3] Initializing BudgetIO...")
init_start = time.perf_counter()
sim = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=3)
init_time = time.perf_counter() - init_start
print(f"✓ BudgetIO initialized in {init_time:.2f}s")

print("\n[2/3] Setting up timestep list...")
tids = list(range(25000, 32559, 100))
print(f"✓ Timesteps to load: {len(tids)}")

# Pick midpoint indices for y and z
data_test = sim.slice(budget_terms=["ubar"], tidx=tids[0])
print(f"  ubar shape: {data_test['ubar'].shape}  (expected: x, y, z)")
j_mid = data_test["ubar"].shape[1] // 2  # mid y index
k_mid = data_test["ubar"].shape[2] // 2  # mid z index
print(f"  Using y index={j_mid}, z index={k_mid}")

print("\n[3/3] Loading and plotting...\n")
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
colors = cmc.batlow(np.linspace(0, 1, len(tids)))
load_start = time.perf_counter()

for k, tid in enumerate(tids):
    iter_start = time.perf_counter()

    data = sim.slice(budget_terms=["ubar"], tidx=tid)

    # Single line through domain at fixed y, z — preserves x variation
    ubar_line = data["ubar"][:, j_mid, k_mid]
    ax.plot(sim.x, ubar_line, color=colors[k], lw=0.8)

    iter_time = time.perf_counter() - iter_start
    progress = (k + 1) / len(tids) * 100
    print(f"  [{k+1:3d}/{len(tids):3d}] tid={tid:6d} ({progress:5.1f}%) - {iter_time:.3f}s")

total_load_time = time.perf_counter() - load_start

# Colorbar
sm = mpl.cm.ScalarMappable(cmap=cmc.batlow,
                            norm=mpl.colors.Normalize(vmin=tids[0], vmax=tids[-1]))
sm.set_array([])
fig.subplots_adjust(right=0.82)
cbar_ax = fig.add_axes([0.85, 0.15, 0.03, 0.7])
fig.colorbar(sm, cax=cbar_ax, label="tid")

ax.set(xlabel="x", ylabel="ubar",
       title="Streamwise Ubar Profile at Mid y/z (Unblocked Transient Period)")
ax.ticklabel_format(useOffset=False, style='plain', axis='y')
ax.grid(True, alpha=0.3)

plt.savefig("UNB_streamwise_profile_trans.png", dpi=300, bbox_inches="tight")
print("✓ Figure saved as 'UNB_streamwise_profile_trans.png'")
plt.close()

total_time = time.perf_counter() - init_start
print("\n" + "=" * 60)
print(f"TOTAL TIME: {total_time:.2f}s")
print("=" * 60)
print("✓ Done!")