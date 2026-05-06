import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

data_path = Path(au.DATA_PATH)
# Load Data
sim = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=3)

# Initial Views
uviewz = sim.slice(field_terms="u", ylim=6.25)
umeanviewz = sim.slice(budget_terms="ubar", ylim=6.25)
uviewy = sim.slice(field_terms="u", zlim=6.25)
umeanviewy = sim.slice(budget_terms="ubar", zlim=6.25)

uviewz["u"].imshow()
plt.title("Final Velocity Field for Unblocked Domain", pad = 20)
plt.savefig("./UNB_Final_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
umeanviewz["ubar"].imshow(ax=ax)
ax.set_title("Time-Averaged Mean Velocity Field for Unblocked Domain", pad=20)
fig.subplots_adjust(top=0.88)
plt.savefig("./UNB_Mean_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

uviewy["u"].imshow()
plt.title("Final Velocity Field for Unblocked Domain", pad = 20)
plt.savefig("./UNB_Final_Fieldy.png", dpi=300, bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
umeanviewy["ubar"].imshow(ax=ax)
ax.set_title("Time-Averaged Mean Velocity Field for Unblocked Domain", pad=20)
fig.subplots_adjust(top=0.88)
plt.savefig("./UNB_Mean_Fieldy.png", dpi=300, bbox_inches="tight")
plt.close()

# 3D fields
uc = np.asarray(sim.slice(field_terms="u")["u"])
vc = np.asarray(sim.slice(field_terms="v")["v"])
wc = np.asarray(sim.slice(field_terms="w")["w"])

ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])
vbar = np.asarray(sim.slice(budget_terms="vbar")["vbar"])
wbar = np.asarray(sim.slice(budget_terms="wbar")["wbar"])

print("uc shape:", uc.shape)
print("ubar shape:", ubar.shape)

# Fluctuations
uprime_3d = uc - ubar
vprime_3d = vc - vbar
wprime_3d = wc - wbar

# Variance over y and z
uvar_x = np.mean(uprime_3d**2, axis=(1, 2))
vvar_x = np.mean(vprime_3d**2, axis=(1, 2))
wvar_x = np.mean(wprime_3d**2, axis=(1, 2))

# Mean over y and z
ubar_x = np.mean(ubar, axis=(1, 2))
vbar_x = np.mean(vbar, axis=(1, 2))
wbar_x = np.mean(wbar, axis=(1, 2))

#Magnitudes
uprime_mag = np.sqrt(uprime_3d**2 + vprime_3d**2 + wprime_3d**2)
uprime_mag = np.mean(uprime_mag, axis=(1, 2))
ubar_mag = np.sqrt(ubar**2 + vbar**2 + wbar**2)
ubar_mag = np.mean(ubar_mag, axis=(1, 2))

# Turbulence Intensity as a Function of X
TI = np.where(ubar_mag!= 0, (np.sqrt(uprime_mag) / ubar_mag) * 100, np.nan)
print("TI shape:", TI.shape)
# np.save("./UNB_TIu_x.npy", TIu)
# np.save("./UNB_x.npy", sim.x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sim.x, TI, label="TI%")
plt.xlabel("x/D")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity vs x/D in Unblocked Domain")
plt.legend()
plt.grid()
plt.savefig("./UNB_TI.png", dpi=300, bbox_inches="tight")
plt.close()

# TKE With X Averaged Over Y and Z
TKE_x = 0.5 * (uvar_x + vvar_x + wvar_x)

plt.figure(figsize=(10, 6))
plt.plot(sim.x, TKE_x, label="TKE", color="purple")
plt.xlabel("x/D")
plt.ylabel("TKE")
plt.title("Turbulent Kinetic Energy vs x/D in Unblocked Domain")
plt.legend()
plt.grid()
plt.savefig("./UNB_TKE.png", dpi=300, bbox_inches="tight")
plt.close()

# TI Time Series
tids = range(0, 2265, 100)
all_t = sim.unique_times()

# Only keep tids that have a corresponding time
valid_tids = [(i, tid) for i, tid in enumerate(tids) if i < len(all_t)]

ut = []
ubart = []
t = []

for i, tid in valid_tids:
    data_f = sim.slice(field_terms=["u"], xlim=5, ylim=6.25, zlim=6.25, tidx=tid)
    data_b = sim.slice(budget_terms=["ubar"], xlim=5, ylim=6.25, zlim=6.25, tidx=tid)

    ut.append(np.asarray(data_f["u"]))
    ubart.append(np.asarray(data_b["ubar"]))
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

# np.save("./UNB_TIu_RMS_t.npy", TIu_rms)
# np.save("./UNB_t.npy", t)

plt.figure(figsize=(10, 6))
plt.plot(t, TIu_rms, label="RMS TIu", color="blue", linewidth=2)
plt.xlabel("Physical Time")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity at Future Turbine Location in Unblocked Domain")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.savefig("./UNB_TI_TimeSeries.png", dpi=300, bbox_inches="tight")
plt.close()
