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
from sympy import symbols, Eq, solve, N

#Set up Sims/ Import Data
sim_mblock_list = []
for i in range(99):
    sim_folder = os.path.join(au.DATA_PATH, f"B_0006_Files/Sim_{i:04d}")
    sim_m = pio.BudgetIO(f"Data/B_0006_Files/Sim_{i:04d}", padeops = True, runid = 0, normalize_origin = "turbine")
    sim_mblock_list.append(sim_m)

sim_hblock_list = []
for i in range(99):
    sim_folder = os.path.join(au.DATA_PATH, f"B_0007_Files/Sim_{i:04d}")
    sim_h = pio.BudgetIO(f"Data/B_0007_Files/Sim_{i:04d}", padeops = True, runid = 0, normalize_origin = "turbine")
    sim_hblock_list.append(sim_h)

CtPrimes = [-3, -2, -1, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

ct_hblock_0deg = np.load("cp_hblock_0deg.npy")
cp_mblock_0deg = np.load("cp_mblock_0deg.npy")
ct_hblock_0deg = np.load("ct_hblock_0deg.npy")
ct_mblock_0deg = np.load("ct_mblock_0deg.npy")

cp_raw = np.load("cp_raw_cor.npy")
cp_raw = [cp_raw[2], cp_raw[4], cp_raw[6], cp_raw[9], cp_raw[10], cp_raw[11], cp_raw[12], cp_raw[13], cp_raw[14], cp_raw[15], cp_raw[16]]
ct_raw = np.load("ct_raw_cor.npy")
ct_raw = [ct_raw[2], ct_raw[4], ct_raw[6], ct_raw[9], ct_raw[10], ct_raw[11], ct_raw[12], ct_raw[13], ct_raw[14], ct_raw[15], ct_raw[16]]

#Medium Blockage Solve
A1m = 10
Ad = 1
Uin = 1

am_list = []
Uwm_list = []
Usm_list = []
Awm_list = []
A2m_list = []

for i in range(11):
    am, Uwm, Usm, Awm, A2m  = symbols('am, Uwm, Usm, Awm, A2m')
    eq1m = Eq(Ad*Uin*(1-am), Awm*Uwm)
    eq2m = Eq(Awm*Uwm + (A2m - Awm), A1m*Uin)
    eq3m = Eq(-0.5*CtPrimes[i]*Uin**2*(1-am)*Ad, (A2m-Awm)*Usm**2  + Awm*Uwm**2 + A1m*Uin**2)
    eq4m = Eq(0.5*CtPrimes[i]*Uin**2*(1-am)**2, 0.5*Uin**2 - 0.5*Uwm**2)
    eq5m = Eq(0.5*Uin**2, 0.5*Usm**2)

    solnm = solve((eq1m, eq2m, eq3m, eq4m, eq5m), (am, Uwm, Usm, Awm, A2m), dict=True)

# #High Blockage Solve
# A1h = 2.857

# ah_list = []
# Uwh_list = []
# Ush_list = []
# Awh_list = []
# A2h_list = []

# for i in range(11):
#     ah, Uwh, Ush, Awh, A2h  = symbols('ah, Uwh, Ush, Awh, A2h')
#     eq1h = Eq(Ad*Uin*(1-ah), Awh*Uwh)
#     eq2h = Eq(Awh*Uwh + (A2h - Awh), A1h*Uin)
#     eq3h = Eq(-0.5*CtPrimes[i]*Uin**2*(1-ah)*Ad, (A2h-Awh)*Ush**2  + Awh*Uwh**2 + A1h*Uin**2)
#     eq4h = Eq(0.5*CtPrimes[i]*Uin**2*(1-ah)**2, 0.5*Uin**2 - 0.5*Uwh**2)
#     eq5h = Eq(0.5*Uin**2, 0.5*Ush**2)

#     solnh= solve((eq1h, eq2h, eq3h, eq4h, eq5h), (ah, Uwh, Ush, Awh, A2h), dict=True)

#     solh = solnh[0]
#     ah_list.append(solh[ah])
# print(f"{ah_list}")

# #Medium Blockage Calculations
# #Cp
# cpm_hat = []

# for i in range(11):
#     cpm_hat.append(4*am_list[i]*((1-am_list[i])**2))

# #Ct
# ctm_hat = []

# for i in range(11):
#     ctm_hat.append(4*am_list[i]*(1-am_list[i]))

# #High Blockage Corrections
# cph_hat = []

# for i in range(11):
#     cph_hat.append(4*ah_list[i]*((1-ah_list[i])**2))

# #Ct
# cth_hat = []

# for i in range(11):
#     cth_hat.append(4*ah_list[i]*(1-ah_list[i]))

# #Plotting
# plt.figure(figsize =(9,6))
# plt.plot(CtPrimes, cp_raw, linestyle = '-', marker = '^', color = 'black', label = 'Unblocked LES')
# plt.plot(CtPrimes, cpm_hat, linestyle = '--', marker = 'o', color = 'blue', label = '10% Blockage')
# plt.plot(CtPrimes, cph_hat, linestyle = '--', marker = 'o', color = 'red', label = '35% Blockage')
# plt.ylim(-1, 1)
# plt.xlabel('Ct Prime')
# plt.ylabel(r"$\hat{C_p}$")
# plt.title('Froude Momentum Theory Blockage Correction Results: Cp')
# plt.legend()
# plt.savefig('./froude_cp')

# plt.figure(figsize =(9,6))
# plt.plot(CtPrimes, ct_raw, linestyle = '-', marker = '^', color = 'black', label = 'Unblocked LES')
# plt.plot(CtPrimes, ctm_hat, linestyle = '--', marker = 'o', color = 'blue', label = '10% Blockage')
# plt.plot(CtPrimes, cth_hat, linestyle = '--', marker = 'o', color = 'red', label = '35% Blockage')
# plt.ylim(-1, 1)
# plt.xlabel('Ct Prime')
# plt.ylabel(r"$\hat{C_t}$")
# plt.title('Froude Momentum Theory Blockage Correction Results: Ct')
# plt.legend()
# plt.savefig('./froude_ct')