import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
data_path = Path(au.DATA_PATH)
sim_folder = os.path.join(au.DATA_PATH, "U_0000_8_Files/Sim_0003")
sim = pio.BudgetIO("Data/U_0008_Files/Sim_0003", padeops = True, runid =1, normalize_origin= "turbine")

#Turbine Power
power_time = sim.read_turb_power("all", turb = 1)[100:]

#Turbine Power Coefficient
u_inf = sim.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_time = power_time / (0.5 *(np.pi/4)* u_inf**3)
Cp_time = Cp_time[100:]
plt.figure(figsize= (9, 6))
plt.plot(Cp_time, label = 'Ct Prime = 1.50')
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient')
plt.savefig("./Turbine_Cp_U_0008_Sim2_Single")
print(f"Power coefficent at Ct'= 1.50: {Cp_time}")

#Instantanious Velocity Field
ds = sim.slice(field_terms='u', ylim=0)
ds['u'].imshow()
plt.savefig("./U_Field_U_0008_Sim2_Single")


#Turbine Thrust 
Ctprime = sim.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time = sim.read_turb_uvel("all", turb = 1)
thrust_time = ud_time**2 * Ctprime * 0.5 * (np.pi/4)
thrust_time = thrust_time[100:]
plt.figure(figsize= (9, 6))
plt.plot(thrust_time, label = 'Ct Prime = 1.50')
plt.xlabel('Timestep')
plt.ylabel('Thrust (Non Dimensional)')
plt.title('Turbine Thrust')
plt.savefig("./Turbine_Thrust_U_0008_Sim2_Single")

print(f"Thrust at Ct' = 1.50: {thrust_time}")
print(f"Uinf at Ct' = 1.50: {u_inf}")
print(f"Ud at Ct' = 1.50: {ud_time}")

#Compare

#Indcution Factor
a = 1 - (ud_time/u_inf)

#Power Coefficient
Cp_t = 4*a*((1-a)**2)
Cp_t = Cp_t[100:]
min_length_cp = min(len(Cp_time), len(Cp_t))
Cp_time = Cp_time[:min_length_cp]
Cp_t = Cp_t[:min_length_cp]
plt.figure(figsize = (9,6))
plt.scatter(range(len(Cp_time)), Cp_time, label='Simulated Cp', color='r', marker='.', s=5)
plt.plot(Cp_t, label = 'Theoretical Cp')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient Theoretical Comparison')
plt.savefig("./Turbine_Cp_Comapre")

percent_dif_cp = np.abs((Cp_t - Cp_time)/Cp_t)*100

plt.figure(figsize = (9,6))
plt.plot(percent_dif_cp)
plt.xlabel('Timestep')
plt.ylabel('Percent Difference')
plt.title('Percent Difference B/W Theory and Simulated Cp')
plt.savefig('./Turbine_Cp_PercentDif')

#Thrust Coefficients
ct_a = Ctprime*((1-a)**2)
ct_a = ct_a[100:]
ct_t = 4*a*(1-a)
ct_t = ct_t[100:]
min_length_ct = min(len(ct_a), len(ct_t))
ct_a = ct_a[:min_length_ct]
ct_t = ct_t[:min_length_ct]
plt.figure(figsize = (9,6))
plt.scatter(range(len(ct_a)), ct_a, label= 'Simulated Ct', marker = '.', s = 5)
plt.plot(ct_t, label = 'Theoretical Ct')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Ct')
plt.title('Thrust Coefficient Theoretical Comparison')
plt.savefig("./Turbine_Ct_Comapre")

percent_dif_ct = np.abs((ct_t - ct_a)/ct_t)*100

plt.figure(figsize = (9,6))
plt.plot(percent_dif_ct)
plt.xlabel('Timestep')
plt.ylabel('Percent Difference')
plt.title('Percent Difference B/W Theory and Simulated Ct')
plt.savefig('./Turbine_Ct_PercentDif')