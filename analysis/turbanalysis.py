import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

data_path = Path(au.DATA_PATH)
# Load Data
sim = pio.BudgetIO("Data/Empty_HIT_Tests/UNB3", padeops=True, runid=3)

# Initial Views
uviewz = sim.slice(field_terms="u", ylim=6.25)
umeanviewz = sim.slice(budget_terms="ubar", ylim=6.25)
uviewy = sim.slice(field_terms="u", zlim=6.25)
umeanviewy = sim.slice(budget_terms="ubar", zlim=6.25)

uviewz["u"].imshow()
plt.title("Final Velocity Field for Empty Unblocked Blocked Domain")
plt.savefig("./UNB_Final_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

umeanviewz["ubar"].imshow()
plt.title("Time-Averaged Mean Velocity Field for Empty Unblocked Blocked Domain")
plt.savefig("./UNB_Mean_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

uviewy["u"].imshow()
plt.title("Final Velocity Field for Empty Unblocked Blocked Domain")
plt.savefig("./UNB_Final_Fieldy.png", dpi=300, bbox_inches="tight")
plt.close()

umeanviewy["ubar"].imshow()
plt.title("Time-Averaged Mean Velocity Field for Empty Unblocked Blocked Domain")
plt.savefig("./UNB_Mean_Fieldy.png", dpi=300, bbox_inches="tight")
plt.close()

# 3D fields
uc = np.asarray(sim.slice(field_terms="u")["u"])

ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])

np.save("./UNB_uc.npy", uc)
np.save("./UNB_ubar.npy", ubar)


print("uc shape:", uc.shape)
print("ubar shape:", ubar.shape)

# Fluctuations
uprime_3d = uc - ubar

# Variance over y and z
uvar_x = np.mean(uprime_3d**2, axis=(1, 2))

# Mean over y and z
ubar_x = np.mean(ubar, axis=(1, 2))

print("ubar_x shape:", ubar_x.shape)

# Turbulence Intensity as a Function of X
TIu = np.where(ubar_x != 0, (np.sqrt(uvar_x) / ubar_x) * 100, np.nan)
print("TIu shape:", TIu.shape)
np.save("./UNB_TIu_x.npy", TIu)
np.save("./UNB_x.npy", sim.x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sim.x, TIu, label="Streamwise TI (u)")
plt.xlabel("x/D")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity vs x/D in Empty Unblocked Blocked Domain")
plt.legend()
plt.grid()
plt.savefig("./UNB_TI.png", dpi=300, bbox_inches="tight")
plt.close()

# Log-log Plot of Velocity and Variance
ratio = np.where(uvar_x != 0, ubar_x / uvar_x, np.nan)
np.save("./UNB_loglog_ratio.npy", ratio)

plt.figure(figsize=(10, 6))
plt.loglog(sim.x, ratio, label="Mean Velocity / Variance")
plt.xlabel("x/D")
plt.ylabel("Mean Velocity / Variance")
plt.title("Log-Log Plot of Mean Velocity / Variance vs x/D in Empty Unblocked Blocked Domain")
plt.legend()
plt.grid(True, which="both")
plt.savefig("./UNB_LogLog.png", dpi=300, bbox_inches="tight")
plt.close()

# TI Time Series
tids = range(0, 18965, 1000)
all_t = sim.unique_times()

ut = []
ubart = []
t = []

for i, tid in enumerate(tids):
    data_f = sim.slice(field_terms=["u"], xlim=5, ylim=6.25, zlim=6.25, tidx=tid)
    data_b = sim.slice(budget_terms=["ubar"], xlim=5, ylim=6.25, zlim=6.25, tidx=tid)

    ut.append(np.asarray(data_f["u"]))
    ubart.append(np.asarray(data_b["ubar"]))

    if i < len(all_t):
        t.append(all_t[i])

ut = np.asarray(ut).squeeze()
ubart = np.asarray(ubart).squeeze()
t = np.asarray(t).squeeze()

uprime = ut - ubart

TIu_inst = np.where(ubart != 0, (np.abs(uprime) / ubart) * 100, np.nan)

window = 20
TIu_rms = np.zeros_like(TIu_inst, dtype=float)

for i in range(len(uprime)):
    start = max(0, i - window)
    u_rms = np.sqrt(np.mean(uprime[start:i + 1] ** 2))
    u_mean = np.mean(ubart[start:i + 1])
    TIu_rms[i] = (u_rms / u_mean) * 100 if u_mean != 0 else np.nan

np.save("./UNB_TIu_RMS_t.npy", TIu_rms)
np.save("./UNB_t.npy", t)

plt.figure(figsize=(10, 6))
plt.plot(t, TIu_rms, label="RMS TIu", color="blue", linewidth=2)
plt.xlabel("Physical Time")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity at Future Turbine Location in Empty Unblocked Blocked Domain")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_TI_TimeSeries.png", dpi=300, bbox_inches="tight")
plt.close()
