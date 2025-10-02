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

sim = pio.BudgetIO("Data/1_5_10_35_Files", padeops = True, normalize_origin = "turbine")

ds_u = sim.slice(field_terms = 'u', ylim = 5)
ds_u['u'].imshow()
plt.savefig('./flow_field_1_5_10_35_xz.png', dpi = 300)
