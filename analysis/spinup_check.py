import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio

# Import Data
sim = pio.BudgetIO("Data/Empty_Domains/Spinups/20PCT", padeops=True, runid=1)

tids = range(0, 999000, 1000)
u, v, w = [], [], []

for tid in tids:
    u.append(np.asarray(sim.slice(field_terms=["u"], tidx=tid)["u"]))
    v.append(np.asarray(sim.slice(field_terms=["v"], tidx=tid)["v"]))
    w.append(np.asarray(sim.slice(field_terms=["w"], tidx=tid)["w"]))

u = np.array(u).squeeze() 
v = np.array(v).squeeze()
w = np.array(w).squeeze()

print(f"u.shape = {u.shape}")

# Time Averaged Fields and Views
ubar = np.asarray(sim.slice(budget_terms=["ubar"], xlim=1.4)['ubar'])
vbar = np.asarray(sim.slice(budget_terms=["vbar"], xlim=1.4)['vbar'])
wbar = np.asarray(sim.slice(budget_terms=["wbar"], xlim=1.4)['wbar'])

ubarview = sim.slice(budget_terms=["ubar"], xlim=1.4)
vbarview = sim.slice(budget_terms=["vbar"], xlim=1.4)
wbarview = sim.slice(budget_terms=["wbar"], xlim=1.4)

ubarview["ubar"].imshow()
plt.title("UBar in 10% Blocked HIT")
plt.savefig("ubar_10PCT.png", dpi=300)
plt.close()

vbarview["vbar"].imshow()
plt.title("VBar in 10% Blocked HIT")
plt.savefig("vbar_10PCT.png", dpi=300)
plt.close()

wbarview["wbar"].imshow()
plt.title("WBar in 10% Blocked HIT")
plt.savefig("wbar_10PCT.png", dpi=300)
plt.close()

# Calculate Fluctuations
uprime = u - ubar
vprime = v - vbar
wprime = w - wbar

# TKE Evolution to Stationarity
ke = 0.5 * np.mean(uprime**2 + vprime**2 + wprime**2, axis=(1, 2, 3))
tke_final = ke[-10:].mean() #Mean of last 10 elements
tke_std   = ke[-10:].std()  #Standard deviation of last 10 elements

plt.figure(figsize=(10, 6))
plt.plot(tids, ke, label="TKE")
plt.axhline(tke_final, color='red', ls='--', lw=2,
            label=f'Final TKE = {tke_final:.3f}')
plt.axhspan(tke_final - tke_std, tke_final + tke_std, alpha=0.2, color='red')
plt.xlabel("Timestep"); plt.ylabel("TKE")
plt.title("TKE Evolution in 10% Blocked Spinup")
plt.legend(); plt.grid(); plt.tight_layout()
plt.savefig("TKE_stationarity_10PCT.png", dpi=300)
plt.close()

# URMS from Field and TKE
urms_vel = np.sqrt(
    np.mean(uprime**2, axis=(1, 2, 3)) +
    np.mean(vprime**2, axis=(1, 2, 3)) +
    np.mean(wprime**2, axis=(1, 2, 3))
)
urms_ke = np.sqrt(2 * tke_final)
print(f"Urms from fluctuation fields : {urms_vel[-1]:.4f}")
print(f"Urms from TKE                : {urms_ke:.4f}")

# ── Grid & Wavenumber Setup ───────────────────────────────────────────────────
n_times, nx, ny, nz = uprime.shape
N_grid = nx * ny * nz

dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

kx = 2 * np.pi * np.fft.fftfreq(nx, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)
kz = 2 * np.pi * np.fft.fftfreq(nz, d=dz)
kx3, ky3, kz3 = np.meshgrid(kx, ky, kz, indexing='ij')
k_mag = np.sqrt(kx3**2 + ky3**2 + kz3**2)

dk      = min(2 * np.pi / (nx * dx), 2 * np.pi / (ny * dy), 2 * np.pi / (nz * dz))
k_bins  = np.arange(0, k_mag.max() + dk, dk)
k_shell = 0.5 * (k_bins[:-1] + k_bins[1:])

mode_counts, _ = np.histogram(k_mag.ravel(), bins=k_bins)
MIN_MODES = 3

# ── 3D Isotropic Spectra from Fluctuating Fields ─────────────────────────────
all_Ek = np.zeros((n_times, len(k_shell)))

for it in range(n_times):
    uhat = np.fft.fftn(uprime[it], axes=(0, 1, 2))
    vhat = np.fft.fftn(vprime[it], axes=(0, 1, 2))
    what = np.fft.fftn(wprime[it], axes=(0, 1, 2))

    E3d = 0.5 * (np.abs(uhat)**2 + np.abs(vhat)**2 + np.abs(what)**2) / N_grid**2

    Ek, _ = np.histogram(k_mag.ravel(), bins=k_bins, weights=E3d.ravel())
    all_Ek[it] = Ek

E_k_mean = np.mean(all_Ek, axis=0)
E_k_std  = np.std(all_Ek,  axis=0)
E_k_last = all_Ek[-1]

# Masking
mask = (
    (k_shell > 0) &
    (mode_counts >= MIN_MODES) & 
    (E_k_mean > 0) &
    np.isfinite(E_k_mean)
)

k_plot = k_shell[mask]
E_mean = E_k_mean[mask]
E_std  = E_k_std[mask]
E_last = E_k_last[mask]

# Plot Spectrum Convergence
plt.figure(figsize=(10, 6))

cumulative_means = np.cumsum(all_Ek, axis=0) / np.arange(1, n_times + 1)[:, None]

n_points  = 10
p         = 2.5
fractions = [(i / n_points) ** p for i in range(1, n_points + 1)]

times_to_plot = sorted({min(int(f * (n_times - 1)), n_times - 1) for f in fractions})
if (n_times - 1) not in times_to_plot:
    times_to_plot.append(n_times - 1)
times_to_plot = sorted(times_to_plot)

cmap      = mpl.colormaps['plasma_r']
colors    = cmap(np.linspace(0.1, 0.9, len(times_to_plot)))
tids_list = list(tids)

for i, nt in enumerate(times_to_plot):
    Ek     = cumulative_means[nt]
    mask_t = (
        (k_shell > 0) &
        (mode_counts >= MIN_MODES) &
        np.isfinite(Ek) &
        (Ek > 0)
    )
    plt.loglog(
        k_shell[mask_t], Ek[mask_t],
        label=f'tid = {tids_list[nt]}',
        color=colors[i], lw=2,
    )

plt.xlabel(r'$k$')
plt.ylabel(r'$E(k)$')
plt.title("Spectrum Convergence to Stationary State for 10% Blocked Spinup")
plt.legend(fontsize=8)
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('spectrum_convergence_10PCT.png', dpi=300)
plt.close()

# Reference Line
comp  = E_mean * k_plot ** (5 / 3)
i_ref = np.argmax(comp)
k_ref = k_plot[i_ref]
C     = E_mean[i_ref] * k_ref ** (5 / 3)

# Fully Developed Spectrum
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Compare Reference, Final, and Time-Averaged
ax1.loglog(k_plot, E_mean, 'o-',  lw=2,              label="Ensemble average (u'v'w')")
ax1.loglog(k_plot, E_last, 's--', lw=1.5, alpha=0.6, label="Final snapshot")
ax1.fill_between(
    k_plot,
    np.maximum(E_mean - E_std, 1e-20),
    np.maximum(E_mean + E_std, 1e-20),
    alpha=0.2, label=r'$\pm1\sigma$',
)
ax1.loglog(k_plot, C * k_plot ** (-5 / 3), 'k--', lw=2,
           label=rf"$Ck^{{-5/3}}$,  $C$={C:.2e}")
ax1.set_ylim(1e-7, 1e-1)            
ax1.set_xlabel(r'$k$'); ax1.set_ylabel(r'$E(k)$')
ax1.set_title("Fully Developed Spectrum for 10% Blocked Spinup")
ax1.legend(fontsize=8); ax1.grid(True, which='both', ls=':')

# Check Kolmogorov Plateau
ax2.semilogx(k_plot, E_mean * k_plot ** (5 / 3), 'o-', lw=2,
             label=r"$E(k)\,k^{5/3}$")
ax2.axhline(y=C, color='k', ls='--', lw=2, label=f"Kolmogorov plateau  $C$={C:.2e}")
ax2.axvline(x=k_ref, color='grey', ls=':', lw=1.5, label=f"$k_{{ref}}={k_ref:.1f}$")
#ax2.set_ylim(1e-5, 1e-1)              
ax2.set_xlabel(r'$k$'); ax2.set_ylabel(r'$E(k)\,k^{5/3}$')
ax2.set_title("Inertial Range Check for 10% Blocked Spinup")
ax2.legend(fontsize=8); ax2.grid(True, which='both', ls=':')

plt.tight_layout()
plt.savefig('fully_developed_spectra_10PCT.png', dpi=300)
plt.close()

print("Done. Outputs: spectrum_convergence_10PCT.png, fully_developed_spectra_10PCT.png")