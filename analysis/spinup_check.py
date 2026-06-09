import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc

# ── Import Data ───────────────────────────────────────────────────────────────
sim = pio.BudgetIO("Data/Empty_Domains/Spinups/UNB_r2", padeops=True, runid=2)

tids = range(394000, 740000, 1000)
u, v, w = [], [], []

for tid in tids:
    u.append(np.asarray(sim.slice(field_terms=["u"], tidx=tid)["u"]))
    v.append(np.asarray(sim.slice(field_terms=["v"], tidx=tid)["v"]))
    w.append(np.asarray(sim.slice(field_terms=["w"], tidx=tid)["w"]))

u = np.array(u).squeeze()
v = np.array(v).squeeze()
w = np.array(w).squeeze()

print(f"u.shape = {u.shape}")

# ── Time Averaged Fields and Views ────────────────────────────────────────────
ubar = np.asarray(sim.slice(budget_terms=["ubar"])['ubar'])
vbar = np.asarray(sim.slice(budget_terms=["vbar"])['vbar'])
wbar = np.asarray(sim.slice(budget_terms=["wbar"])['wbar'])

ubarview = sim.slice(budget_terms=["ubar"], ylim = 6.25)
vbarview = sim.slice(budget_terms=["vbar"], ylim=6.25)
wbarview = sim.slice(budget_terms=["wbar"], ylim=6.25)

ubarview["ubar"].imshow()
plt.title("UBar in Unblocked Spinup")
plt.savefig("ubar_UNB_spin.png", dpi=300)
plt.close()

vbarview["vbar"].imshow()
plt.title("VBar in Unblocked Spinup")
plt.savefig("vbar_UNB_spin.png", dpi=300)
plt.close()

wbarview["wbar"].imshow()
plt.title("WBar in Unblocked Spinup")
plt.savefig("wbar_UNB_spin.png", dpi=300)
plt.close()

# ── Calculate Fluctuations ────────────────────────────────────────────────────
uprime = u - ubar
vprime = v - vbar
wprime = w - wbar

# ── TKE Evolution to Stationarity ────────────────────────────────────────────
print("Computing TKE evolution...")
n_times = uprime.shape[0]
ke = np.zeros(n_times)

for it in range(n_times):
    if it % 1 == 0:
        print(f"  Time step {it+1}/{n_times}")
    ke[it] = 0.5 * np.mean(uprime[it]**2 + vprime[it]**2 + wprime[it]**2)

tke_final = ke[-10:].mean()  # Mean of last 10 elements
tke_std   = ke[-10:].std()   # Standard deviation of last 10 elements

plt.figure(figsize=(10, 6))
plt.plot(tids, ke, label="TKE")
plt.axhline(tke_final, color='red', ls='--', lw=2,
            label=f'Final TKE = {tke_final:.3f}')
plt.axhspan(tke_final - tke_std, tke_final + tke_std, alpha=0.2, color='red')
#plt.ylim(0, 0.04)
plt.xlabel("Timestep"); plt.ylabel("TKE")
plt.title("TKE Evolution in Unblocked Spinup")
plt.legend(); plt.grid(); plt.tight_layout()
plt.savefig("TKE_stationarity_UNB_spin.png", dpi=300)
plt.close()

# ── Urms from Field and TKE ───────────────────────────────────────────────────
print("Computing Urms from fluctuation fields...")
urms_vel = np.zeros(n_times)

for it in range(n_times):
    if it % 50 == 0:
        print(f"  Time step {it+1}/{n_times}")
    urms_vel[it] = np.sqrt(
        np.mean(uprime[it]**2) +
        np.mean(vprime[it]**2) +
        np.mean(wprime[it]**2)
    )

urms_ke = np.sqrt(2 * tke_final)
print(f"Urms from fluctuation fields : {urms_vel[-1]:.4f}")
print(f"Urms from TKE                : {urms_ke:.4f}")

# ── Grid & Wavenumber Setup ───────────────────────────────────────────────────
nx, ny, nz = uprime[0].shape
N_grid = nx * ny * nz

dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

kx = 2 * np.pi * np.fft.fftfreq(nx, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)
kz = 2 * np.pi * np.fft.fftfreq(nz, d=dz)
kx3, ky3, kz3 = np.meshgrid(kx, ky, kz, indexing='ij')
k_mag = np.sqrt(kx3**2 + ky3**2 + kz3**2)

dk     = min(2 * np.pi / (nx * dx), 2 * np.pi / (ny * dy), 2 * np.pi / (nz * dz))
k_bins = np.arange(0, k_mag.max() + dk, dk)
k_shell = 0.5 * (k_bins[:-1] + k_bins[1:])

mode_counts, _ = np.histogram(k_mag.ravel(), bins=k_bins)
MIN_MODES = 3

# ── 3D Isotropic Spectra from Fluctuating Fields ──────────────────────────────
print("\n" + "="*70)
print("Computing 3D Isotropic Spectra...")
print("="*70)

all_Ek = np.zeros((n_times, len(k_shell)))

for it in range(n_times):
    if it % 10 == 0:
        print(f"  Processing time step {it+1}/{n_times}")

    # Normalize by N_grid BEFORE squaring so that |uhat|^2 satisfies Parseval.
    # np.fft.fftn is unnormalized: fftn(u) = N * û, so dividing by N_grid here
    # gives the properly normalized DFT coefficients.
    uhat = np.fft.fftn(uprime[it], axes=(0, 1, 2)) / N_grid
    vhat = np.fft.fftn(vprime[it], axes=(0, 1, 2)) / N_grid
    what = np.fft.fftn(wprime[it], axes=(0, 1, 2)) / N_grid

    # Energy density in Fourier space — correctly normalized
    E3d = 0.5 * (np.abs(uhat)**2 + np.abs(vhat)**2 + np.abs(what)**2)

    # Bin energy into spherical shells (no further normalization needed)
    Ek, _ = np.histogram(k_mag.ravel(), bins=k_bins, weights=E3d.ravel())

    all_Ek[it] = Ek

print("✓ Spectral computation complete")

# ── Parseval Check: Verify Energy Conservation ────────────────────────────────
print("\n" + "="*70)
print("Parseval's Theorem Verification")
print("="*70)

E_total_spectral = np.sum(all_Ek[-1])
TKE_physical = 0.5 * (
    np.mean(uprime[-1]**2) +
    np.mean(vprime[-1]**2) +
    np.mean(wprime[-1]**2)
)
rel_error = abs(E_total_spectral - TKE_physical) / TKE_physical * 100

print(f"TKE from spectrum (last snapshot): {E_total_spectral:.6f}")
print(f"TKE from physical space           : {TKE_physical:.6f}")
print(f"Relative error                    : {rel_error:.2f}%")

if rel_error > 5:
    print("⚠ WARNING: Energy conservation check FAILED (error > 5%)")
else:
    print("✓ Energy conservation check PASSED")

print("="*70 + "\n")

E_k_mean = np.mean(all_Ek, axis=0)
E_k_std  = np.std(all_Ek,  axis=0)
E_k_last = all_Ek[-1]

# ── Masking ───────────────────────────────────────────────────────────────────
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

# ── Spectrum Convergence Plot ─────────────────────────────────────────────────
print("Plotting spectrum convergence...")
plt.figure(figsize=(10, 6))

cumulative_means = np.cumsum(all_Ek, axis=0) / np.arange(1, n_times + 1)[:, None]

n_points  = 10
p         = 2.5
fractions = [(i / n_points) ** p for i in range(1, n_points + 1)]

times_to_plot = sorted({min(int(f * (n_times - 1)), n_times - 1) for f in fractions})
if (n_times - 1) not in times_to_plot:
    times_to_plot.append(n_times - 1)
times_to_plot = sorted(times_to_plot)

cmap      = cmc.batlow  
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

# Floating -5/3 reference line (placed in open mid-plot space)
# Floating -5/3 reference line — starts early, spans ~1.5 decades
_i0    = max(len(k_plot) // 25, 1)      # start earlier (further left)
_i1    = len(k_plot) * 2 // 3           # extend further right
_k_ref = k_plot[_i0 : _i1]
# Vertical offset keeps the line in open space below the spectral bundle
_E_ref = 0.18 * E_mean[_i0] * (_k_ref / _k_ref[0]) ** (-5 / 3)
plt.loglog(_k_ref, _E_ref, 'k--', lw=2.5, label=r'$k^{-5/3}$')

plt.xlabel(r'$k$')
plt.ylabel(r'$E(k)$')
plt.title("Spectrum Convergence to Stationary State for Unblocked Spinup")
plt.legend(fontsize=8)
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('spectrum_convergence_UNB_spin.png', dpi=300)
plt.close()
print("✓ Saved: spectrum_convergence_UNB_spin.png")

# ── Reference Kolmogorov Line ─────────────────────────────────────────────────
comp  = E_mean * k_plot ** (5 / 3)
i_ref = np.argmax(comp)
k_ref = k_plot[i_ref]
C     = E_mean[i_ref] * k_ref ** (5 / 3)

print(f"\nKolmogorov Constant: C = {C:.4e}")
print(f"Reference wavenumber: k_ref = {k_ref:.4f}")

# ── Fully Developed Spectrum ──────────────────────────────────────────────────
print("Plotting fully developed spectrum...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: compare reference, final snapshot, and ensemble average
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
ax1.set_xlabel(r'$k$'); ax1.set_ylabel(r'$E(k)$')
#ax1.set_ylim(1e-6, 1e-1)
ax1.set_title("Fully Developed Spectrum for Unblocked Spinup")
ax1.legend(fontsize=8); ax1.grid(True, which='both', ls=':')

# Right panel: compensated spectrum to check inertial range plateau
ax2.loglog(k_plot, E_mean * k_plot ** (5 / 3), 'o-', lw=2,
             label=r"$E(k)\,k^{5/3}$")
ax2.axhline(y=C, color='k', ls='--', lw=2, label=f"Kolmogorov plateau  $C$={C:.2e}")
ax2.axvline(x=k_ref, color='grey', ls=':', lw=1.5, label=f"$k_{{ref}}={k_ref:.1f}$")
ax2.set_xlabel(r'$k$'); ax2.set_ylabel(r'$E(k)\,k^{5/3}$')
ax2.set_title("Inertial Range Check for Unblocked Spinup")
ax2.legend(fontsize=8); ax2.grid(True, which='both', ls=':')

plt.tight_layout()
plt.savefig('fully_developed_spectra_UNB_spin.png', dpi=300)
plt.close()
print("✓ Saved: fully_developed_spectra_UNB_spin.png")

print("\n" + "="*70)
print("Done. All outputs saved successfully!")
print("="*70)