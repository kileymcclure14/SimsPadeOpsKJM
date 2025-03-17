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

#Change these each new sim
data_path = Path(au.DATA_PATH)
sim1_folder = os.path.join(au.DATA_PATH, "U_0000_9_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/U_0009_Files/Sim_0000", padeops=True, runid = 1, normalize_origin = "turbine")
sim2_folder = os.path.join(au.DATA_PATH, "U_0000_9_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/U_0009_Files/Sim_0001", padeops=True, runid = 1, normalize_origin = "turbine")
sim3_folder = os.path.join(au.DATA_PATH, "U_0000_9_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/U_0009_Files/Sim_0002", padeops=True, runid = 1, normalize_origin = "turbine")
sim4_folder = os.path.join(au.DATA_PATH, "U_0000_9_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/U_0009_Files/Sim_0003", padeops=True, runid = 1, normalize_origin = "turbine")
#fwidth1 = 
#fwidth2=
#fwidth3=
#fwidth4=

# M1 = turbine.get_correction(CT, fwidth, D)
# M2= turbine.get_correction(CT, fwidth, D)
# M3 = turbine.get_correction(CT, fwidth, D)
# M4 = turbine.get_correction(CT, fwidth, D)

#Turbine Power
power_time_s1 = sim1.read_turb_power("all", steady=False)[50:]
power_time_s2 = sim2.read_turb_power("all", steady=False)[50:]
power_time_s3 = sim3.read_turb_power("all", steady=False)[50:]
power_time_s4 = sim4.read_turb_power("all", steady=False)[50:]

#Power Coefficent
u_inf1 = sim1.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf2 = sim2.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf3 = sim3.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
u_inf4 = sim4.slice(field_terms=['u'], xlim = -5, zlim= 0)['u'].mean("y").values
Cp_les_s1 = power_time_s1 / (0.5 * (np.pi/4)*u_inf1**3)
Cp_les_s1 = Cp_les_s1[50:]
Cp_les_s2 = power_time_s2 / (0.5 * (np.pi/4)* u_inf2**3)
Cp_les_s2 = Cp_les_s2[50:]
Cp_les_s3 = power_time_s3 / (0.5 * (np.pi/4)* u_inf3**3)
Cp_les_s3= Cp_les_s3[50:]
Cp_les_s4 = power_time_s4 / (0.5*(np.pi/4) *u_inf4**3)
Cp_les_s4 = Cp_les_s4[50:]
plt.figure(figsize= (9, 6))
plt.plot(Cp_les_s1, label = 'Ct Prime = 1.0', color='red')
plt.plot(Cp_les_s2, label = 'Ct Prime = 1.50', color='blue')
plt.plot(Cp_les_s3, label = 'Ct Prime = 2.0', color='green')
plt.plot(Cp_les_s4, label = 'Ct Prime = 2.5', color='black')
plt.legend()
plt.xlabel('Timestep')
plt.ylabel('Cp')
plt.title('Power Coefficient')
plt.savefig("./Turbine_Cp_U_0009") #Change with each new sim
#Change with each new sim
print(f"Power coefficent for Ct' = 1.0: {Cp_les_s1}")
print(f"Power coefficent for Ct' = 1.50: {Cp_les_s2}")
print(f"Power coefficent for Ct' =  2.0: {Cp_les_s3}")
print(f"Power coefficent for Ct' = 2.50: {Cp_les_s4}")

#Instantaneous Velocity Field
ds1 = sim1.slice(field_terms='u', ylim=0)
ds1['u'].imshow()
plt.savefig("./U_Field_U_0009_Sim1") #Change with each new sim
ds2 = sim2.slice(field_terms='u', ylim=0)
ds2['u'].imshow()
plt.savefig("./U_Field_U_0009_Sim2") #Change with each new sim
ds3 = sim3.slice(field_terms='u', ylim=0)
ds3['u'].imshow()
plt.savefig("./U_Field_U_0009_Sim3") #Change with each new sim
ds4 = sim4.slice(field_terms='u', ylim=0)
ds4['u'].imshow()
plt.savefig("./U_Field_U_0009_Sim4") #Change with each new sim

#Turbine Thrust
Ctprime1 = sim1.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time1 = sim1.read_turb_uvel("all", steady=False)
thrust_time1 = ud_time1**2 * Ctprime1 * 0.5 * (np.pi/4)
thrust_time1 = thrust_time1[50:]
Ctprime2 = sim2.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time2 = sim2.read_turb_uvel("all", steady=False)
thrust_time2 = ud_time2**2 * Ctprime2 * 0.5 * (np.pi/4)
thrust_time2 = thrust_time2[50:]
Ctprime3 = sim3.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time3 = sim3.read_turb_uvel("all", steady=False)
thrust_time3 = ud_time3**2 * Ctprime3 * 0.5 * (np.pi/4)
thrust_time3 = thrust_time3[50:]
Ctprime4 = sim4.ta[0].ct  # same as: sim.turbineArray.turbines[0].ct
ud_time4 = sim4.read_turb_uvel("all", steady=False)
thrust_time4 = ud_time4**2 * Ctprime4 * 0.5 * (np.pi/4)
thrust_time4 = thrust_time4[50:]
plt.figure(figsize= (9, 6))
# #Change labels with each sim
# plt.plot(thrust_time1, label = 'Ct Prime = 1.0', color='red')
# plt.plot(thrust_time2, label = 'Ct Prime = 1.50', color='blue')
# plt.plot(thrust_time3, label = 'Ct Prime = 2.0', color='green')
# plt.plot(thrust_time4, label = 'Ct Prime = 2.50', color='black')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Thrust')
# plt.title('Turbine Thrust')
# plt.savefig("./Turbine_Thrust_U_0009")
#Change with each sim
print(f"Thrust for Ct' = 1.0: {thrust_time1}")
print(f"Thrust for Ct' = 1.50: {thrust_time2}")
print(f"Thrust for Ct' = 2.0: {thrust_time3}")
print(f"Thrust for Ct' = 2.5: {thrust_time4}")
print(f"Uinf for Ct' = 1.0: {u_inf1} and ud: {ud_time1}")
print(f"Uinf for Ct' = 1.50: {u_inf2} and ud: {ud_time2}")
print(f"Uinf for Ct' = 2.0: {u_inf3} and ud: {ud_time3}")
print(f"Uinf for Ct' = 2.5: {u_inf4} and ud: {ud_time4}")

#Compare

#Induction Factores
a1_les = 1-(power_time_s1/(0.5*(np.pi)*Ctprime1*M1**3))**(1/3)
a1_t = Ctprime1/(4+Ctprime1)
a2_les = 1-(power_time_s2/(0.5*(np.pi)*Ctprime2*M2**3))**(1/3)
a2_t = Ctprime2/(4+Ctprime2)
a3_les = 1-(power_time_s3/(0.5*(np.pi)*Ctprime3*M**3))**(1/3)
a3_t = Ctprime3/(4+Ctprime3)
a4_les = 1-(power_time_s4/(0.5*(np.pi)*Ctprime3*M3**3))**(1/3)
a4_t = Ctprime4/(4+Ctprime4)

#Change with each sim
print(f"Induction factor for Ct' = 1.0: {a1_les}")
print(f"Induction factor for Ct' = 1.50: {a2_les}")
print(f"Induction factor for Ct' = 2.0: {a3_les}")
print(f"Induction factor for Ct' = 2.50: {a4_les}")

#Power Coefficients
#First Sim
Cp_t1 = 4*a1_t*((1-a1_t)**2)
# Cp_t1 = Cp_t1[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(Cp_les_s1)), Cp_les_s1, label='Simulated Cp', marker='.', s=5)
# plt.plot(Cp_t1, label = 'Theoretical Cp')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Cp')
# plt.title('Power Coefficient Theoretical Comparison Sim1: Ct Prime = 1.0') #Change with each sim
# plt.savefig("./Turbine_Cp_Comapre_Sim1")

#Second Sim
Cp_t2 = 4*a2_t*((1-a2_t)**2)
# Cp_t2 = Cp_t2[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(Cp_les_s2)), Cp_les_s2, label='Simulated Cp', marker='.', s=5)
# plt.plot(Cp_t2, label = 'Theoretical Cp')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Cp')
# plt.title('Power Coefficient Theoretical Comparison Sim2: Ct Prime = 1.50') #Change with each sim
# plt.savefig("./Turbine_Cp_Comapre_Sim2")

#Third Sim
Cp_t3 = 4*a3_t*((1-a3_t)**2)
# Cp_t3 = Cp_t3[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(Cp_les_s3)), Cp_les_s3, label='Simulated Cp', marker='.', s=5)
# plt.plot(Cp_t3, label = 'Theoretical Cp')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Cp')
# plt.title('Power Coefficient Theoretical Comparison Sim3: Ct Prime = 2.0') #Change with each sim
# plt.savefig("./Turbine_Cp_Comapre_Sim3")

#Fourth Sim
Cp_t4 = 4*a4_t*((1-a4_t)**2)
# Cp_t4 = Cp_t4[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(Cp_les_s4)), Cp_les_s4, label='Simulated Cp', marker='.', s=5)
# plt.plot(Cp_t4, label = 'Theoretical Cp')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Cp')
# plt.title('Power Coefficient Theoretical Comparison Sim4: Ct Prime = 2.5')
# plt.savefig("./Turbine_Cp_Comapre_Sim4")

#Combined Plot, Change labels with each new sim
plt.figure(figsize = (9,6))
plt.scatter(range(len(Cp_les_s1)), Cp_les_s1, label='Simulated Cp at Ct Prime = 1.0 ', color = 'red', marker='.', s=5)
plt.plot(Cp_t1, label = 'Theoretical Cp at Ct Prime = 0.75', color = 'red')
plt.scatter(range(len(Cp_les_s2)), Cp_les_s2, label='Simulated Cp at Ct Prime = 1.50', color = 'blue', marker='.', s=5)
plt.plot(Cp_t2, label = 'Theoretical Cp at Ct Prime = 1.50', color = 'blue')
plt.scatter(range(len(Cp_les_s3)), Cp_les_s3, label='Simulated Cp at Ct Prime = 2.0', color = 'green', marker='.', s=5)
plt.plot(Cp_t3, label = 'Theoretical Cp at Ct Prime = 2.25', color = 'green')
plt.scatter(range(len(Cp_les_s4)), Cp_les_s4, label='Simulated Cp at Ct Prime = 2.5', color = 'black', marker='.', s=5)
plt.plot(Cp_t4, label = 'Theoretical Cp at Ct Prime = 3.0', color = 'black')
plt.legend()
plt.savefig('./Cp_Comapare_all')

#Thrust Coefficients, change labels with each new sim
#First Sim
ct_les1 = Ctprime1*((1-a1_les)**2)
ct_les1 = ct_les1[50:]
ct_t1 = Ctprime1*((1-a1_t)**2)
# ct_t1 = ct_t1[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(ct_les1)), ct_les1, label = 'Simulated Ct at Ct Prime = 1.0', marker = '.', s = 5)
# plt.plot(ct_t1, label = 'Theoretical Ct')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Ct')
# plt.title('Thrust Coefficient Theoretical Comparison Sim1: Ct Prime = 1.0')
# plt.savefig("./Turbine_Ct_Comapre_Sim1")

#Second Sim
ct_les2 = Ctprime2*((1-a2_les)**2)
ct_les2 = ct_les2[50:]
ct_t2 = Ctprime2*((1-a2_t)**2)
# ct_t2 = ct_t2[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(ct_les2)), ct_les2, label = 'Simulated Ct at Ct Prime = 1.50', marker = '.', s = 5)
# plt.plot(ct_t2, label = 'Theoretical Ct')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Ct')
# plt.title('Thrust Coefficient Theoretical Comparison Sim2: Ct Prime = 1.50')
# plt.savefig("./Turbine_Ct_Comapre_Sim2")

#Third Sim
ct_les3 = Ctprime3*((1-a3_les)**2)
ct_les3 = ct_les3[50:]
ct_t3 = Ctprime3*((1-a3_t)**2)
# ct_t3 = ct_t3[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(ct_les3)), ct_les3, label = 'Simulated Ct at Ct Prime = 2.0', marker = '.', s = 5)
# plt.plot(ct_t3, label = 'Theoretical Ct')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Ct')
# plt.title('Thrust Coefficient Theoretical Comparison Sim3: Ct Prime = 2.0')
# plt.savefig("./Turbine_Ct_Comapre_Sim3")

#Fourth Sim
ct_les4 = Ctprime4*((1-a4_les)**2)
ct_les4 = ct_les4[50:]
ct_t4 = Ctprime4*((1-a4_t)**2)
# ct_t4 = ct_t4[50:]
# plt.figure(figsize = (9,6))
# plt.scatter(range(len(ct_les4)), ct_les4, label = 'Simulated Ct at Ct Prime = 2.5', marker = '.', s = 5)
# plt.plot(ct_t4, label = 'Theoretical Ct')
# plt.legend()
# plt.xlabel('Timestep')
# plt.ylabel('Ct')
# plt.title('Thrust Coefficient Theoretical Comparison Sim4: Ct Prime = 2.5')
# plt.savefig("./Turbine_Ct_Comapre_Sim4")

#Combined Plot, change labels with each new sim
# plt.figure(figsize=(9,6))
# plt.scatter(range(len(ct_les1)), ct_les1, label = 'Simulated Ct at Ct Prime = 1.0', marker = '.', s = 5, color ='red')
# plt.plot(ct_t1, label = 'Theoretical Ct at Ct Prime = 1.0', color = 'red')
# plt.scatter(range(len(ct_les2)), ct_les2, label = 'Simulated Ct at Ct Prime = 1.50', marker = '.', s = 5, color = 'blue')
# plt.plot(ct_t2, label = 'Theoretical Ct at Ct Prime = 1.50', color = 'blue')
# plt.scatter(range(len(ct_les3)), ct_les3, label = 'Simulated Ct at Ct Prime = 2.0', marker = '.', s = 5, color = 'green')
# plt.plot(ct_t3, label = 'Theoretical Ct at Ct Prime = 2.0', color = 'green')
# plt.scatter(range(len(ct_les4)), ct_les4, label = 'Simulated Ct at Ct Prime = 2.5', marker = '.', s = 5, color = 'black')
# plt.plot(ct_t4, label = 'Theoretical Ct at Ct Prime = 2.5', color = 'black')
# plt.legend()
# plt.savefig('./ct_compare_all')

#Percent Differences

#Cp
cp1_les_compare = Cp_les_s1[-1]
percent_dif_cp_sim1 = np.abs((Cp_t1 - cp1_les_compare)/Cp_t1)*100
cp2_les_compare = Cp_les_s2[-1]
percent_dif_cp_sim2 = np.abs((Cp_t2 - cp2_les_compare)/Cp_t2)*100
cp3_les_compare = Cp_les_s3[-1]
percent_dif_cp_sim3 = np.abs((Cp_t3 - cp3_les_compare)/Cp_t3)*100
cp4_les_compare = Cp_les_s4[-1]
percent_dif_cp_sim4 = np.abs((Cp_t4 - cp4_les_compare)/Cp_t4)*100


# plt.figure(figsize=(9,6))
# plt.plot(percent_dif_cp_sim1, label = 'Ct Prime = 1.0', color = 'red')
# plt.plot(percent_dif_cp_sim2, label = 'Ct Prime = 1.50', color = 'blue')
# plt.plot(percent_dif_cp_sim3, label = 'Ct Prime = 2.0', color = 'green')
# plt.plot(percent_dif_cp_sim4, label = 'Ct Prime = 2.5', color = 'black')
# plt.xlabel('Timestep')
# plt.ylabel('Percent Difference')
# plt.title('Percent Difference Theory vs. Simulated Cp')
# plt.legend()
# plt.savefig('./Percent_Compare_Cp')

print(f"Cp at Ct Prime = 1.50: {cp1_les_compare}")
print(f"Theoretical Cp at Ct Prime = 1.50: {Cp_t1}")
print(f"Cp percent difference: {percent_dif_cp_sim1}")

print(f"Cp at Ct Prime = 1.50: {cp2_les_compare}")
print(f"Theoretical Cp at Ct Prime = 1.50: {Cp_t2}")
print(f"Cp percent difference: {percent_dif_cp_sim2}")

print(f"Cp at Ct Prime = 1.50: {cp3_les_compare}")
print(f"Theoretical Cp at Ct Prime = 1.50: {Cp_t3}")
print(f"Cp percent difference: {percent_dif_cp_sim3}")

print(f"Cp at Ct Prime = 1.50: {cp3_les_compare}")
print(f"Theoretical Cp at Ct Prime = 1.50: {Cp_t3}")
print(f"Cp percent difference: {percent_dif_cp_sim3}")

#Ct
ct_les1_compare = ct_les1[-1]
percent_dif_ct_sim1 = np.abs((ct_t1 - ct_les1_compare)/ct_t1)*100
ct_les2_compare = ct_les2[-1]
percent_dif_ct_sim2 = np.abs((ct_t2 - ct_les2_compare)/ct_t2)*100
ct_les3_compare = ct_les3[-1]
percent_dif_ct_sim3 = np.abs((ct_t3 - ct_les3_compare)/ct_t3)*100
ct_les4_compare = ct_les4[-1]
percent_dif_ct_sim4 = np.abs((ct_t4 - ct_les4)/ct_t4)*100

# plt.figure(figsize=(9,6))
# plt.plot(percent_dif_ct_sim1, label = 'Ct Prime = 1,0', color = 'red')
# plt.plot(percent_dif_ct_sim2, label = 'Ct Prime = 1.50', color = 'blue')
# plt.plot(percent_dif_ct_sim3, label = 'Ct Prime = 2.0', color = 'green')
# plt.plot(percent_dif_ct_sim4, label = 'Ct Prime = 2.5', color = 'black')
# plt.xlabel('Timestep')
# plt.ylabel('Percent Difference')
# plt.title('Percent Difference Theory vs. Simulated Ct')
# plt.legend()
# plt.savefig('./Percent_Compare_Ct')

print(f"Ct at Ct Prime = 1.50: {ct_les1_compare}")
print(f"Theoretical Ct at Ct Prime = 1.50: {ct_t1}")
print(f"Ct percent difference: {percent_dif_ct_sim1}")

print(f"Ct at Ct Prime = 1.50: {ct_les2_compare}")
print(f"Theoretical Ct at Ct Prime = 1.50: {ct_t2}")
print(f"Ct percent difference: {percent_dif_ct_sim2}")

print(f"Ct at Ct Prime = 1.50: {ct_les3_compare}")
print(f"Theoretical Ct at Ct Prime = 1.50: {ct_t3}")
print(f"Ct percent difference: {percent_dif_ct_sim3}")

print(f"Ct at Ct Prime = 1.50: {ct_les4_compare}")
print(f"Theoretical Ct at Ct Prime = 1.50: {ct_t4}")
print(f"Ct percent difference: {percent_dif_ct_sim4}")