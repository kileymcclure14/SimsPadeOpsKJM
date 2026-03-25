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
plt.savefig("Ru_time.png", dpi=300)

plt.figure()
plt.plot(lags_x, Ru_c / Ru_c[0])
plt.xlabel("Spatial Lag")
plt.ylabel("Normalized Autocovariance")
plt.title("Spatial Autocorrelation (u)")
plt.savefig("Ru_space.png", dpi=300)