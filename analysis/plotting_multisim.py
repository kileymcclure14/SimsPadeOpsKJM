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
sim1_folder = os.path.join(au.DATA_PATH, "U_0000_7_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/U_0007_Files/Sim_0000", padeops=True, runid = 1, normalize_origin = "turbine")
sim2_folder = os.path.join(au.DATA_PATH, "U_0000_7_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/U_0007_Files/Sim_0001", padeops=True, runid = 1, normalize_origin = "turbine")
sim3_folder = os.path.join(au.DATA_PATH, "U_0000_7_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/U_0007_Files/Sim_0002", padeops=True, runid = 1, normalize_origin = "turbine")
sim4_folder = os.path.join(au.DATA_PATH, "U_0000_7_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/U_0007_Files/Sim_0003", padeops=True, runid = 1, normalize_origin = "turbine")

#Turbine Power
power_time_s1 = sim1.read_turb_power(steady=False)
power_time_s2 = sim2.read_turb_power(steady=False)
power_time_s3 = sim3.read_turb_power(steady=False)
power_time_s4 = sim4.read_turb_power(steady=False)
plt.figure(figsize = (9,6))
plt.plot(power_time_s1, label = 'Ct Prime = 0.5', color='red')
plt.plot(power_time_s2, label = 'Ct Prime = 0.75', color='blue')
plt.plot(power_time_s3, label = 'Ct Prime = 1.0', color='green')
plt.plot(power_time_s4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Power (Non Dimensionalized by $D^2U^3$ )')
plt.title('Power Output')
plt.savefig("./Turbine_Power_U_0007")

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
plt.plot(Cp_time_s1, label = 'Ct Prime = 0.5', color='red')
plt.plot(Cp_time_s2, label = 'Ct Prime = 0.75', color='blue')
plt.plot(Cp_time_s3, label = 'Ct Prime = 1.0', color='green')
plt.plot(Cp_time_s4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficent')
plt.savefig("./Turbine_Cp_U_0007")

#Instantaneous Velocity Field
ds1 = sim1.slice(field_terms='u', ylim=0)
ds1['u'].imshow()
plt.savefig("./U_Field_U_0007_Sim1")
ds2 = sim2.slice(field_terms='u', ylim=0)
ds2['u'].imshow()
plt.savefig("./U_Field_U_0007_Sim2")
ds3 = sim3.slice(field_terms='u', ylim=0)
ds3['u'].imshow()
plt.savefig("./U_Field_U_0007_Sim3")
ds4 = sim4.slice(field_terms='u', ylim=0)
ds4['u'].imshow()
plt.savefig("./U_Field_U_0007_Sim4")

#Turbine Thrust
Ctprime1 = sim1.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time1 = sim1.read_turb_uvel(steady=False)
thrust_time1 = ud_time1**2 * Ctprime1 * 0.5 * (np.pi/4)
Ctprime2 = sim2.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time2 = sim2.read_turb_uvel(steady=False)
thrust_time2 = ud_time2**2 * Ctprime2 * 0.5 * (np.pi/4)
Ctprime3 = sim3.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time3 = sim3.read_turb_uvel(steady=False)
thrust_time3 = ud_time3**2 * Ctprime3 * 0.5 * (np.pi/4)
Ctprime4 = sim4.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time4 = sim4.read_turb_uvel(steady=False)
thrust_time4 = ud_time4**2 * Ctprime4 * 0.5 * (np.pi/4)
plt.figure(figsize= (9, 6))
plt.plot(thrust_time1, label = 'Ct Prime = 0.5', color='red')
plt.plot(thrust_time2, label = 'Ct Prime = 0.75', color='blue')
plt.plot(thrust_time3, label = 'Ct Prime = 1.0', color='green')
plt.plot(thrust_time4, label = 'Ct Prime = 3.0', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Thrust')
plt.title('Turbine Thrust')
plt.savefig("./Turbine_Thrust_U_0007")

print(thrust_time1, ud_time1)
print(thrust_time2, ud_time2)