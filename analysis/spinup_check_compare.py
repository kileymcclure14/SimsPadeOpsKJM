import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc

# ── Configuration: Simulations to Compare ─────────────────────────────────────
SIMULATIONS = {
    "10% Spinup, Filtered": "Data/Filtered_Spinups/10PCT",
    "20% Spinup, Filtered": "Data/Filtered_Spinups/20PCT",
    "10% Spinup, Unfiltered": "Data/Empty_Domains/Spinups/10PCT_r2",
    "20% Spinup, Unfiltered": "Data/Empty_Domains/Spinups/20PCT_r2",
}

TIME_RANGE = range(210000, 990000, 10000)
MIN_MODES = 3

# ── Storage for Results ───────────────────────────────────────────────────────
results = {}  # Dict to store results for each simulation

# ══════════════════════════════════════════════════════════════════════════════
# LOOP THROUGH EACH SIMULATION
# ══════════════════════════════════════════════════════════════════════════════

for sim_name, sim_path in SIMULATIONS.items():
    print(f"\n{'='*70}")
    print(f"Processing: {sim_name} ({sim_path})")
    print(f"{'='*70}\n")
    
    # ── Import Data ───────────────────────────────────────────────────────────
    sim = pio.BudgetIO(sim_path, padeops=True, runid=1)
    
    tids = list(TIME_RANGE)
    u, v, w = [], [], []
    
    for tid in tids:
        u.append(np.asarray(sim.slice(field_terms=["u"], tidx=tid)["u"]))
        v.append(np.asarray(sim.slice(field_terms=["v"], tidx=tid)["v"]))
        w.append(np.asarray(sim.slice(field_terms=["w"], tidx=tid)["w"]))
    
    u = np.array(u).squeeze()
    v = np.array(v).squeeze()
    w = np.array(w).squeeze()
    
    print(f"u.shape = {u.shape}")
    
    # ── Time Averaged Fields ──────────────────────────────────────────────────
    ubar = np.asarray(sim.slice(budget_terms=["ubar"])['ubar'])
    vbar = np.asarray(sim.slice(budget_terms=["vbar"])['vbar'])
    wbar = np.asarray(sim.slice(budget_terms=["wbar"])['wbar'])
    
    # ── Calculate Fluctuations ────────────────────────────────────────────────
    uprime = u - ubar
    vprime = v - vbar
    wprime = w - wbar
    
    # ── TKE Evolution ─────────────────────────────────────────────────────────
    print("Computing TKE evolution...")
    n_times = uprime.shape[0]
    ke = np.zeros(n_times)
    
    for it in range(n_times):
        if it % 1 == 0:
            print(f"  Time step {it+1}/{n_times}")
        ke[it] = 0.5 * np.mean(uprime[it]**2 + vprime[it]**2 + wprime[it]**2)
    
    tke_final = ke[-10:].mean()
    tke_std   = ke[-10:].std()
    
    # ── Grid & Wavenumber Setup ───────────────────────────────────────────────
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
    
    # ── 3D Isotropic Spectra ──────────────────────────────────────────────────
    print("Computing 3D Isotropic Spectra...")
    
    all_Ek = np.zeros((n_times, len(k_shell)))
    
    for it in range(n_times):
        if it % 10 == 0:
            print(f"  Processing time step {it+1}/{n_times}")
        
        uhat = np.fft.fftn(uprime[it], axes=(0, 1, 2)) / N_grid
        vhat = np.fft.fftn(vprime[it], axes=(0, 1, 2)) / N_grid
        what = np.fft.fftn(wprime[it], axes=(0, 1, 2)) / N_grid
        
        E3d = 0.5 * (np.abs(uhat)**2 + np.abs(vhat)**2 + np.abs(what)**2)
        
        Ek, _ = np.histogram(k_mag.ravel(), bins=k_bins, weights=E3d.ravel())
        all_Ek[it] = Ek
    
    print("✓ Spectral computation complete")
    
    # ── Parseval Check ────────────────────────────────────────────────────────
    print("\nParseval's Theorem Verification")
    E_total_spectral = np.sum(all_Ek[-1])
    TKE_physical = 0.5 * (
        np.mean(uprime[-1]**2) +
        np.mean(vprime[-1]**2) +
        np.mean(wprime[-1]**2)
    )
    rel_error = abs(E_total_spectral - TKE_physical) / TKE_physical * 100
    
    print(f"TKE from spectrum: {E_total_spectral:.6f}")
    print(f"TKE from physical: {TKE_physical:.6f}")
    print(f"Relative error: {rel_error:.2f}%")
    
    # ── Compute Mean Spectra ──────────────────────────────────────────────────
    E_k_mean = np.mean(all_Ek, axis=0)
    E_k_std  = np.std(all_Ek,  axis=0)
    E_k_last = all_Ek[-1]
    
    # ── Masking for mean spectrum ─────────────────────────────────────────────
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
    
    # ── Masking for last timestep spectrum ────────────────────────────────────
    mask_last = (
        (k_shell > 0) &
        (mode_counts >= MIN_MODES) &
        (E_k_last > 0) &
        np.isfinite(E_k_last)
    )
    
    k_plot_last = k_shell[mask_last]
    E_last_masked = E_k_last[mask_last]
    
    # ── Kolmogorov Constant (from mean spectrum) ──────────────────────────────
    comp  = E_mean * k_plot ** (5 / 3)
    i_ref = np.argmax(comp)
    k_ref = k_plot[i_ref]
    C     = E_mean[i_ref] * k_ref ** (5 / 3)
    
    print(f"Kolmogorov Constant: C = {C:.4e}")
    
    # ── Store Results ─────────────────────────────────────────────────────────
    results[sim_name] = {
        'k_shell': k_shell,
        'k_plot': k_plot,
        'k_plot_last': k_plot_last,
        'all_Ek': all_Ek,
        'E_mean': E_mean,
        'E_std': E_std,
        'E_last': E_last,
        'E_last_masked': E_last_masked,
        'C': C,
        'n_times': n_times,
        'tids': tids,
        'mode_counts': mode_counts,
    }

# ══════════════════════════════════════════════════════════════════════════════
# PLOTTING: FINAL TIMESTEP SPECTRA COMPARISON (Multi-Simulation)
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*70}")
print("Plotting Final Timestep Spectra Comparison")
print(f"{'='*70}\n")

fig = plt.figure(figsize=(12, 8))

# Define colormaps for each simulation
cmaps = {
    "10% Spinup, Filtered": cmc.batlow,
    "20% Spinup, Filtered": cmc.bilbao,
    "10% Spinup, Unfiltered": cmc.lapaz,
    "20% Spinup, Unfiltered": cmc.turku,
}

# Find common k-range for all simulations
k_min = max([data['k_plot_last'][0] for data in results.values()])
k_max = min([data['k_plot_last'][-1] for data in results.values()])

# Create a common k-grid with high resolution
n_k_common = 500
k_common = np.logspace(np.log10(k_min), np.log10(k_max), n_k_common)

all_E_final_interp = []

for sim_name, data in results.items():
    k_plot_last = data['k_plot_last']
    E_last_masked = data['E_last_masked']
    C = data['C']
    
    # Get colormap for this simulation
    cmap = cmaps.get(sim_name, cmc.batlow)
    color = cmap(0.4)  # Use a middle value from the colormap
    
    plt.loglog(
        k_plot_last, E_last_masked, 'o-', lw=2.5, markersize=6,
        label=f'{sim_name}', color=color,
    )
    
    # Interpolate to common grid
    E_interp = np.interp(k_common, k_plot_last, E_last_masked)
    all_E_final_interp.append(E_interp)
    
    # Print Kolmogorov constant
    print(f"{sim_name}: C = {C:.4e}")

# Average E_final across all simulations on common grid
E_final_avg = np.mean(all_E_final_interp, axis=0)

# Compute reference -5/3 line
_i0 = max(len(k_common) // 25, 1)
_i1 = len(k_common) * 2 // 3
_k_ref = k_common[_i0 : _i1]
_C_ref = E_final_avg[_i0]  # Use actual energy at reference point
_E_ref = _C_ref * (_k_ref / _k_ref[0]) ** (-5 / 3)

plt.loglog(_k_ref, _E_ref, 'k--', lw=2.5, label=r'$k^{-5/3}$ (ref)')

plt.xlabel(r'$k$', fontsize=12)
plt.ylabel(r'$E(k)$', fontsize=12)
plt.title("Final Timestep Spectra Comparison with $k^{-5/3}$ Scaling", fontsize=14, fontweight='bold')
plt.legend(fontsize=10, loc='best')
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('final_timestep_spectra_comparison_filter.png', dpi=300)
plt.close()
print("✓ Saved: final_timestep_spectra_comparison_filter.png")

# ══════════════════════════════════════════════════════════════════════════════
# PLOTTING: FULLY DEVELOPED SPECTRA COMPARISON
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*70}")
print("Plotting Fully Developed Spectra Comparison")
print(f"{'='*70}\n")

fig = plt.figure(figsize=(14, 8))

for sim_idx, (sim_name, data) in enumerate(results.items(), 1):
    k_plot = data['k_plot']
    E_mean = data['E_mean']
    E_std = data['E_std']
    E_last = data['E_last']
    C = data['C']
    
    cmap = cmaps.get(sim_name, cmc.batlow)
    color = cmap(0.7)
    
    plt.loglog(k_plot, E_mean, 'o-', lw=2.5, color=color,
               label=f"{sim_name} (ensemble avg)", markersize=5)
    plt.loglog(k_plot, E_last, 's--', lw=1.5, alpha=0.5, color=color,
               label=f"{sim_name} (final snapshot)", markersize=4)
    plt.fill_between(
        k_plot,
        np.maximum(E_mean - E_std, 1e-20),
        np.maximum(E_mean + E_std, 1e-20),
        alpha=0.1, color=color,
    )
    plt.loglog(k_plot, C * k_plot ** (-5 / 3), '--', lw=2, color=color,
               label=rf"{sim_name}: $Ck^{{-5/3}}$, $C$={C:.2e}")

plt.xlabel(r'$k$', fontsize=12)
plt.ylabel(r'$E(k)$', fontsize=12)
plt.title("Fully Developed Spectra Comparison", fontsize=14, fontweight='bold')
plt.legend(fontsize=8, loc='best', ncol=2)
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('fully_developed_spectra_comparison_multi_filter.png', dpi=300)
plt.close()
print("✓ Saved: fully_developed_spectra_comparison_multi_filter.png")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY TABLE
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("SUMMARY: Multi-Simulation Comparison")
print("="*70)
print(f"{'Simulation':<30} {'Kolmogorov C':<20}")
print("-"*50)
for sim_name, data in results.items():
    print(f"{sim_name:<30} {data['C']:<20.6e}")
print("="*70)
print("Done. All outputs saved successfully!")
print("="*70)