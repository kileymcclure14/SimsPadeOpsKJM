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

#Data and Path Stuff
data_path = Path(au.DATA_PATH)

#Uncorrected
sim_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0016")
sim = pio.BudgetIO("Data/U_0017_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Corrected
sim_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0016")
sim_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Med Blocked Uncorrected
sim_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0016")
sim_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Med Blocked Corrected
sim_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0016")
sim_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#High Blocked Uncorrected
sim_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0016")
sim_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#High Blocked Corrected
sim_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0016")
sim_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Prime (Manual Input)
Ctprime = 4

#Turbine Power
#Uncorrected
p_les = sim.read_turb_power("all", turb = 1)[-1]

#Corrected
p_les_cor = sim_cor.read_turb_power("all", turb = 1)[-1]

#Medium Blocked Uncorrected
p_les_mblock = sim_mblock.read_turb_power("all", turb = 1)[-1]

#Medium Blocked Corrected
p_les_mblock_cor = sim_mblock_cor.read_turb_power("all", turb =1)[-1]

#High Blocked Uncorrected
p_les_hblock = sim_hblock.read_turb_power("all", turb = 1)[-1]

#High Blocked Corrected
p_les_hblock_cor = sim_hblock_cor.read_turb_power("all", turb = 1)[-1]

#Free Stream Velocities

#Uncorrected
u_inf = sim.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Corrected
u_inf_cor = sim_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Med Blocked, Uncorrected
u_inf_mblock = sim_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

#Med Blocked, Corrected
u_inf_mblock_cor = sim_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

#High Blocked, Uncorrected
u_inf_hblock = sim_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

#High Blocked, Corrected
u_inf_hblock_cor = sim_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

#Power Coefficients

#Uncorrected
cp_les = p_les / (0.5*(np.pi/4)*(u_inf**3))

#Corrected
cp_les_cor = p_les_cor / (0.5*(np.pi/4)*(u_inf_cor**3))

#Med Blocked, Uncorrected
cp_les_mblock = p_les_mblock / (0.5*(np.pi/4)*(u_inf_mblock**3))

#Med Blocked, Corrected
cp_les_mblock_cor = p_les_mblock_cor / (0.5*(np.pi/4)*(u_inf_mblock_cor**3))

#High Blockage, Uncorrected
cp_les_hblock = p_les_hblock / (0.5*(np.pi/4)*(u_inf_hblock**3))

#High Blockage, Corrected
cp_les_hblock_cor = p_les_hblock_cor / (0.5*(np.pi/4)*(u_inf_hblock_cor**3))

#Disk Velocities

#Uncorrected
ud_les = sim.read_turb_uvel("all", steady = False)
ud_les = ud_les[-1]

#Corrected
ud_les_cor = sim_cor.read_turb_uvel("all", steady = False)
ud_les_cor = ud_les_cor[-1]

#Med Blocked, Uncorrected
ud_les_mblock = sim_mblock.read_turb_uvel("all", steady = False)
ud_les_mblock = ud_les_mblock[-1]

#Med Blocked, Corrected
ud_les_mblock_cor = sim_mblock_cor.read_turb_uvel("all", steady = False)
ud_les_mblock_cor = ud_les_mblock_cor[-1]

#High Blocked, Uncorrected
ud_les_hblock = sim_hblock.read_turb_uvel("all", steady = False)
ud_les_hblock = ud_les_hblock[-1]

#High Blocked, Corrected
ud_les_hblock_cor = sim_hblock_cor.read_turb_uvel("all", steady = False)
ud_les_hblock_cor = ud_les_hblock_cor[-1]

#Thrust Force

#Uncorrected
thrust_les = 2*(np.pi/4)*(ud_les)*(u_inf - ud_les)

#Corrected
thrust_les_cor = 2*(np.pi/4)*(ud_les_cor)*(u_inf_cor - ud_les_cor)

#Med Blocked, No Correction
thrust_les_mblock = 2*(np.pi/4)*(ud_les_mblock)*(u_inf_mblock - ud_les_mblock)

#Med Blocked, Corrected
thrust_les_mblock_cor = 2*(np.pi/4)*(ud_les_mblock_cor)*(u_inf_mblock_cor - ud_les_mblock_cor)

#High Blocked, No Correction
thrust_les_hblock = 2*(np.pi/4)*(ud_les_hblock)*(u_inf_hblock - ud_les_hblock)

#High Blocked, Corrected
thrust_les_hblock_cor = 2*(np.pi/4)*(ud_les_hblock_cor)*(u_inf_hblock_cor - ud_les_hblock_cor)

#Ct

#Uncorrected
ct_les = thrust_les/(0.5*(np.pi/4)*(u_inf**2))

#Corrected
ct_les_cor = thrust_les_cor/(0.5*(np.pi/4)*(u_inf_cor**2))

#Med Blocked, No Correction
ct_les_mblock = thrust_les_mblock/(0.5*(np.pi/4)*(u_inf_mblock**2))

#Med Blocked, Corrected
ct_les_mblock_cor = thrust_les_mblock_cor/(0.5*(np.pi/4)*(u_inf_mblock_cor**2))

#High Blockage, No Correction
ct_les_hblock = thrust_les_hblock/(0.5*(np.pi/4)*(u_inf_hblock**2))

#High Blockage, Corrected
ct_les_hblock_cor = thrust_les_hblock_cor/(0.5*(np.pi/4)*(u_inf_hblock_cor**2))

#Induction Factors

#Uncorrected
a_les = 1-np.cbrt((p_les/(0.5*(np.pi/4)*Ctprime)))

#Corrected
a_les_cor = 1-np.cbrt((p_les_cor/(0.5*(np.pi/4)*Ctprime)))

#Med Blocked, No Correction
a_les_mblock = 1-np.cbrt((p_les_mblock/(0.5*(np.pi/4)*Ctprime)))

#Med Blocked, Corrected
a_les_mblock_cor = 1-np.cbrt((p_les_mblock_cor/(0.5*(np.pi/4)*Ctprime)))

#High Blocked, No Correction
a_les_hblock = 1-np.cbrt((p_les_hblock/(0.5*(np.pi/4)*Ctprime)))

#High Blockage, Corrected
a_les_hblock_cor = 1-np.cbrt((p_les_hblock_cor/(0.5*(np.pi/4)*Ctprime)))

#Arrays
blockage = [0, 10, 35]
cp_plot = [cp_les, cp_les_mblock, cp_les_hblock]
cp_cor_plot = [cp_les_cor, cp_les_mblock_cor, cp_les_hblock_cor]
a_plot = [a_les, a_les_mblock, a_les_hblock]
a_cor_plot = [a_les_cor, a_les_mblock_cor, a_les_hblock_cor]
ct_plot = [ct_les, ct_les_mblock, ct_les_hblock]
ct_cor_plot = [ct_les_cor, ct_les_mblock_cor, ct_les_hblock_cor]

#Plotting

#Cp
plt.figure(figsize = (9,6))
plt.scatter(blockage, cp_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, cp_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabel('Power Coefficient')
plt.title('Power Coefficient by Blockage pct at Ct Prime = 4')
plt.savefig('./cp_ctprime_4')

#a
plt.figure(figsize = (9,6))
plt.scatter(blockage, a_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, a_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabel('Induction Factor')
plt.title('Induction Factor by Blockage pct at Ct Prime = 4')
plt.savefig('./a_ctprime_4')

#Ct
plt.figure(figsize = (9,6))
plt.scatter(blockage, ct_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, ct_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabel('Thrust Coefficient')
plt.title('Thrust Coefficient by Blockage pct at Ct Prime = 4')
plt.savefig('./ct_ctprime_4')
