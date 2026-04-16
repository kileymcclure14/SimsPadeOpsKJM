import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import padeopsIO as pio

#Centerline Velocities and Mean Velocities
uc10 = np.load('./10PCT_uc.npy')
ubar10 = np.load('./10PCT_ubar.npy')
uc20 = np.load('./20PCT_uc.npy')
ubar20 = np.load('./20PCT_ubar.npy')
ucUNB = np.load('./UNB_uc.npy')
ubarUNB = np.load('./UNB_ubar.npy')

# X Vals
x10 = np.load('./10PCT_x.npy')
x20 = np.load('./20PCT_x.npy')
xUNB = np.load('./UNB_x.npy')

# Centerline Turbulence Intensities
TIu10 = np.load('./10PCT_TIu_x.npy')
TIu20 = np.load('./20PCT_TIu_x.npy')
TIuUNB = np.load('./UNB_TIu_x.npy')

# Plot Together
plt.figure(figsize=(10, 6))
plt.plot(x10, TIu10, label='10PCT')
plt.plot(x20, TIu20, label='20PCT')
plt.plot(xUNB, TIuUNB, label='UNB')
plt.xlabel('x/D')
plt.ylabel('Turbulence Intensity (%)')
plt.title('Turbulence Intensity vs x/D')
plt.legend()
plt.grid()
plt.savefig('./TI_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Log Log Ratios
log10 = np.load('./10PCT_loglog_ratio.npy')
log20 = np.load('./20PCT_loglog_ratio.npy')
logUNB = np.load('./UNB_loglog_ratio.npy')

# Plot Together
plt.figure(figsize=(10, 6))
plt.loglog(x10, log10, label='10PCT')
plt.loglog(x20, log20, label='20PCT')
plt.loglog(xUNB, logUNB, label='UNB')
plt.xlabel('x/D')
plt.ylabel('Mean Velocity / Variance')
plt.title('Log-Log Plot of Mean Velocity / Variance vs x/D')
plt.legend()
plt.grid(True, which="both")
plt.savefig('./loglog_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Y Spectra
ky10 = np.load('./10PCT_ky.npy')
ky20 = np.load('./20PCT_ky.npy')
kyUNB = np.load('./UNB_ky.npy')

# ADD SPECTRA DATA LOAD BY TIDX AND BLOCKAGE

# ADD REFERENCE LINES BY TIDX AND BLOCKAGE??

# ADD PLOTS TOGETHER

# Z Spectra
kz10 = np.load('./10PCT_kz.npy')
kz20 = np.load('./20PCT_kz.npy')
kzUNB = np.load('./UNB_kz.npy')

# ADD SPECTRA DATA LOAD BY TIDX AND BLOCKAGE 

# ADD REFERENCE LINES BY TIDX AND BLOCKAGE??

# ADD PLOTS TOGETHER

# Physical Time
t10 = np.load('./10PCT_t.npy')
t20 = np.load('./20PCT_t.npy')
tUNB = np.load('./UNB_t.npy')

# RMS TI by Time
TIu_t10 = np.load('./10PCT_TIu_RMS_t.npy')
TIu_t20 = np.load('./20PCT_TIu_RMS_t.npy')
TIu_tUNB = np.load('./UNB_TIu_RMS_t.npy')

# Plot Together
plt.figure(figsize=(10, 6))
plt.plot(t10, TIu_t10, label='10PCT')
plt.plot(t20, TIu_t20, label='20PCT')
plt.plot(tUNB, TIu_tUNB, label='UNB')
plt.xlabel('Physical Time')
plt.ylabel('Turbulence Intensity (%)')
plt.title('Turbulence Intensity at Future Turbine Location')
plt.legend()
plt.grid()
plt.savefig('./TI_t_comparison.png', dpi=300, bbox_inches='tight')

# Time Spectra at Various X Locations
f10 = np.load('./10PCT_freq.npy')
f20 = np.load('./20PCT_freq.npy')
fUNB = np.load('./UNB_freq.npy')

# ADD SPECTRA DATA LOAD BY TIDX AND BLOCKAGE

# ADD REFERENCE LINES BY TIDX AND BLOCKAGE??

# PLOT TOGETHER