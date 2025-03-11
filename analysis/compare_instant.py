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

#Power
power_time = sim.read_turb_power(turb = 1)

#Cp
u_inf = sim.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_a = power_time / (0.5 *(np.pi/4)* u_inf**3)
print(f"Cp at Ct Prime = 2.25: {Cp_a}")
ud = sim.read_turb_uvel(turb = 1)
a = 1 - (ud/u_inf)
print(f"Induction factor at Ct Prime = 2.25: {a}")
Cp_t = (4*a)*((1-a)**2)
print(f"Theoretical Cp at Ct Prime = 2.25: {Cp_t}")

#Ct
Ctprime = sim.ta[0].ct
ct_a = Ctprime*((1-a)**2)
print(f"Ct at Ct Prime = 2.25: {ct_a}")
ct_t = 4*a*(1-a)
print(f"Theoretical Ct at Ct Prime = 2.25: {ct_t}")