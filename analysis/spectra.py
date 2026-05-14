import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio
from scipy.signal import welch
import gc

sim = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=3)

# ─────────────────────────────────────────────
# Data Load / Fluctuations  (single snapshot)
# ─────────────────────────────────────────────
u    = np.asarray(sim.slice(field_terms="u")["u"])
ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])

v    = np.asarray(sim.slice(field_terms="v")["v"])
vbar = np.asarray(sim.slice(budget_terms="vbar")["vbar"])

w    = np.asarray(sim.slice(field_terms="w")["w"])
wbar = np.asarray(sim.slice(budget_terms="wbar")["wbar"])

uprime = u - ubar
vprime = v - vbar
wprime = w - wbar

Umag_prime = np.sqrt(uprime**2 + vprime**2 + wprime**2)

# Grid
nx, ny, nz = Umag_prime.shape
dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

REF_SLOPE = -5 / 3


# ─────────────────────────────────────────────────────────────────────────────
# Single global ref line helper (in graph space, not attached to data lines)
# ─────────────────────────────────────────────────────────────────────────────
def _geom_interp(a, b, frac):
    return a * (b / a) ** frac

def add_global_powerlaw_ref(ax, slope=-5/3, label=r"$k^{-5/3}$ ref",
                            color="k", xfrac=(0.52, 0.86), yfrac=0.80,
                            lw=2.2, alpha=0.9):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if xmin <= 0 or xmax <= 0 or ymin <= 0 or ymax <= 0:
        return

    x0 = _geom_interp(xmin, xmax, xfrac[0])
    x1 = _geom_interp(xmin, xmax, xfrac[1])
    y0 = _geom_interp(ymin, ymax, yfrac)

    C = y0 / (x0 ** slope)
    xx = np.logspace(np.log10(x0), np.log10(x1), 120)
    yy = C * xx**slope
    ax.loglog(xx, yy, "--", color=color, linewidth=lw, alpha=alpha, label=label)


# ─────────────────────────────────────────────────────────────────────────────
# 1-D Spatial Energy Spectra
# ─────────────────────────────────────────────────────────────────────────────
def spatial_spectrum_1d(field_2d, d):
    """
    Compute 1-D energy spectrum via FFT.

    field_2d : ndarray, shape (n0, n1)
        Fluctuation field (2D spatial slice)
    d : float
        Grid spacing
    """
    n0, n1 = field_2d.shape

    # Remove mean along transform direction for each line
    field_2d = field_2d - field_2d.mean(axis=0, keepdims=True)

    # FFT
    fhat = np.fft.rfft(field_2d, axis=0)

    # One-sided power
    power = (np.abs(fhat) ** 2) / (n0 ** 2)
    power *= 2
    power[0] /= 2
    if n0 % 2 == 0:
        power[-1] /= 2

    # Scale by spacing -> density
    power *= d

    # Average over second axis
    E = power.mean(axis=1)

    # Wavenumbers
    freq = np.fft.rfftfreq(n0, d=d)
    k = 2 * np.pi * freq

    # Positive only
    pos = k > 0
    return k[pos], E[pos]


x_targets_spatial = [5, 30, 50]
x_indices_spatial = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets_spatial]

for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

ky_results = {}
kz_results = {}

for idx in x_indices_spatial:
    field = Umag_prime[idx]  # (ny, nz)

    # ky: FFT along y, avg over z
    ky, E_ky = spatial_spectrum_1d(field, dy)

    # kz: FFT along z (after transpose), avg over y
    kz, E_kz = spatial_spectrum_1d(field.T, dz)

    ky_results[idx] = (ky, E_ky)
    kz_results[idx] = (kz, E_kz)

# ── Plot ky (log–log) ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    ky_pos, E_ky = ky_results[idx]
    ax.loglog(ky_pos, E_ky, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")

add_global_powerlaw_ref(
    ax, slope=REF_SLOPE, label=r"$k^{-5/3}$ ref",
    color="k", xfrac=(0.52, 0.86), yfrac=0.80
)

ax.set_xlabel(r"$k_y$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_y)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_y$ Spectrum of $|U'|$ — Unblocked Domain", fontsize=13, fontweight="bold")
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(fontsize=11, loc="best")
plt.tight_layout()
plt.savefig("./UNB_Emag_ky_log.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot ky (linear) ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    ky_pos, E_ky = ky_results[idx]
    ax.plot(ky_pos, E_ky, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")
ax.set_xlabel(r"$k_y$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_y)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_y$ Spectrum of $|U'|$ — Unblocked Domain (linear)",
             fontsize=13, fontweight="bold")
ax.grid(True, alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("./UNB_Emag_ky.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot kz (log–log) ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    ax.loglog(kz_pos, E_kz, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")

add_global_powerlaw_ref(
    ax, slope=REF_SLOPE, label=r"$k^{-5/3}$ ref",
    color="k", xfrac=(0.52, 0.86), yfrac=0.80
)

ax.set_xlabel(r"$k_z$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_z)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_z$ Spectrum of $|U'|$ — Unblocked Domain", fontsize=13, fontweight="bold")
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(fontsize=11, loc="best")
plt.tight_layout()
plt.savefig("./UNB_Emag_kz_log.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot kz (linear) ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    ax.plot(kz_pos, E_kz, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")
ax.set_xlabel(r"$k_z$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_z)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_z$ Spectrum of $|U'|$ — Unblocked Domain (linear)",
             fontsize=13, fontweight="bold")
ax.grid(True, alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("./UNB_Emag_kz.png", dpi=300, bbox_inches="tight")
plt.close()


# ─────────────────────────────────────────────────────────────────────────────
# Frequency Spectra (original block kept; only global ref line change)
# ─────────────────────────────────────────────────────────────────────────────
x_targets_time = [2, 5, 24, 30, 36, 45, 51, 60]
tids           = range(0, 16161, 10)
all_t          = sim.unique_times()

t  = np.asarray([all_t[i] for i in range(min(len(list(tids)), len(all_t)))]).squeeze()
dt = np.mean(np.diff(t))
nt = len(t)
fs_t = 1.0 / dt
print(f"nt = {nt}   dt = {dt:.4f}   fs = {fs_t:.4f}")

x_indices_time = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets_time]

for xt, idx in zip(x_targets_time, x_indices_time):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# Pre-allocate per-x-location storage; shape (nt, ny*nz)
u_store = {idx: np.empty((nt, ny * nz), dtype=np.float64) for idx in x_indices_time}
v_store = {idx: np.empty((nt, ny * nz), dtype=np.float64) for idx in x_indices_time}
w_store = {idx: np.empty((nt, ny * nz), dtype=np.float64) for idx in x_indices_time}

# OUTER loop over tidx, INNER loop over x-locations
for k, tid in enumerate(list(tids)[:nt]):
    sl = sim.slice(field_terms=["u", "v", "w"], tidx=tid)
    u_full = np.asarray(sl["u"])
    v_full = np.asarray(sl["v"])
    w_full = np.asarray(sl["w"])

    for idx in x_indices_time:
        u_store[idx][k, :] = np.array(u_full[idx, :, :]).ravel()
        v_store[idx][k, :] = np.array(v_full[idx, :, :]).ravel()
        w_store[idx][k, :] = np.array(w_full[idx, :, :]).ravel()

    del sl, u_full, v_full, w_full
    if hasattr(sim, "field") and isinstance(sim.field, dict):
        sim.field.clear()
    if k % 50 == 0:
        gc.collect()
        print(f"  read tidx {tid}  ({k+1}/{nt})")

gc.collect()

# Compute Welch PSDs per x-location
time_spectra = {}
nperseg = max(4, nt // 2)

for idx in x_indices_time:
    u_ts = u_store[idx]
    v_ts = v_store[idx]
    w_ts = w_store[idx]

    uprime_ts = u_ts - u_ts.mean(axis=0, keepdims=True)
    vprime_ts = v_ts - v_ts.mean(axis=0, keepdims=True)
    wprime_ts = w_ts - w_ts.mean(axis=0, keepdims=True)

    Umag_prime_ts = np.sqrt(uprime_ts**2 + vprime_ts**2 + wprime_ts**2)
    del uprime_ts, vprime_ts, wprime_ts

    psds = np.array([
        welch(Umag_prime_ts[:, i], fs=fs_t, nperseg=nperseg, window="hann")[1]
        for i in range(Umag_prime_ts.shape[1])
    ])
    f0 = welch(Umag_prime_ts[:, 0], fs=fs_t, nperseg=nperseg, window="hann")[0]
    psd_mean = np.nanmean(psds, axis=0)

    pos_ft = f0 > 0
    time_spectra[idx] = (f0[pos_ft], psd_mean[pos_ft])

    del u_store[idx], v_store[idx], w_store[idx], u_ts, v_ts, w_ts, Umag_prime_ts, psds
    gc.collect()

# Plot Frequency Spectra (log) with ONE global reference line
fig, ax = plt.subplots(figsize=(12, 6))
fig.subplots_adjust(right=0.72)

for xt, idx in zip(x_targets_time, x_indices_time):
    ft_pos, E_ft = time_spectra[idx]
    ax.loglog(ft_pos, E_ft, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")

add_global_powerlaw_ref(
    ax, slope=-5/3, label=r"$f^{-5/3}$ ref",
    color="k", xfrac=(0.52, 0.86), yfrac=0.80
)

ax.set_xlabel("Frequency [1/time]")
ax.set_ylabel(r"$E_{|U'|}(f)$")
ax.set_title(r"Time Spectrum of $|U'|$ averaged over $y$-$z$ — Unblocked Domain")
ax.grid(True, which="both", ls=":")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0),
          borderaxespad=0.0, fontsize=9)
plt.savefig("./UNB_Emag_time_yz_log.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot Frequency Spectra (linear)
fig, ax = plt.subplots(figsize=(10, 6))
for xt, idx in zip(x_targets_time, x_indices_time):
    ft_pos, E_ft = time_spectra[idx]
    ax.plot(ft_pos, E_ft, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
ax.set_xlabel("Frequency [1/time]")
ax.set_ylabel(r"$E_{|U'|}(f)$")
ax.set_title(r"Time Spectrum of $|U'|$ averaged over $y$-$z$ — Unblocked Domain (linear)")
ax.grid(True)
ax.legend(ncol=2, fontsize=9)
plt.tight_layout()
plt.savefig("./UNB_Emag_time_yz.png", dpi=300, bbox_inches="tight")
plt.close()

print("Done.")