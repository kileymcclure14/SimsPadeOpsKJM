import padeopsIO as pio
import analysis_utils as au
# from pathlib import Path
import matplotlib.pyplot as plt
# import numpy as np
import os
import csv
import math
import statistics

# single image
# fig, ax = plt.subplots(figsize=(9, 3))
# folder = au.DATA_PATH + "B_0000_Files/"
# sim = pio.BudgetIO(folder, padeops = True, runid = 1)
# # dt = sim.input_nml["input"]["dt"]
# # print(dt)
# # trans_tau = int(math.ceil(50 / dt) + 1)
# # print(trans_tau)
# # TODO: ask Kirby if default should be "all", rather than None
# # as it was confusing and when it is saved as a file first, they all printed I think?
# power = sim.read_turb_power("all", turb=1)
# n_steps = len(power)
# strt_step = math.ceil(n_steps * 0.2)
# print(power)
# power = power[strt_step:]
# # time = [50 + dt * n for n in range(len(power))]
# label = "cT = 3"
# ax.plot(power, label=label, lw=0.7)
# plt.legend(loc="lower right")
# plt.savefig(folder + 'suite_power.png')



suite_path = au.DATA_PATH + "F_0000_X_Files/"
sub_folders = [f.path for f in os.scandir(suite_path) if f.is_dir()]
# TODO: In the long term, should make sure the IDs are in the right order!

# Open the CSV file for reading
fields = []
rows = []
with open(suite_path + "sim_ids.csv", mode='r') as file:
    csvreader = csv.reader(file)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

fig, ax = plt.subplots(figsize=(9, 3))

power_lists = []
for i, folder in enumerate(sub_folders):
    # TODO: there should be a way to supress warnings
    sim = pio.BudgetIO(folder, padeops = True, runid = 1)
    dt = sim.input_nml["input"]["dt"]
    trans_tau = int(math.ceil(50 / dt) + 1)
    # TODO: ask Kirby if default should be "all", rather than None
    # as it was confusing and when it is saved as a file first, they all printed I think?
    power = sim.read_turb_power("all", turb=1)[trans_tau:]
    power_lists.append(power)
    time = [50 + dt * n for n in range(len(power))]
    label = ""
    nfields = len(fields)
    for j, fld in enumerate(fields):
        if fld != "id":
            label += f"{fld}: {rows[i][j]}"
            if nfields != j + 1: 
                label += ", "

    ax.plot(time, power, label=label, lw=0.7)

plt.legend(loc="lower right")
plt.savefig(suite_path + 'suite_power.png')

power_means = [statistics.fmean(p) for p in power_lists]
print(power_means)

ct1_dt_diff = abs(power_means[0] - power_means[2])
ct3_dt_diff = abs(power_means[1] - power_means[3])

min_ct_diff = min(abs(power_means[0] - power_means[1]), abs(power_means[2] - power_means[3]))

print(ct1_dt_diff / min_ct_diff)
print(ct3_dt_diff / min_ct_diff)
