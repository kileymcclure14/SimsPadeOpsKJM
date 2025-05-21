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
sim13_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0012")
sim13 = pio.BudgetIO("Data/U_0017_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#Corrected
sim13_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0012")
sim13_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#Med Blocked, Uncorrected
sim13_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0012")
sim13_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#Med Blocked, Corrected
sim13_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0012")
sim13_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#High Blocked, Uncorrected
sim13_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0012")
sim13_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#High Blocked, Corrected
sim13_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0012")
sim13_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Prime (Set Manually, Should all be the same)
Ctprime = 2

#Turbine Power

#Uncorrected
p_les13 = sim13.read_turb_power("all", turb =1)[-1]

#Corrected
p_les13_cor = sim13_cor.read_turb_power("all", turb = 1)[-1]

#Med Blocked, Uncorrected
p_les13_mblock = sim13_mblock.read_turb_power("all", turb = 1)[-1]

#Med Blocked, Corrected
p_les13_mblock_cor = sim13_mblock_cor.read_turb_power("all", turb = 1)[-1]

#High Blocked, Uncorrected
p_les13_hblock = sim13_hblock.read_turb_power("all", turb = 1)[-1]

#High Blocked, Corrected
p_les13_hblock_cor = sim13_hblock_cor.read_turb_power("all", turb = 1)[-1]

#Free Stream Velocities

#Uncorrected
u_inf13 = sim13.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Corrected
u_inf13_cor = sim13_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Med Blocked, Uncorrected
u_inf13_mblock = sim13_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

#Med Blocked, Corrected
u_inf13_mblock_cor = sim13_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

#High Blocked, Uncorrected
u_inf13_hblock = sim13_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

#High Blocked, Corrected
u_inf13_hblock_cor = sim13_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

#Power Coefficients

#Uncorrected
cp_les13 = p_les13 / (0.5*(np.pi/4)*(u_inf13**3))

#Corrected
cp_les13_cor = p_les13_cor / (0.5*(np.pi/4)*(u_inf13_cor**3))

#Med Blocked, Uncorrected
cp_les13_mblock = p_les13_mblock / (0.5*(np.pi/4)*(u_inf13_mblock**3))

#Med Blocked, Corrected
cp_les13_mblock_cor = p_les13_mblock_cor / (0.5*(np.pi/4)*(u_inf13_mblock_cor**3))

#High Blockage, Uncorrected
cp_les13_hblock = p_les13_hblock / (0.5*(np.pi/4)*(u_inf13_hblock**3))

#High Blockage, Corrected
cp_les13_hblock_cor = p_les13_hblock_cor / (0.5*(np.pi/4)*(u_inf13_hblock_cor**3))

#Disk Velocities

#Uncorrected
ud_les13 = sim13.read_turb_uvel("all", steady = False)
ud_les13 = ud_les13[-1]

#Corrected
ud_les13_cor = sim13_cor.read_turb_uvel("all", steady = False)
ud_les13_cor = ud_les13_cor[-1]

#Med Blocked, Uncorrected
ud_les13_mblock = sim13_mblock.read_turb_uvel("all", steady = False)
ud_les13_mblock = ud_les13_mblock[-1]

#Med Blocked, Corrected
ud_les13_mblock_cor = sim13_mblock_cor.read_turb_uvel("all", steady = False)
ud_les13_mblock_cor = ud_les13_mblock_cor[-1]

#High Blocked, Uncorrected
ud_les13_hblock = sim13_hblock.read_turb_uvel("all", steady = False)
ud_les13_hblock = ud_les13_hblock[-1]

#High Blocked, Corrected
ud_les13_hblock_cor = sim13_hblock_cor.read_turb_uvel("all", steady = False)
ud_les13_hblock_cor = ud_les13_hblock_cor[-1]

#Thrust Force

#Uncorrected
thrust_les13 = 2*(np.pi/4)*(ud_les13)*(u_inf13 - ud_les13)

#Corrected
thrust_les13_cor = 2*(np.pi/4)*(ud_les13_cor)*(u_inf13_cor - ud_les13_cor)

#Med Blocked, No Correction
thrust_les13_mblock = 2*(np.pi/4)*(ud_les13_mblock)*(u_inf13_mblock - ud_les13_mblock)

#Med Blocked, Corrected
thrust_les13_mblock_cor = 2*(np.pi/4)*(ud_les13_mblock_cor)*(u_inf13_mblock_cor - ud_les13_mblock_cor)

#High Blocked, No Correction
thrust_les13_hblock = 2*(np.pi/4)*(ud_les13_hblock)*(u_inf13_hblock - ud_les13_hblock)

#High Blocked, Corrected
thrust_les13_hblock_cor = 2*(np.pi/4)*(ud_les13_hblock_cor)*(u_inf13_hblock_cor - ud_les13_hblock_cor)

#Ct

#Uncorrected
ct_les13 = thrust_les13/(0.5*(np.pi/4)*(u_inf13**2))

#Corrected
ct_les13_cor = thrust_les13_cor/(0.5*(np.pi/4)*(u_inf13_cor**2))

#Med Blocked, No Correction
ct_les13_mblock = thrust_les13_mblock/(0.5*(np.pi/4)*(u_inf13_mblock**2))

#Med Blocked, Corrected
ct_les13_mblock_cor = thrust_les13_mblock_cor/(0.5*(np.pi/4)*(u_inf13_mblock_cor**2))

#High Blockage, No Correction
ct_les13_hblock = thrust_les13_hblock/(0.5*(np.pi/4)*(u_inf13_hblock**2))

#High Blockage, Corrected
ct_les13_hblock_cor = thrust_les13_hblock_cor/(0.5*(np.pi/4)*(u_inf13_hblock_cor**2))

#Induction Factors

#Uncorrected
a_les13 = 1-np.cbrt((p_les13/(0.5*(np.pi/4)*Ctprime)))

#Corrected
a_les13_cor = 1-np.cbrt((p_les13_cor/(0.5*(np.pi/4)*Ctprime)))

#Med Blocked, No Correction
a_les13_mblock = 1-np.cbrt((p_les13_mblock/(0.5*(np.pi/4)*Ctprime)))

#Med Blocked, Corrected
a_les13_mblock_cor = 1-np.cbrt((p_les13_mblock_cor/(0.5*(np.pi/4)*Ctprime)))

#High Blocked, No Correction
a_les13_hblock = 1-np.cbrt((p_les13_hblock/(0.5*(np.pi/4)*Ctprime)))

#High Blockage, Corrected
a_les13_hblock_cor = 1-np.cbrt((p_les13_hblock_cor/(0.5*(np.pi/4)*Ctprime)))

#Arrays
blockage = [0, 10, 35]
cp_plot = [cp_les13, cp_les13_mblock, cp_les13_hblock]
cp_cor_plot = [cp_les13_cor, cp_les13_mblock_cor, cp_les13_hblock_cor]
a_plot = [a_les13, a_les13_mblock, a_les13_hblock]
a_cor_plot = [a_les13_cor, a_les13_mblock_cor, a_les13_hblock_cor]
ct_plot = [ct_les13, ct_les13_mblock, ct_les13_hblock]
ct_cor_plot = [ct_les13_cor, ct_les13_mblock_cor, ct_les13_hblock_cor]

#Plotting

#Cp
plt.figure(figsize = (9,6))
plt.scatter(blockage, cp_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, cp_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabel('Power Coefficient')
plt.title('Power Coefficient by Blockage % at Ct Prime = 2')

#a
plt.figure(figsize = (9,6))
plt.scatter(blockage, a_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, a_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabel('Induction Factor')
plt.title('Induction Factor by Blockage % at Ct Prime = 2')

#Ct
plt.figure(figsize = (9,6))
plt.scatter(blockage, ct_plot, marker = 'o', color = 'blue', label = 'Uncorrected')
plt.scatter(blockage, ct_cor_plot, marker = 'o', color = 'red', label = 'Corrected')
plt.legend()
plt.xlabel('Blockage %')
plt.ylabal('Thrust Coefficient')
plt.title('Thrust Coefficient by Blockage % at Ct Prime = 2')
