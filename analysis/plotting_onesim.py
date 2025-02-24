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
sim_folder = os.path.join(au.DATA_PATH, "U_0000_6_Files")
sim = pio.BudgetIO("Data/U_0006_Files", padeops = True, runid =1, normalize_origin= "turbine")

#Turbine Power
power_time = sim.read_turb_power(steady=False)
plt.figure(figsize= (9, 6))
plt.plot(power_time, label = 'Ct Prime = 0.8248')
plt.xlabel('Timestep')
plt.ylabel('Power (Non Dimensionalized by $D^2U^3$ )')
plt.title('Power Output')
plt.savefig("./Turbine_Power_U_0006")

#Turbine Power Coefficent
u_inf = sim.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_time = power_time / (0.5 * np.pi*0.5**2*u_inf**3)
plt.figure(figsize= (9, 6))
plt.plot(Cp_time, label = 'Ct Prime = 0.8248')
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficent')
plt.savefig("./Turbine_Cp_U_0006")

#Instantanious Velocity Field
ds = sim.slice(field_terms='u', ylim=0)
ds['u'].imshow()
plt.savefig("./U_Field_U_0006")

#Turbine Thrust 
Ctprime = sim.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time = sim.read_turb_uvel(steady=False)
thrust_time = ud_time**2 * Ctprime * 0.5 * (np.pi/4)
plt.figure(figsize= (9, 6))
plt.plot(thrust_time, label = 'Ct Prime = 0.8248')
plt.xlabel('Timestep')
plt.ylabel('Thrust (Non Dimensional)')
plt.title('Turbine Thrust')
plt.savefig("./Turbine_Thrust_U_0006")
