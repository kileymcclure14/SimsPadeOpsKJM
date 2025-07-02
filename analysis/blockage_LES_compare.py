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

#Load Arrays
cp_prime_mblock_gl = np.load("cp_prime_mblock_gl.npy")
cp_prime_mblock_ms = np.load("cp_prime_mblock_ms.npy")
cp_prime_mblock_cor_gl = np.load("cp_prime_mblock_cor_gl.npy")
cp_prime_mblock_cor_ms = np.load("cp_prime_mblock_cor_ms.npy")
ct_prime_mblock_gl = np.load("ct_prime_mblock_gl.npy")
ct_prime_mblock_ms = np.load("ct_prime_mblock_ms.npy")
ct_prime_mblock_cor_gl = np.load("ct_prime_mblock_cor_gl.npy")
ct_prime_mblock_cor_ms = np.load("ct_prime_mblock_cor_ms.npy")
cp_prime_hblock_gl = np.load("cp_prime_hblock_gl.npy")
cp_prime_hblock_ms = np.load("cp_prime_hblock_ms.npy")
cp_prime_hblock_cor_gl = np.load("cp_prime_hblock_cor_gl.npy")
cp_prime_hblock_cor_ms = np.load("cp_prime_hblock_cor_ms.npy")
ct_prime_hblock_gl = np.load("ct_prime_hblock_gl.npy")
ct_prime_hblock_ms = np.load("ct_prime_hblock_ms.npy")
ct_prime_hblock_cor_gl = np.load("ct_prime_hblock_cor_gl.npy")
ct_prime_hblock_cor_ms = np.load("ct_prime_hblock_cor_ms.npy")
cp_raw = np.load("cp_raw.npy")
ct_raw = np.load("ct_raw.npy")
cp_raw_cor = np.load("cp_raw_cor.npy")
ct_raw_cor = np.load("ct_raw_cor.npy")
Ctprimes = np.load("CtPrime_Values.npy")

#Combined Graph for Cp
#Without Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage, Glauert')
plt.plot(Ctprimes[1:16], cp_prime_mblock_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '10% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], cp_prime_hblock_gl[1:16], linestyle = '--', marker = 'o', color =  'green', label = '35% Blockage, Glauert')
plt.plot(Ctprimes[1:16], cp_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color =  'magenta', label = '35% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], cp_raw[1:16], linestyle = '--', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Emperical Blockage Correction Results Without Filtering')
plt.legend()
plt.savefig('./cp_prime_LES_compare.png')

#With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage, Glauert')
plt.plot(Ctprimes[1:16], cp_prime_mblock_cor_ms, linestyle = '--', marker = 'o', color =  'red', label = '10% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], cp_prime_hblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'green', label = '35% Blockage, Glauert')
plt.plot(Ctprimes[1:16], cp_prime_hblock_cor_ms[1:16], linestyle = '--', marker = 'o', color =  'magenta', label = '35% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], cp_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Emperical Blockage Correction Results With Filtering')
plt.legend()
plt.savefig('./cp_prime_LES_compare_cor.png')

#Combined graph for Ct
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage, Glauert')
plt.plot(Ctprimes[1:16], ct_prime_mblock_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '10% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], ct_prime_hblock_gl[1:16], linestyle = '--', marker = 'o', color =  'green', label = '35% Blockage, Glauert')
plt.plot(Ctprimes[1:16], ct_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color =  'magenta', label = '35% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], ct_raw[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Emperical Blockage Correction Results Without Filtering')
plt.legend()
plt.savefig('./ct_prime_LES_compare.png')

#With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage, Glauert')
plt.plot(Ctprimes[1:16], ct_prime_mblock_cor_ms, linestyle = '--', marker = 'o', color =  'red', label = '10% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], ct_prime_hblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'green', label = '35% Blockage, Glauert')
plt.plot(Ctprimes[1:16], ct_prime_hblock_cor_ms[1:16], linestyle = '--', marker = 'o', color =  'magenta', label = '35% Blockage, Mikkelsen/Sorensen')
plt.plot(Ctprimes[1:16], ct_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Emperical Blockage Correction Results With Filtering')
plt.legend()
plt.savefig('./ct_prime_LES_compare_cor.png')

#By Method
#Glauert
#Cp Without Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], cp_prime_hblock_gl[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], cp_raw[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Glauert Method Without Filtering: Power Coefficient')
plt.legend()
plt.savefig('./cp_prime_gl.png')

#Cp With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], cp_prime_hblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], cp_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Glauert Method With Filtering: Power Coefficient')
plt.legend()
plt.savefig('./cp_prime_gl_cor.png')

#Ct Without Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], ct_prime_hblock_gl[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], ct_raw[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Glauert Method Without Filtering: Thrust Coefficient')
plt.legend()
plt.savefig('./ct_prime_gl.png')

#Ct With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], ct_prime_hblock_cor_gl[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], ct_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Glauert Method With Filtering: Thrust Coefficient')
plt.legend()
plt.savefig('./ct_prime_gl_cor.png')

#Mikkelsen/Sorensen
#Cp Without Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_ms[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], cp_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], cp_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Mikkelsen/Sorensen Method Without Filtering: Power Coefficient')
plt.legend()
plt.savefig('./cp_prime_ms.png')

#Cp With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], cp_prime_mblock_cor_ms, linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], cp_prime_hblock_cor_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], cp_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Cp (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Cp')
plt.title('Mikkelsen/Sorensen Method With Filtering: Power Coefficient')
plt.legend()
plt.savefig('./cp_prime_ms_cor.png')    

#Ct Without Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_ms[1:16], linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], ct_prime_hblock_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], ct_raw[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Mikkelsen/Sorensen Method Without Filtering: Thrust Coefficient')
plt.legend()
plt.savefig('./ct_prime_ms.png')

#Ct With Filtering
plt.figure(figsize=(9,6))
plt.plot(Ctprimes[1:16], ct_prime_mblock_cor_ms, linestyle = '--', marker = 'o', color =  'blue', label = '10% Blockage')
plt.plot(Ctprimes[1:16], ct_prime_hblock_cor_ms[1:16], linestyle = '--', marker = 'o', color =  'red', label = '35% Blockage')
plt.plot(Ctprimes[1:16], ct_raw_cor[1:16], linestyle = '-', marker = '^', color =  'black', label = 'Unblocked Ct (LES)')
plt.ylim(-1, 1)
plt.xlabel('Ct\'')
plt.ylabel('Ct')
plt.title('Mikkelsen/Sorensen Method With Filtering: Thrust Coefficient')
plt.legend()
plt.savefig('./ct_prime_ms_cor.png')