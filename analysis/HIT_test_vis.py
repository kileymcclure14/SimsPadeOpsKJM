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

data_path = Path(au.DATA_PATH)

sim = pio.BudgetIO("Data/HIT_Spinup_Test", padeops = True, runid = 1)

ds = sim.slice(field_terms = "u", ylim = 6.25)

ds['u'].imshow()
plt.savefig('./HIT_test_vis.png', dpi = 300)