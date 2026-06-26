import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine


sim = pio.BudgetIO("Data/HIT_Turbines/CTP_2/TI_3/10PCT", padeops=True, runid=3)

ubar = np.asarray(sim.slice(budget_terms="ubar")["ubar"])