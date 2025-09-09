import analysis_utils as au
from pathlib import Path
import os
import math
import cmath
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

CtPrimes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

simulations = []
for i in range(0, 7):
  sim_name = f"Sim_000{i}"
  folder = f"Data/U_0_Files/{sim_name}"
  simulations[sim_name] = pio.BudgetIO(folder, padeops = True, runid = 0, normalize_origin = "turbine")
p = []
for i in range(8):
    p.append(simulations[i].read_turb_power("all", turb = 1)[-1])
u_inf = []
for i in range(8):
    u_inf.append(simulations[i].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp = []
for i in range(8):
   cp.append(p[i]/(0.5*(np.pi/4)*u_inf[i]**3))

np.save("cp_raw.npy", cp)