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

ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])

np.save("./10PCT_uc.npy", uc)
np.save("./10PCT_ubar.npy", ubar)

print("uc shape:", uc.shape)
print("ubar shape:", ubar.shape)

# Fluctuations
uprime_3d = uc - ubar

np.save("./10PCT_uprime_3d.npy", uprime_3d)

# Variance over y and z
uvar_x = np.mean(uprime_3d**2, axis=(1, 2))

# Mean over y and z
ubar_x = np.mean(ubar, axis=(1, 2))

print("ubar_x shape:", ubar_x.shape)

# Turbulence Intensity as a Function of X
TIu = np.where(ubar_x != 0, (np.sqrt(uvar_x) / ubar_x) * 100, np.nan)
print("TIu shape:", TIu.shape)
np.save("./10PCT_TIu_x.npy", TIu)
np.save("./10PCT_x.npy", sim.x)

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
np.save("./10PCT_loglog_ratio.npy", ratio)

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

# y spectrum: Euu(x, ky, z) averaged over z at selected x
u_y = uprime * wz
uhat_y = np.fft.fft(u_y, axis=1)
ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)

Euu_ky_xz = (np.abs(uhat_y) ** 2) / ny
Euu_ky_x = np.mean(Euu_ky_xz, axis=2)

pos_ky = ky > 0
ky_pos = ky[pos_ky]
Euu_ky_pos = Euu_ky_x[:, pos_ky]

np.save("./10PCT_ky.npy", ky_pos)
np.save("./10PCT_Euu_ky_xz.npy", Euu_ky_pos)

x_targets = [5, 10, 17]
x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]

for xt, idx in zip(x_targets, x_indices):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# Ky Plots
plt.figure(figsize=(10, 6))
ky_ref_idx = 2 if len(ky_pos) > 2 else 1
ky_ref_slice = slice(ky_ref_idx, min(len(ky_pos), ky_ref_idx + 12))
for xt, idx in zip(x_targets, x_indices):
    spectrum_line, = plt.loglog(
        ky_pos,
        Euu_ky_pos[idx, :],
        linewidth=2,
        label=f"x/D={sim.x[idx]:.2f}",
    )
    c = spectrum_line.get_color()

    ky_ref = ky_pos[ky_ref_idx]
    ky_ref_amp = Euu_ky_pos[idx, ky_ref_idx]

    ky_ref_x = ky_pos[ky_ref_slice]
    ky_ref_y = ky_ref_amp * (ky_ref_x / ky_ref) ** (-5 / 3)

    np.save(f"./10PCT_ky_ref_x_xidx_{idx}.npy", ky_ref_x)
    np.save(f"./10PCT_ky_ref_y_xidx_{idx}.npy", ky_ref_y)

    plt.loglog(
        ky_ref_x,
        ky_ref_y,
        "--",
        color=c,
        linewidth=1.6,
        label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}",
    )
plt.xlabel(r"$k_y$")
plt.ylabel(r"$E_{uu}(x,k_y)$")
plt.title("Euu vs ky at selected x/D (log-log)")
plt.ylim(10e-6, 10e-2)
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_ky_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(ky_pos, Euu_ky_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_y$")
plt.ylabel(r"$E_{uu}(x,k_y)$")
plt.title("Euu vs ky (linear)")
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_ky.png", dpi=300, bbox_inches="tight")
plt.close()

# z spectrum: Euu(x, y, kz) averaged over y at selected x
u_z = uprime * wy
uhat_z = np.fft.fft(u_z, axis=2)
kz = 2 * np.pi * np.fft.fftfreq(nz, d=dz)

Euu_kz_xy = (np.abs(uhat_z) ** 2) / nz
Euu_kz_x = np.mean(Euu_kz_xy, axis=1)

pos_kz = kz > 0
kz_pos = kz[pos_kz]
Euu_kz_pos = Euu_kz_x[:, pos_kz]

np.save("./10PCT_kz.npy", kz_pos)
np.save("./10PCT_Euu_kz.npy", Euu_kz_pos)

# Kz Plots
plt.figure(figsize=(10, 6))
kz_ref_idx = 2 if len(kz_pos) > 2 else 1
kz_ref_slice = slice(kz_ref_idx, min(len(kz_pos), kz_ref_idx + 12))
for xt, idx in zip(x_targets, x_indices):
    spectrum_line, = plt.loglog(
        kz_pos,
        Euu_kz_pos[idx, :],
        linewidth=2,
        label=f"x/D={sim.x[idx]:.2f}",
    )
    c = spectrum_line.get_color()

    kz_ref = kz_pos[kz_ref_idx]
    kz_ref_amp = Euu_kz_pos[idx, kz_ref_idx]

    kz_ref_x = kz_pos[kz_ref_slice]
    kz_ref_y = kz_ref_amp * (kz_ref_x / kz_ref) ** (-5 / 3)

    np.save(f"./10PCT_kz_ref_x_xidx_{idx}.npy", kz_ref_x)
    np.save(f"./10PCT_kz_ref_y_xidx_{idx}.npy", kz_ref_y)

    plt.loglog(
        kz_ref_x,
        kz_ref_y,
        "--",
        color=c,
        linewidth=1.6,
        label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}",
    )

plt.xlabel(r"$k_z$")
plt.ylabel(r"$E_{uu}(x,k_z)$")
plt.title("Euu vs kz at selected x/D (log-log)")
plt.ylim(10e-6, 10e-2)
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_kz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(kz_pos, Euu_kz_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_z$")
plt.ylabel(r"$E_{uu}(x,k_z)$")
plt.title("Euu vs kz at selected x/D (linear)")
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_kz.png", dpi=300, bbox_inches="tight")
plt.close()

# TI Time Series
tids = range(0, 3360, 10)
all_t = sim.unique_times()

ut = []
ubart = []
t = []

for i, tid in enumerate(tids):
    data_f = sim.slice(field_terms=["u"], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)
    data_b = sim.slice(budget_terms=["ubar"], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)

    ut.append(np.asarray(data_f["u"]))

    ubart.append(np.asarray(data_b["ubar"]))

    if i < len(all_t):
        t.append(all_t[i])


ut = np.asarray(ut).squeeze()
ubart = np.asarray(ubart).squeeze()
t = np.asarray(t).squeeze()

np.save("./10PCT_ut.npy", ut)
np.save("./10PCT_ubart.npy", ubart)

uprime = ut - ubart

np.save("./10PCT_uprime_t.npy", uprime)

TIu_inst = np.where(ubart != 0, (np.abs(uprime) / ubart) * 100, np.nan)

window = 20
TIu_rms = np.zeros_like(TIu_inst, dtype=float)

for i in range(len(uprime)):
    start = max(0, i - window)
    u_rms = np.sqrt(np.mean(uprime[start:i + 1] ** 2))
    u_mean = np.mean(ubart[start:i + 1])
    TIu_rms[i] = (u_rms / u_mean) * 100 if u_mean != 0 else np.nan


np.save("./10PCT_TIu_RMS_t.npy", TIu_rms)
np.save("./10PCT_t.npy", t)


plt.figure(figsize=(10, 6))
plt.plot(t, TIu_rms, label="RMS TIu", color="blue", linewidth=2)
plt.xlabel("Physical Time")
plt.ylabel("Turbulence Intensity (%)")
plt.title("Instantaneous and RMS Turbulence Intensity at Future Turbine Location")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_TI_TimeSeries.png", dpi=300, bbox_inches="tight")
plt.close()

# Time Spectra Averaged Over y and z plane
x_targets = [2, 5, 8, 10, 12, 15, 17, 20]
tids = range(0, 3360, 10)
all_t = sim.unique_times()

# Build time array
t = []
for i, tid in enumerate(tids):
    if i < len(all_t):
        t.append(all_t[i])

t = np.asarray(t).squeeze()
dt = np.mean(np.diff(t))
nt = len(t)

print("nt =", nt)
print("dt =", dt)

# Frequency axis
ft = np.fft.fftfreq(nt, d=dt)
pos_ft = ft > 0
ft_pos = ft[pos_ft]

np.save("./10PCT_freq.npy", ft_pos)

# Hanning window in time
wt = np.hanning(nt)[:, None, None]

# Map requested x/D values to nearest grid indices
x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]
np.save("./10PCT_time_x_targets.npy", np.asarray(x_targets))
np.save("./10PCT_time_x_indices.npy", np.asarray(x_indices))

# Store spectra by x index
time_spectra = {}
for xt, idx in zip(x_targets, x_indices):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

    u_tseries = []

    for tid in tids:
        data_f = sim.slice(
            field_terms="u",
            xlim=sim.x[idx],
            tidx=tid,
        )
        u_tseries.append(np.asarray(data_f["u"]))

    u_tseries = np.asarray(u_tseries).squeeze()
    print(f"x/D={sim.x[idx]:.2f}, u_tseries shape: {u_tseries.shape}")

    # Remove temporal mean at each (y,z)
    uprime_t = u_tseries - np.mean(u_tseries, axis=0, keepdims=True)

    # FFT in time
    uhat_t = np.fft.fft(uprime_t * wt, axis=0)

    # Power spectrum averaged over y,z
    Euu_ft_yz = (np.abs(uhat_t) ** 2) / nt
    Euu_ft = np.mean(Euu_ft_yz, axis=(1, 2))

    # Keep only positive frequencies
    time_spectra[idx] = Euu_ft[pos_ft]
    np.save(f"./10PCT_time_spectrum_xidx_{idx}.npy", time_spectra[idx])

fig, ax = plt.subplots(figsize=(12, 6))
fig.subplots_adjust(right=0.72)

for xt, idx in zip(x_targets, x_indices):
    yspec = time_spectra[idx]

    spectrum_line, = ax.loglog(
        ft_pos,
        yspec,
        linewidth=2,
        label=f"x/D={sim.x[idx]:.2f}",
    )
    c = spectrum_line.get_color()

    # Anchor frequency:
    # x/D = 20 -> anchor at 10^-2
    # all others -> anchor at first point to the right of 10^-1
    if int(round(xt)) == 20:
        f_anchor_target = 1e-2
    else:
        valid = np.where(ft_pos > 1e-1)[0]
        if len(valid) == 0:
            continue
        ref_idx = valid[0]
        f_anchor_target = ft_pos[ref_idx]

    # Find nearest available frequency index to desired anchor
    ref_idx = np.argmin(np.abs(ft_pos - f_anchor_target))

    # Length of reference segment
    ref_len = 10
    ref_slice = slice(ref_idx, min(len(ft_pos), ref_idx + ref_len))

    f_ref = ft_pos[ref_idx]
    f_ref_amp = yspec[ref_idx]

    f_ref_x = ft_pos[ref_slice]
    f_ref_y = f_ref_amp * (f_ref_x / f_ref) ** (-5 / 3)

    np.save(f"./10PCT_f_ref_x_xidx_{idx}.npy", f_ref_x)
    np.save(f"./10PCT_f_ref_y_xidx_{idx}.npy", f_ref_y)

    ax.loglog(
        f_ref_x,
        f_ref_y,
        "--",
        color=c,
        linewidth=1.6,
        label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}",
    )
ax.set_xlabel("Frequency [1/time]")
ax.set_ylabel(r"$E_{uu}(f)$")
ax.set_title("Time spectrum of u averaged over y,z at selected x/D")
ax.set_ylim(1e-6, 1e-2)
ax.grid(True, which="both")
ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.02, 1.0),
    borderaxespad=0.0,
    fontsize=9,
)
plt.savefig("./10PCT_Euu_time_yz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(
        ft_pos,
        time_spectra[idx],
        linewidth=2,
        label=f"x/D={sim.x[idx]:.2f}",
    )
plt.xlabel("Frequency [1/time]")
plt.ylabel(r"$E_{uu}(f)$")
plt.title("Time spectrum of u averaged over y,z at selected x/D (linear)")
plt.grid(True)
plt.legend(ncol=2, fontsize=9)
plt.savefig("./10PCT_Euu_time_yz.png", dpi=300, bbox_inches="tight")
plt.close()