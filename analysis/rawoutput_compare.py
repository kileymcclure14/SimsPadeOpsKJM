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

#Load in Data
cp_0_5 = np.load("cp_0_5.npy")
cp_1 = np.load("cp_1.npy")
cp_1_5 = np.load("cp_1_5.npy")
cp_2 = np.load("cp_2.npy")
cp_2_5 = np.load("cp_2_5.npy")
cp_3 = np.load("cp_3.npy")
cp_3_5 = np.load("cp_3_5.npy")
cp_4 = np.load("cp_4.npy")
cp_neg1 = np.load("cp_neg1.npy")
cp_neg2 = np.load("cp_neg2.npy")
cp_neg3 = np.load("cp_neg3.npy")

ct_0_5 = np.load("ct_0_5.npy")
ct_1 = np.load("ct_1.npy")
ct_1_5 = np.load("ct_1_5.npy")
ct_2 = np.load("ct_2.npy")
ct_2_5 = np.load("ct_2_5.npy")
ct_3 = np.load("ct_3.npy")
ct_3_5 = np.load("ct_3_5.npy")
ct_4 = np.load("ct_4.npy")
ct_neg1 = np.load("ct_neg1.npy")
ct_neg2 = np.load("ct_neg2.npy")
ct_neg3 = np.load("ct_neg3.npy")

cp_unb = np.load("cp_raw_cor.npy")
ct_unb = np.load("ct_raw_cor.npy")

CtPrimes_unb = np.load("CtPrime_Values.npy")
CtPrimes_Yaw = np.load("CtPrimes_Yaw.npy")

cp_noyaw_10 = [cp_neg3[0], cp_neg2[0], cp_neg1[0], cp_0_5[0], cp_1[0], cp_1_5[0], cp_2[0], cp_2_5[0], cp_3[0], cp_3_5[0], cp_4[0]]
cp_y10_10 = [cp_neg3[1], cp_neg2[1], cp_neg1[1], cp_0_5[1], cp_1[1], cp_1_5[1], cp_2[1], cp_2_5[1], cp_3[1], cp_3_5[1], cp_4[1]]
cp_y20_10 = [cp_neg3[2],cp_neg2[2], cp_neg1[2], cp_0_5[2], cp_1[2], cp_1_5[2], cp_2[2], cp_2_5[2], cp_3[2], cp_3_5[2], cp_4[2]]
cp_y30_10 = [cp_neg3[3],cp_neg2[3], cp_neg1[3], cp_0_5[3], cp_1[3], cp_1_5[3], cp_2[3], cp_2_5[3], cp_3[3], cp_3_5[3], cp_4[3]]
cp_y40_10 = [cp_neg3[4],cp_neg2[4], cp_neg1[4], cp_0_5[4], cp_1[4], cp_1_5[4], cp_2[4], cp_2_5[4], cp_3[4], cp_3_5[4], cp_4[4]]
cp_y50_10 = [cp_neg3[5],cp_neg2[5], cp_neg1[5], cp_0_5[5], cp_1[5], cp_1_5[5], cp_2[5], cp_2_5[5], cp_3[5], cp_3_5[5], cp_4[5]]
cp_y60_10 = [cp_neg3[6],cp_neg2[6], cp_neg1[6], cp_0_5[6], cp_1[6], cp_1_5[6], cp_2[6], cp_2_5[6], cp_3[6], cp_3_5[6], cp_4[6]]
cp_y70_10 = [cp_neg3[7],cp_neg2[7], cp_neg1[7], cp_0_5[7], cp_1[7], cp_1_5[7], cp_2[7], cp_2_5[7], cp_3[7], cp_3_5[7], cp_4[7]]
cp_y80_10 = [cp_neg3[8],cp_neg2[8], cp_neg1[8], cp_0_5[8], cp_1[8], cp_1_5[8], cp_2[8], cp_2_5[8], cp_3[8], cp_3_5[8], cp_4[8]]
cp_y90_10 = [cp_neg3[9],cp_neg2[9], cp_neg1[9], cp_0_5[9], cp_1[9], cp_1_5[9], cp_2[9], cp_2_5[9], cp_3[9], cp_3_5[9], cp_4[9]]
yaw_values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

ct_noyaw_10 = [ct_neg3[0], ct_neg2[0], ct_neg1[0], ct_0_5[0], ct_1[0], ct_1_5[0], ct_2[0], ct_2_5[0], ct_3[0], ct_3_5[0], ct_4[0]]
ct_y10_10 = [ct_neg3[1], ct_neg2[1], ct_neg1[1], ct_0_5[1], ct_1[1], ct_1_5[1], ct_2[1], ct_2_5[1], ct_3[1], ct_3_5[1], ct_4[1]]
ct_y20_10 = [ct_neg3[2],ct_neg2[2], ct_neg1[2], ct_0_5[2], ct_1[2], ct_1_5[2], ct_2[2], ct_2_5[2], ct_3[2], ct_3_5[2], ct_4[2]]
ct_y30_10 = [ct_neg3[3],ct_neg2[3], ct_neg1[3], ct_0_5[3], ct_1[3], ct_1_5[3], ct_2[3], ct_2_5[3], ct_3[3], ct_3_5[3], ct_4[3]]
ct_y40_10 = [ct_neg3[4],ct_neg2[4], ct_neg1[4], ct_0_5[4], ct_1[4], ct_1_5[4], ct_2[4], ct_2_5[4], ct_3[4], ct_3_5[4], ct_4[4]]
ct_y50_10 = [ct_neg3[5],ct_neg2[5], ct_neg1[5], ct_0_5[5], ct_1[5], ct_1_5[5], ct_2[5], ct_2_5[5], ct_3[5], ct_3_5[5], ct_4[5]]
ct_y60_10 = [ct_neg3[6],ct_neg2[6], ct_neg1[6], ct_0_5[6], ct_1[6], ct_1_5[6], ct_2[6], ct_2_5[6], ct_3[6], ct_3_5[6], ct_4[6]]
ct_y70_10 = [ct_neg3[7],ct_neg2[7], ct_neg1[7], ct_0_5[7], ct_1[7], ct_1_5[7], ct_2[7], ct_2_5[7], ct_3[7], ct_3_5[7], ct_4[7]]
ct_y80_10 = [ct_neg3[8],ct_neg2[8], ct_neg1[8], ct_0_5[8], ct_1[8], ct_1_5[8], ct_2[8], ct_2_5[8], ct_3[8], ct_3_5[8], ct_4[8]]
ct_y90_10 = [ct_neg3[9],ct_neg2[9], ct_neg1[9], ct_0_5[9], ct_1[9], ct_1_5[9], ct_2[9], ct_2_5[9], ct_3[9], ct_3_5[9], ct_4[9]]

np.save("cp_noyaw_10.npy", cp_noyaw_10)
np.save("cp_y10_10.npy", cp_y10_10)
np.save("cp_y20_10.npy", cp_y20_10)
np.save("cp_y30_10.npy", cp_y30_10)
np.save("cp_y40_10.npy", cp_y40_10)
np.save("cp_y50_10.npy", cp_y50_10)
np.save("cp_y60_10.npy", cp_y60_10)
np.save("cp_y70_10.npy", cp_y70_10)
np.save("cp_y80_10.npy", cp_y80_10)
np.save("cp_y90_10.npy", cp_y90_10)

np.save("ct_noyaw_10.npy", ct_noyaw_10)
np.save("ct_y10_10.npy", ct_y10_10)
np.save("ct_y20_10.npy", ct_y20_10)
np.save("ct_y30_10.npy", ct_y30_10)
np.save("ct_y40_10.npy", ct_y40_10)
np.save("ct_y50_10.npy", ct_y50_10)
np.save("ct_y60_10.npy", ct_y60_10)
np.save("ct_y70_10.npy", ct_y70_10)
np.save("ct_y80_10.npy", ct_y80_10)
np.save("ct_y90_10.npy", ct_y90_10)

np.save("yaw_values.npy", yaw_values)

# Graph Outputs
plt.figure(figsize = (9,6))
plt.plot(CtPrimes_unb[9:17], cp_unb[9:17], linestyle = '--', marker = 'o', color = 'blue', label = 'Unblocked')
plt.plot(CtPrimes_Yaw[3:10], cp_noyaw_10[3:10], linestyle = '--', marker = 'o', color = 'red', label = '10% Blocked')
plt.xlabel("Ct Prime")
plt.ylabel("Cp")
plt.title("10% vs. Unblocked Cp at 0 Degree Yaw")
plt.legend()
plt.savefig('Cp_10_Unb_0_pos')

plt.figure(figsize = (9,6))
plt.plot(CtPrimes_unb[9:17], ct_unb[9:17], linestyle = '--', marker = 'o', color = 'blue', label = 'Unblocked')
plt.plot(CtPrimes_Yaw[3:10], ct_noyaw_10[3:10], linestyle = '--', marker = 'o', color = 'red', label = '10% Blocked')
plt.xlabel("Ct Prime")
plt.ylabel("Ct")
plt.title("10% vs. Unblocked Ct at 0 Degree Yaw")
plt.legend()
plt.savefig('Ct_10_Unb_0_pos')

plt.figure(figsize = (9,6))
plt.plot(CtPrimes_unb[0:8], cp_unb[0:8], linestyle = '--', marker = 'o', color = 'blue', label = 'Unblocked')
plt.plot(CtPrimes_Yaw[0:3], cp_noyaw_10[0:3], linestyle = '--', marker = 'o', color = 'red', label = '10% Blocked')
plt.ylim(-500, 500)
plt.xlabel('Ct Prime')
plt.ylabel('Cp')
plt.title('10% vs. Unblocked Cp at 0 Degree Yaw')
plt.legend()
plt.savefig('Cp_10_Unb_0_neg')

plt.figure(figsize = (9,6))
plt.plot(CtPrimes_unb[0:8], ct_unb[0:8], linestyle = '--', marker = 'o', color = 'blue', label = 'Unblocked')
plt.plot(CtPrimes_Yaw[0:3], ct_noyaw_10[0:3], linestyle = '--', marker = 'o', color = 'red', label = '10% Blocked')
plt.ylim(-500, 500)
plt.xlabel('Ct Prime')
plt.ylabel('Ct')
plt.title('10% vs. Unblocked Ct at 0 Degree Yaw')
plt.legend()
plt.savefig('Ct_10_Unb_0_neg')

plt.figure(figsize = (9,6))
plt.plot(CtPrimes_Yaw[3:10], cp_noyaw_10[3:10], linestyle = '--', marker = 'o', color = 'red', label = 'No Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y10_10[3:10], linestyle = '--', marker = 'o', color = 'blue', label = '10 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y20_10[3:10], linestyle = '--', marker = 'o', color = 'purple', label = '20 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y30_10[3:10], linestyle = '--', marker = 'o', color = 'green', label = '30 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y40_10[3:10], linestyle = '--', marker = 'o', color = 'orange', label = '40 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y50_10[3:10], linestyle = '--', marker = 'o', color = 'magenta', label = '50 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y60_10[3:10], linestyle = '--', marker = 'o', color = 'brown', label = '60 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y70_10[3:10], linestyle = '--', marker = 'o', color = 'pink', label = '70 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y80_10[3:10], linestyle = '--', marker = 'o', color = 'gray', label = '80 Deg Yaw')
plt.plot(CtPrimes_Yaw[3:10], cp_y90_10[3:10], linestyle = '--', marker = 'o', color = 'black', label = '90 Deg Yaw')
plt.xlabel("Ct Prime")
plt.ylabel("Cp")
plt.title("Cp Results at 10% Blockage by Yaw Angle")
plt.legend()
plt.savefig('10_yaw_pos')

plt.figure(figsize = (9,6))
plt.plot(yaw_values, cp_0_5, linestyle = '--', marker = 'o', color = 'red', label = 'Ct Prime = 0.5')
plt.plot(yaw_values, cp_1, linestyle = '--', marker = 'o', color = 'blue', label = 'Ct Prime = 1')
plt.plot(yaw_values, cp_1_5, linestyle = '--', marker = 'o', color = 'green', label = 'Ct Prime = 1.5')
plt.plot(yaw_values, cp_2, linestyle = '--', marker = 'o', color = 'orange', label = 'Ct Prime = 2')
plt.plot(yaw_values, cp_2_5, linestyle = '--', marker = 'o', color = 'pink', label = 'Ct Prime = 2.5')
plt.plot(yaw_values, cp_3, linestyle = '--', marker = 'o', color = 'purple', label = 'Ct Prime = 3')
plt.plot(yaw_values, cp_3_5, linestyle = '--', marker = 'o', color = 'brown', label = 'Ct Prime = 3.5')
plt.plot(yaw_values, cp_4, linestyle = '--', marker = 'o', color = 'black', label = 'Ct Prime = 4')
plt.xlabel("Yaw Angle (Degrees)")
plt.ylabel("Cp")
plt.title("Cp vs. Yaw Angle at 10% Blockage")
plt.legend()
plt.savefig('10_ctp_pos')
