import matplotlib.pyplot as plt
import numpy as np

#Load Data
cp_yawmodel = np.load("cp_0deg_35.npy")
cp_gl = np.load("cp_gl_35.npy")
cp_mask = np.load("cp_maskell_35_U.npy")
cp_ms = np.load("cp_ms_35.npy")
cp_werle = np.load("cp_werle_35.npy")
CtPrimes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
cp_raw = np.load("cp_raw.npy")

#Plot
plt.figure(figsize = (3,4))
plt.plot(CtPrimes, cp_gl, linestyle = '-', color = 'red', marker = '^', label = 'Glauert Correction')
#plt.plot(CtPrimes, cp_mask, linestyle = '-', color = 'green', marker = '^', label = 'Maskell Correction')
plt.plot(CtPrimes, cp_ms, linestyle = '-', color = 'orange', marker = '^', label = 'Mikkelsen & S\u00f8rensen Correction')
plt.plot(CtPrimes, cp_yawmodel, linestyle = '-', color = 'blue', marker = '^', label = 'Yaw Model Correction')
plt.plot(CtPrimes, cp_werle, linestyle = '-', color = 'purple', marker = '^', label = 'Werle Correction')
plt.plot(CtPrimes, cp_raw, 'o', color = 'black', label = 'Unblocked LES Data')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylim(0,1)
plt.xlabel(r'$C_T^{\prime}$')
plt.ylabel(r'$C_P$')
plt.title('Blockage Correction Comparisson at 35% Blockage Ratio')
plt.savefig('correction_compare_35_U', bbox_inches='tight', dpi = 300)