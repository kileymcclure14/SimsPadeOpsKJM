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

#Initial Views
uview = sim.slice(field_terms = "u", ylim = 6.25) # For X-Z view
umeanview = sim.slice(budget_terms = "ubar", ylim = 6.25) # For X-Z view

uview['u'].imshow()
plt.title("Final Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Final_Field.png', dpi = 300)

umeanview['ubar'].imshow()
plt.title("Time-Averaged Mean Velcoity Field for Empty 10% Domain")
plt.savefig('./10PCT_Mean_Field.png', dpi = 300)

# Set Up Velocities
tids = range(0, 3062, 100)

ut, ubart = [], []
vt, vbart = [], []
wt, wbart = [], []

for tid in tids:
    ut.append(sim.slice(field_terms='u', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['u'])
    ubart.append(sim.slice(budget_terms='ubar', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['ubar'])
    
    vt.append(sim.slice(field_terms='v', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['v'])
    vbart.append(sim.slice(budget_terms='vbar', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['vbar'])
    
    wt.append(sim.slice(field_terms='w', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['w'])
    wbart.append(sim.slice(budget_terms='wbar', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['wbar'])

uc = sim.slice(field_terms = 'u', ylim = 1.4, zlim = 1.4)['u'] #Centerline at last timestep
ubarc = sim.slice(budget_terms = 'ubar', ylim = 1.4, zlim = 1.4, tidx = 3062)['ubar'] #Centerline at last timestep

vc = sim.slice(field_terms = 'v', ylim = 1.4, zlim = 1.4)['v'] #Centerline at last timestep
vbarc = sim.slice(budget_terms = 'vbar', ylim = 1.4, zlim = 1.4, tidx = 3062)['vbar'] #Centerline at last timestep

wc = sim.slice(field_terms = 'w', ylim = 1.4, zlim = 1.4)['w'] #Centerline at last timestep
wbarc = sim.slice(budget_terms = 'wbar', ylim = 1.4, zlim = 1.4, tidx = 3062)['wbar'] #Centerline at last timestep

ut = np.array(ut)
vt = np.array(vt)
wt = np.array(wt)
ubart = np.array(ubart)
vbart = np.array(vbart)
wbart = np.array(wbart)

uc = np.array(uc)
vc = np.array(vc)
wc = np.array(wc)
ubarc = np.array(ubarc)
vbarc = np.array(vbarc)
wbarc = np.array(wbarc)

utprime = ut - ubart #Fluctuation at turbine location
vtprime = vt - vbart
wtprime = wt - wbart

ucprime = uc - ubarc #Fluctuation at centerline at last timestep
vcprime = vc - vbarc 
wcprime = wc - wbarc 

# Turbulence Intensities
# At Turbine Location Through Time
# X Component
ti_xt = np.sqrt(np.mean(utprime**2)) /ubart
# Y Component
ti_yt = np.sqrt(np.mean(vtprime**2))/ vbart
# Z Component
ti_zt = np.sqrt(np.mean(wtprime**2))/ wbart

# At Centerline at Last Timestep
# X Component
ti_xc = np.sqrt(np.mean(ucprime**2)) /ubarc
# Y Component
ti_yc = np.sqrt(np.mean(vcprime**2))/ vbarc
# Z Component
ti_zc = np.sqrt(np.mean(wcprime**2))/ wbarc

#Plots
tidx = np.array(range(0, 3062, 100))

plt.figure(figsize=(10,6))
plt.plot(tidx, ti_xt, label = "U Component")
#plt.plot(tidx, ti_yt, label = "V Component")
#plt.plot(tidx, ti_zt, label = "W Component")
plt.ylim(-.5, 0.5)
plt.xlabel("Time Step")
plt.ylabel("Turbulence Intensity")
plt.title("Turbulence Intensities at Future Turbine Location Through Time")
plt.legend()
plt.savefig('./10PCT_Turbulence_Intensity_TIDX.png', dpi = 300)

plt.figure(figsize=(10,6))
plt.plot(sim.x, ti_xc, label = "U Component")
#plt.plot(sim.x, ti_yc, label = "V Component")
#plt.plot(sim.x, ti_zc, label = "W Component")
plt.ylim(-.5, 0.5)
plt.xlabel("X/D")
plt.ylabel("Turbulence Intensity")
plt.title("Turbulence Intensities at Centerline at Last Timestep")
plt.legend()
plt.savefig('./10PCT_Turbulence_Intensity_Centerline.png', dpi = 300)

# Time Varying Autocovariance Function
def autocov_time(uprime):
    Nt = uprime.shape[0]

    uprime_flat = uprime.reshape(Nt, -1)

    R = np.zeros(Nt)

    for tau in range(Nt):
        prod = uprime_flat[:Nt - tau] * uprime_flat[tau:, :]
        R[tau] = np.mean(prod)
    return R

# Spatial Varying Autocovariance Function
def autocov_space(uprime):
    Nx = uprime.shape[0]

    R = np.zeros(Nx)

    for r in range(Nx):
        prod = uprime[:Nx - r] * uprime[r:]
        R[r] = np.mean(prod)
    return R

# Integral Time Scale Function
def its(R, dt):
    Rnorm = R/R[0]

    cutoff = np.where(Rnorm<0)[0]
    if len(cutoff) > 0:
        Rnorm = Rnorm[:cutoff[0]]
    T = np.trapz(Rnorm, dx=dt)
    return T

# Integral Length Scale Function
def ils(R, dx):
    Rnorm = R/R[0]

    cutoff = np.where(Rnorm<0)[0]
    if len(cutoff) > 0:
        Rnorm = Rnorm[:cutoff[0]]
    L = np.trapz(Rnorm, dx=dx)
    return L

# Integral Time Scales at Turbine Location
dt = 100
Ru_t = autocov_time(utprime)
Rv_t = autocov_time(vtprime)
Rw_t = autocov_time(wtprime)

Tu = its(Ru_t, dt)
Tv = its(Rv_t, dt)
Tw = its(Rw_t, dt)

print("Integral Time Sclaes:")
print("U Component:", Tu)
print("V Component:", Tv)
print("W Component:", Tw)

# Integral Length Scales at Centerline at Last Timestep
dx = sim.x[1] - sim.x[0]
Ru_c = autocov_space(ucprime)
Rv_c = autocov_space(vcprime)
Rw_c = autocov_space(wcprime)

Lu = ils(Ru_c, dx)
Lv = ils(Rv_c, dx)
Lw = ils(Rw_c, dx)

print("Integral Length Sclaes:")
print("U Component:", Lu)
print("V Component:", Lv)
print("W Component:", Lw)

# Plot Correlations
lags_t = np.arange(len(Ru_t)) * dt
lags_x = np.arange(len(Ru_c)) * dx

plt.figure()
plt.plot(lags_t, Ru_t / Ru_t[0])
plt.xlabel("Time Lag")
plt.ylabel("Normalized Autocovariance")
plt.title("Temporal Autocorrelation (u)")
plt.savefig("./Ru_time.png", dpi=300)

plt.figure()
plt.plot(lags_x, Ru_c / Ru_c[0])
plt.xlabel("Spatial Lag")
plt.ylabel("Normalized Autocovariance")
plt.title("Spatial Autocorrelation (u)")
plt.savefig("./Ru_space.png", dpi=300)

# Energy Spectra Frequency Space
#Energy Spectrum Function
def energy_spectrum_fft(uprime, dt):

    Nt = uprime.shape[0]

    uflat = uprime.reshape(Nt, -1)
    umean = np.mean(uflat, axis=1)

    U = np.fft.fft(umean)

    freqs = np.fft.fftfreq(Nt, d=dt)
    omega = 2*np.pi*freqs

    S = (np.abs(U)**2) / Nt

    mask = freqs > 0
    return omega[mask], S[mask]

# Apply to Temporal Data
omega_fft, Su_fft = energy_spectrum_fft(utprime, dt)

# Plot
plt.figure(figsize=(10,6))
plt.loglog(omega_fft, Su_fft)
plt.xlabel("Frequency")
plt.ylabel("Energy Spectrum")
plt.title("Energy Spectrum at Future Turbine Location")
plt.savefig('./10PCT_Energy_Spectrum_Frequency.png', dpi = 300)

# Convert to k space
def omega_k(omega, S_omega, U):
    k = omega / U
    E_k = U*S_omega
    return k, E_k

# Apply to Temporal Data
k, Ek = omega_k(omega_fft, Su_fft, np.mean(ubart))

#Plot
# Reference -5/3 slope
k_ref = np.linspace(min(k), max(k), 100)
Ek_ref = Ek[0] * (k_ref / k[0])**(-5/3)

plt.figure()
plt.loglog(k, Ek, label="E(k)")
plt.loglog(k_ref, Ek_ref, '--', label="-5/3 slope")
plt.xlabel("k")
plt.ylabel("E(k)")
plt.legend()
plt.title("Energy Spectrum with -5/3 Scaling")
plt.savefig("./k_spectrum_10PCT.png", dpi=300)

# Spatial Energy Spectrum
def spatial_spectrum(uprime, dx):
    Nx = len(uprime)

    U = np.fft.fft(uprime)
    k = np.fft.fftfreq(Nx, d=dx) * 2 * np.pi

    E_k = (np.abs(U)**2) / Nx

    mask = k > 0
    return k[mask], E_k[mask]

# Apply to Spatial Data
k_space, Ek_space = spatial_spectrum(ucprime, dx)

# Plot
k_ref_space = np.linspace(min(k_space), max(k_space), 100)
Ek_ref_space = Ek_space[0] * (k_ref_space / k_space[0])**(-5/3)


plt.figure(figsize=(10,6))
plt.loglog(k_space, Ek_space)
plt.loglog(k_ref_space, Ek_ref_space, '--', label="-5/3 slope")
plt.xlabel("k")
plt.ylabel("E(k)")
plt.title("Spatial Energy Spectrum")
plt.savefig("./10PCT_spatial_energy_spectrum.png", dpi=300)

# Dissipation Length Scales
# From Converted Time Series
logE = np.log(Ek)
grad = np.gradient(logE)

k_index = np.argmax(grad)
kd = k[k_index]
eta = 1/kd
print("Dissipation Length Scale (from time series):", eta)

# From Spatial Series
logEspace = np.log(Ek_space)
grad_space = np.gradient(logEspace)

k_index_space = np.argmin(grad_space)
kd_space = k_space[k_index_space]
eta_space = 1/kd_space
print("Dissipation Length Scale (from spatial series):", eta_space)

# Injection Length Scales
# Time Series
lit = (utprime**3)/eta
lit_mean = np.mean(lit)
print("Injection Length Scale (from time series):", lit_mean)

# Spatial Series
lispace = (ucprime**3)/eta_space
lispace_mean = np.mean(lispace)
print("Injection Length Scale (from spatial series):", lispace_mean)

# TKE Calculations
# Time Series
uut = []
vvt = []
wwt = []
for tid in tids:
    uu = sim.slice(budget_terms='uu', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['uu']
    uut.append(uu)
    vv = sim.slice(budget_terms='vv', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['vv']
    vvt.append(vv)
    ww = sim.slice(budget_terms='ww', xlim=5, ylim=1.4, zlim=1.4, tidx=tid)['ww']
    wwt.append(ww)
uut = np.array(uut)
vvt = np.array(vvt)
wwt = np.array(wwt)

TKEUt = 0.5 * uut
TKEVt = 0.5 * vvt
TKEWt = 0.5 * wwt

# Spatial Series
uuc = sim.slice(budget_terms='uu', ylim=1.4, zlim=1.4)['uu']
vvc = sim.slice(budget_terms='vv', ylim=1.4, zlim=1.4)['vv']
wwc = sim.slice(budget_terms='ww', ylim=1.4, zlim=1.4)['ww'] 

uuc = np.array(uuc)
vvc = np.array(vvc)
wwc = np.array(wwc)

TKEUc = 0.5 * uuc
TKEVc = 0.5 * vvc
TKEWc = 0.5 * wwc

# Plots
# Time Series
plt.figure(figsize=(10,6))
plt.plot(tidx, TKEUt, label="TKE U Component")
plt.plot(tidx, TKEVt, label="TKE V Component")
plt.plot(tidx, TKEWt, label="TKE W Component")
plt.xlabel("Time Step")
plt.ylabel("Turbulent Kinetic Energy")
plt.title("Turbulent Kinetic Energy at Future Turbine Location Through Time")
plt.legend()
plt.savefig('./10PCT_TKE_TIDX.png', dpi = 300)

# Spatial Series
plt.figure(figsize=(10,6))
plt.plot(sim.x, TKEUc, label="TKE U Component")
plt.plot(sim.x, TKEVc, label="TKE V Component")
plt.plot(sim.x, TKEWc, label="TKE W Component")
plt.xlabel("X/D")
plt.ylabel("Turbulent Kinetic Energy")
plt.title("Turbulent Kinetic Energy at Centerline at Last Timestep")
plt.legend()
plt.savefig('./10PCT_TKE_Centerline.png', dpi = 300)