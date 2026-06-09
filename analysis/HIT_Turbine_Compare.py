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

# Load Simulations
# Empty
sim10_2_3_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_3/10PCT", padeops = True, runid = 2)
sim20_2_3_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_3/20PCT", padeops = True, runid = 2)

sim10_2_8_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_8/10PCT", padeops = True, runid = 2)
sim20_2_8_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_8/20PCT", padeops = True, runid = 2)

sim10_2_12_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_12/10PCT", padeops = True, runid = 2)
sim20_2_12_e = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_12/20PCT", padeops = True, runid = 2)

# Turbine
sim10_2_3_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_3/10PCT", padeops = True, runid = 3, normalize_origin = "turbine")
sim20_2_3_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_3/20PCT", padeops = True, runid = 3, normalize_origin = "turbine")

sim10_2_8_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_8/10PCT", padeops = True, runid = 3, normalize_origin = "turbine")
sim20_2_8_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_8/20PCT", padeops = True, runid = 3, normalize_origin = "turbine")

sim10_2_12_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_12/10PCT", padeops = True, runid = 3, normalize_origin = "turbine")
sim20_2_12_t = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_12/20PCT", padeops = True, runid = 3, normalize_origin = "turbine")

# Tidx and Physical Time Values

# Ct Primes
ct_primes = [2]

# Power from Turbines by tidx
p10_2_3 = sim10_2_3_t.read_turb_power("all", turb = 1)
p20_2_3 = sim20_2_3_t.read_turb_power("all", turb = 1)

p10_2_8 = sim10_2_8_t.read_turb_power("all", turb = 1)
p20_2_8 = sim20_2_8_t.read_turb_power("all", turb = 1)

p10_2_12 = sim10_2_12_t.read_turb_power("all", turb = 1)
p20_2_12 = sim20_2_12_t.read_turb_power("all", turb = 1)

