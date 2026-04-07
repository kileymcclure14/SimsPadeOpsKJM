import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine
import matplotlib.cm as cm
from matplotlib.colors import Normalize

data_path = Path(au.DATA_PATH)

# Load Data
sim = pio.BudgetIO("Data/Empty_HIT_Tests/10pct", padeops = True, runid = 3)

# Initial Views
uviewz = sim.slice(field_terms = "u", ylim = 1.4) # For X-Z view
umeanviewz = sim.slice(budget_terms = "ubar", ylim = 1.4) # For X-Z view
uviewy = sim.slice(field_terms = "u", zlim = 1.4) # For X-Y view
umeanviewy = sim.slice(budget_terms = "ubar", zlim = 1.4) # For X-Y view

uviewz['u'].imshow()
plt.title("Final Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Final_Fieldz.png', dpi = 300)

umeanviewz['ubar'].imshow()
plt.title("Time-Averaged Mean Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Mean_Fieldz.png', dpi = 300)

uviewy['u'].imshow()
plt.title("Final Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Final_Fieldy.png', dpi = 300)

umeanviewy['ubar'].imshow()
plt.title("Time-Averaged Mean Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Mean_Fieldy.png', dpi = 300)

# 3D Slices
uc = np.array(sim.slice(field_terms='u')['u'])
vc = np.array(sim.slice(field_terms='v')['v'])
wc = np.array(sim.slice(field_terms='w')['w'])

ubar = np.array(sim.slice(budget_terms='ubar')['ubar'])
vbar = np.array(sim.slice(budget_terms='vbar')['vbar'])
wbar = np.array(sim.slice(budget_terms='wbar')['wbar'])

print("uc shape:", uc.shape)
print("ubar shape:", ubar.shape)

# Fluctuations
uprime = uc - ubar
vprime = vc - vbar
wprime = wc - wbar

# Variance over y and z
uvar_x = np.mean(uprime**2, axis=(1,2))
vvar_x = np.mean(vprime**2, axis=(1,2))
wvar_x = np.mean(wprime**2, axis=(1,2))

# Mean over y and z
ubar_x = np.mean(ubar, axis=(1,2))
vbar_x = np.mean(vbar, axis=(1,2))
wbar_x = np.mean(wbar, axis=(1,2))

print("ubar_x shape:", ubar_x.shape)

# Turbulence Intensity as a Function of X
TIu = (np.sqrt(uvar_x) / ubar_x) * 100

print("TIu shape:", TIu.shape)

plt.figure(figsize=(10, 6))
plt.plot(sim.x, TIu, label='Streamwise TI (u)')
plt.xlabel('x/D')
plt.ylabel('Turbulence Intensity (%)')
plt.title('Turbulence Intensity vs x/D')
plt.legend()
plt.grid()
plt.savefig('./10PCT_TI.png', dpi=300)

# Log-Log Plot of Velocity and Variance
log = np.mean(uc, axis=(1,2))/uvar_x

plt.figure(figsize=(10, 6))
plt.loglog(sim.x, log, label='Mean Velocity / Variance')
plt.xlabel('x/D')
plt.ylabel('Mean Velocity / Variance')
plt.title('Log-Log Plot of Mean Velocity / Variance vs x/D')
plt.legend()
plt.grid()
plt.savefig('./10PCT_LogLog.png', dpi=300)

# Spectrum in Kx Space Averaged over y-z
# Domain
nx, ny, nz  = uc.shape
dx = sim.x[1] - sim.x[0]

print("Grid:", nx, ny, nz)
print("dx:", dx)

# FFT in X Direction for each y, z
uhat = np.fft.fft(uprime, axis=0)

# Wace Numbers
kx = np.fft.fftfreq(nx, d=dx) * 2 * np.pi

# Energy Spectrum
Euu_3d = (np.abs(uhat)**2) / nx

# Average over y and z
Euu_kx = np.mean(Euu_3d, axis=(1,2))

print("Euu_kx shape:", Euu_kx.shape)

# Mask Negative Values
pos_mask = kx > 0
kx_pos = kx[pos_mask]
Euu_pos = Euu_kx[pos_mask]

k_ref = kx_pos[1:1000]  # choose a reasonable range
ref_line = Euu_pos[1] * (k_ref / k_ref[0])**(-5/3)


plt.figure(figsize=(10, 6))
plt.loglog(kx_pos, Euu_pos, label='Euu(kx)')
plt.loglog(k_ref, ref_line, '--', color='red', label='-5/3 slope')
plt.xlabel('kx')
plt.ylabel('Euu(kx)')
plt.title('Energy Spectrum Euu vs kx')
plt.legend()
plt.grid()
plt.savefig('./10PCT_Ekuu_log.png', dpi=300)

plt.figure(figsize=(10, 6))
plt.plot(kx_pos, Euu_pos, label='Euu(kx)')
plt.plot(k_ref, ref_line, '--', color='red', label='-5/3 power law')
plt.xlabel('kx')
plt.ylabel('Euu(kx)')
plt.title('Energy Spectrum Euu vs kx')
plt.legend()
plt.grid()
plt.savefig('./10PCT_Ekuu.png', dpi=300)

# Energy Spectra as Functions of ky and kz
nx, ny, nz = uc.shape
dy = sim.y[1] - sim.y[0]
dz = sim.z[1] - sim.z[0]

use_window = True

if use_window:
    window_y = np.hanning(ny)[None, :, None]
    window_z = np.hanning(nz)[None, None, :]
else:
    window_y = 1
    window_z = 1

# Ky and averaging along z
# FFT along y
uhat_y = np.fft.fft(uprime * window_y, axis=1)

# Wavenumbers
ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)

# Energy spectrum (proper normalization)
Euu_ky_3d = (np.abs(uhat_y)**2) * dy / ny 

# Average over z ONLY
Euu_ky = np.mean(Euu_ky_3d, axis=2)

# Keep positive ky
pos_mask_ky = ky > 0
ky_pos = ky[pos_mask_ky]
Euu_ky_pos = Euu_ky[:, pos_mask_ky]

# Desired x/D locations
x_targets = [5, 10, 15]
x_indices = [np.argmin(np.abs(sim.x - xt)) for xt in x_targets]
for xt, idx in zip(x_targets, x_indices):
    print(f"Requested x/D={xt}, using x/D={sim.x[idx]:.2f} (index {idx})")

# Plots
plt.figure(figsize=(10,6))
for xt, idx in zip(x_targets, x_indices):
    plt.loglog(ky_pos, Euu_ky_pos[idx, :], label=f'x/D={sim.x[idx]:.2f}')
mid_idx = x_indices[len(x_indices)//2]
plt.loglog(k_ref, ref_line, '--', color='red', label='-5/3 slope')   
plt.xlabel('ky')
plt.ylabel('Euu(ky, x)')
plt.title('Euu vs ky at selected x/D')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_ky_log.png', dpi=300)

plt.figure(figsize=(10,6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(ky_pos, Euu_ky_pos[idx, :], label=f'x/D={sim.x[idx]:.2f}')
plt.plot(k_ref, ref_line, '--', color='red', label='-5/3 power law')
plt.xlabel('ky')
plt.ylabel('Euu(ky, x)')
plt.title('Euu vs ky (linear)')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_ky.png', dpi=300)

# Kz and averaging along y
# FFT along z
uhat_z = np.fft.fft(uprime * window_z, axis=2)

# Wavenumbers
kz = 2 * np.pi * np.fft.fftfreq(nz, d=dz)

# Energy spectrum (proper normalization)
Euu_kz_3d = (np.abs(uhat_z)**2) * dz / nz 

# Average over y
Euu_kz = np.mean(Euu_kz_3d, axis=1)

# Keep positive kz
pos_mask_kz = kz > 0
kz_pos = kz[pos_mask_kz]
Euu_kz_pos = Euu_kz[:, pos_mask_kz]

# Plots
plt.figure(figsize=(10,6))
for xt, idx in zip(x_targets, x_indices):
    plt.loglog(kz_pos, Euu_kz_pos[idx, :], label=f'x/D={sim.x[idx]:.2f}')
mid_idx = x_indices[len(x_indices)//2]
plt.loglog(k_ref, ref_line, '--', color='red', label='-5/3 slope')
plt.xlabel('kz')
plt.ylabel('Euu(kz, x)')
plt.title('Euu vs kz at selected x/D (log-log)')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_kz_log.png', dpi=300)

plt.figure(figsize=(10,6))
for xt, idx in zip(x_targets, x_indices):
    plt.plot(kz_pos, Euu_kz_pos[idx, :], label=f'x/D={sim.x[idx]:.2f}')
plt.plot(k_ref, ref_line, '--', color='red', label='-5/3 power law')
plt.xlabel('kz')
plt.ylabel('Euu(kz, x)')
plt.title('Euu vs kz at selected x/D (linear)')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_kz.png', dpi=300)

# TI Time Series
tids = range(0, 3062, 10)
all_t = sim.unique_times()

ut, vt, wt = [], [], []
ubart, vbart, wbart = [], [], []
t = []

for i, tid in enumerate(tids):
    data_f = sim.slice(field_terms=['u','v','w'], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)
    data_b = sim.slice(budget_terms=['ubar','vbar','wbar'], xlim=5, ylim=1.4, zlim=1.4, tidx=tid)

    ut.append(data_f['u'])
    vt.append(data_f['v'])
    wt.append(data_f['w'])

    ubart.append(data_b['ubar'])
    vbart.append(data_b['vbar'])
    wbart.append(data_b['wbar'])

  
    if i < len(all_t):
        t.append(all_t[i])

# Arrays
ut = np.array(ut).squeeze()
vt = np.array(vt).squeeze()
wt = np.array(wt).squeeze()
ubart = np.array(ubart).squeeze()
vbart = np.array(vbart).squeeze()
wbart = np.array(wbart).squeeze()
t = np.array(t).squeeze()

# Fluctuations
uprime = ut - ubart
vprime = vt - vbart
wprime = wt - wbart

# Instantaneous TI
TIu_inst = (np.abs(uprime) / ubart) * 100
TIv_inst = (np.abs(vprime) / vbart) * 100
TIw_inst = (np.abs(wprime) / wbart) * 100

# RMS TI
window = 20 
TIu_rms = np.zeros_like(TIu_inst)
TIv_rms = np.zeros_like(TIv_inst)
TIw_rms = np.zeros_like(TIw_inst)

for i in range(len(uprime)):
    start = max(0, i - window)
    
    u_rms = np.sqrt(np.mean(uprime[start:i+1]**2))
    v_rms = np.sqrt(np.mean(vprime[start:i+1]**2))
    w_rms = np.sqrt(np.mean(wprime[start:i+1]**2))
    
    u_mean = np.mean(ubart[start:i+1])
    v_mean = np.mean(vbart[start:i+1])
    w_mean = np.mean(wbart[start:i+1])
    
    TIu_rms[i] = (u_rms / u_mean) * 100
    TIv_rms[i] = (v_rms / v_mean) * 100
    TIw_rms[i] = (w_rms / w_mean) * 100

# Plot
plt.figure(figsize=(10,6))
plt.plot(t, TIu_inst, label='Instantaneous TIu', alpha=0.5)
plt.plot(t, TIu_rms, label='RMS TIu', color='blue', linewidth=2)
plt.xlabel('Physical Time')
plt.ylabel('Turbulence Intensity (%)')
plt.title('Instantaneous and RMS Turbulence Intensity at Future Turbine Location')
plt.grid(True)
plt.legend()
plt.savefig('./10PCT_TI_TimeSeries.png', dpi=300)
