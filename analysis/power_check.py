import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine

path = r"/scratch/10268/kileymcclure/Data/HIT_Turbines/CTP_2/TI_8/UNB"
sim = pio.BudgetIO(path, padeops = True, runid = 3)
power_time = sim.read_turb_power(tidx="all")
Cp_time = power_time/(np.pi/8)

fig, ax = plt.subplots(figsize=(10, 1.5))
ax.plot(Cp_time)
ax.set_xlabel("TID")
ax.set_ylabel("$C_P$")
ax.text(0.99, 0.95, f"Mean $C_P$: {np.mean(Cp_time[1000:]):.3f}", transform=ax.transAxes, ha="right", va="top")
plt.savefig('powercheck.png')