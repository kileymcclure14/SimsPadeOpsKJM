import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine
import matplotlib.cm as cm
from matplotlib.colors import Normalize

data_path = Path(au.DATA_PATH)

sim = pio.BudgetIO("Data/Filtered_Spinups/10PCT", padeops = True, runid = 1)

ds = sim.slice(field_terms = "u")

dsy = sim.slice(field_terms = "u", ylim = 1.4)
dsz = sim.slice(field_terms = "u", zlim = 1.4)


dsy['u'].imshow()
plt.title('XZ HIT Spinup Test')
plt.savefig('./10PCT_spintest_xz.png', dpi = 300)

dsz['u'].imshow()
plt.title('XY HIT Spinup Test')
plt.savefig('./10PCT_spintest_xy.png', dpi = 300)


