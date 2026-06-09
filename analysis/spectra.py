import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio
from scipy.signal import welch
import gc

sim = pio.BudgetIO("Data/Empty_Domains/UNB", padeops=True, runid=4)

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
                            color="k", xfrac=(0.05, 0.95), yfrac=0.18,
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


x_targets_spatial = [5, 35, 50]
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
    color="k", xfrac=(0.68, 0.95), yfrac=0.18
)

ax.set_xlabel(r"$k_y$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_y)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_y$ Spectrum of $|U'|$ — Unblcoked Domain", fontsize=13, fontweight="bold")
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(fontsize=11, loc="best")
plt.tight_layout()
plt.savefig("./UNB_Emag_ky_log_full.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot ky (linear) ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    ky_pos, E_ky = ky_results[idx]
    ax.plot(ky_pos, E_ky, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")
ax.set_xlabel(r"$k_y$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_y)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_y$ Spectrum of $|U'|$ — Unblcoked Domain (linear)",
             fontsize=13, fontweight="bold")
ax.grid(True, alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("./UNB_Emag_ky_full.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot kz (log–log) ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    ax.loglog(kz_pos, E_kz, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")

add_global_powerlaw_ref(
    ax, slope=REF_SLOPE, label=r"$k^{-5/3}$ ref",
    color="k", xfrac=(0.68, 0.95), yfrac=0.18
)

ax.set_xlabel(r"$k_z$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_z)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_z$ Spectrum of $|U'|$ — Unblcoked Domain", fontsize=13, fontweight="bold")
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(fontsize=11, loc="best")
plt.tight_layout()
plt.savefig("./UNB_Emag_kz_log_full.png", dpi=300, bbox_inches="tight")
plt.close()

# ── Plot kz (linear) ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 7))
for xt, idx in zip(x_targets_spatial, x_indices_spatial):
    kz_pos, E_kz = kz_results[idx]
    ax.plot(kz_pos, E_kz, linewidth=2.2, label=f"x/D={sim.x[idx]:.2f}")
ax.set_xlabel(r"$k_z$  [rad / length]", fontsize=12)
ax.set_ylabel(r"$E_{|U'|}(x,\,k_z)$  [field$^2$ · length]", fontsize=12)
ax.set_title(r"$k_z$ Spectrum of $|U'|$ — Unblcoked Domain (linear)",
             fontsize=13, fontweight="bold")
ax.grid(True, alpha=0.5)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("./UNB_Emag_kz_full.png", dpi=300, bbox_inches="tight")
plt.close()

# # ─────────────────────────────────────────────────────────────────────────────
# # Frequency Spectra — using budget ubar/vbar/wbar at each timestep
# # ─────────────────────────────────────────────────────────────────────────────
# x_targets_time = [2, 5, 8, 10, 12, 15, 17, 20]
# tids           = range(1000, 13663, 100)
# all_t          = sim.unique_times()

# t  = np.asarray([all_t[i] for i in range(min(len(list(tids)), len(all_t)))]).squeeze()
# dt = np.mean(np.diff(t))
# nt = len(t)
# fs_t = 1.0 / dt
# print(f"nt = {nt}   dt = {dt:.4f}   fs = {fs_t:.4f}")

# x_indices_time = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets_time]

# for xt, idx in zip(x_targets_time, x_indices_time):
#     print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# # Pre-allocate storage for |U'| directly — shape (nt, ny*nz)
# Umag_prime_store = {idx: np.empty((nt, ny * nz), dtype=np.float64)
#                     for idx in x_indices_time}

# # Load instantaneous fields AND budget means at every timestep
# for k, tid in enumerate(list(tids)[:nt]):
#     # Instantaneous velocity
#     sl      = sim.slice(field_terms=["u", "v", "w"], tidx=tid)
#     u_full  = np.asarray(sl["u"])
#     v_full  = np.asarray(sl["v"])
#     w_full  = np.asarray(sl["w"])

#     # Time-averaged budget means at this same tidx
#     sl_bar   = sim.slice(budget_terms=["ubar", "vbar", "wbar"], tidx=tid)
#     ubar_full = np.asarray(sl_bar["ubar"])
#     vbar_full = np.asarray(sl_bar["vbar"])
#     wbar_full = np.asarray(sl_bar["wbar"])

#     for idx in x_indices_time:
#         up = u_full[idx] - ubar_full[idx]   # (ny, nz)
#         vp = v_full[idx] - vbar_full[idx]
#         wp = w_full[idx] - wbar_full[idx]
#         Umag_prime_store[idx][k, :] = np.sqrt(up**2 + vp**2 + wp**2).ravel()

#     del sl, sl_bar, u_full, v_full, w_full, ubar_full, vbar_full, wbar_full, up, vp, wp
#     if hasattr(sim, "field") and isinstance(sim.field, dict):
#         sim.field.clear()
#     if k % 50 == 0:
#         gc.collect()
#         print(f"  read tidx {tid}  ({k+1}/{nt})")

# gc.collect()

# # Compute Welch PSDs per x-location
# time_spectra = {}
# nperseg = max(4, nt // 8)   # more segments → smoother spectrum

# for idx in x_indices_time:
#     Umag_ts = Umag_prime_store[idx]   # (nt, ny*nz) — already fluctuations

#     psds = np.array([
#         welch(Umag_ts[:, i], fs=fs_t, nperseg=nperseg, window="hann")[1]
#         for i in range(Umag_ts.shape[1])
#     ])
#     f0 = welch(Umag_ts[:, 0], fs=fs_t, nperseg=nperseg, window="hann")[0]
#     psd_mean = np.nanmean(psds, axis=0)

#     pos_ft = f0 > 0
#     time_spectra[idx] = (f0[pos_ft], psd_mean[pos_ft])

#     del Umag_prime_store[idx], Umag_ts, psds
#     gc.collect()

# # Plot Frequency Spectra (log) with ONE global reference line
# fig, ax = plt.subplots(figsize=(12, 6))
# fig.subplots_adjust(right=0.72)

# for xt, idx in zip(x_targets_time, x_indices_time):
#     ft_pos, E_ft = time_spectra[idx]
#     ax.loglog(ft_pos, E_ft, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")

# add_global_powerlaw_ref(
#     ax, slope=-5/3, label=r"$f^{-5/3}$ ref",
#     color="k", xfrac=(0.68, 0.95), yfrac=0.18
# )

# ax.set_xlabel("Frequency [1/time]")
# ax.set_ylabel(r"$E_{|U'|}(f)$")
# ax.set_title(r"Time Spectrum of $|U'|$ averaged over $y$-$z$ — 10% Blocked Domain")
# ax.grid(True, which="both", ls=":")
# ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0),
#           borderaxespad=0.0, fontsize=9)
# plt.savefig("./10PCT_Emag_time_yz_log_trans.png", dpi=300, bbox_inches="tight")
# plt.close()

# # Plot Frequency Spectra (linear)
# fig, ax = plt.subplots(figsize=(10, 6))
# for xt, idx in zip(x_targets_time, x_indices_time):
#     ft_pos, E_ft = time_spectra[idx]
#     ax.plot(ft_pos, E_ft, linewidth=2, label=f"x/D={sim.x[idx]:.2f}")
# ax.set_xlabel("Frequency [1/time]")
# ax.set_ylabel(r"$E_{|U'|}(f)$")
# ax.set_title(r"Time Spectrum of $|U'|$ averaged over $y$-$z$ — 10% Blocked Domain (linear)")
# ax.grid(True)
# ax.legend(ncol=2, fontsize=9)
# plt.tight_layout()
# plt.savefig("./10PCT_Emag_time_yz_trans.png", dpi=300, bbox_inches="tight")
# plt.close()

# print("Done.")

# # At a single tidx, compare the magnitude of ubar vs u
# sl = sim.slice(field_terms="u", tidx=tids[0])
# sl_bar = sim.slice(budget_terms="ubar", tidx=tids[0])
# print(np.mean(np.abs(sl["u"])))      # typical |u|
# print(np.mean(np.abs(sl_bar["ubar"])))  # typical |ubar|
# print(np.mean(np.abs(sl["u"] - sl_bar["ubar"])))  # typical |u'|