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

#Import data
#Cp
cp_prime_h_cor_ph = np.load("cp_prime_h_cor_ph.npy")
cp_prime_h_ph = np.load("cp_prime_h_ph.npy")
cp_prime_hblock_cor_gl = np.load("cp_prime_hblock_cor_gl.npy")
cp_prime_hblock_cor_ms = np.load("cp_prime_hblock_cor_ms.npy")
cp_prime_hblock_gl = np.load("cp_prime_hblock_gl.npy")
cp_prime_hblock_ms = np.load("cp_prime_hblock_ms.npy")
cp_prime_m_cor_ph = np.load("cp_prime_m_cor_ph.npy")
cp_prime_m_ph = np.load("cp_prime_m_ph.npy")
cp_prime_mblock_cor_gl = np.load("cp_prime_mblock_cor_gl.npy")
cp_prime_mblock_cor_ms = np.load("cp_prime_mblock_cor_ms.npy")
cp_prime_mblock_gl = np.load("cp_prime_mblock_gl.npy")
cp_prime_mblock_ms = np.load("cp_prime_mblock_ms.npy")

#Ct
ct_prime_h_cor_ph = np.load("ct_prime_h_cor_ph.npy")
ct_prime_h_ph = np.load("ct_prime_h_ph.npy")
ct_prime_hblock_cor_gl = np.load("ct_prime_hblock_cor_gl.npy")
ct_prime_hblock_cor_ms = np.load("ct_prime_hblock_cor_ms.npy")
ct_prime_hblock_gl = np.load("ct_prime_hblock_gl.npy")
ct_prime_hblock_ms = np.load("ct_prime_hblock_ms.npy")
ct_prime_m_cor_ph = np.load("ct_prime_m_cor_ph.npy")
ct_prime_m_ph = np.load("ct_prime_m_ph.npy")
ct_prime_mblock_cor_gl = np.load("ct_prime_mblock_cor_gl.npy")
ct_prime_mblock_cor_ms = np.load("ct_prime_mblock_cor_ms.npy")
ct_prime_mblock_gl = np.load("ct_prime_mblock_gl.npy")
ct_prime_mblock_ms = np.load("ct_prime_mblock_ms.npy")

#Ct Prime Array
CtPrimes = np.load("CtPrime_Values.npy")

#Plots
#Cp
#Medium Blockage No Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], cp_prime_mblock_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], cp_prime_mblock_ms[1:16], label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], cp_prime_m_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Cp Prime')
plt.title('Emperical Blockage Correction Comparison: 10% Blockage, No Correction')
plt.savefig('./method_compare_cp_mnc')

#Medium Blockage With Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], cp_prime_mblock_cor_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], cp_prime_mblock_cor_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], cp_prime_m_cor_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Cp Prime')
plt.title('Emperical Blockage Correction Comparison: 10% Blockage, With Correction')
plt.savefig('./method_compare_cp_mwc')

#High Blockage No Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], cp_prime_hblock_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], cp_prime_hblock_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], cp_prime_h_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Cp Prime')
plt.title('Emperical Blockage Correction Comparison: 35% Blockage, No Correction')
plt.savefig('./method_compare_cp_hnc')

#High Blockage With Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], cp_prime_hblock_cor_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], cp_prime_hblock_cor_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], cp_prime_h_cor_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Cp Prime')
plt.title('Emperical Blockage Correction Comparison: 35% Blockage, With Correction')
plt.savefig('./method_compare_cp_hwc')

#Ct
#Medium Blockage No Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], ct_prime_mblock_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], ct_prime_mblock_ms[1:16], label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], ct_prime_m_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Ct Prime (Eq Ct)')
plt.title('Emperical Blockage Correction Comparison: 10% Blockage, No Correction')
plt.savefig('./method_compare_ct_mnc')

#Medium Blockage With Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], ct_prime_mblock_cor_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], ct_prime_mblock_cor_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], ct_prime_m_cor_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Ct Prime (Eq Ct)')
plt.title('Emperical Blockage Correction Comparison: 10% Blockage, With Correction')
plt.savefig('./method_compare_ct_mwc')

#High Blockage No Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], ct_prime_hblock_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], ct_prime_hblock_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], ct_prime_h_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Ct Prime (Eq Ct)')
plt.title('Emperical Blockage Correction Comparison: 35% Blockage, No Correction')
plt.savefig('./method_compare_ct_hnc')

#High Blockage With Correction
plt.figure(figsize=(9,6))
plt.scatter(CtPrimes[1:16], ct_prime_hblock_cor_gl[1:16], label = 'Glauert', marker = 'o', color = 'blue')
plt.scatter(CtPrimes[1:16], ct_prime_hblock_cor_ms, label = 'Mikkelsen/Sorensen', marker = 'o', color = 'red')
plt.scatter(CtPrimes[1:16], ct_prime_h_cor_ph[1:16], label = 'Pope/Harper', marker = 'o', color = 'green')
plt.legend()
plt.ylim(-1,1)
plt.xlabel('Ct Prime')
plt.ylabel('Ct Prime (Eq Ct)')
plt.title('Emperical Blockage Correction Comparison: 35% Blockage, With Correction')
plt.savefig('./method_compare_ct_hwc')