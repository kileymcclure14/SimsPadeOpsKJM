import analysis_utils as au
import quick_metadata_plots as mplts
from pathlib import Path
import os
import math

import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
import pyGCS as pg
data_path = Path(au.DATA_PATH)
sim_folder = os.path.join(au.DATA_PATH, "F_0000_SU_X_Files")

# fig, ax = plt.subplots(figsize=(9, 3))
# labels = ["coarse", "medium", "fine"]
# for i, e in enumerate([8, 6]):
#     run_folder = os.path.join(sim_folder, "Sim_000" + str(e))
#     sim = pio.BudgetIO(run_folder, padeops = True, runid = 1)
#     dt = sim.input_nml["input"]["dt"]
#     trans_tau = int(math.ceil(50 / dt) + 1)
#     # TODO: ask Kirby if default should be "all", rather than None
#     # as it was confusing and when it is saved as a file first, they all printed I think?
#     power = sim.read_turb_power("all", turb=1)[trans_tau:]
#     time = [50 + dt * n for n in range(len(power))]
#     ax.plot(time, power, label = labels[i], lw=0.7)

# plt.legend(loc="lower right")
# plt.savefig(os.path.join(sim_folder, 'suite_power.png'))

# au.plot_gci_cp([0, 3, 6], sim_folder, "static_turbine_cp.png")
# au.plot_gci_cp([1, 4, 7], sim_folder, "max_surge_turbine_cp.png")
# au.plot_gci_cp([2, 5, 8], sim_folder, "max_pitch_turbine_cp.png")

zoom = (100, 110)
# au.plot_gci_cp([0, 3, 6], sim_folder, "zoomed_static_turbine_cp.png", zoom = zoom)
# au.plot_gci_cp([1, 4, 7], sim_folder, "zoomed_max_surge_turbine_cp.png", zoom = zoom)
# au.plot_gci_cp([2, 5, 8], sim_folder, "zoomed_max_pitch_turbine_cp.png", zoom = zoom)

zoom = (100, 150)
# au.plot_gci_cp([0, 3, 6], sim_folder, "less_zoomed_static_turbine_cp.png", zoom = zoom)

print("STATIC")
# au.plot_gci_cp([0, 3, 6], sim_folder, to_plot = False, gci = True)

print("SURGE")
au.plot_gci_cp([1, 4, 7], sim_folder, to_plot = False, gci = True, peak = True)

print("PITCH")
print("mean")
au.plot_gci_cp([2, 5, 8], sim_folder, to_plot = False, gci = True)
print("peak")
au.plot_gci_cp([2, 5, 8], sim_folder, to_plot = False, gci = True, peak = True)
print("trough")
au.plot_gci_cp([2, 5, 8], sim_folder, to_plot = False, gci = True, trough = True)
