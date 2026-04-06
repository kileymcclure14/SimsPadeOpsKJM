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

plt.figure(figsize=(10, 6))
plt.loglog(kx_pos, Euu_pos, label='Euu(kx)')
plt.xlabel('kx')
plt.ylabel('Euu(kx)')
plt.title('Energy Spectrum Euu vs kx')
plt.legend()
plt.grid()
plt.savefig('./10PCT_Ekuu_log.png', dpi=300)

plt.figure(figsize=(10, 6))
plt.plot(kx_pos, Euu_pos, label='Euu(kx)')
plt.xlabel('kx')
plt.ylabel('Euu(kx)')
plt.title('Energy Spectrum Euu vs kx')
plt.legend()
plt.grid()
plt.savefig('./10PCT_Ekuu.png', dpi=300)

# Energy Spectra as Functions of Ky and Kz averaged in other plane
# Ky
ny = uc.shape[1]
dy = sim.y[1] - sim.y[0]

# FFT along y
uhat_y = np.fft.fft(uprime, axis=1)

# Wavenumbers
ky = np.fft.fftfreq(ny, d=dy) * 2 * np.pi

# Energy Spectrum
Euu_ky_3d = (np.abs(uhat_y)**2) / ny

# Average Over Z
Euu_ky = np.mean(Euu_ky_3d, axis=2)

# Mask Negative Values
pos_mask_ky = ky > 0
ky_pos = ky[pos_mask_ky]
Euu_ky_pos = Euu_ky[:, pos_mask_ky]

plt.figure(figsize=(10,6))
plt.loglog(ky_pos, Euu_ky_pos[0,:], label=f'x/D={sim.x[0]:.2f}')
plt.loglog(ky_pos, Euu_ky_pos[nx//2,:], label=f'x/D={sim.x[nx//2]:.2f}')
plt.loglog(ky_pos, Euu_ky_pos[nx//4,:], label=f'x/D={sim.x[nx//4]:.2f}')
plt.xlabel('ky')
plt.ylabel('Euu(ky, x)')
plt.title('Streamwise Energy Spectrum vs ky at selected x locations')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_ky_log.png', dpi=300)

plt.figure(figsize=(10,6))
plt.plot(ky_pos, Euu_ky_pos[0,:], label=f'x/D={sim.x[0]:.2f}')
plt.plot(ky_pos, Euu_ky_pos[nx//2,:], label=f'x/D={sim.x[nx//2]:.2f}')
plt.plot(ky_pos, Euu_ky_pos[nx//4,:], label=f'x/D={sim.x[nx//4]:.2f}')
plt.xlabel('ky')
plt.ylabel('Euu(ky, x)')
plt.title('Streamwise Energy Spectrum vs ky at selected x locations')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_ky.png', dpi=300)

# Kz
nz = uc.shape[2]
dz = sim.z[1] - sim.z[0]

# FFT along z
uhat_z = np.fft.fft(uprime, axis=2)

# Wavenumbers
kz = np.fft.fftfreq(nz, d=dz) * 2 * np.pi

# Energy Spectrum
Euu_kz_3d = (np.abs(uhat_z)**2) / nz

# Average Over Z
Euu_kz = np.mean(Euu_kz_3d, axis=2)

# Mask Negative Values
pos_mask_kz = kz > 0
kz_pos = kz[pos_mask_kz]
Euu_kz_pos = Euu_kz[:, pos_mask_kz]

plt.figure(figsize=(10,6))
plt.loglog(kz_pos, Euu_kz_pos[0,:], label=f'x/D={sim.x[0]:.2f}')
plt.loglog(kz_pos, Euu_kz_pos[nx//2,:], label=f'x/D={sim.x[nx//2]:.2f}')
plt.loglog(kz_pos, Euu_kz_pos[nx//4,:], label=f'x/D={sim.x[nx//4]:.2f}')
plt.xlabel('kz')
plt.ylabel('Euu(kz, x)')
plt.title('Streamwise Energy Spectrum vs kz at selected x locations')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_kz_log.png', dpi=300)

plt.figure(figsize=(10,6))
plt.plot(kz_pos, Euu_kz_pos[0,:], label=f'x/D={sim.x[0]:.2f}')
plt.plot(kz_pos, Euu_kz_pos[nx//2,:], label=f'x/D={sim.x[nx//2]:.2f}')
plt.plot(kz_pos, Euu_kz_pos[nx//4,:], label=f'x/D={sim.x[nx//4]:.2f}')
plt.xlabel('kz')
plt.ylabel('Euu(kz, x)')
plt.title('Streamwise Energy Spectrum vs kz at selected x locations')
plt.grid()
plt.legend()
plt.savefig('./10PCT_Euu_kz.png', dpi=300)