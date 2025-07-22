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
from sympy import symbols, Eq, solve

#Set up Sims
sim_mblock_list = []
for i in range(99):
    sim_folder = os.path.join(au.DATA_PATH, f"B_0006_Files/Sim_{i:04d}")
    sim_m = pio.BudgetIO(f"Data/B_0006_Files/Sim_{i:04d}", padeops = True, runid = 0, normalize_origin = "turbine")
    sim_mblock_list.append(sim_m)

sim_hblock_list = []
for i in range(99):
    sim_folder = os.path.join(au.DATA_PATH, f"B_0007_Files/Sim_{i:04d}")
    sim_h = pio.BudgetIO(f"Data/B_0007_Files/Sim_{i:04d}", padeops = True, runid = 0, normalize_origin = "turbine")
    sim_hblock_list.append(sim_h)