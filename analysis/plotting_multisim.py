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
sim1_folder = os.path.join(au.DATA_PATH, "U_0000_8_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/U_0008_Files/Sim_0000", padeops=True, runid = 1, normalize_origin = "turbine")
sim2_folder = os.path.join(au.DATA_PATH, "U_0000_8_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/U_0008_Files/Sim_0001", padeops=True, runid = 1, normalize_origin = "turbine")
sim3_folder = os.path.join(au.DATA_PATH, "U_0000_8_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/U_0008_Files/Sim_0002", padeops=True, runid = 1, normalize_origin = "turbine")
sim4_folder = os.path.join(au.DATA_PATH, "U_0000_8_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/U_0008_Files/Sim_0003", padeops=True, runid = 1, normalize_origin = "turbine")

#Turbine Power
power_time_s1 = sim1.read_turb_power("all", steady=False)
power_time_s2 = sim2.read_turb_power("all", steady=False)
power_time_s3 = sim3.read_turb_power("all", steady=False)
power_time_s4 = sim4.read_turb_power("all", steady=False)
plt.figure(figsize = (9,6))
plt.plot(power_time_s1, label = 'Ct Prime = 0.75', color='red')
plt.plot(power_time_s2, label = 'Ct Prime = 1.50', color='blue')
plt.plot(power_time_s3, label = 'Ct Prime = 2.25', color='green')
plt.plot(power_time_s4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Power (Non Dimensionalized by $D^2U^3$ )')
plt.title('Power Output')
plt.savefig("./Turbine_Power_U_0008")
print(f"Power for Ct' = 0.75: {power_time_s1}")
print(f"Power for Ct' = 1.50: {power_time_s2}")
print(f"Power for Ct' = 2.25: {power_time_s3}")
print(f"Power for Ct' = 3.0: {power_time_s4}")

#Power Coefficent
u_inf1 = sim1.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf2 = sim2.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf3 = sim3.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf4 = sim4.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_time_s1 = power_time_s1 / (0.5 * np.pi*0.5**2*u_inf1**3)
Cp_time_s2 = power_time_s2 / (0.5 * np.pi*0.5**2*u_inf2**3)
Cp_time_s3 = power_time_s3 / (0.5 * np.pi*0.5**2*u_inf3**3)
Cp_time_s4 = power_time_s4 / (0.5 * np.pi*0.5**2*u_inf4**3)
plt.figure(figsize= (9, 6))
plt.plot(Cp_time_s1, label = 'Ct Prime = 0.75', color='red')
plt.plot(Cp_time_s2, label = 'Ct Prime = 1.50', color='blue')
plt.plot(Cp_time_s3, label = 'Ct Prime = 2.25', color='green')
plt.plot(Cp_time_s4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficent')
plt.savefig("./Turbine_Cp_U_0008")
print(f"Power coefficent for Ct' = 0.75: {Cp_time_s1}")
print(f"Power coefficent for Ct' = 1.50: {Cp_time_s2}")
print(f"Power coefficent for Ct' =  2.25: {Cp_time_s3}")
print(f"Power coefficent for Ct' = 3.0: {Cp_time_s4}")

#Instantaneous Velocity Field
ds1 = sim1.slice(field_terms='u', ylim=0)
ds1['u'].imshow()
plt.savefig("./U_Field_U_0008_Sim1")
ds2 = sim2.slice(field_terms='u', ylim=0)
ds2['u'].imshow()
plt.savefig("./U_Field_U_0008_Sim2")
ds3 = sim3.slice(field_terms='u', ylim=0)
ds3['u'].imshow()
plt.savefig("./U_Field_U_0008_Sim3")
ds4 = sim4.slice(field_terms='u', ylim=0)
ds4['u'].imshow()
plt.savefig("./U_Field_U_0008_Sim4")

#Turbine Thrust
Ctprime1 = sim1.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time1 = sim1.read_turb_uvel("all", steady=False)
thrust_time1 = ud_time1**2 * Ctprime1 * 0.5 * (np.pi/4)
Ctprime2 = sim2.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time2 = sim2.read_turb_uvel("all", steady=False)
thrust_time2 = ud_time2**2 * Ctprime2 * 0.5 * (np.pi/4)
Ctprime3 = sim3.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time3 = sim3.read_turb_uvel("all", steady=False)
thrust_time3 = ud_time3**2 * Ctprime3 * 0.5 * (np.pi/4)
Ctprime4 = sim4.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time4 = sim4.read_turb_uvel("all", steady=False)
thrust_time4 = ud_time4**2 * Ctprime4 * 0.5 * (np.pi/4)
plt.figure(figsize= (9, 6))
plt.plot(thrust_time1, label = 'Ct Prime = 0.75', color='red')
plt.plot(thrust_time2, label = 'Ct Prime = 1.50', color='blue')
plt.plot(thrust_time3, label = 'Ct Prime = 2.25', color='green')
plt.plot(thrust_time4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Thrust')
plt.title('Turbine Thrust')
plt.savefig("./Turbine_Thrust_U_0008")
print(f"Thrust for Ct' = 0.75: {thrust_time1}")
print(f"Thrust for Ct' = 1.50: {thrust_time2}")
print(f"Thrust for Ct' = 2.25: {thrust_time3}")
print(f"Thrust for Ct' = 3.0: {thrust_time4}")
print(f"Uinf for Ct' = 0.75: {u_inf1} and ud: {ud_time1}")
print(f"Uinf for Ct' = 1.50: {u_inf2} and ud: {ud_time2}")
print(f"Uinf for Ct' = 2.25: {u_inf3} and ud: {ud_time3}")
print(f"Uinf for Ct' = 3.0: {u_inf4} and ud: {ud_time4}")

#Compare

#Induction Factores
a1 = 1-(ud_time1/u_inf1)
a2 = 1-(ud_time2/u_inf2)
a3 = 1-(ud_time3/u_inf3)
a4 = 1-(ud_time4/u_inf4)

#Power Coefficients
#First Sim
Cp_t1 = 4*a1*((1-a1)**2)
plt.figure(figsize = (9,6))
plt.plot(Cp_time_s1, label = 'Simulated Cp')
plt.plot(Cp_t1, label = 'Theoretical Cp')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient Theoretical Comparison Sim1: Ct Prime = 0.75')
plt.savefig("./Turbine_Cp_Comapre_Sim1")

#Second Sim
Cp_t2 = 4*a2*((1-a2)**2)
plt.figure(figsize = (9,6))
plt.plot(Cp_time_s2, label = 'Simulated Cp')
plt.plot(Cp_t2, label = 'Theoretical Cp')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient Theoretical Comparison Sim2: Ct Prime = 1.50')
plt.savefig("./Turbine_Cp_Comapre_Sim2")

#Third Sim
Cp_t3 = 4*a3*((1-a3)**2)
plt.figure(figsize = (9,6))
plt.plot(Cp_time_s3, label = 'Simulated Cp')
plt.plot(Cp_t3, label = 'Theoretical Cp')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient Theoretical Comparison Sim3: Ct Prime = 2.25')
plt.savefig("./Turbine_Cp_Comapre_Sim3")

#Fourth Sim
Cp_t4 = 4*a4*((1-a4)**2)
plt.figure(figsize = (9,6))
plt.plot(Cp_time_s4, label = 'Simulated Cp')
plt.plot(Cp_t4, label = 'Theoretical Cp')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient Theoretical Comparison Sim4: Ct Prime = 3.0')
plt.savefig("./Turbine_Cp_Comapre_Sim4")

#Thrust Coefficients
#First Sim
ct_a1 = Ctprime1*((1-a1)**2)
ct_t1 = 4*a1*(1-a1)
plt.figure(figsize = (9,6))
plt.plot(ct_a1, label = 'Simulated Ct')
plt.plot(ct_t1, label = 'Theoretical Ct')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Ct')
plt.title('Thrust Coefficient Theoretical Comparison Sim1: Ct Prime = 0.75')
plt.savefig("./Turbine_Ct_Comapre_Sim1")

#Second Sim
ct_a2 = Ctprime2*((1-a2)**2)
ct_t2 = 4*a2*(1-a2)
plt.figure(figsize = (9,6))
plt.plot(ct_a2, label = 'Simulated Ct')
plt.plot(ct_t2, label = 'Theoretical Ct')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Ct')
plt.title('Thrust Coefficient Theoretical Comparison Sim2: Ct Prime = 1.50')
plt.savefig("./Turbine_Ct_Comapre_Sim2")

#Third Sim
ct_a3 = Ctprime3*((1-a3)**2)
ct_t3 = 4*a3*(1-a3)
plt.figure(figsize = (9,6))
plt.plot(ct_a3, label = 'Simulated Ct')
plt.plot(ct_t3, label = 'Theoretical Ct')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Ct')
plt.title('Thrust Coefficient Theoretical Comparison Sim3: Ct Prime = 2.25')
plt.savefig("./Turbine_Ct_Comapre_Sim3")

#Fourth Sim
ct_a4 = Ctprime4*((1-a4)**2)
ct_t4 = 4*a4*(1-a4)
plt.figure(figsize = (9,6))
plt.plot(ct_a4, label = 'Simulated Ct')
plt.plot(ct_t4, label = 'Theoretical Ct')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Ct')
plt.title('Thrust Coefficient Theoretical Comparison Sim4: Ct Prime = 3.0')
plt.savefig("./Turbine_Ct_Comapre_Sim4")