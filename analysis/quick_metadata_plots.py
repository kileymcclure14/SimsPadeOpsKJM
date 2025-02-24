import padeopsIO as pio
import analysis_utils as au
# from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import numpy as np
import os
import csv
import math
import statistics
import numpy as np
import cv2
import glob
from pathlib import Path
import moviepy.video.io.ImageSequenceClip
import re

# single image
def plot_run_power(run_folder, label = ""):
    fig, ax = plt.subplots(figsize=(9, 3))
    sim = pio.BudgetIO(run_folder, padeops = True, runid = 1)
    power = sim.read_turb_power("all", turb=1)
    Cp = [au.power_to_Cp(p) for p in power]
    n_steps = len(Cp)
    strt_step = math.ceil(n_steps * 0.2)
    Cp = Cp[strt_step:]
    ax.plot(Cp, label=label, lw=0.7)
    plt.legend(loc="lower right")
    os.path.join(run_folder, 'run_power.png')
    plt.savefig(os.path.join(run_folder, 'run_power.png'))


def get_sim_varied_params(suite_folder):
    fields = []
    rows = []
    with open(os.path.join(suite_folder, "sim_ids.csv"), mode='r') as file:
        csvreader = csv.reader(file)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    return rows, fields


def plot_suite_power(suite_folder, save = True, figsize = (9, 3)):
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
    fig, ax = plt.subplots(figsize = figsize)
    # Plot power from each run
    for i, folder in enumerate(sub_folders):
        try:
            sim = pio.BudgetIO(folder, padeops = True, runid = 1)
            dt = sim.input_nml["input"]["dt"]
            trans_tau = int(math.ceil(50 / dt) + 1)
            # TODO: ask Kirby if default should be "all", rather than None
            # as it was confusing and when it is saved as a file first, they all printed I think?
            power = sim.read_turb_power("all", turb=1)[trans_tau:]
            Cp = [au.power_to_Cp(p) for p in power]
            time = [50 + dt * n for n in range(len(Cp))]
            label = ""
            nfields = len(fields)
            for j, fld in enumerate(fields):
                if fld != "id":
                    label += f"{fld}: {rows[i][j]}"
                    if nfields != j + 1: 
                        label += ", "
        except FileNotFoundError:
            continue

        ax.plot(time, Cp, label=label, lw=0.7)

    if save:
        plt.legend(loc="lower right")
        plt.savefig(os.path.join(suite_folder, 'suite_cp.png'))
    return fig, ax

def _plot_instantaneous_field(save_folder, sim, *, tidx, field, xlim = [-5, 20], ylim =  [-5, 5], zlim = 0):
    ds = sim.slice(field_terms=[field], xlim = xlim, ylim = ylim, zlim = zlim, tidx = tidx)
    fig, ax = plt.subplots()
    ds[field].imshow(ax = ax)
    plt.title("TIDX: " + str(tidx))
    plt.savefig(os.path.join(save_folder, field + '_' + str(tidx) + '.png'))
    plt.close()
    return

def plot_instantaneous_field(run_folder, runid, tidx = 0, field = "u", **kwargs):
    sim = pio.BudgetIO(run_folder, padeops = True, runid = runid, normalize_origin="turbine")
    save_folder = run_folder
    if tidx == "all":
        save_folder = os.path.join(run_folder, field + "_plots")
        Path(save_folder).mkdir(parents=True, exist_ok=True)
        for tidx in sim.unique_tidx():
            _plot_instantaneous_field(save_folder, sim, tidx = tidx, field = field, **kwargs) 
    else:
        _plot_instantaneous_field(run_folder, sim, tidx = tidx, field = field, **kwargs)
    return save_folder

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(re.compile('([0-9]+)'), s)] 
 
def film_instantaneous_field(image_folder, fps = 10, video_name = "video.mp4"):
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    image_files.sort(key=natural_sort_key)
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(os.path.join(image_folder, video_name))
    return

def plot_requested_turb_power(ax, folder, runs, labels, zoom = None):
    for i, e in enumerate(runs):  # 
        run_folder = os.path.join(folder, "Sim_000" + str(e))
        sim = pio.BudgetIO(run_folder, padeops = True, runid = 1)
        dt = sim.input_nml["input"]["dt"]
        trans_tau = int(math.ceil(50 / dt) + 1)
        # TODO: ask Kirby if default should be "all", rather than None
        # as it was confusing and when it is saved as a file first, they all printed I think?
        power = sim.read_turb_power("all", turb=1)[trans_tau:]
        Cp = [au.power_to_Cp(p) for p in power]
        time = [50 + dt * n for n in range(len(Cp))]
        if zoom is not None:
            time, Cp = au.x_zoom_plot(zoom, time, Cp)
        ax.plot(time, Cp, label = labels[i], lw=0.7)
    return

def plot_theoretical_turb_power(ax, CT, folder, run, zoom = None):
    run_folder = os.path.join(folder, "Sim_000" + str(run))
    sim = pio.BudgetIO(run_folder, padeops = True, runid = 1)
    dt = sim.input_nml["input"]["dt"]
    trans_tau = int(math.ceil(50 / dt) + 1)
    power = sim.read_turb_power("all", turb=1)[trans_tau:]
    time = [50 + dt * n for n in range(len(power))]
    a = au.analytical_a(CT)
    Cp = [au.a_to_Cp(a)] * len(time)
    if zoom is not None:
        time, Cp = au.x_zoom_plot(zoom, time, Cp)
    ax.plot(time, Cp, label = "Analytical Cp", lw=0.7)
    return
