import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio
from scipy.signal import welch

sim = pio.BudgetIO("Data/Empty_Domains/10PCT", padeops=True, runid=3)

# Load 3D Fields
u = np.asarray(sim.slice(field_terms="u")['u'])
ubar = np.asarray(sim.slice(budget_terms="ubar")['ubar'])

v = np.asarray(sim.slice(field_terms="v")['v'])
vbar = np.asarray(sim.slice(budget_terms="vbar")['vbar'])

w = np.asarray(sim.slice(field_terms="w")['w'])
wbar = np.asarray(sim.slice(budget_terms="wbar")['wbar'])

# Velocity magnitudes
Umag     = np.sqrt(u**2    + v**2    + w**2)
Umag_bar = np.sqrt(ubar**2 + vbar**2 + wbar**2)
Umag_prime = Umag - Umag_bar  

# Parameters
nx, ny, nz = Umag_prime.shape
dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

def welch_avg(data, axis, fs, nperseg_frac=0.5):
    n = data.shape[axis]
    nperseg = max(4, int(n * nperseg_frac))
    data_2d = np.moveaxis(data, axis, 0).reshape(n, -1)
    f, _ = welch(data_2d[:, 0], fs=fs, nperseg=nperseg)
    psds = np.array([welch(data_2d[:, i], fs=fs, nperseg=nperseg)[1]
                     for i in range(data_2d.shape[1])])
    return f, np.nanmean(psds, axis=0)


def plot_ref_line(ax_or_plt, k_arr, E_arr, i_ref, n_pts, color, label):
    ref_slice = slice(i_ref, min(len(k_arr), i_ref + n_pts))
    k_ref = k_arr[i_ref]
    A = E_arr[i_ref] * k_ref ** (5/3)
    ax_or_plt.loglog(k_arr[ref_slice], A * k_arr[ref_slice] ** (-5/3),
                     "--", color=color, linewidth=1.6, label=label)


newshape_y = list(Umag_prime.shape); newshape_y[1] = 1
Umag_prime_y = Umag_prime - np.mean(Umag_prime, axis=1).reshape(newshape_y)

x_targets_spatial = [5, 10, 17]
x_indices_spatial = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets_spatial]
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

ky_results = {}
for idx in x_indices_spatial:
    fy, psd_y = welch_avg(Umag_prime_y[idx], axis=0, fs=1.0/dy)
    pos = fy > 0
    ky_results[idx] = (2 * np.pi * fy[pos], psd_y[pos])

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    ky_pos, E_ky = ky_results[idx]
    line, = plt.loglog(ky_pos, E_ky, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
    plot_ref_line(plt, ky_pos, E_ky, len(ky_pos)//7, 30, line.get_color(),
                  rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_y$"); plt.ylabel(r"$E_{|U|}(x,k_y)$")
plt.title(r"$E_{|U|}$ vs $k_y$ — 10% Blocked Domain (log-log, Welch)")
plt.ylim(10e-7, 10e-3)
plt.grid(True, which="both"); plt.legend()
plt.savefig("./10PCT_Emag_ky_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    ky_pos, E_ky = ky_results[idx]
    plt.plot(ky_pos, E_ky, label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_y$"); plt.ylabel(r"$E_{|U|}(x,k_y)$")
plt.title(r"$E_{|U|}$ vs $k_y$ — 10% Blocked Domain (linear, Welch)")
plt.grid(True); plt.legend()
plt.savefig("./10PCT_Emag_ky.png", dpi=300, bbox_inches="tight")
plt.close()


newshape_z = list(Umag_prime.shape); newshape_z[2] = 1
Umag_prime_z = Umag_prime - np.mean(Umag_prime, axis=2).reshape(newshape_z)

kz_results = {}
for idx in x_indices_spatial:
    fz, psd_z = welch_avg(Umag_prime_z[idx], axis=1, fs=1.0/dz)
    pos = fz > 0
    kz_results[idx] = (2 * np.pi * fz[pos], psd_z[pos])

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    line, = plt.loglog(kz_pos, E_kz, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
    plot_ref_line(plt, kz_pos, E_kz, len(kz_pos)//7, 30, line.get_color(),
                  rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_z$"); plt.ylabel(r"$E_{|U|}(x,k_z)$")
plt.title(r"$E_{|U|}$ vs $k_z$ — 10% Blocked Domain (log-log, Welch)")
plt.ylim(10e-7, 10e-3)
plt.grid(True, which="both"); plt.legend()
plt.savefig("./10PCT_Emag_kz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    plt.plot(kz_pos, E_kz, label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel(r"$k_z$"); plt.ylabel(r"$E_{|U|}(x,k_z)$")
plt.title(r"$E_{|U|}$ vs $k_z$ — 10% Blocked Domain (linear, Welch)")
plt.grid(True); plt.legend()
plt.savefig("./10PCT_Emag_kz.png", dpi=300, bbox_inches="tight")
plt.close()


x_targets_time = [2, 5, 8, 10, 12, 15, 17, 20]
tids = range(0, 11449, 10)
all_t = sim.unique_times()

t = np.asarray([all_t[i] for i in range(min(len(list(tids)), len(all_t)))]).squeeze()
dt = np.mean(np.diff(t))
nt = len(t)
print("nt =", nt, "  dt =", dt)

x_indices_time = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets_time]

time_spectra = {}
for xt, idx in zip(x_targets_time, x_indices_time):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

    u_ts, v_ts, w_ts = [], [], []
    for tid in tids:
        u_ts.append(np.asarray(sim.slice(field_terms="u", xlim=sim.x[idx], tidx=tid)["u"]))
        v_ts.append(np.asarray(sim.slice(field_terms="v", xlim=sim.x[idx], tidx=tid)["v"]))
        w_ts.append(np.asarray(sim.slice(field_terms="w", xlim=sim.x[idx], tidx=tid)["w"]))

    u_ts = np.asarray(u_ts).reshape(nt, -1)
    v_ts = np.asarray(v_ts).reshape(nt, -1)
    w_ts = np.asarray(w_ts).reshape(nt, -1)

    # Magnitude of instantaneous and mean velocity, then fluctuation
    Umag_ts     = np.sqrt(u_ts**2 + v_ts**2 + w_ts**2)
    Umag_bar_ts = np.mean(Umag_ts, axis=0, keepdims=True)
    Umag_prime_ts = Umag_ts - Umag_bar_ts  # (nt, ny*nz)

    nperseg = max(4, nt // 2)
    fs_t = 1.0 / dt
    f0, _ = welch(Umag_prime_ts[:, 0], fs=fs_t, nperseg=nperseg)
    psds = np.array([welch(Umag_prime_ts[:, i], fs=fs_t, nperseg=nperseg)[1]
                     for i in range(Umag_prime_ts.shape[1])])
    psd_mean = np.nanmean(psds, axis=0)

    pos_ft = f0 > 0
    time_spectra[idx] = (f0[pos_ft], psd_mean[pos_ft])

fig, ax = plt.subplots(figsize=(12, 6))
fig.subplots_adjust(right=0.72)
for xt, idx in zip(x_targets_time, x_indices_time):
    ft_pos, yspec = time_spectra[idx]
    line, = ax.loglog(ft_pos, yspec, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
    if xt == x_targets_time[-1]:
        continue
    plot_ref_line(ax, ft_pos, yspec, len(ft_pos)//2, 30, line.get_color(),
                  rf"$-5/3$ ref, x/D={sim.x[idx]:.2f}")
ax.set_xlabel("Frequency [1/time]"); ax.set_ylabel(r"$E_{|U|}(f)$")
ax.set_title(r"Time spectrum of $|U'|$ averaged over y,z — 10% Blocked Domain (Welch)")
ax.grid(True, which="both")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0.0, fontsize=9)
plt.savefig("./10PCT_Emag_time_yz_log.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 6))
for xt, idx in zip(x_targets_time, x_indices_time):
    ft_pos, yspec = time_spectra[idx]
    plt.plot(ft_pos, yspec, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
plt.xlabel("Frequency [1/time]"); plt.ylabel(r"$E_{|U|}(f)$")
plt.title(r"Time spectrum of $|U'|$ averaged over y,z — 10% Blocked Domain (linear, Welch)")
plt.grid(True); plt.legend(ncol=2, fontsize=9)
plt.savefig("./10PCT_Emag_time_yz.png", dpi=300, bbox_inches="tight")
plt.close()