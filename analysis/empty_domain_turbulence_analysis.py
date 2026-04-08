import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

data_path = Path(au.DATA_PATH)

# Load Data
sim = pio.BudgetIO("Data/Empty_HIT_Tests/10pct", padeops=True, runid=3)

# Initial Views
uviewz = sim.slice(field_terms="u", ylim=1.4)
umeanviewz = sim.slice(budget_terms="ubar", ylim=1.4)
uviewy = sim.slice(field_terms="u", zlim=1.4)
umeanviewy = sim.slice(budget_terms="ubar", zlim=1.4)

uviewz["u"].imshow()
plt.title("Final Velocity Field for Empty 10% Domain")
plt.savefig("./10PCT_Final_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

umeanviewz["ubar"].imshow()
plt.title("Time-Averaged Mean Velocity Field for Empty 10% Domain")
plt.savefig("./10PCT_Mean_Fieldz.png", dpi=300, bbox_inches="tight")
plt.close()

uviewy["u"].imshow()
plt.title("Final Velocity Field for Empty 10% Domain")
plt.savefig("./10PCT_Final_Fieldy.png", dpi=300, bbox_inches="tight")
plt.close()

umeanviewy["ubar"].imshow()
plt.title("Time-Averaged Mean Velocity Field for Empty 10% Domain")
plt.savefig("./10PCT_Mean_Fieldy.png", dpi=300, bbox_inches="tight")
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

print("ubar_x shape:", ubar_x.shape)

# Turbulence Intensity as a Function of X
TIu = np.where(ubar_x != 0, (np.sqrt(uvar_x) / ubar_x) * 100, np.nan)
print("TIu shape:", TIu.shape)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sim.x, TIu, label="Streamwise TI (u)")
plt.xlabel("x/D")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Turbulence Intensity vs x/D")
plt.legend()
plt.grid()
plt.savefig("./10PCT_TI.png", dpi=300, bbox_inches="tight")
plt.close()

# Log-log Plot of Velocity and Variance
mean_u_x = np.mean(uc, axis=(1, 2))
ratio = np.where(uvar_x != 0, mean_u_x / uvar_x, np.nan)

plt.figure(figsize=(10, 6))
plt.loglog(sim.x, ratio, label="Mean Velocity / Variance")
plt.xlabel("x/D")
plt.ylabel("Mean Velocity / Variance")
plt.title("Log-Log Plot of Mean Velocity / Variance vs x/D")
plt.legend()
plt.grid(True, which="both")
plt.savefig("./10PCT_LogLog.png", dpi=300, bbox_inches="tight")
plt.close()

# Spectra
uprime = uprime_3d
nx, ny, nz = uprime.shape
dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

print("Grid:", nx, ny, nz)
print("dx, dy, dz:", dx, dy, dz)

use_window = True
if use_window:
    wx = np.hanning(nx)[:, None, None]
    wy = np.hanning(ny)[None, :, None]
    wz = np.hanning(nz)[None, None, :]
else:
    wx = 1.0
    wy = 1.0
    wz = 1.0

# x spectrum: Euu(kx, y, z) averaged over y,z
u_x = uprime * wy * wz
uhat_x = np.fft.fft(u_x, axis=0)
kx = 2 * np.pi * np.fft.fftfreq(nx, d=dx)

Euu_kx_yz = (np.abs(uhat_x) ** 2) / nx
Euu_kx = np.mean(Euu_kx_yz, axis=(1, 2))

pos_kx = kx > 0
kx_pos = kx[pos_kx]
Euu_kx_pos = Euu_kx[pos_kx]

# Reference line for kx spectrum
kx_ref_idx = 1 if len(kx_pos) > 1 else 0
kx_ref = kx_pos[kx_ref_idx]
kx_ref_amp = Euu_kx_pos[kx_ref_idx]
kx_line = kx_ref_amp * (kx_pos / kx_ref) ** (-2/3)

# Kx Plots
plt.figure(figsize=(10, 6))
plt.loglog(kx_pos, Euu_kx_pos, label=r'$\langle E_{uu}(k_x,y,z)\rangle_{yz}$')
plt.loglog(kx_pos, kx_line, '--', color='red', label=r'$-2/3$ reference')
plt.xlabel(r'$k_x$')
plt.ylabel(r'$E_{uu}(k_x)$')
plt.title('Streamwise spectrum averaged over y,z')
plt.grid(True, which='both')
plt.legend()
plt.savefig("./10PCT_Euu_kx_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(kx_pos, Euu_kx_pos, label=r'$\langle E_{uu}(k_x,y,z)\rangle_{yz}$')
plt.xlabel(r'$k_x$')
plt.ylabel(r'$E_{uu}(k_x)$')
plt.title('Streamwise spectrum averaged over y,z (linear)')
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_kx.png", dpi=300, bbox_inches = "tight")
plt.close()

# y spectrum: Euu(x, ky, z) averaged over z at selected x
u_y = uprime * wx * wz
uhat_y = np.fft.fft(u_y, axis=1)
ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)

Euu_ky_xz = (np.abs(uhat_y) ** 2) / ny
Euu_ky_x = np.mean(Euu_ky_xz, axis=2)

pos_ky = ky > 0
ky_pos = ky[pos_ky]
Euu_ky_pos = Euu_ky_x[:, pos_ky]

x_targets = [5, 10, 15]
x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]
for xt, idx in zip(x_targets, x_indices):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# Reference lines for log-log spectra
ref_x_idx = x_indices[1]  # use the middle x location, e.g. x/D ~ 10

# Reference Line for Ky Spectra
ky_ref_idx = 1 if len(ky_pos) > 1 else 0
ky_ref_amp = Euu_ky_pos[ref_x_idx, ky_ref_idx]
ky_ref = ky_pos[ky_ref_idx]
ky_line = ky_ref_amp * (ky_pos / ky_ref) ** (-5/3)

# Ky Plots
plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.loglog(ky_pos, Euu_ky_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.loglog(ky_pos, ky_line, "--", color="red", label=r"$-5/3$ reference")
plt.xlabel(r"$k_y$")
plt.ylabel(r"$E_{uu}(x,k_y)$")
plt.title("Euu vs ky at selected x/D")
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_ky_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(ky_pos, Euu_ky_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r'$k_y$')
plt.ylabel(r'$E_{uu}(x,k_y)$')
plt.title('Euu vs ky (linear)')
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_ky.png", dpi=300, bbox_inches="tight")
plt.close()

# z spectrum: Euu(x, y, kz) averaged over y at selected x
u_z = uprime * wx * wy
uhat_z = np.fft.fft(u_z, axis=2)
kz = 2 * np.pi * np.fft.fftfreq(nz, d=dz)

Euu_kz_xy = (np.abs(uhat_z) ** 2) / nz
Euu_kz_x = np.mean(Euu_kz_xy, axis=1)

pos_kz = kz > 0
kz_pos = kz[pos_kz]
Euu_kz_pos = Euu_kz_x[:, pos_kz]

# Reference Line for Kz
kz_ref_idx = 1 if len(kz_pos) > 1 else 0
kz_ref_amp = Euu_kz_pos[ref_x_idx, kz_ref_idx]
kz_ref = kz_pos[kz_ref_idx]
kz_line = kz_ref_amp * (kz_pos / kz_ref) ** (-5/3)

# Kx Plots
plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.loglog(kz_pos, Euu_kz_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.loglog(kz_pos, kz_line, "--", color="red", label=r"$-5/3$ reference")
plt.xlabel(r"$k_z$")
plt.ylabel(r"$E_{uu}(x,k_z)$")
plt.title("Euu vs kz at selected x/D")
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_kz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(kz_pos, Euu_kz_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r'$k_z$')
plt.ylabel(r'$E_{uu}(x,k_z)$')
plt.title('Euu vs kz at selected x/D (linear)')
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_kz.png", dpi=300, bbox_inches="tight")
plt.close()

# TI Time Series
tids = range(0, 3062, 10)
all_t = sim.unique_times()

ut, vt, wt = [], [], []
ubart, vbart, wbart = [], [], []
t = []

for i, tid in enumerate(tids):
    data_f = sim.slice(field_terms=["u", "v", "w"], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)
    data_b = sim.slice(budget_terms=["ubar", "vbar", "wbar"], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)

    ut.append(np.asarray(data_f["u"]))
    vt.append(np.asarray(data_f["v"]))
    wt.append(np.asarray(data_f["w"]))

    ubart.append(np.asarray(data_b["ubar"]))
    vbart.append(np.asarray(data_b["vbar"]))
    wbart.append(np.asarray(data_b["wbar"]))

    if i < len(all_t):
        t.append(all_t[i])

ut = np.asarray(ut).squeeze()
vt = np.asarray(vt).squeeze()
wt = np.asarray(wt).squeeze()
ubart = np.asarray(ubart).squeeze()
vbart = np.asarray(vbart).squeeze()
wbart = np.asarray(wbart).squeeze()
t = np.asarray(t).squeeze()

uprime = ut - ubart
vprime = vt - vbart
wprime = wt - wbart

TIu_inst = np.where(ubart != 0, (np.abs(uprime) / ubart) * 100, np.nan)
TIv_inst = np.where(vbart != 0, (np.abs(vprime) / vbart) * 100, np.nan)
TIw_inst = np.where(wbart != 0, (np.abs(wprime) / wbart) * 100, np.nan)

window = 20
TIu_rms = np.zeros_like(TIu_inst, dtype=float)

for i in range(len(uprime)):
    start = max(0, i - window)
    u_rms = np.sqrt(np.mean(uprime[start:i+1] ** 2))
    u_mean = np.mean(ubart[start:i+1])
    TIu_rms[i] = (u_rms / u_mean) * 100 if u_mean != 0 else np.nan

plt.figure(figsize=(10, 6))
plt.plot(t, TIu_inst, label="Instantaneous TIu", alpha=0.5)
plt.plot(t, TIu_rms, label="RMS TIu", color="blue", linewidth=2)
plt.xlabel("Physical Time")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Instantaneous and RMS Turbulence Intensity at Future Turbine Location")
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_TI_TimeSeries.png", dpi=300, bbox_inches="tight")
plt.close()