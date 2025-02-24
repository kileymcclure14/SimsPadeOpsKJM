import analysis_utils as au
import quick_metadata_plots as mplts
from pathlib import Path
import os
import math
import statistics
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
import pyGCS as pg
import quick_metadata_plots as mplts

data_path = Path(au.DATA_PATH)
sim_folder_1 = os.path.join(au.DATA_PATH, "F_0000_SU_X_Files")
sim_folder_2 = os.path.join(au.DATA_PATH, "F_0002_SU_PI_X_Files")

spatial = ["coarse", "medium", "fine"]
temporal = ["small", "large"]

# zoom = (150, 160)
# Plot static turbine Cp calcualted from output power
# fig, ax = plt.subplots(figsize=(9, 6))
# mplts.plot_requested_turb_power(ax, sim_folder_1, [0, 3, 6], [s + ", " + temporal[0] for s in spatial], zoom = zoom)
# mplts.plot_requested_turb_power(ax, sim_folder_2, [0, 2], [spatial[0] + ", " + temporal[1], spatial[2] + ", " + temporal[1]], zoom = zoom)
# mplts.plot_theoretical_turb_power(ax, 1.0, sim_folder_1, 0, zoom = zoom)
# plt.title("Static Turbine Cp vs Time")
# plt.legend(loc="lower right")
# plt.ylabel("Cp")
# plt.xlabel("Simulation Time")
# plt.savefig(os.path.join(sim_folder_2, 'static_suite_power.png'))
# Plot static turbine Cp calculated from output velocity
# fig, ax = plt.subplots(figsize=(9, 6))
# mplts.plot_theoretical_turb_power(ax, sim_folder_1, [0, 3, 6], [s + ", " + temporal[0] for s in spatial], zoom = zoom)
# mplts.plot_theoretical_turb_power(ax, sim_folder_2, [0, 2], [spatial[0] + ", " + temporal[1], spatial[2] + ", " + temporal[1]], zoom = zoom)
# plt.title("Static Turbine U vs Time")
# plt.legend(loc="lower right")
# plt.ylabel("U")
# plt.xlabel("Simulation Time")
# plt.savefig(os.path.join(sim_folder_2, 'static_suite_velocity.png'))

# Plot pitching turbine
# fig, ax = plt.subplots(figsize=(9, 6))
# mplts.plot_requested_turb_power(ax, sim_folder_1, [2, 5, 8], [s + ", " + temporal[0] for s in spatial], zoom = zoom)
# mplts.plot_requested_turb_power(ax, sim_folder_2, [1, 3], [spatial[0] + ", " + temporal[1], spatial[2] + ", " + temporal[1]], zoom = zoom)
# plt.title("Pitching Turbine (f = 1, degree = 5) Cp vs Time")
# plt.legend(loc="lower right")
# plt.xlabel("Simulation Time")
# plt.ylabel("Cp")
# plt.savefig(os.path.join(sim_folder_2, 'pitching_suite_power.png'))
run_folder = "/scratch/10264/sgering/Data/F_0002_SU_PI_X_Files/Sim_0001"
save_folder = os.path.join(run_folder, "u_plots")
# save_folder = mplts.plot_instantaneous_field(run_folder, 1, tidx = "all", field = "u")
mplts.film_instantaneous_field(save_folder)