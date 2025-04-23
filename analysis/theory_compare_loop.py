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
sim_folders = []
sims = []

for i in range(17):
    sim_name = f"Sim_{i:04d}"
    folder_name = os.path.join("U_0017_Files", sim_name)
    sim_folder = os.path.join(au.DATA_PATH, folder_name)
    sim_folders.append(sim_folder)
    sim = pio.BudgetIO(f"Data/{folder_name}", padeops=True, normalize_origin = "turbine")
    sims.append(sim)
    print(sims)

sim_folders_cor = []
sims_cor = []

for i in range(17):
    sim_name_cor = f"Sim_{i:04d}"
    folder_name_cor = os.path.join("U_0018_Files", sim_name_cor)
    sim_folder_cor = os.path.join(au.DATA_PATH, folder_name_cor)
    sim_folders_cor.append(sim_folder_cor)
    sim_cor = pio.BudgetIO(f"Data/{folder_name_cor}", padeops=True, normalize_origin = "turbine")
    sims_cor.append(sim_cor)

#Extract CtPrime Values
Ctprimes = {}
for i in range(17):
    Ctprimes[i] = sims[i].ta[0].ct
    Ctprimes = np.array(list(Ctprimes.values()))
    print(Ctprimes)
    
#Filter Widths
filterwidths = {}
for i in range(17):
    filterwidths[i] = 0.5

#Correction Factor Values
mvalues = {}
for i in range(17):
    mvalues[i] = turbine.get_correction(Ctprimes[i], filterwidths[i],1)

#Turbine Power to include Steady State
turbinepowers = {}
for i in range(17):
    turbinepowers[i] = sims[i].read_turb_power("all", turb = 1)[-1]

turbinepowers_cor = {}
for i in range(17):
    turbinepowers_cor[i] = sims_cor[i].read_turb_power("all", turb=1)[-1]

#Free Stream Velocities
uinfvalues = {}
for i in range(17):
    uinfvalues[i] = sims[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values[-1]

uinfvalues_cor = {}
for i in range(17):
    uinfvalues_cor[i] = sims_cor[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values[-1]

#End Velocities
uwvalues = {}
for i in range(17):
    uwvalues[i] = sims[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values[-1]

uwvalues_cor = {}
for i in range(17):
    uwvalues_cor[i] = sims_cor[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values[-1]

#Power Coefficients
cples = {}
for i in range(17):
    cples[i] = turbinepowers[i]/(0.5*(np.pi/4)*(uinfvalues[i]**3))

cples_cor = {}
for i in range(17):
    cples_cor[i]  = turbinepowers_cor[i]/(0.5*(np.pi/4)*(uinfvalues_cor[i]**3))

#Disk Velocities
udvalues = {}
for i in range(17):
    udvalues[i] = sims[i].read_turb_uvel("all", steady = False)[-1]

udvalues_cor = {}
for i in range(17):
    udvalues_cor[i]= sims_cor[i].read_turb_uvel("all", steady = False)[-1]

#Thrust Force
thrustles = {}
for i in range(17):
    thrustles[i] = 2*(np.pi/4)*udvalues[i]*(uinfvalues[i]-udvalues[i])

thrustles_cor = {}
for i in range(17):
    thrustles_cor[i] = 2*(np.pi/4)*udvalues_cor[i]*(uinfvalues_cor[i]-udvalues_cor[i])

#Thrust Coefficients
ctles = {}
for i in range(17):
    ctles[i] = thrustles[i]/(0.5*(np.pi/4)*(uinfvalues[i]**2))

ctles_cor = {}
for i in range(17):
    ctles_cor[i] = thrustles_cor[i]/(0.5*(np.pi/4)*(uinfvalues_cor[i]**2))

#Induction Factors
ales = {}
for i in range(17):
    ales[i] = 1-(turbinepowers[i]/(0.5*(np.pi/4)*Ctprimes[i]))**(1/3)

ales_cor = {}
for i in range(17):
    ales_cor[i] = 1-(turbinepowers_cor[i]/(0.5*(np.pi/4)*Ctprimes[i]))**(1/3)

#Plotting
#Set up arrays
ctprimes_plot = np.linspace(-4,4,100)
a_t_plot = ctprimes_plot/(4+ctprimes_plot)
cp_t_plot = 4*a_t_plot*((1-(a_t_plot))**2)
ct_t_plot = ctprimes_plot*((1-a_t_plot)**2)

#Cp
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, cples, marker = 'o', color = "black", label = "LES")
plt.scatter(Ctprimes, cples_cor, marker = 'o', color = "red", label = "Corrected LES")
plt.plot(ctprimes_plot, cp_t_plot, label = "Theoretical Values")
plt.legend()
plt.xlabel('Ct Prime')
plt.ylabel('Cp')
plt.title("Corrected and Uncorrected LES Cp Values vs. Ct Prime and Theory")
plt.savefig("./Cp_Compare")

#Ct
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, ctles, marker = 'o', color = "black", label = "LES")
plt.scatter(Ctprimes, ctles_cor, marker = 'o', color = "red", label = "Corrected LES")
plt.plot(ctprimes_plot, ct_t_plot, label = "Theoretical Values")
plt.legend()
plt.xlabel('Ct Prime')
plt.ylabel('Ct')
plt.title("Corrected and Uncorrected LES Ct Values vs. Ct Prime and Theory")
plt.savefig("./Ct_Compare")

#a
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, ales, marker = 'o', color = "black", label = "LES")
plt.scatter(Ctprimes, ales_cor, marker = 'o', color = "red", label = "Corrected LES")
plt.plot(ctprimes_plot, a_t_plot, label = "Theoretical Values")
plt.legend()
plt.xlabel('Ct Prime')
plt.ylabel('a')
plt.title("Corrected and Uncorrected LES a Values vs. Ct Prime and Theory")
plt.savefig("./a_Compare")