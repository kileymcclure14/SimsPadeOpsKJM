import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

#Load Data
cp_prime_hblock_ms = np.load('cp_prime_hblock_cor_ms.npy')
cp_prime_mblock_ms = np.load('cp_prime_mblock_cor_ms.npy')
cp_prime_hblock_wr = np.load('cp_prime_hblock_wr.npy')
cp_prime_mblock_wr = np.load('cp_prime_mblock_wr.npy')
ct_prime_mblock_ms = np.load('ct_prime_mblock_cor_ms.npy')
ct_prime_hblock_ms = np.load('ct_prime_hblock_cor_ms.npy')
ct_prime_mblock_wr = np.load('ct_prime_mblock_wr.npy')
ct_prime_hblock_wr = np.load('ct_prime_hblock_wr.npy')
cp_raw = np.load('cp_raw_cor.npy')
ct_raw = np.load('ct_raw_cor.npy')
ctprimes = np.load('CtPrime_Values.npy')

#Plotting
plt.figure(figsize = (9,6))
plt.plot(ctprimes[1:16], cp_raw[1:16], linestyle = '-', marker = '^', color = 'black', label = 'Unblocked')
plt.plot(ctprimes[1:16], cp_prime_mblock_ms, linestyle = '--', marker = 'o', color = 'blue', label = 'Mikkelsen/Sorensen')
plt.plot(ctprimes[1:16], cp_prime_mblock_wr[1:16], linestyle = '--', marker = 'o', color = 'red', label = 'Werle')
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel(r'$\hat{C_p}$')
plt.title('Blockage Method Comparison at 10% Blockage: Cp')
plt.legend()
plt.savefig('./ms_wr_cpm')

plt.figure(figsize = (9,6))
plt.plot(ctprimes[1:16], ct_raw[1:16], linestyle = '-', marker = '^', color = 'black', label = 'Unblocked')
plt.plot(ctprimes[1:16], ct_prime_mblock_ms, linestyle = '--', marker = 'o', color = 'blue', label = 'Mikkelsen/Sorensen')
plt.plot(ctprimes[1:16], ct_prime_mblock_wr[1:16], linestyle = '--', marker = 'o', color = 'red', label = 'Werle')
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel(r'$\hat{C_t}$')
plt.title('Blockage Method Comparison at 10% Blockage: Ct')
plt.legend()
plt.savefig('./ms_wr_ctm')

plt.figure(figsize = (9,6))
plt.plot(ctprimes[1:16], cp_raw[1:16], linestyle = '-', marker = '^', color = 'black', label = 'Unblocked')
plt.plot(ctprimes[1:16], cp_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color = 'blue', label = 'Mikkelsen/Sorensen')
plt.plot(ctprimes[1:16], cp_prime_hblock_wr[1:16], linestyle = '--', marker = 'o', color = 'red', label = 'Werle')
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel(r'$\hat{C_p}$')
plt.title('Blockage Method Comparison at 35% Blockage: Cp')
plt.legend()
plt.savefig('./ms_wr_cph')

plt.figure(figsize = (9,6))
plt.plot(ctprimes[1:16], ct_raw[1:16], linestyle = '-', marker = '^', color = 'black', label = 'Unblocked')
plt.plot(ctprimes[1:16], ct_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color = 'blue', label = 'Mikkelsen/Sorensen')
plt.plot(ctprimes[1:16], ct_prime_hblock_wr[1:16], linestyle = '--', marker = 'o', color = 'red', label = 'Werle')
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel(r'$\hat{C_t}$')
plt.title('Blockage Method Comparison at 35% Blockage: Ct')
plt.legend()
plt.savefig('./ms_wr_cth')
