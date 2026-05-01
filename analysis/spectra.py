import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

# Load Data
sim = pio.BudgetIO("Data/Empty_Domains/10PCT", padeops = True, runid = 3)

# Reynolds Decomposition
u = np.asarray(sim.slice(field_terms="u")['u'])
ubar = np.asarray(sim.slice(budget_terms="ubar")['ubar'])
uprime = u - ubar

# Parmaters
nx, ny, nz = uprime.shape
dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

# Y Spectra
newshape_y = list(uprime.shape)
newshape_y[1] = 1
uprime_y = uprime - np.mean(uprime, axis=1).reshape(newshape_y)

uhat_y = np.fft.rfft(uprime_y, axis=1) * (2 / ny)
psd_y = np.real(uhat_y * np.conj(uhat_y))
filt_y = psd_y > 1e-20
psd_y[~filt_y] = np.nan

ky = 2 * np.pi * np.fft.rfftfreq(ny, d=dy)
pos_ky = ky > 0
ky_pos = ky[pos_ky]
Euu_ky_x = np.mean(psd_y, axis=2)
Euu_ky_pos = Euu_ky_x[:, pos_ky]

#np.save("./10PCT_ky.npy", ky_pos)

x_targets = [5, 10, 17]
x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]

for xt, idx in zip(x_targets, x_indices):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# Ky Plots
plt.figure(figsize=(10, 6))
ky_ref_idx = 2 if len(ky_pos) > 2 else 1
ky_ref_slice = slice(ky_ref_idx, min(len(ky_pos), ky_ref_idx + 12))
for xt, idx in zip(x_targets, x_indices):
    # np.save(f"./10PCT_Euuky_x_{sim.x[idx]:.2f}.npy", Euu_ky_pos[idx, :])

    spectrum_line, = plt.loglog(
        ky_pos, Euu_ky_pos[idx, :], linewidth=2, label=f"x/D={sim.x[idx]:.2f}",
    )
    c = spectrum_line.get_color()

    ky_ref = ky_pos[ky_ref_idx]
    ky_ref_amp = Euu_ky_pos[idx, ky_ref_idx]
    ky_ref_x = ky_pos[ky_ref_slice]
    ky_ref_y = ky_ref_amp * (ky_ref_x / ky_ref) ** (-5 / 3)

    # np.save(f"./10PCT_ky_ref_x_xidx_{sim.x[idx]:.2f}.npy", ky_ref_x)
    # np.save(f"./10PCT_ky_ref_xidx_{sim.x[idx]:.2f}.npy", ky_ref_y)

    plt.loglog(ky_ref_x, ky_ref_y, "--", color=c, linewidth=1.6,
               label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}")

plt.xlabel(r"$k_y$")
plt.ylabel(r"$E_{uu}(x,k_y)$")
plt.title("Euu vs ky at selected x/D in 10% Blocked Domain (log-log)")
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_ky_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(ky_pos, Euu_ky_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_y$")
plt.ylabel(r"$E_{uu}(x,k_y)$")
plt.title("Euu vs ky at selected x/D in 10% Blocked Domain (linear)")
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_ky.png", dpi=300, bbox_inches="tight")
plt.close()

#Z Spectra
newshape_z = list(uprime.shape)
newshape_z[2] = 1
uprime_z = uprime - np.mean(uprime, axis=2).reshape(newshape_z)

uhat_z = np.fft.rfft(uprime_z, axis=2) * (2 / nz)
psd_z = np.real(uhat_z * np.conj(uhat_z))
filt_z = psd_z > 1e-20
psd_z[~filt_z] = np.nan

kz = 2 * np.pi * np.fft.rfftfreq(nz, d=dz)
pos_kz = kz > 0
kz_pos = kz[pos_kz]
Euu_kz_x = np.mean(psd_z, axis=1)
Euu_kz_pos = Euu_kz_x[:, pos_kz]

# np.save("./10PCT_kz.npy", kz_pos)

# Kz Plots
plt.figure(figsize=(10, 6))
kz_ref_idx = 2 if len(kz_pos) > 2 else 1
kz_ref_slice = slice(kz_ref_idx, min(len(kz_pos), kz_ref_idx + 12))
for xt, idx in zip(x_targets, x_indices):
    # np.save(f"./10PCT_Euukz_xidx_{idx}.npy", Euu_kz_pos[idx, :])

    spectrum_line, = plt.loglog(
        kz_pos, Euu_kz_pos[idx, :], linewidth=2, label=f"x/D={sim.x[idx]:.2f}",
    )
    c = spectrum_line.get_color()

    kz_ref = kz_pos[kz_ref_idx]
    kz_ref_amp = Euu_kz_pos[idx, kz_ref_idx]
    kz_ref_x = kz_pos[kz_ref_slice]
    kz_ref_y = kz_ref_amp * (kz_ref_x / kz_ref) ** (-5 / 3)

    #np.save(f"./10PCT_kz_ref_x_xidx_{sim.x[idx]:.2f}.npy", kz_ref_x)
    #np.save(f"./10PCT_kz_ref_xidx_{sim.x[idx]:.2f}.npy", kz_ref_y)

    plt.loglog(kz_ref_x, kz_ref_y, "--", color=c, linewidth=1.6,
               label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}")

plt.xlabel(r"$k_z$")
plt.ylabel(r"$E_{uu}(x,k_z)$")
plt.title("Euu vs kz at selected x/D in 10% Blocked Domain (log-log)")
plt.grid(True, which="both")
plt.legend()
plt.savefig("./10PCT_Euu_kz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(kz_pos, Euu_kz_pos[idx, :], label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_z$")
plt.ylabel(r"$E_{uu}(x,k_z)$")
plt.title("Euu vs kz at selected x/D in 10% Blocked Domain (linear)")
plt.grid(True)
plt.legend()
plt.savefig("./10PCT_Euu_kz.png", dpi=300, bbox_inches="tight")
plt.close()

# Time Spectra
x_targets = [2, 5, 8, 10, 12, 15, 17, 20]
tids = range(0, 3159, 10)
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
ft = np.fft.rfftfreq(nt, d=dt)
pos_ft = ft > 0
ft_pos = ft[pos_ft]

#np.save("./10PCT_freq.npy", ft_pos)

x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]

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

    u_tseries = np.asarray(u_tseries)
    u_tseries = u_tseries.reshape(nt, -1)  # shape: (nt, ny*nz)
    assert u_tseries.shape[0] == nt, (
        f"Time axis mismatch at x/D={sim.x[idx]:.2f}: got shape {u_tseries.shape}"
    )
    print(f"x/D={sim.x[idx]:.2f}, u_tseries shape: {u_tseries.shape}")

    # Remove time mean (matching original function)
    uprime_t = u_tseries - np.mean(u_tseries, axis=0, keepdims=True)

    # PSD using exact same equation as original function
    uhat_t = np.fft.rfft(uprime_t, axis=0) * (2 / nt)
    psd_t = np.real(uhat_t * np.conj(uhat_t))
    filt_t = psd_t > 1e-20
    psd_t[~filt_t] = np.nan

    # Average over spatial dimensions, then select positive frequencies
    Euu_ft = np.nanmean(psd_t, axis=1)
    time_spectra[idx] = Euu_ft[pos_ft]
    # np.save(f"./10PCT_time_spectrum_xidx_{sim.x[idx]:.2f}.npy", time_spectra[idx])

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

    # Skip reference line for last x target
    if xt == x_targets[-1]:
        continue

    if int(round(xt)) == 20:
        f_anchor_target = 1e-2
    else:
        valid = np.where(ft_pos > 1e-1)[0]
        if len(valid) == 0:
            continue
        ref_idx = valid[0]
        f_anchor_target = ft_pos[ref_idx]

    ref_idx = np.argmin(np.abs(ft_pos - f_anchor_target))
    ref_len = 30
    ref_slice = slice(ref_idx, min(len(ft_pos), ref_idx + ref_len))

    f_ref = ft_pos[ref_idx]
    f_ref_amp = yspec[ref_idx]
    f_ref_x = ft_pos[ref_slice]
    f_ref_y = f_ref_amp * (f_ref_x / f_ref) ** (-5 / 3)

    # np.save(f"./10PCT_f_ref_x_xidx_{sim.x[idx]:.2f}.npy", f_ref_x)
    # np.save(f"./10PCT_f_ref_y_xidx_{sim.x[idx]:.2f}.npy", f_ref_y)

    ax.loglog(
        f_ref_x, f_ref_y, "--", color=c, linewidth=1.6,
        label=rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}",
    )

ax.set_xlabel("Frequency [1/time]")
ax.set_ylabel(r"$E_{uu}(f)$")
ax.set_title("Time spectrum of u averaged over y,z at selected x/D in 10% Blocked Domain")
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
    plt.plot(ft_pos, time_spectra[idx], linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel("Frequency [1/time]")
plt.ylabel(r"$E_{uu}(f)$")
plt.title("Time spectrum of u averaged over y,z at selected x/D in 10% Blocked Domain (linear)")
plt.grid(True)
plt.legend(ncol=2, fontsize=9)
plt.savefig("./10PCT_Euu_time_yz.png", dpi=300, bbox_inches="tight")
plt.close()

