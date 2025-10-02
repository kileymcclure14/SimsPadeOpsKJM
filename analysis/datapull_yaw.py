import analysis_utils as au
from pathlib import Path
import os
import math
import cmath
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

CtPrimes =  [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
np.save("CtPrimes_Yaw.npy", CtPrimes)

#0.5 Ct Prime
simulations_0_5 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_0_5 = f"sim0_5_{i}_10"
    folder = f"Data/0_5_{i}_10_Files"
    simulations_0_5[sim_name_0_5] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_0_5 = []
for i in range(10):
    p_0_5.append(simulations_0_5[f"sim0_5_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_0_5 = []
for i in range(10):
    u_inf_0_5.append(simulations_0_5[f"sim0_5_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_0_5 = []
for i in range(10):
    cp_0_5.append(p_0_5[i]/(0.5*(np.pi/4)*(u_inf_0_5[i]**3)))
ud_0_5 = []
for i in range(10):
    ud_0_5.append(simulations_0_5[f"sim0_5_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_0_5 = []
for i in range(10):
    t_0_5.append(2*(np.pi/4)*(ud_0_5[i])*(u_inf_0_5[i]-ud_0_5[i]))
ct_0_5 = []
for i in range(10):
    ct_0_5.append(t_0_5[i]/(0.5*(np.pi/4)*(u_inf_0_5[i]**2)))
#Export to .npy
np.save("cp_0_5.npy", cp_0_5)
np.save("ct_0_5.npy", ct_0_5)

#1 Ct Prime
simulations_1 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_1 = f"sim1_{i}_10"
    folder = f"Data/1_{i}_10_Files"
    simulations_1[sim_name_1] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_1 = []
for i in range(10):
    p_1.append(simulations_1[f"sim1_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_1 = []
for i in range(10):
    u_inf_1.append(simulations_1[f"sim1_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_1 = []
for i in range(10):
    cp_1.append(p_1[i]/(0.5*(np.pi/4)*(u_inf_1[i]**3)))
ud_1 = []
for i in range(10):
    ud_1.append(simulations_1[f"sim1_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_1 = []
for i in range(10):
    t_1.append(2*(np.pi/4)*(ud_1[i])*(u_inf_1[i]-ud_1[i]))
ct_1 = []
for i in range(10):
    ct_1.append(t_1[i]/(0.5*(np.pi/4)*(u_inf_1[i]**2)))
#Export to .npy
np.save("cp_1.npy", cp_1)
np.save("ct_1.npy", ct_1)

#1.5 Ct Prime
simulations_1_5= {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_1_5 = f"sim1_5_{i}_10"
    folder = f"Data/1_5_{i}_10_Files"
    simulations_1_5[sim_name_1_5] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_1_5 = []
for i in range(10):
    p_1_5.append(simulations_1_5[f"sim1_5_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_1_5 = []
for i in range(10):
    u_inf_1_5.append(simulations_1_5[f"sim1_5_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_1_5 = []
for i in range(10):
    cp_1_5.append(p_1_5[i]/(0.5*(np.pi/4)*(u_inf_1_5[i]**3)))
ud_1_5 = []
for i in range(10):
    ud_1_5.append(simulations_1_5[f"sim1_5_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_1_5 = []
for i in range(10):
    t_1_5.append(2*(np.pi/4)*(ud_1_5[i])*(u_inf_1_5[i]-ud_1_5[i]))
ct_1_5 = []
for i in range(10):
    ct_1_5.append(t_1_5[i]/(0.5*(np.pi/4)*(u_inf_1_5[i]**2)))
#Export to .npy
np.save("cp_1_5.npy", cp_1_5)
np.save("ct_1_5.npy", ct_1_5)

#2 Ct Prime
simulations_2 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_2 = f"sim2_{i}_10"
    folder = f"Data/2_{i}_10s_Files"
    simulations_2[sim_name_2] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_2 = []
for i in range(10):
    p_2.append(simulations_2[f"sim2_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_2 = []
for i in range(10):
    u_inf_2.append(simulations_2[f"sim2_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_2 = []
for i in range(10):
    cp_2.append(p_2[i]/(0.5*(np.pi/4)*(u_inf_2[i]**3)))
ud_2 = []
for i in range(10):
    ud_2.append(simulations_2[f"sim2_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_2 = []
for i in range(10):
    t_2.append(2*(np.pi/4)*(ud_2[i])*(u_inf_2[i]-ud_2[i]))
ct_2 = []
for i in range(10):
    ct_2.append(t_2[i]/(0.5*(np.pi/4)*(u_inf_2[i]**2)))
#Export to .npy
np.save("cp_2s.npy", cp_2)
np.save("ct_2s.npy", ct_2)

#2.5 Ct Prime
simulations_2_5= {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_2_5 = f"sim2_5_{i}_10"
    folder = f"Data/2_5_{i}_10s_Files"
    simulations_2_5[sim_name_2_5] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_2_5 = []
for i in range(10):
    p_2_5.append(simulations_2_5[f"sim2_5_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_2_5 = []
for i in range(10):
    u_inf_2_5.append(simulations_2_5[f"sim2_5_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_2_5 = []
for i in range(10):
    cp_2_5.append(p_2_5[i]/(0.5*(np.pi/4)*(u_inf_2_5[i]**3)))
ud_2_5 = []
for i in range(10):
    ud_2_5.append(simulations_2_5[f"sim2_5_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_2_5 = []
for i in range(10):
    t_2_5.append(2*(np.pi/4)*(ud_2_5[i])*(u_inf_2_5[i]-ud_2_5[i]))
ct_2_5 = []
for i in range(10):
    ct_2_5.append(t_2_5[i]/(0.5*(np.pi/4)*(u_inf_2_5[i]**2)))
#Export to .npy
np.save("cp_2_5s.npy", cp_2_5)
np.save("ct_2_5s.npy", ct_2_5)

#3 Ct Prime
simulations_3= {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_3 = f"sim3_{i}_10"
    folder = f"Data/3_{i}_10s_Files"
    simulations_3[sim_name_3] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_3 = []
for i in range(10):
    p_3.append(simulations_3[f"sim3_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_3 = []
for i in range(10):
    u_inf_3.append(simulations_3[f"sim3_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_3 = []
for i in range(10):
    cp_3.append(p_3[i]/(0.5*(np.pi/4)*(u_inf_3[i]**3)))
ud_3 = []
for i in range(10):
    ud_3.append(simulations_3[f"sim3_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_3 = []
for i in range(10):
    t_3.append(2*(np.pi/4)*(ud_3[i])*(u_inf_3[i]-ud_3[i]))
ct_3 = []
for i in range(10):
    ct_3.append(t_3[i]/(0.5*(np.pi/4)*(u_inf_3[i]**2)))
#Export to .npy
np.save("cp_3s.npy", cp_3)
np.save("ct_3s.npy", ct_3)

#3.5 Ct Prime
simulations_3_5= {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_3_5 = f"sim3_5_{i}_10"
    folder = f"Data/3_5_{i}_10s_Files"
    simulations_3_5[sim_name_3_5] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_3_5 = []
for i in range(10):
    p_3_5.append(simulations_3_5[f"sim3_5_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_3_5 = []
for i in range(10):
    u_inf_3_5.append(simulations_3_5[f"sim3_5_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_3_5 = []
for i in range(10):
    cp_3_5.append(p_3_5[i]/(0.5*(np.pi/4)*(u_inf_3_5[i]**3)))
ud_3_5 = []
for i in range(10):
    ud_3_5.append(simulations_3_5[f"sim3_5_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_3_5 = []
for i in range(10):
    t_3_5.append(2*(np.pi/4)*(ud_3_5[i])*(u_inf_3_5[i]-ud_3_5[i]))
ct_3_5 = []
for i in range(10):
    ct_3_5.append(t_3_5[i]/(0.5*(np.pi/4)*(u_inf_3_5[i]**2)))
#Export to .npy
np.save("cp_3_5s.npy", cp_3_5)
np.save("ct_3_5s.npy", ct_3_5)

#4 Ct Prime
simulations_4= {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_4 = f"sim4_{i}_10"
    folder = f"Data/4_{i}_10s_Files"
    simulations_4[sim_name_4] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_4 = []
for i in range(10):
    p_4.append(simulations_4[f"sim4_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_4 = []
for i in range(10):
    u_inf_4.append(simulations_4[f"sim4_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_4 = []
for i in range(10):
    cp_4.append(p_4[i]/(0.5*(np.pi/4)*(u_inf_4[i]**3)))
ud_4 = []
for i in range(10):
    ud_4.append(simulations_4[f"sim4_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_4 = []
for i in range(10):
    t_4.append(2*(np.pi/4)*(ud_4[i])*(u_inf_4[i]-ud_4[i]))
ct_4 = []
for i in range(10):
    ct_4.append(t_4[i]/(0.5*(np.pi/4)*(u_inf_4[i]**2)))
#Export to .npy
np.save("cp_4s.npy", cp_4)
np.save("ct_4s.npy", ct_4)

#-3 Ct Prime
simulations_neg3 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_neg3 = f"simneg3_{i}_10"
    folder = f"Data/neg3_{i}_10s_Files"
    simulations_neg3[sim_name_neg3] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_neg3 = []
for i in range(10):
    p_neg3.append(simulations_neg3[f"simneg3_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_neg3 = []
for i in range(10):
    u_inf_neg3.append(simulations_neg3[f"simneg3_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_neg3 = []
for i in range(10):
    cp_neg3.append(p_neg3[i]/(0.5*(np.pi/4)*(u_inf_neg3[i]**3)))
ud_neg3 = []
for i in range(10):
    ud_neg3.append(simulations_neg3[f"simneg3_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_neg3 = []
for i in range(10):
    t_neg3.append(2*(np.pi/4)*(ud_neg3[i])*(u_inf_neg3[i]-ud_neg3[i]))
ct_neg3 = []
for i in range(10):
    ct_neg3.append(t_neg3[i]/(0.5*(np.pi/4)*(u_inf_neg3[i]**2)))
#Export to .npy
np.save("cp_neg3.npy", cp_neg3)
np.save("ct_neg3.npy", ct_neg3)

#-2 Ct Prime
simulations_neg2 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_neg2 = f"simneg2_{i}_10"
    folder = f"Data/neg2_{i}_10_Files"
    simulations_neg2[sim_name_neg2] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_neg2 = []
for i in range(10):
    p_neg2.append(simulations_neg2[f"simneg2_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_neg2 = []
for i in range(10):
    u_inf_neg2.append(simulations_neg2[f"simneg2_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_neg2 = []
for i in range(10):
    cp_neg2.append(p_neg2[i]/(0.5*(np.pi/4)*(u_inf_neg2[i]**3)))
ud_neg2 = []
for i in range(10):
    ud_neg2.append(simulations_neg2[f"simneg2_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_neg2 = []
for i in range(10):
    t_neg2.append(2*(np.pi/4)*(ud_neg2[i])*(u_inf_neg2[i]-ud_neg2[i]))
ct_neg2 = []
for i in range(10):
    ct_neg2.append(t_neg2[i]/(0.5*(np.pi/4)*(u_inf_neg2[i]**2)))
#Export to .npy
np.save("cp_neg2.npy", cp_neg2)
np.save("ct_neg2.npy", ct_neg2)

#-3 Ct Prime
simulations_neg1 = {}
for i in range(0, 100, 10):  # 0, 10, ..., 90
    sim_name_neg1 = f"simneg1_{i}_10"
    folder = f"Data/neg1_{i}_10_Files"
    simulations_neg1[sim_name_neg1] = pio.BudgetIO(folder, padeops=True, runid=1, normalize_origin="turbine")
p_neg1 = []
for i in range(10):
    p_neg1.append(simulations_neg1[f"simneg1_{i*10}_10"].read_turb_power("all", turb = 1)[-1])
u_inf_neg1 = []
for i in range(10):
    u_inf_neg1.append(simulations_neg1[f"simneg1_{i*10}_10"].slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values)
cp_neg1 = []
for i in range(10):
    cp_neg1.append(p_neg1[i]/(0.5*(np.pi/4)*(u_inf_neg1[i]**3)))
ud_neg1 = []
for i in range(10):
    ud_neg1.append(simulations_neg1[f"simneg1_{i*10}_10"].read_turb_uvel("all", steady = False)[-1])
t_neg1 = []
for i in range(10):
    t_neg1.append(2*(np.pi/4)*(ud_neg1[i])*(u_inf_neg1[i]-ud_neg1[i]))
ct_neg1 = []
for i in range(10):
    ct_neg1.append(t_neg1[i]/(0.5*(np.pi/4)*(u_inf_neg1[i]**2)))
#Export to .npy
np.save("cp_neg1.npy", cp_neg1)
np.save("ct_neg1.npy", ct_neg1)