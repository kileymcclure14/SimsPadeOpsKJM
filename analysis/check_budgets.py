import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio
from scipy.signal import find_peaks 

data_path = Path(au.DATA_PATH)

# Load Data
sim = pio.BudgetIO("Data/Empty_Domains/Spinups/20PCT", padeops=True, runid=1)

# Pull Data
tids = range(0, 1362, 10)
u, ubar = [], []

for tid in tids:
    data_f = sim.slice(field_terms=["u"], xlim=0.99, ylim=0.99, zlim=0.99, tidx=tid)
    data_b = sim.slice(budget_terms=["ubar"], xlim=0.99, ylim=0.99, zlim=0.99, tidx=tid)

    u.append(np.asarray(data_f["u"]))
    ubar.append(np.asarray(data_b["ubar"]))
u = np.array(u).squeeze()
ubar = np.array(ubar).squeeze()

uprime = u - ubar

# RMS Turbulence Intensity
TIu_inst = np.where(ubar != 0, (np.abs(uprime) / ubar) * 100, np.nan)

window = 20
TIu_rms = np.zeros_like(TIu_inst, dtype=float)

for i in range(len(uprime)):
    start = max(0, i - window)
    u_rms = np.sqrt(np.mean(uprime[start:i+1] ** 2))
    u_mean = np.mean(ubar[start:i+1])
    TIu_rms[i] = (u_rms / u_mean) * 100 if u_mean != 0 else np.nan

# Peaks and Valleys
TIu_rms = np.asarray(TIu_rms)
tids_array = np.array(list(tids))

valid = ~np.isnan(TIu_rms)
TI_clean = TIu_rms[valid]
tids_clean = tids_array[valid]

# Find Max and Timestep
peaks, peak_props = find_peaks(TI_clean, prominence=0.5, distance=5)
t_peaks = tids_clean[peaks]
TI_peaks = TI_clean[peaks]

# Find Min and Timestep
valleys, valley_props = find_peaks(-TI_clean, prominence=0.5, distance=5)
t_valleys = tids_clean[valleys]
TI_valleys = TI_clean[valleys]

print("Maxima at:")
for t, val in zip(t_peaks, TI_peaks):
    print(f"t = {t}, TI = {val:.2f}%")

print("\nMinima at:")
for t, val in zip(t_valleys, TI_valleys):
    print(f"t = {t}, TI = {val:.2f}%")

# Plot

plt.figure(figsize=(10, 6))
plt.plot(tids, TIu_rms, label='RMS Turbulence Intensity', color='blue')

# Plot peaks
plt.scatter(t_peaks, TI_peaks, color='red', label='Maxima', zorder=3)

# Plot valleys
plt.scatter(t_valleys, TI_valleys, color='green', label='Minima', zorder=3)

plt.xlabel('Time Index')
plt.ylabel('Turbulence Intensity (%)')
plt.title('Turbulence Intensity Budget Check for Unblocked Domain Spinup')
plt.grid()
plt.legend()
plt.savefig("20PCTSpin_budgetcheck", dpi=300)
plt.show()