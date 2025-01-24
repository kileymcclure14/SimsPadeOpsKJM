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
def plot_run_power(run_folder, label = ""):
    fig, ax = plt.subplots(figsize=(9, 3))
    sim = pio.BudgetIO(run_folder, padeops = True, runid = 1)
    power = sim.read_turb_power("all", turb=1)
    n_steps = len(power)
    strt_step = math.ceil(n_steps * 0.2)
    power = power[strt_step:]
    ax.plot(power, label=label, lw=0.7)
    plt.legend(loc="lower right")
    os.path.join(run_folder, 'run_power.png')
    plt.savefig(os.path.join(run_folder, 'run_power.png'))


def plot_suite_power(suite_folder):
    sub_folders = [f.path for f in os.scandir(suite_folder) if f.is_dir()]
    # Open the CSV file for reading
    fields = []
    rows = []

    with open(os.path.join(suite_folder, "sim_ids.csv"), mode='r') as file:
        csvreader = csv.reader(file)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    
    # Make empty figure
    fig, ax = plt.subplots(figsize=(9, 3))
    # Plot power from each run
    power_lists = []
    for i, folder in enumerate(sub_folders):
        # TODO: there should be a way to supress warnings
        print(folder)
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
    print(os.path.join(suite_folder, 'suite_power.png'))
    plt.savefig(os.path.join(suite_folder, 'suite_power.png'))