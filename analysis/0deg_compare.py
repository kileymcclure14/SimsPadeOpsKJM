import numpy as np
import matplotlib.pyplot as plt

CtPrimes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# Induction
a_unb = np.load('a_0deg_U.npy')
a_10 = np.load('a_0deg_10.npy')
a_35 = np.load('a_0deg_35.npy')
a_unb_model = np.load('a_0deg_U_model.npy')
a_10_model = np.load('a_0deg_10_model.npy')
a_35_model = np.load('a_0deg_35_model.npy')

# Cp
Cp_unb = np.load('cp_0deg_U.npy')
Cp_10 = np.load('cp_0deg_10.npy')
Cp_35 = np.load('cp_0deg_35.npy')
Cp_unb_model = np.load('cp_0deg_U_model.npy')
Cp_10_model = np.load('cp_0deg_10_model.npy')
Cp_35_model = np.load('cp_0deg_35_model.npy')

# Ct
Ct_unb = np.load('ct_0deg_U.npy')
Ct_10 = np.load('ct_0deg_10.npy')
Ct_35 = np.load('ct_0deg_35.npy')
Ct_unb_model = np.load('ct_0deg_U_model.npy')
Ct_10_model = np.load('ct_0deg_10_model.npy')
Ct_35_model = np.load('ct_0deg_35_model.npy')

# Plots

plt.figure(figsize = (3,4))
plt.plot(CtPrimes, a_unb, 'o', color = 'green', label = 'Unblocked LES')
plt.plot(CtPrimes, a_unb_model, '-', color = 'green', label = 'Unblocked Model')
plt.plot(CtPrimes, a_10, 'o', color = 'orange', label = '10% Blocked LES')
plt.plot(CtPrimes, a_10_model, '-', color = 'orange', label = '10% Blocked Model')
plt.plot(CtPrimes, a_35, 'o', color = 'red', label = '35% Blocked LES')
plt.plot(CtPrimes, a_35_model, '-', color = 'red', label = '35% Blocked Model')
plt.xlabel('$C_T\'$')
plt.ylabel('Induction Factor, a')
plt.ylim(0, 1)
plt.title('Induction Factor Model Comparison at 0$^\circ$ Yaw')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left', fontsize=8)
plt.savefig('0deg_a_compare.png', dpi = 300, bbox_inches = 'tight')

plt.figure(figsize = (3,4))
plt.plot(CtPrimes, Cp_unb, 'o', color = 'green', label = 'Unblocked LES')
plt.plot(CtPrimes, Cp_unb_model, '-', color = 'green', label = 'Unblocked Model')
plt.plot(CtPrimes, Cp_10, 'o', color = 'orange', label = '10% Blocked LES')
plt.plot(CtPrimes, Cp_10_model, '-', color = 'orange', label = '10% Blocked Model')
plt.plot(CtPrimes, Cp_35, 'o', color = 'red', label = '35% Blocked LES')
plt.plot(CtPrimes, Cp_35_model, '-', color = 'red', label = '35% Blocked Model')
plt.xlabel('$C_T\'$')
plt.ylabel('Power Coefficient, $C_P$')
plt.ylim(0, 2)
plt.title('Power Coefficient Model Comparison at 0$^\circ$ Yaw')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left', fontsize=8)
plt.savefig('0deg_cp_compare.png', dpi = 300, bbox_inches = 'tight')

plt.figure(figsize = (3,4))
plt.plot(CtPrimes, Ct_unb, 'o', color = 'green', label = 'Unblocked LES')
plt.plot(CtPrimes, Ct_unb_model, '-', color = 'green', label = 'Unblocked Model')
plt.plot(CtPrimes, Ct_10, 'o', color = 'orange', label = '10% Blocked LES')
plt.plot(CtPrimes, Ct_10_model, '-', color = 'orange', label = '10% Blocked Model')
plt.plot(CtPrimes, Ct_35, 'o', color = 'red', label = '35% Blocked LES')
plt.plot(CtPrimes, Ct_35_model, '-', color = 'red', label = '35% Blocked Model')
plt.xlabel('$C_T\'$')
plt.ylabel('Thrust Coefficient, $C_T$')
plt.ylim(0, 2)
plt.title('Thrust Coefficient Model Comparison at 0$^\circ$ Yaw')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left', fontsize=8)
plt.savefig('0deg_ct_compare.png', dpi = 300, bbox_inches = 'tight')