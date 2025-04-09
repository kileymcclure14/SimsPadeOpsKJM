import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

#Data Path and Folder Stuff
data_path = Path(au.DATA_PATH)

#Set up Sims
simulations = {}

for i in range(17):  # Loop over the range of simulation numbers (0 to 16)
    sim_folder = os.path.join(au.DATA_PATH, f"U_0014_Files/Sim_{i:04d}")  # Format the folder name with zero-padding
    sim = pio.BudgetIO(f"Data/U_0014_Files/Sim_{i:04d}", padeops=True, runid=1, normalize_origin="turbine")
    simulations[f"sim{i}"] = sim  # Store the simulation in the dictionary with a key like 'sim0', 'sim1', etc.

simulations_cor = {}
for i in range(17):
    sim_folder_cor = os.path.join(au.DATA_PATH, f"U_0015_Files/Sim_{i:04d}")
    sim_cor = pio.BudgetIO(f"Data/U_0015_Files/Sim_{i:04d}", padeops=True,runid=1, normalize_origin="turbine")
    simulations_cor[f"sim{i}_cor"] = sim_cor

#Extract CtPrime Values
Ctprimes = {}
for i in range(17):
    Ctprimes[f"Ctprime{i}"] = simulations[f"sim{i}"].ta[0].ct

#Filter Widths
filterwidths = {}
for i in range(17):
    filterwidths[f"filterwidth{i}"] = 0.5

#Correction Factor Values
mvalues = {}
for i in range(17):
    mvalues[f"M{i}"] = turbine.get_correction(Ctprimes[i], filterwidths[i],1)

#Turbine Power to include Steady State
turbinepowers = {}
for i in range(17):
    turbinepowers[f"p_les{i}"] = simulations[i].read_turb_power("all", turb = 1)[-1]

turbinepowers_cor = {}
for i in range(17):
    turbinepowers_cor[f"p_les{i}_cor"] = simulations_cor[i].read_turb_power("all", turb=1)[-1]

#Free Stream Velocities
uinfvalues = {}
for i in range(17):
    uinfvalues[f"u_inf{i}"] = simulations[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

uinfvalues_cor = {}
for i in range(17):
    uinfvalues_cor[f"u_inf{i}_cor"] = simulations_cor[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#End Velocities
uwvalues = {}
for i in range(17):
    uwvalues[f"u_w{i}"] = simulations[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values

uwvalues_cor = {}
for i in range(17):
    uwvalues_cor[f"u_w{i}_cor"] = simulations_cor[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values

#Power Coefficients
cples = {}
for i in range(17):
    cples[f"cp_les{i}"] = turbinepowers[i]/(0.5*(np.pi/4)*(uinfvalues[i]**3))

cples_cor = {}
for i in range(17):
    cples_cor[f"cp_les{i}_cor"]  = turbinepowers_cor[i]/(0.5*(np.pi/4)*(uinfvalues_cor[i]**3))

#Disk Velocities
udvalues = {}
for i in range(17):
    udvalues[f"ud_les{i}"] = simulations[i].read_turb_uvel("all", steady = False)[-1]

udvalues_cor = {}
for i in range(17):
    udvalues_cor[f"ud_les{i}_cor"]= simulations_cor[i].read_turb_uvel("all", steady = False)[-1]

#Thrust Force
thrustles = {}
for i in range(17):
    thrustles[f"thrust_les{i}"] = 2*(np.pi/4)*udvalues[i]*(uinfvalues[i]-udvalues[i])

thrustles_cor = {}
for i in range(17):
    thrustles_cor[f"thrust_les{i}_cor"] = 2*(np.pi/4)*udvalues_cor[i]*(uinfvalues_cor[i]-udvalues_cor[i])

#Thrust Coefficients
ctles = {}
for i in range(17):
    ctles[f"ct_les{i}"] = thrustles[i]/(0.5*(np.pi/4)*(uinfvalues[i]**2))

ctles_cor = {}
for i in range(17):
    ctles_cor[f"ct_les{i}_cor"] = thrustles_cor[i]/(0.5*(np.pi/4)*(uinfvalues_cor[i]**2))

#Induction Factors
ales = {}
for i in range(17):
    ales[f"a_les{i}"] = 1-(turbinepowers[i]/(0.5*(np.pi/4)*Ctprimes[i]))**(1/3)

ales_cor = {}
for i in range(17):
    ales_cor[f"a_les{i}"] = 1-(turbinepowers_cor[i]/(0.5*(np.pi/4)*Ctprimes[i]))**(1/3)

#Theory Values
#Induction Factor
a_t = {}
for i in range(17):
    a_t[f"a_t{i}"] = Ctprimes[i]/(4+Ctprimes[i])

#Cp
cp_t = {}
for i in range(17):
    cp_t[f"cp_t{i}"] = 4*a_t[i]*((1-a_t[i])**2)

#Ct
ct_t = {}
for i in range(17):
    ct_t[f"ct_t{i}"] = Ctprimes[i]*((1-a_t[i])**2)

#Plotting
#Set up arrays
ctprimes_plot = np.linspace(-4,4,100)