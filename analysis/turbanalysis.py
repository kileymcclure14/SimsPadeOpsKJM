import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio
import gc

data_path = Path(au.DATA_PATH)

# =============================================================================
# Load Data
# =============================================================================
sim = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=4)

# =============================================================================
# Initial Views
# =============================================================================
uviewz    = sim.slice(field_terms="u",        ylim=6.25)
umeanviewz = sim.slice(budget_terms="ubar",   ylim=6.25)
uviewy    = sim.slice(field_terms="u",        zlim=6.25)
umeanviewy = sim.slice(budget_terms="ubar",   zlim=6.25)

uviewz["u"].imshow()
plt.title("Final Velocity Field for Unblocked Domain", pad=20)
plt.savefig("./UNB_Final_Fieldz_full.png", dpi=300, bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
umeanviewz["ubar"].imshow(ax=ax)
ax.set_title("Time-Averaged Mean Velocity Field for Unblocked Domain", pad=20)
fig.subplots_adjust(top=0.88)
plt.savefig("./UNB_Mean_Fieldz_full.png", dpi=300, bbox_inches="tight")
plt.close()

uviewy["u"].imshow()
plt.title("Final Velocity Field for Unblocked Domain", pad=20)
plt.savefig("./UNB_Final_Fieldy_full.png", dpi=300, bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
umeanviewy["ubar"].imshow(ax=ax)
ax.set_title("Time-Averaged Mean Velocity Field for Unblocked Domain", pad=20)
fig.subplots_adjust(top=0.88)
plt.savefig("./UNB_Mean_Fieldy_full.png", dpi=300, bbox_inches="tight")
plt.close()

# =============================================================================
# 3D Fields
# =============================================================================
uc   = np.asarray(sim.slice(field_terms="u")["u"])
vc   = np.asarray(sim.slice(field_terms="v")["v"])
wc   = np.asarray(sim.slice(field_terms="w")["w"])

ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])
vbar = np.asarray(sim.slice(budget_terms="vbar")["vbar"])
wbar = np.asarray(sim.slice(budget_terms="wbar")["wbar"])

print("uc shape:  ", uc.shape)
print("ubar shape:", ubar.shape)

# =============================================================================
# Fluctuations
# =============================================================================
uprime_3d = uc   - ubar
vprime_3d = vc   - vbar
wprime_3d = wc   - wbar

# Per-component variance averaged over y and z  (shape: nx)
uvar_x = np.mean(uprime_3d**2, axis=(1, 2))
vvar_x = np.mean(vprime_3d**2, axis=(1, 2))
wvar_x = np.mean(wprime_3d**2, axis=(1, 2))

# Mean velocity components averaged over y and z  (shape: nx)
ubar_x = np.mean(ubar, axis=(1, 2))
vbar_x = np.mean(vbar, axis=(1, 2))
wbar_x = np.mean(wbar, axis=(1, 2))

# =============================================================================
# Spatial Turbulence Intensity vs x
# =============================================================================
u_rms = np.sqrt((uvar_x + vvar_x + wvar_x) / 3)   # shape (nx,)

ubar_speed = np.sqrt(ubar**2 + vbar**2 + wbar**2)  # shape (nx, ny, nz)
ubar_mag   = np.mean(ubar_speed, axis=(1, 2))       # shape (nx,)

TI = np.where(ubar_mag != 0, (u_rms / ubar_mag) * 100, np.nan)
print("TI shape:", TI.shape)

plt.figure(figsize=(10, 6))
plt.plot(sim.x, TI, label="TI%")
plt.xlabel("x/D")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity vs x/D in Unblocked Domain")
plt.legend()
plt.grid()
plt.savefig("./UNB_TI_full.png", dpi=300, bbox_inches="tight")
plt.close()

np.save("./UNB_TIx_full.npy", TI)

# =============================================================================
# Turbulent Kinetic Energy vs x (averaged over y and z)
# =============================================================================
TKE_x = 0.5 * (uvar_x + vvar_x + wvar_x)

plt.figure(figsize=(10, 6))
plt.plot(sim.x, TKE_x, label="TKE", color="purple")
plt.xlabel("x/D")
plt.ylabel("TKE")
plt.title("Turbulent Kinetic Energy vs x/D in Unblocked Domain")
plt.legend()
plt.grid()
plt.savefig("./UNB_TKE_full.png", dpi=300, bbox_inches="tight")
plt.close()

np.save("./UNB_TKEx_full.npy", TKE_x)

# =============================================================================
# TI Time Series at Future Turbine Location (x=5D)
# =============================================================================
tids    = range(33000, 64422, 1000) 
all_t   = sim.unique_times()

# Only keep tids that don't exceed what we have
valid_tids = [(i, tid) for i, tid in enumerate(tids) if i < len(all_t)]

print(f"Processing {len(valid_tids)} timesteps...\n")

# Store only scalar results
TIu_rms_list = []
t_list = []
successful_count = 0

# Pre-compute tid to time mapping parameters
tid_min, tid_max = min(tids), max(tids)
t_min, t_max = all_t.min(), all_t.max()
tid_range = tid_max - tid_min
t_range = t_max - t_min

for idx, (i, tid) in enumerate(valid_tids):
    try:
        if (idx + 1) % 10 == 0:
            print(f"  Processing timestep {idx + 1}/{len(valid_tids)}...")
        
        # Load data
        data_f = sim.slice(field_terms=["u"],    xlim=5, ylim=6.25, zlim=6.25, tidx=tid)
        data_b = sim.slice(budget_terms=["ubar"], xlim=5, ylim=6.25, zlim=6.25, tidx=tid)

        # Extract velocity and mean velocity
        ut    = np.asarray(data_f["u"]).squeeze()
        ubart = np.asarray(data_b["ubar"]).squeeze()
        
        # Calculate fluctuations and RMS
        uprime = ut - ubart
        u_rms_t = np.sqrt(np.mean(uprime ** 2))
        u_mean  = np.mean(ubart)
        
        # Calculate turbulence intensity
        ti_value = (u_rms_t / u_mean) * 100 if u_mean != 0 else np.nan
        TIu_rms_list.append(ti_value)
        
        # Map tid to corresponding time in all_t
        approx_time = t_min + (tid - tid_min) / tid_range * t_range
        closest_idx = np.argmin(np.abs(all_t - approx_time))
        t_list.append(all_t[closest_idx])
        
        successful_count += 1
        
        # Clean up
        del data_f, data_b, ut, ubart, uprime
        gc.collect()
        
    except MemoryError as e:
        print(f"  Memory error at tidx {tid}, skipping...")
        continue
    except Exception as e:
        print(f"  Error at tidx {tid}: {e}, skipping...")
        continue

print(f"\nSuccessfully loaded {successful_count}/{len(valid_tids)} timesteps\n")

# Convert to arrays
TIu_rms = np.asarray(TIu_rms_list)
t = np.asarray(t_list)

# =============================================================================
# Apply Rolling Window
# =============================================================================
window = 20
TIu_rms_rolling = np.zeros_like(TIu_rms, dtype=float)

for i in range(len(TIu_rms)):
    start = max(0, i - window)
    TIu_rms_rolling[i] = np.nanmean(TIu_rms[start:i + 1])

# =============================================================================
# Calculate Statistics
# =============================================================================
mean_TI = np.nanmean(TIu_rms_rolling)
std_TI = np.nanstd(TIu_rms_rolling)

print(f"Mean TI: {mean_TI:.2f}%")
print(f"Std TI:  {std_TI:.2f}%\n")

# =============================================================================
# Plot Time-Series with ±1 std shading
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(t, TIu_rms_rolling, label="TI%", color="blue", linewidth=2)
ax.axhline(mean_TI, color="red", linestyle="--", linewidth=1.5,
           label=f"Mean = {mean_TI:.1f}%")
ax.axhline(mean_TI + std_TI, color="red", linestyle=":", linewidth=1.0)
ax.axhline(mean_TI - std_TI, color="red", linestyle=":", linewidth=1.0)
ax.fill_between(t, mean_TI - std_TI, mean_TI + std_TI,
                color="red", alpha=0.15, label=f"±1 Std ({std_TI:.1f}%)")

ax.set_xlabel("Physical Time", fontsize=12)
ax.set_ylabel("Turbulence Intensity (%)", fontsize=12)
ax.set_title("Turbulence Intensity at Future Turbine Location in Unblocked Domain", 
             fontsize=14, pad=20)
ax.set_ylim(0, 100)
ax.grid(True, alpha=0.3)
ax.legend(loc='best', fontsize=10)
fig.tight_layout()
fig.savefig("./UNB_TI_TimeSeries_full.png", dpi=300, bbox_inches="tight")
plt.close()

# =============================================================================
# Save Results
# =============================================================================
np.save("./UNB_TItime_full.npy", TIu_rms_rolling)
np.save("./UNB_phystime_full.npy", t)

print("Analysis complete!")