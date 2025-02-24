import analysis_utils as au
import matplotlib.pyplot as plt
import os
from pathlib import Path
import quick_metadata_plots as mplts
import padeopsIO as pio

data_path = Path(au.DATA_PATH)
sim_folder = os.path.join(au.DATA_PATH, "F_0003_X_Files")

fig, ax = plt.subplots()
fig.suptitle("$C_p$ vs Simulation Time for Stationary Turbine ($C_T^' = 1$)")
zoom = (50, 250)

rows, fields = mplts.get_sim_varied_params(sim_folder)
ids, Ly, Lz, ny, nz = zip(*rows)
finished_sims_idx = [0, 2]
mplts.plot_requested_turb_power(ax, sim_folder, finished_sims_idx, [Ly[i] for i in finished_sims_idx], zoom = zoom)
mplts.plot_theoretical_turb_power(ax, 1.0, sim_folder, 0, zoom = zoom)

ax.legend(loc = "upper right", title = "Ly and Lz [D]", fancybox = True)
plt.xlabel("Simulation Time")
plt.ylabel("Cp")
plt.savefig(os.path.join(sim_folder, 'static_diff_blockage_power.png'))

