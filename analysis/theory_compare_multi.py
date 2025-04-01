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

#Change these in each sim
sim1_folder = os.path.join(au.DATA_PATH, "U_0013_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/U_0013_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder = os.path.join(au.DATA_PATH, "U_0013_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/U_0013_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder = os.path.join(au.DATA_PATH, "U_0013_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/U_0013_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder = os.path.join(au.DATA_PATH, "U_0013_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/U_0013_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim1_cor_folder = os.path.join(au.DATA_PATH, "U_0014_Files/Sim_0000")
sim1_cor = pio.BudgetIO("Data/U_0014_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_cor_folder = os.path.join(au.DATA_PATH, "U_0014_Files/Sim_0001")
sim2_cor = pio.BudgetIO("Data/U_0014_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_cor_folder = os.path.join(au.DATA_PATH, "U_0014_Files/Sim_0002")
sim3_cor = pio.BudgetIO("Data/U_0014_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_cor_folder = os.path.join(au.DATA_PATH, "U_0014_Files/Sim_0003")
sim4_cor = pio.BudgetIO("Data/U_0014_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Prime Values (Ct Prime is the same for sets of corrected/non-corrected sims)
Ctprime1 = sim1.ta[0].ct
Ctprime2 = sim2.ta[0].ct
Ctprime3 = sim3.ta[0].ct
Ctprime4 = sim4.ta[0].ct

#Filter Widths, manual input, comment out if not using correction factor

fwidth1 = 0.5
fwidth2= 0.5
fwidth3= 0.5
fwidth4= 0.5

#Correction Factors, comment out if not using
M1 = turbine.get_correction(Ctprime1, fwidth1, 1)
M2 = turbine.get_correction(Ctprime2, fwidth2, 1)
M3 = turbine.get_correction(Ctprime3, fwidth3, 1)
M4 = turbine.get_correction(Ctprime4, fwidth4, 1)

#Turbine Power, adjust vector based on when simulation reaches steady state solution
p_les1 = sim1.read_turb_power("all", turb =1)[-1]
p_les2 = sim2.read_turb_power("all", turb =1)[-1]
p_les3 = sim3.read_turb_power("all", turb =1)[-1]
p_les4 = sim4.read_turb_power("all", turb =1)[-1]

p_les1_cor = sim1_cor.read_turb_power("all", turb = 1)[-1]
p_les2_cor = sim2_cor.read_turb_power("all", turb = 1)[-1]
p_les3_cor = sim3_cor.read_turb_power("all", turb = 1)[-1]
p_les4_cor = sim4_cor.read_turb_power("all", turb = 1)[-1]

#Free Stream Velocities
u_inf1 = sim1.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2 = sim2.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3 = sim3.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4 = sim4.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

u_inf1_cor = sim1_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_cor = sim2_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_cor = sim3_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_cor = sim4_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

u_w1 = sim1.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w2 = sim2.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w3 = sim3.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w4 = sim4.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values

u_w1_cor = sim1_cor.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w2_cor = sim2_cor.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w3_cor = sim3_cor.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values
u_w4_cor = sim4_cor.slice(field_terms = ['u'], xlim = 22, zlim = 0)['u'].mean("y").values

#Power Coefficients
cp_les1 = p_les1 / (0.5*(np.pi/4)*(u_inf1**3))
cp_les2 = p_les2 / (0.5*(np.pi/4)*(u_inf2**3))
cp_les3 = p_les3 / (0.5*(np.pi/4)*(u_inf3**3))
cp_les4 = p_les4 / (0.5*(np.pi/4)*(u_inf4**3))

cp_les1_cor = p_les1_cor/(0.5*(np.pi/4)*(u_inf1_cor**3))
cp_les2_cor = p_les2_cor/(0.5*(np.pi/4)*(u_inf2_cor**3))
cp_les3_cor = p_les3_cor/(0.5*(np.pi/4)*(u_inf3_cor**3))
cp_les4_cor = p_les4_cor/(0.5*(np.pi/4)*(u_inf4_cor**3))

#Percent Difference Compare
pdif_cples1 = np.abs((np.mean(cp_les1)-np.mean(cp_les1_cor))/np.mean(cp_les1))*100
pdif_cples2 = np.abs((np.mean(cp_les2)-np.mean(cp_les2_cor))/np.mean(cp_les2))*100
pdif_cples3 = np.abs((np.mean(cp_les3)-np.mean(cp_les3_cor))/np.mean(cp_les3))*100
pdif_cples4 = np.abs((np.mean(cp_les4)-np.mean(cp_les4_cor))/np.mean(cp_les4))*100

#Print Results
print(f"Power Coefficient for Ct' = 1.0: {cp_les1}")
print(f"Power Coefficient with Correction Factor for Ct' = 1.0: {cp_les1_cor}")
print(f"Cp Percent Difference for Correcting Cp Prime = 1.0 = {pdif_cples1}")

print(f"Power Coefficient for Ct' = 1.25: {cp_les2}")
print(f"Power Coefficient with Correction Factor for Ct' = 1.25: {cp_les2_cor}")
print(f"Cp Percent Difference for Correcting Cp Prime = 1.25 = {pdif_cples2}")

print(f"Power Coefficient for Ct' = 1.5: {cp_les3}")
print(f"Power Coefficient with Correction Factor for Ct' = 1.5: {cp_les3_cor}")
print(f"Cp Percent Difference for Correcting Cp Prime = 1.5 = {pdif_cples3}")

print(f"Power Coefficient for Ct' = 1.75: {cp_les4}")
print(f"Power Coefficient with Correction Factor for Ct' = 1.75: {cp_les4_cor}")
print(f"Cp Percent Difference for Correcting Cp Prime = 1.75 = {pdif_cples4}")

#Velocities at Disk
ud_les1 = sim1.read_turb_uvel("all", steady = False)
ud_les1_cor = sim1_cor.read_turb_uvel("all", steady = False)
ud_les1 = ud_les1[-1]
ud_les1_cor = ud_les1_cor[-1]

ud_les2 = sim2.read_turb_uvel("all", steady = False)
ud_les2_cor = sim2_cor.read_turb_uvel("all", steady = False)
ud_les2 = ud_les2[-1]
ud_les2_cor = ud_les2_cor[-1]

ud_les3 = sim3.read_turb_uvel("all", steady = False)
ud_les3_cor = sim3_cor.read_turb_uvel("all", steady = False)
ud_les3 = ud_les3[-1]
ud_les3_cor = ud_les3_cor[-1]

ud_les4 = sim4.read_turb_uvel("all", steady = False)
ud_les4_cor = sim4_cor.read_turb_uvel("all", steady = False)
ud_les4 = ud_les4[-1]
ud_les4_cor = ud_les4_cor[-1]

#Disk Velocity Value Check (Should be within 0.5%, only use the solve to compare)
ud_solve1 = (p_les1/(0.5*(np.pi/4)*Ctprime1))**(1/3)
pdif_ud1 = ((np.abs(np.mean(ud_solve1)-np.mean(ud_les1))/np.mean(ud_solve1)))*100

ud_solve2 = (p_les2/(0.5*(np.pi/4)*Ctprime2))**(1/3)
pdif_ud2 = ((np.abs(np.mean(ud_solve2)-np.mean(ud_les2))/np.mean(ud_solve2)))*100

ud_solve3 = (p_les3/(0.5*(np.pi/4)*Ctprime3))**(1/3)
pdif_ud3 = (((np.abs(np.mean(ud_solve3)-np.mean(ud_les3)))/np.mean(ud_solve3)))*100

ud_solve4 = (p_les4/(0.5*(np.pi/4)*Ctprime4))**(1/3)
pdif_ud4 = ((np.abs(np.mean(ud_solve4)-np.mean(ud_les4))/np.mean(ud_solve4)))*100

ud_solve1_cor = (p_les1_cor/(0.5*(np.pi/4)*Ctprime1))**(1/3)
pdif_ud1_cor = ((np.abs(np.mean(ud_solve1_cor)-np.mean(ud_les1_cor)))/np.mean(ud_solve1_cor))*100

ud_solve2_cor = (p_les2_cor/(0.5*(np.pi/4)*Ctprime2 ))**(1/3)
pdif_ud2_cor = ((np.abs(np.mean(ud_solve2_cor)-np.mean(ud_les2_cor)))/np.mean(ud_solve2_cor))*100

ud_solve3_cor = (p_les3_cor/(0.5*(np.pi/4)*Ctprime3))**(1/3)
pdif_ud3_cor = ((np.abs(np.mean(ud_solve3_cor)-np.mean(ud_les3_cor)))/np.mean(ud_solve3_cor))*100

ud_solve4_cor = (p_les4_cor/(0.5*(np.pi/4)*Ctprime4))**(1/3)
pdif_ud4_cor = ((np.abs(np.mean(ud_solve4_cor)-np.mean(ud_les4_cor)))/np.mean(ud_solve4_cor))*100

#Print Results by Simulation
print(f"Ud Percent Difference at Ct Prime = 1.0: {pdif_ud1}")
print(f"Ud Percent Difference with Correction Factor at Ct Prime = 1.0: {pdif_ud1_cor}")

print(f"Ud Percent Difference at Ct Prime = 1.25: {pdif_ud2}")
print(f"Ud Percent Difference with Correction Factor at Ct Prime = 1.25: {pdif_ud2_cor}")

print(f"Ud Percent Difference at Ct Prime = 1.5: {pdif_ud3}")
print(f"Ud Percent Difference with Correction Factor at Ct Prime = 1.5: {pdif_ud3_cor}")

print(f"Ud Percent Difference at Ct Prime = 1.75: {pdif_ud4}")
print(f"Ud Percent Difference with Correction Factor at Ct Prime = 1.75: {pdif_ud4_cor}")

#Thrust Force
thrust_les1 = 2*(np.pi/4)*(ud_les1)*(u_inf1 - ud_les1)
thrust_les2 = 2*(np.pi/4)*(ud_les2)*(u_inf2 - ud_les2)
thrust_les3 = 2*(np.pi/4)*(ud_les3)*(u_inf3 - ud_les3)
thrust_les4 = 2*(np.pi/4)*(ud_les4)*(u_inf4 - ud_les4)

thrust_les1_cor = 2*(np.pi/4)*(ud_les1_cor)*(u_inf1_cor - ud_les1_cor)
thrust_les2_cor = 2*(np.pi/4)*(ud_les2_cor)*(u_inf2_cor - ud_les2_cor)
thrust_les3_cor = 2*(np.pi/4)*(ud_les3_cor)*(u_inf3_cor - ud_les3_cor)
thrust_les4_cor = 2*(np.pi/4)*(ud_les4_cor)*(u_inf4_cor - ud_les4_cor)

#Thrust Coefficients
ct_les1 = thrust_les1/(0.5*(np.pi/4)*(u_inf1**2))
ct_les1_cor = thrust_les1_cor/(0.5*(np.pi/4)*(u_inf1_cor**2))
pdif_ct_les1 = np.abs((np.mean(ct_les1)-np.mean(ct_les1_cor))/np.mean(ct_les1))*100

ct_les2 = thrust_les2/(0.5*(np.pi/4)*(u_inf2**2))
ct_les2_cor = thrust_les2_cor/(0.5*(np.pi/4)*(u_inf2_cor**2))
pdif_ct_les2 = np.abs((np.mean(ct_les2)-np.mean(ct_les2_cor))/np.mean(ct_les2))*100

ct_les3 = thrust_les3/(0.5*(np.pi/4)*(u_inf3**2))
ct_les3_cor = thrust_les3_cor/(0.5*(np.pi/4)*(u_inf3_cor**2))
pdif_ct_les3 = np.abs((np.mean(ct_les3)-np.mean(ct_les3_cor))/np.mean(ct_les3))*100

ct_les4 = thrust_les4/(0.5*(np.pi/4)*(u_inf4**2))
ct_les4_cor = thrust_les4_cor/(0.5*(np.pi/4)*(u_inf4_cor**2))
pdif_ct_les4 = np.abs((np.mean(ct_les4)-np.mean(ct_les4_cor))/np.mean(ct_les4))*100

#Induction Factors
a_les1 = 1-(p_les1/(0.5*(np.pi/4)*Ctprime1))**(1/3)
a_les1_cor = 1-(p_les1_cor/(0.5*(np.pi/4)*Ctprime1))**(1/3)
pdif_a_les1 = np.abs((np.mean(a_les1)-np.mean(a_les1_cor))/np.mean(a_les1))*100

a_les2 = 1-(p_les2/(0.5*(np.pi/4)*Ctprime2))**(1/3)
a_les2_cor = 1-(p_les2_cor/(0.5*(np.pi/4)*Ctprime2))**(1/3)
pdif_a_les2 = np.abs((np.mean(a_les2)-np.mean(a_les2_cor))/np.mean(a_les2))*100

a_les3 = 1-(p_les3/(0.5*(np.pi/4)*Ctprime3))**(1/3)
a_les3_cor = 1-(p_les3_cor/(0.5*(np.pi/4)*Ctprime3))**(1/3)
pdif_a_les3 = np.abs((np.mean(a_les3)-np.mean(a_les3_cor))/np.mean(a_les3))*100

a_les4 = 1-(p_les4/(0.5*(np.pi/4)*Ctprime4))**(1/3)
a_les4_cor = 1-(p_les4_cor/(0.5*(np.pi/4)*Ctprime4))**(1/3)
pdif_a_les4 = np.abs((np.mean(a_les4)-np.mean(a_les4_cor))/np.mean(a_les4))*100

#Theory Values (No Correction Factor used in Theory Calcs)

#Induction Factor and Compare
a_t1 = Ctprime1/(4+Ctprime1)
pdif_a1 = np.abs((a_t1 - np.mean(a_les1))/np.mean(a_t1))*100
pdif_a1_cor = np.abs((a_t1 - np.mean(a_les1_cor))/np.mean(a_t1))*100
print(f"Induction Factor Percent Difference (No Correction) for Ct Prime = 1.0: {pdif_a1}")
print(f"Induction Factor Percent Difference (Corrected) for Ct Prime = 1.0: {pdif_a1_cor}")

a_t2 = Ctprime2/(4+Ctprime2)
pdif_a2 = np.abs((a_t2 - np.mean(a_les2))/np.mean(a_t2))*100
pdif_a2_cor = np.abs((a_t2 - np.mean(a_les2_cor))/np.mean(a_t2))*100
print(f"Induction Factor Percent Difference (No Correction) for Ct Prime = 1.25: {pdif_a2}")
print(f"Induction Factor Percent Difference (Corrected) for Ct Prime = 1.25: {pdif_a2_cor}")
 
a_t3 = Ctprime3/(4+Ctprime3)
pdif_a3 = np.abs((a_t3 - np.mean(a_les3))/np.mean(a_t3))*100
pdif_a3_cor = np.abs((a_t3 - np.mean(a_les3_cor))/np.mean(a_t3))*100
print(f"Induction Factor Percent Difference (No Correction) for Ct Prime = 1.5: {pdif_a3}")
print(f"Induction Factor Percent Difference (Corrected) for Ct Prime = 1.5: {pdif_a3_cor}")

a_t4 = Ctprime4/(4+Ctprime4)
pdif_a4 = np.abs((a_t4 - np.mean(a_les4))/np.mean(a_t4))*100
pdif_a4_cor = np.abs((a_t4 - np.mean(a_les4_cor))/np.mean(a_t4))*100
print(f"Induction Factor Percent Difference (No Correction) for Ct Prime = 1.75: {pdif_a4}")
print(f"Induction Factor Percent Difference (Corrected) for Ct Prime = 1.75: {pdif_a4_cor}")

#Theororetical Cp and Compare
cp_t1 = 4*a_t1*((1-a_t1)**2)
pdif_cp1 = np.abs((cp_t1 - np.mean(cp_les1))/cp_t1)*100
pdif_cp1_cor = np.abs((cp_t1 - np.mean(cp_les1_cor))/cp_t1)*100
print(f"Percent Difference Cp (No Correction) at Ct Prime = 1.0: {pdif_cp1}")
print(f"Percent Difference Cp (Correction) at Ct Prime = 1.0: {pdif_cp1_cor}")

cp_t2 = 4*a_t2*((1-a_t2)**2)
pdif_cp2 = np.abs((cp_t2 - np.mean(cp_les2))/cp_t2)*100
pdif_cp2_cor = np.abs((cp_t2 - np.mean(cp_les2_cor))/cp_t2)*100
print(f"Percent Difference Cp (No Correction) at Ct Prime = 1.25: {pdif_cp2}")
print(f"Percent Difference Cp (Correction) at Ct Prime = 1.25: {pdif_cp2_cor}")

cp_t3 = 4*a_t3*((1-a_t3)**2)
pdif_cp3 = np.abs((cp_t3 - np.mean(cp_les3))/cp_t3)*100
pdif_cp3_cor = np.abs((cp_t3 - np.mean(cp_les3_cor))/cp_t3)*100
print(f"Percent Difference Cp (No Correction) at Ct Prime = 1.5: {pdif_cp3}")
print(f"Percent Difference Cp (Correction) at Ct Prime = 1.5: {pdif_cp3_cor}")

cp_t4 = 4*a_t4*((1-a_t4)**2)
pdif_cp4 = np.abs((cp_t4 - np.mean(cp_les4))/cp_t4)*100
pdif_cp4_cor = np.abs((cp_t4 - np.mean(cp_les4_cor))/cp_t4)*100
print(f"Percent Difference Cp (No Correction) at Ct Prime = 1.75: {pdif_cp4}")
print(f"Percent Difference Cp (Correction) at Ct Prime = 1.75: {pdif_cp4_cor}")

#Ct and Compare
ct_t1 = Ctprime1*((1-a_t1)**2)
pdif_ct1 = np.abs((ct_t1 - np.mean(ct_les1))/ct_t1)*100
pdif_ct1_cor = np.abs((ct_t1 - np.mean(ct_les1_cor))/ct_t1)*100
print(f"Percent Difference Ct (No Correction) at Ct Prime = 1.0: {pdif_ct1}")
print(f"Percent Difference Ct (Correction) at Ct Prime = 1.0: {pdif_ct1_cor}")

ct_t2 = Ctprime2*((1-a_t2)**2)
pdif_ct2 = np.abs((ct_t2 - np.mean(ct_les2))/ct_t2)*100
pdif_ct2_cor = np.abs((ct_t2 - np.mean(ct_les2_cor))/ct_t2)*100
print(f"Percent Difference Ct (No Correction) at Ct Prime = 1.25: {pdif_ct2}")
print(f"Percent Difference Ct (Correction) at Ct Prime = 1.25: {pdif_ct2_cor}")

ct_t3 = Ctprime3*((1-a_t3)**2)
pdif_ct3 = np.abs((ct_t3 - np.mean(ct_les3))/ct_t3)*100
pdif_ct3_cor = np.abs((ct_t3 - np.mean(ct_les3_cor))/ct_t3)*100
print(f"Percent Difference Ct (No Correction) at Ct Prime = 1.50: {pdif_ct3}")
print(f"Percent Difference Ct (Correction) at Ct Prime = 1.50: {pdif_ct3_cor}")

ct_t4 = Ctprime4*((1-a_t4)**2)
pdif_ct4 = np.abs((ct_t4 - np.mean(ct_les4))/ct_t4)*100
pdif_ct4_cor = np.abs((ct_t4 - np.mean(ct_les4_cor))/ct_t4)*100
print(f"Percent Difference Ct (No Correction) at Ct Prime = 1.75: {pdif_ct4}")
print(f"Percent Difference Ct (Correction) at Ct Prime = 1.75: {pdif_ct4_cor}")

#Set up arrays for plotting
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4]

Cp_les_plot = [np.mean(cp_les1), np.mean(cp_les2), np.mean(cp_les3), np.mean(cp_les4)]
Cp_les_cor_plot = [np.mean(cp_les1_cor), np.mean(cp_les2_cor), np.mean(cp_les3_cor), np.mean(cp_les4_cor)]
Cp_t_plot = [np.mean(cp_t1), np.mean(cp_t2), np.mean(cp_t3), np.mean(cp_t4)]

Ct_les_plot = [np.mean(ct_les1), np.mean(ct_les2), np.mean(ct_les3), np.mean(ct_les4)]
Ct_les_cor_plot = [np.mean(ct_les1_cor), np.mean(ct_les2_cor), np.mean(ct_les3_cor), np.mean(ct_les4_cor)]
Ct_t_plot = [np.mean(ct_t1), np.mean(ct_t2), np.mean(ct_t3), np.mean(ct_t4)]

a_les_plot = [np.mean(a_les1), np.mean(a_les2), np.mean(a_les3), np.mean(a_les4)]
a_les_cor_plot = [np.mean(a_les1_cor), np.mean(a_les2_cor), np.mean(a_les3_cor), np.mean(a_les4_cor)]
a_t_plot = [np.mean(a_t1), np.mean(a_t2), np.mean(a_t3), np.mean(a_t4)]

#Plotting
#Cp
plt.figure(figsize = (9,6))
plt.plot(Ctprime_plot, Cp_les_plot, label = "LES Cp Uncorrected")
plt.plot(Ctprime_plot, Cp_les_cor_plot, label = "LES Cp Corrected")
plt.scatter(Ctprime_plot, Cp_t_plot, marker = 'o', label = "Theoretical Cp Values" )
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("Cp")
plt.title("Corrected and Uncorrected LES Cp Values vs. Ct Prime and Theory")
plt.savefig("./Cp_Compare")

#Ct
plt.figure(figsize = (9,6))
plt.plot(Ctprime_plot, Ct_les_plot, label = "LES Ct Uncorrected")
plt.plot(Ctprime_plot, Ct_les_cor_plot, label = "LES Ct Corrected")
plt.scatter(Ctprime_plot, Ct_t_plot, marker = 'o', label = "Theoretical Ct Values" )
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("Ct")
plt.title("Corrected and Uncorrected LES Ct Values vs. Ct Prime and Theory")
plt.savefig("./Ct_Compare")

#a
plt.figure(figsize = (9,6))
plt.plot(Ctprime_plot, a_les_plot, label = "LES a Uncorrected")
plt.plot(Ctprime_plot, a_les_cor_plot, label = "LES a Corrected")
plt.scatter(Ctprime_plot, a_t_plot, marker = 'o', label = "Theoretical a Values" )
plt.legend()
plt.xlabel("Ct Prime")
plt.ylabel("a")
plt.title("Corrected and Uncorrected LES a Values vs. Ct Prime and Theory")
plt.savefig("./a_Compare")

