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
data_path = Path(au.DATA_PATH)
sim_folder = os.path.join(au.DATA_PATH, "U_0011_Files")
sim = pio.BudgetIO("Data/U_0011_Files", padeops = True, runid =1, normalize_origin= "turbine")
fwidth = 0.22118565
M = turbine.get_correction(1.5, 0.22118565, 1)

#Turbine Power
power_time = sim.read_turb_power("all", turb = 1)[100:]

#Turbine Power Coefficient
u_inf = sim.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_les = power_time / (0.5 *(np.pi/4)* u_inf**3)
Cp_les = Cp_les[500:]
plt.figure(figsize= (9, 6))
plt.plot(Cp_les, label = 'Ct Prime = 1.50')
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient')
plt.savefig("./Turbine_Cp_U_0011")
print(f"Power coefficent at Ct'= 1.50: {Cp_les}")

#Instantanious Velocity Field
ds = sim.slice(field_terms='u', ylim=0)
ds['u'].imshow()
plt.savefig("./U_Field_U_0011")


#Turbine Thrust 
Ctprime = sim.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time = sim.read_turb_uvel("all", turb = 1)
thrust_time = ud_time**2 * Ctprime * 0.5 * (np.pi/4)
thrust_time = thrust_time[500:]
plt.figure(figsize= (9, 6))
plt.plot(thrust_time, label = 'Ct Prime = 1.50')
plt.xlabel('Timestep')
plt.ylabel('Thrust (Non Dimensional)')
plt.title('Turbine Thrust')
plt.savefig("./Turbine_Thrust_U_0011")

print(f"Thrust at Ct' = 1.50: {thrust_time}")
print(f"Uinf at Ct' = 1.50: {u_inf}")
print(f"Ud at Ct' = 1.50: {ud_time}")

#Compare

#Indcution Factor
a_les = 1 - (power_time/(0.5*(np.pi/4)*Ctprime * M**3))
a_t = Ctprime/(4+Ctprime)
print(f"Induction Factor at Ct Prime = 1.50: {a_les}")
print(f"Theoretical Induction Factor at Ct Prime = 1.50 {a_t}")

#Power Coefficient Compare
Cp_t = 4*a_t*((1-a_t)**2)
# Cp_t = Cp_t[100:]
# min_length_cp = min(len(Cp_les), len(Cp_t))
# Cp_les = Cp_les[:min_length_cp]
# Cp_t = Cp_t[:min_length_cp]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(Cp_les)), Cp_les, label='Simulated Cp', color='r', marker='.', s=5)
# plt.plot(Cp_t, label = 'Theoretical Cp')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Cp')
# plt.title('Power Coefficient Theoretical Comparison')
# plt.savefig("./Turbine_Cp_Comapre_U_0011")

Cp_les_compare = Cp_les[-1]
percent_dif_cp = np.abs((Cp_t - Cp_les_compare)/Cp_t)*100
print(f"Cp at Ct Prime = 1.50: {Cp_les_compare}")
print(f"Theoretical Cp at Ct Prime = 1.50: {Cp_t}")
print(f"Cp percent difference: {percent_dif_cp}")
# plt.figure(figsize = (9,6))
# plt.plot(percent_dif_cp)
# plt.xlabel('Timestep')
# plt.ylabel('Percent Difference')
# plt.title('Percent Difference B/W Theory and Simulated Cp')
# plt.savefig('./Turbine_Cp_PercentDif_U_0011')

#Thrust Coefficients
ct_les = Ctprime*((1-a_les)**2)
ct_t = 4*a_t*(1-a_t)
# min_length_ct = min(len(ct_les), len(ct_t))
# ct_les = ct_les[:min_length_ct]
# ct_t = ct_t[:min_length_ct]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(ct_les)), ct_les, label= 'Simulated Ct', marker = '.', s = 5)
# plt.plot(ct_t, label = 'Theoretical Ct')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Ct')
# plt.title('Thrust Coefficient Theoretical Comparison')
# plt.savefig("./Turbine_Ct_Comapre_U_0011")

ct_les_compare = ct_les[-1]
percent_dif_ct = np.abs((ct_t - ct_les_compare)/ct_t)*100
print(f"Ct at Ct Prime = 1.50: {ct_les_compare}")
print(f"Theoretical Ct at Ct Prime = 1.50: {ct_t}")
print(f"Percent Difference Ct: {percent_dif_ct}")

# plt.figure(figsize = (9,6))
# plt.plot(percent_dif_ct)
# plt.xlabel('Timestep')
# plt.ylabel('Percent Difference')
# plt.title('Percent Difference B/W Theory and Simulated Ct')
# plt.savefig('./Turbine_Ct_PercentDif_U_0011')