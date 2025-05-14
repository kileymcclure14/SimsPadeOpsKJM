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

sim_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0012")
sim = pio.BudgetIO("Data/B_0000_Files/Sim_0012", padeops = True, runid = 1)

ds_u = sim.slice(field_terms = 'u', ylim = 0)
ds_u['u'].imshow()
plt.savefig('./u_field_test')
