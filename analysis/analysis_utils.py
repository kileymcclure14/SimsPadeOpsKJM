import argparse
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import padeopsIO as pio
import pyGCS as pg
from scipy.signal import find_peaks
import statistics


DATA_PATH = os.environ['SCRATCH'] + "/Data/"


def arg_parser(arg_list = ["write_dir", "filename"]):
    parser = argparse.ArgumentParser()
    for a in arg_list:
        parser.add_argument(a)
    args = parser.parse_args()
    return args

def power_to_Cp(power, uinf = 1, rho = 1):
    """
    Calculate Cp from PadeOps turbine power input for simple momentum theory of an actuator disk
    """
    return power / (0.5 * rho * math.pi * 0.5**2 * uinf**3)

def vel_to_a(udisk, uinf = 1, alg = "classical"):
    a = 1 - (udisk / uinf)
    # TODO: want to remove the turbine motion from both terms
    # urel = uturb + udisk
    # uinf_adjusted = uinf - uturb
    # a = 1 - (urel / uinf_adjusted)
    return a

def analytical_a(CT):
    # note that CT is actually CT'
    return CT / (4 + CT)

def a_to_Cp(a, alg = "classical"):
    return 4 * a * (1 - a)**2

def find_nearest(array, value):
    array = np.asarray(array)
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx

def x_zoom_plot(zoom, xs, ys):
    s_i = find_nearest(xs, zoom[0])
    e_i = find_nearest(xs, zoom[1])
    return xs[s_i : e_i + 1], ys[s_i : e_i + 1]

def plot_gci_cp(sim_nums, sim_folder, plot_title = None, zoom = None, to_plot = True, gci = False, peak = False, trough = False):
    fig, ax = plt.subplots(figsize=(9, 3))
    labels = ["coarse", "medium", "fine"]
    cp_sol = [0, 0, 0]
    cells = [0, 0, 0]
    for i, e in enumerate(sim_nums):
        run_folder = os.path.join(sim_folder, "Sim_000" + str(e))
        sim = pio.BudgetIO(run_folder, padeops = True, runid = e)
        dt = sim.input_nml["input"]["dt"]
        cells[i] = sim.input_nml["input"]["nx"] * sim.input_nml["input"]["ny"] * sim.input_nml["input"]["nz"]
        trans_tau = int(math.ceil(50 / dt) + 1)
        # TODO: ask Kirby if default should be "all", rather than None
        # as it was confusing and when it is saved as a file first, they all printed I think?
        power = sim.read_turb_power("all", turb=1)[trans_tau:]
        Cp = [power_to_Cp(p) for p in power]
        time = [50 + dt * n for n in range(len(Cp))]
        if zoom is not None:
            s_i = find_nearest(time, zoom[0])
            e_i = find_nearest(time, zoom[1])
            time = time[s_i : e_i + 1]
            Cp = Cp[s_i : e_i + 1]
        if gci:
            if peak:
                cp_peak_idx, _ = find_peaks(Cp)
                cp_peak_vals = [Cp[pi] for pi in cp_peak_idx]
                cp_sol[i] = statistics.mean(cp_peak_vals)
            elif trough:
                cp_trough_idx, _ = find_peaks([-c for c in Cp])
                cp_trough_vals = [Cp[ti] for ti in cp_trough_idx]
                cp_sol[i] = statistics.mean(cp_trough_vals)
            else:
                cp_sol[i] = statistics.mean(Cp)
        if to_plot:
            ax.plot(time, Cp, label = labels[i], lw=0.7)
    if to_plot:
        plt.legend(loc="lower right")
        plt.savefig(os.path.join(sim_folder, plot_title))
    if gci:
        gci = pg.GCI(dimension=3, simulation_order=4, volume=25*10*5, cells=cells, solution=cp_sol)
        print("Solution Values: " + str(cp_sol))
        print("GCI Values: " + str(gci.get('gci')))
        print("Asymptotic GCI: " + str(gci.get('asymptotic_gci')))
        print("Refinement Ratio: " + str(gci.get('refinement_ratio')))