import analysis_utils as au
import matplotlib.pyplot as plt
import os
from pathlib import Path
import quick_metadata_plots as mplts
import padeopsIO as pio

data_path = Path(au.DATA_PATH)
sim_folder = os.path.join(au.DATA_PATH, "F_0002_X_Files")

fig, (ax1, ax2) = plt.subplots(ncols=2, sharey = True)
fig.suptitle("$C_p$ vs Simulation Time for Stationary Turbine ($C_T^' = 1$)")
ax1.set_title("Correction On")
ax2.set_title("Correction Off")
zoom = (50, 75)

rows, fields = mplts.get_sim_varied_params(sim_folder)
ids, useCorrection, filterWidth = zip(*rows)
rounded_filter_width = [round(float(width), 3) for width in filterWidth]
idx_corrected = [i for i, val in enumerate(useCorrection) if val == 'True']
idx_not_corrected = [i for i, val in enumerate(useCorrection) if val == 'False']
mplts.plot_requested_turb_power(ax1, sim_folder, idx_corrected, [rounded_filter_width[i] for i in idx_corrected], zoom = zoom)
mplts.plot_requested_turb_power(ax2, sim_folder, idx_not_corrected, [rounded_filter_width[i] for i in idx_not_corrected], zoom = zoom)

mplts.plot_theoretical_turb_power(ax1, 1.0, sim_folder, 0, zoom = zoom)
mplts.plot_theoretical_turb_power(ax2, 1.0, sim_folder, 0, zoom = zoom)

ax1.legend(loc = "upper center", title = "Filter Width $\Delta$", fancybox = True)
plt.xlabel("Simulation Time")
plt.ylabel("Cp")
plt.savefig(os.path.join(sim_folder, 'static_diff_filter_power.png'))
