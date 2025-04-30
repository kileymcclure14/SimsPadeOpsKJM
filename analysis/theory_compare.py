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

#Set Up Sims
sim_list = []

for i in range(8):  
    sim_folder = os.path.join(au.DATA_PATH, f"U_0021_Files/Sim_{i:04d}")
    sim = pio.BudgetIO(f"Data/U_0021_Files/Sim_{i:04d}", padeops=True, runid=1, normalize_origin="turbine")
    sim_list.append(sim)

sim_list_cor = []

for i in range(8):  
    sim_folder_cor = os.path.join(au.DATA_PATH, f"U_0022_Files/Sim_{i:04d}")
    sim_cor = pio.BudgetIO(f"Data/U_0022_Files/Sim_{i:04d}", padeops=True, runid=1, normalize_origin="turbine")
    sim_list_cor.append(sim)

# Extract CtPrime Values
Ctprimes = []
for i in range(8):
    Ctprimes.append(sim_list[i].ta[0].ct)
print(Ctprimes)
#Filter Widths (Manual Input)
fwidths = []
for i in range(8):
    fwidths.append(0.5)

#Correction Factors
m = []
for i in range(8):
    m.append(turbine.get_correction(Ctprimes[i], fwidths[i], 1))

#Turbine Power
turbine_powers = []
for i in range(8):
    turbine_powers.append(sim_list[i].read_turb_power(turb = 1))
print(turbine_powers)
turbine_powers_cor = []
for i in range(8):
    turbine_powers_cor.append(sim_list_cor[i].read_turb_power(turb =1))
print(turbine_powers)
#Free Stream Velocities
u_inf = []
for i in range(8):
    u_inf.append(sim_list[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values)

u_inf_cor = []
for i in range(8):
    u_inf_cor.append(sim_list_cor[i].slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values)

#Wake/End Velocities
u_w = []
for i in range(8):
    u_w.append(sim_list[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values)

u_w_cor = []
for i in range(8):
    u_w_cor.append(sim_list_cor[i].slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values)

#Power Coefficients
cp = []
for i in range(8):
    cp.append(turbine_powers[i]/(0.5*(np.pi/4)*(u_inf[i]**3)))

cp_cor = []
for i in range(8):
    cp_cor.append(turbine_powers_cor[i]/(0.5*(np.pi/4)*(u_inf_cor[i]**3)))

#Velocity at Disk
ud = []
for i in range(8):
    ud.append(sim_list[i].read_turb_uvel(steady = False)[-1])

ud_cor = []
for i in range(8):
    ud_cor.append(sim_list_cor[i].read_turb_uvel(steady = False)[-1])

#Thrust Force
thrust = []
for i in range(8):
    thrust.append(2*(np.pi/4)*(ud[i])*(u_inf[i]-ud[i]))

thrust_cor = []
for i in range(8):
    thrust_cor.append(2*(np.pi/4)*(ud_cor[i])*(u_inf_cor[i]-ud_cor[i]))

#Thrust Coefficients
ct = []
for i in range(8):
    ct.append(thrust[i]/(0.5*(np.pi/4)*(u_inf[i]**2)))

ct_cor = []
for i in range(8):
    ct_cor.append(thrust_cor[i]/(0.5*(np.pi/4)*(u_inf_cor[i]**2)))

#Induction Factors
a = []
for i in range(8):
   if Ctprimes[i] == 0:
    a.append(0)
   else:
    a.append(1 - np.cbrt((turbine_powers[i]/(0.5*(np.pi/4)*Ctprimes[i]))))

a_cor = []
for i in range(8):
   if Ctprimes[i] == 0:
    a_cor.append(0)
   else:
    a_cor.append(1 - np.cbrt((turbine_powers_cor[i]/(0.5*(np.pi/4)*Ctprimes[i]))))

#Theororetical Induction
a_t = []
for i in range (8):
  if Ctprimes[i] == -4:
     a_t.append(0)
  else:
     a_t.append(Ctprimes[i]/(4+Ctprimes[i]))

#Theroretical Cp
cp_t = []
for i in range(8):
   cp_t.append(4*a_t[i]*((1-a_t[i])**2))

#Theroretical Ct
ct_t = []
for i in range(8):
   ct_t.append(Ctprimes[i]*((1-a_t[i])**2))

#Plotting
#Cp
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, cp, marker ='o', color = 'black', label = 'LES Cp Uncorrected')
plt.scatter(Ctprimes, cp_cor, marker = 'o', color = 'orange', label = 'LES Cp Corrected')
plt.plot(Ctprimes, cp_t, label = "Theoretical Cp Values")
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("Cp")
plt.title("Corrected and Uncorrected LES Cp Values vs. Theory")
plt.savefig("./Cp_Compare")

#Ct
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, ct, marker ='o', color = 'black', label = 'LES Ct Uncorrected')
plt.scatter(Ctprimes, ct_cor, marker = 'o', color = 'orange', label = 'LES Ct Corrected')
plt.plot(Ctprimes, ct_t, label = "Theoretical Ct Values")
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("Ct")
plt.title("Corrected and Uncorrected LES Ct Values vs. Theory")
plt.savefig("./Ct_Compare")

#a
plt.figure(figsize = (9,6))
plt.scatter(Ctprimes, a, marker ='o', color = 'black', label = 'LES a Uncorrected')
plt.scatter(Ctprimes, a_cor, marker = 'o', color = 'orange', label = 'LES a Corrected')
plt.plot(Ctprimes, a_t, label = "Theoretical a Values")
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("a")
plt.title("Corrected and Uncorrected LES a Values vs. Theory")
plt.savefig("./a_Compare")