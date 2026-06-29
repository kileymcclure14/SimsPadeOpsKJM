import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

sim10 = pio.BudgetIO("Data/Empty_Domains/10PCT", padeops=True, runid=4)
sim20 = pio.BudgetIO("Data/Empty_Domains/20PCT", padeops=True, runid=4)
simUNB = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=4)

# TI as a function of X
TI10 = np.load("./10PCT_TIx_full.npy")
TI20 = np.load("./20PCT_TIx_full.npy")
TIUNB = np.load("./UNB_TIx_full.npy")

plt.figure(figsize=(10, 6))
plt.plot(sim10.x, TI10, label="10% Blocked Domain")
plt.plot(sim20.x, TI20, label="20% Blocked Domain")
plt.plot(simUNB.x, TIUNB, label="Unblocked Domain")
plt.xlabel("x/D")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity vs x/D in Empty Domains")
plt.legend()
plt.grid()
plt.savefig("./Empty_Domain_TI_comparison.png", dpi=300, bbox_inches="tight")
plt.close()

# TKE as a function of X
TKE10 = np.load("./10PCT_TKEx_full.npy")
TKE20 = np.load("./20PCT_TKEx_full.npy")
TKEUNB = np.load("./UNB_TKEx_full.npy")

plt.figure(figsize=(10, 6))
plt.plot(sim10.x, TKE10, label="10% Blocked Domain")
plt.plot(sim20.x, TKE20, label="20% Blocked Domain")
plt.plot(simUNB.x, TKEUNB, label="Unblocked Domain")
plt.xlabel("x/D")
plt.ylabel("Turbulent Kinetic Energy")
plt.title("Turbulent Kinetic Energy vs x/D in Empty Domains")
plt.legend()
plt.grid()
plt.savefig("./Empty_Domain_TKE_comparison.png", dpi=300, bbox_inches="tight")
plt.close()

# TI Time Sereis at Future Turbine Location
import numpy as np
import matplotlib.pyplot as plt

# TI Time Series at Future Turbine Location
TI10_time = np.load("./10PCT_TItime_full.npy")
TI20_time = np.load("./20PCT_TItime_full.npy")
TIUNB_time = np.load("./UNB_TItime_full.npy")
phys_time10 = np.load("./10PCT_phystime_full.npy")
phys_time20 = np.load("./20PCT_phystime_full.npy")
phys_timeUNB = np.load("./UNB_phystime_full.npy")

# Compute statistics
mean10, std10 = np.mean(TI10_time), np.std(TI10_time)
mean20, std20 = np.mean(TI20_time), np.std(TI20_time)
meanUNB, stdUNB = np.mean(TIUNB_time), np.std(TIUNB_time)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot time series
c10, c20, cUNB = "#1f77b4", "#ff7f0e", "#2ca02c"
ax.plot(phys_time10, TI10_time, color=c10, alpha=0.6, linewidth=0.8)
ax.plot(phys_time20, TI20_time, color=c20, alpha=0.6, linewidth=0.8)
ax.plot(phys_timeUNB, TIUNB_time, color=cUNB, alpha=0.6, linewidth=0.8)

# Mean lines (horizontal) with std fill — added to legend via these handles
ax.axhline(mean10, color=c10, linewidth=2, linestyle="--",
           label=f"10% Blocked Domain  |  μ={mean10:.2f}%  σ={std10:.2f}%")
ax.axhline(mean20, color=c20, linewidth=2, linestyle="--",
           label=f"20% Blocked Domain  |  μ={mean20:.2f}%  σ={std20:.2f}%")
ax.axhline(meanUNB, color=cUNB, linewidth=2, linestyle="--",
           label=f"Unblocked Domain  |  μ={meanUNB:.2f}%  σ={stdUNB:.2f}%")

# ±1σ shaded bands
ax.axhspan(mean10 - std10, mean10 + std10, color=c10, alpha=0.15)
ax.axhspan(mean20 - std20, mean20 + std20, color=c20, alpha=0.15)
ax.axhspan(meanUNB - stdUNB, meanUNB + stdUNB, color=cUNB, alpha=0.15)

ax.set_xlabel("Time")
ax.set_ylabel("Turbulence Intensity (%)")
ax.set_title("Turbulence Intensity Time Series at Future Turbine Location")
ax.legend()
ax.grid()

plt.savefig("./Empty_Domain_TI_time_series.png", dpi=300, bbox_inches="tight")
plt.close()