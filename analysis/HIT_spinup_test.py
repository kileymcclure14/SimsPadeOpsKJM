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

sim = pio.BudgetIO("Data/HIT_Spinup_Test", padeops = True, runid = 1)

ds = sim.slice(field_terms = "u")

dsy = sim.slice(field_terms = "u", ylim = 3.14)
dsz = sim.slice(field_terms = "u", zlim = 3.14)

dsy['u'].imshow()
plt.title('XZ HIT Spinup Test')
plt.savefig('./HIT_spintest_xz.png', dpi = 300)

dsz['u'].imshow()
plt.title('XY HIT Spinup Test')
plt.savefig('./HIT_spintest_xy.png', dpi = 300)

ds1xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 1000)
ds2xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 2000)
ds3xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 3000)
ds4xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 4000)
ds5xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 5000)
ds6xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 6000)
ds7xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 7000)
ds8xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 8000)
ds89xy = sim.slice(field_terms = "u", zlim = 3.14, ylim = 3.14, tidx = 8914)
tidx_vals = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 8914])
datasets = [ds1xy, ds2xy, ds3xy, ds4xy, ds5xy, ds6xy, ds7xy, ds8xy, ds89xy]

norm = Normalize(vmin=tidx_vals.min(), vmax=tidx_vals.max())
cmap = cm.get_cmap('cividis_r')

plt.figure(figsize=(10, 6))

for tidx, ds_xy in zip(tidx_vals, datasets):
    color = cmap(norm(tidx))
    plt.plot(ds.x, ds_xy['u'], color=color, label=f'tidx={tidx}')

plt.xlabel('x/D')
plt.ylabel('u/U')
plt.title('Centerline Streamwise Velocity Evolution for HIT Spinup Test')
plt.legend()
plt.savefig('./HIT_spintest_centerline.png', dpi = 300)

