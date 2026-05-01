import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio

# Import Data
sim = pio.BudgetIO("Data/Empty_Domains/Spinups/20PCT", padeops=True, runid=1)

tids = range(0, 13494, 10)
u, v, w = [], [], []

for tid in tids:
    data_f = sim.slice(field_terms=["u", "v", "w"], tidx=tid)
    u.append(np.asarray(data_f["u"]))
    v.append(np.asarray(data_f["v"]))
    w.append(np.asarray(data_f["w"]))

u = np.array(u).squeeze()
v = np.array(v).squeeze()
w = np.array(w).squeeze()

print(f"u.shape = {u.shape}") 

# TKE Evolution
ke = 0.5 * np.mean(u**2 + v**2 + w**2, axis=(1, 2, 3))
tke_final = ke[-10:].mean()
tke_std = ke[-10:].std()

plt.figure(figsize=(10, 6))
plt.plot(tids, ke, label="TKE")
plt.axhline(tke_final, color='red', ls='--', lw=2, 
           label=f'Final TKE={tke_final:.3f}')
plt.axhspan(tke_final-tke_std, tke_final+tke_std, alpha=0.2, color='red')
plt.xlabel("Timestep"); plt.ylabel("TKE")
plt.title("TKE evolution (stationarity check)")
plt.legend(); plt.grid(); plt.tight_layout()
plt.ylim(0.02, 0.04)
plt.savefig("./TKE_stationarity_20PCT.png", dpi=300)
plt.close()

# Check against Urms
urms_vel = np.sqrt(np.mean(u**2, axis=(1, 2, 3))+np.mean(v**2, axis=(1, 2, 3))+np.mean(w**2, axis=(1, 2, 3)))
urms_ke = np.sqrt(2*tke_final)

print(f"Calculated URMS from velocity fields: {urms_vel[-1]:.4f}")
print(f"Calculated URMS from TKE: {urms_ke:.4f}")

# 3D Spectra computation
nx, ny, nz = u.shape[1:]
dx = sim.x[1] - sim.x[0]
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

kx = 2*np.pi * np.fft.fftfreq(nx, d=dx)
ky = 2*np.pi * np.fft.fftfreq(ny, d=dy)
kz = 2*np.pi * np.fft.fftfreq(nz, d=dz)
kx, ky, kz = np.meshgrid(kx, ky, kz, indexing='ij')
k_mag = np.sqrt(kx**2 + ky**2 + kz**2)

dk = min(2*np.pi/(nx*dx), 2*np.pi/(ny*dy), 2*np.pi/(nz*dz))
k_bins = np.arange(0, k_mag.max() + dk, dk)
k_shell = 0.5 * (k_bins[:-1] + k_bins[1:])

N = nx * ny * nz
all_Ek = []

for it in range(u.shape[0]):
    uhat = np.fft.fftn(u[it], axes=(0, 1, 2))
    vhat = np.fft.fftn(v[it], axes=(0, 1, 2))
    what = np.fft.fftn(w[it], axes=(0, 1, 2))
    E3d = 0.5 * (np.abs(uhat)**2 + np.abs(vhat)**2 + np.abs(what)**2) / N**2
    Ek, _ = np.histogram(k_mag.ravel(), bins=k_bins, weights=E3d.ravel())
    all_Ek.append(Ek)

all_Ek = np.array(all_Ek)
E_k_mean = np.mean(all_Ek, axis=0)
E_k_std = np.std(all_Ek, axis=0)
E_k_last = all_Ek[-1]

# Masks
mask = (k_shell > 0) & (E_k_mean > 0)
k_plot = k_shell[mask]
E_mean = E_k_mean[mask]
E_std = E_k_std[mask]
E_last = E_k_last[mask]

# PLOT 2: Spectrum convergence (stationarity)
plt.figure(figsize=(10, 6))
cumulative_means = np.cumsum(all_Ek, axis=0) / np.arange(1, len(all_Ek)+1)[:, None]

times_to_plot = [
    len(all_Ek)//100,
    len(all_Ek)//50,
    len(all_Ek)//10,
    len(all_Ek)//5,
    len(all_Ek)//4,
    len(all_Ek)//2,
    -1
]

cmap = mpl.colormaps['plasma']
colors = cmap(np.linspace(0.1, 0.9, len(times_to_plot)))

for i, nt in enumerate(times_to_plot):
    mask_t = (k_shell > 0) & (cumulative_means[nt] > 0)
    plt.loglog(
        k_shell[mask_t],
        cumulative_means[nt][mask_t],
        label=f't={tids[nt]} (n={nt+1}/{len(all_Ek)})',
        color=colors[i],
        lw=2
    )

plt.xlabel(r'$k$')
plt.ylabel(r'$E(k)$')
plt.title('Spectrum convergence to stationary state')
plt.legend()
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('spectrum_convergence_20PCT.png', dpi=300)
plt.close()

i_ref = len(k_plot) // 4
k_ref = k_plot[i_ref]
C = E_mean[i_ref] * k_ref**(5/3)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Raw spectrum
ax1.loglog(k_plot, E_mean, 'o-', lw=2, label='Time-averaged')
ax1.loglog(k_plot, E_last, 's--', lw=1.5, alpha=0.8, label='Final snapshot')
ax1.fill_between(k_plot, np.maximum(E_mean-E_std, 1e-20), E_mean+E_std, alpha=0.2)
ax1.loglog(k_plot, C * k_plot**(-5/3), 'k--', lw=2, label=r'$k^{-5/3}$')
#ax1.set_ylim(10e-5, 10e-1)
ax1.set_xlabel(r'$k$'); ax1.set_ylabel(r'$E(k)$')
ax1.set_title('Fully developed spectrum'); ax1.legend(); ax1.grid()

# Compensated plot
ax2.loglog(k_plot, E_mean * k_plot**(5/3), 'o-', lw=2, label='E(k) × k^{5/3}')
ax2.axhline(y=C, color='k', ls='--', lw=2, label='Kolmogorov plateau')
ax2.set_xlabel(r'$k$'); ax2.set_ylabel(r'$E(k) k^{5/3}$')
#ax2.set_ylim(10e-5, 10e0)
ax2.set_title('Inertial range check'); ax2.legend(); ax2.grid()

plt.tight_layout()
plt.savefig('fully_developed_spectra_20PCT.png', dpi=300)
plt.close()