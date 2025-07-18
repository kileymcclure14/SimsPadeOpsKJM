import analysis_utils as au
from pathlib import Path
import os
import math
import cmath
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

#Load
cp_prime_msm = np.load('cp_prime_mblock_cor_ms.npy')
cp_prime_msh = np.load('cp_prime_hblock_cor_ms.npy')
ct_prime_msm = np.load('ct_prime_mblock_cor_ms.npy')
ct_prime_msh = np.load('ct_prime_hblock_cor_ms.npy')
cp_prime_maskm = np.load('cp_primem_mask.npy')
cp_prime_maskh = np.load('cp_primeh_mask.npy')
ct_prime_maskm = np.load('ct_primem_mask.npy')
ct_prime_maskh = np.load('ct_primeh_mask.npy')
ctprimes = np.load('CtPrime_Values.npy')
cp_unb = np.load('cp_raw_cor.npy')
ct_unb = np.load('ct_raw_cor.npy')

#Plotting
plt.figure(figsize = (9,6))
plt.plot(ctprimes[2,16], cp_unb[2:16], linestyle = '-', marker = '^', color = 'black', label = 'Unblocked')
plt.plot(ctprimes[2:16], cp_prime_msm[1:15], linestyle = '--', marker = 'o', color = 'blue', label = 'Mikkelsen/Sorensen')
plt.plot(ctprimes[2:16], cp_prime_maskm, linestyle = '--', marker = 'o', color = 'red', label = 'Maskell')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel(r'$\hat{C_p}$')
plt.title('Blockage Method Comparison for Cp at 10% Blockage')
plt.savefig('./ms_maskell_cpm')