import numpy as np
import matplotlib.pyplot as plt

ctprimes  = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
cp_les = np.load('cp_10deg_35.npy')
cp_ctprime = np.load('cp_10deg_35_model.npy')
#cp_ct= np.load('cp_0deg_35_ct_f.npy')

plt.figure(figsize = (3,4))
plt.plot(ctprimes, cp_les, 'o', label = '35% Blocked LES', color = 'black')
plt.plot(ctprimes, cp_ctprime, linestyle = '-', label = 'Ct Prime Input', color = 'blue')
#plt.plot(ctprimes, cp_ct, linestyle = '-', label = 'Ct Input', color = 'red')
plt.xlabel('Ct Prime/Ct')
plt.ylabel('Cp')
plt.title('LES and Model Output Compare (35% Blockage, 10 deg Yaw)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('cp_lescomp_10_35.png', bbox_inches='tight', dpi=300)