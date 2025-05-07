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

#Data Path/Folder Stuff
data_path = Path(au.DATA_PATH)

#Change these with each sim
#Change these in each sim
#Uncorrected
sim1_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/B_0000_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/B_0000_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/B_0000_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/B_0000_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0004")
sim5 = pio.BudgetIO("Data/B_0000_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0005")
sim6 = pio.BudgetIO("Data/B_0000_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0006")
sim7 = pio.BudgetIO("Data/B_0000_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0007")
sim8 = pio.BudgetIO("Data/B_0000_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0008")
sim9 = pio.BudgetIO("Data/B_0000_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0009")
sim10 = pio.BudgetIO("Data/B_0000_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0010")
sim11 = pio.BudgetIO("Data/B_0000_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0011")
sim12 = pio.BudgetIO("Data/B_0000_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0012")
sim13 = pio.BudgetIO("Data/B_0000_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0013")
sim14 = pio.BudgetIO("Data/B_0000_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0014")
sim15 = pio.BudgetIO("Data/B_0000_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0015")
sim16 = pio.BudgetIO("Data/B_0000_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0016")
sim17 = pio.BudgetIO("Data/B_0000_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Corrected
sim1_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0000")
sim1_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0001")
sim2_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0002")
sim3_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_cor = os.path.join(au.DATA_PATH, "B_0010_Files/Sim_0003")
sim4_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0004")
sim5_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0005")
sim6_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0006")
sim7_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0007")
sim8_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0008")
sim9_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0009")
sim10_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0010")
sim11_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0011")
sim12_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0012")
sim13_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0013")
sim14_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0014")
sim15_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0015")
sim16_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0016")
sim17_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Prime Values
Ctprime1 = sim1.ta[0].ct
Ctprime2 = sim2.ta[0].ct
Ctprime3 = sim3.ta[0].ct
Ctprime4 = sim4.ta[0].ct
Ctprime5 = sim5.ta[0].ct
Ctprime6 = sim6.ta[0].ct
Ctprime7 = sim7.ta[0].ct
Ctprime8 = sim8.ta[0].ct
Ctprime9 = sim9.ta[0].ct
Ctprime10 = sim10.ta[0].ct
Ctprime11 = sim11.ta[0].ct
Ctprime12 = sim12.ta[0].ct
Ctprime13 = sim13.ta[0].ct
Ctprime14 = sim14.ta[0].ct
Ctprime15 = sim15.ta[0].ct
Ctprime16 = sim16.ta[0].ct
Ctprime17 = sim17.ta[0].ct

#Turbine Power
#Uncorrected
p_les1 = sim1.read_turb_power("all", turb =1)[-1]
p_les2 = sim2.read_turb_power("all", turb =1)[-1]
p_les3 = sim3.read_turb_power("all", turb =1)[-1]
p_les4 = sim4.read_turb_power("all", turb =1)[-1]
p_les5 = sim5.read_turb_power("all", turb =1)[-1]
p_les6 = sim6.read_turb_power("all", turb =1)[-1]
p_les7 = sim7.read_turb_power("all", turb =1)[-1]
p_les8 = sim8.read_turb_power("all", turb =1)[-1]
p_les9 = sim9.read_turb_power("all", turb =1)[-1]
p_les10 = sim10.read_turb_power("all", turb =1)[-1]
p_les11 = sim11.read_turb_power("all", turb =1)[-1]
p_les12 = sim12.read_turb_power("all", turb =1)[-1]
p_les13 = sim13.read_turb_power("all", turb =1)[-1]
p_les14 = sim14.read_turb_power("all", turb =1)[-1]
p_les15 = sim15.read_turb_power("all", turb =1)[-1]
p_les16 = sim16.read_turb_power("all", turb =1)[-1]
p_les17 = sim17.read_turb_power("all", turb =1)[-1]

#Corrected
p_les1_cor = sim1_cor.read_turb_power("all", turb = 1)[-1]
p_les2_cor = sim2_cor.read_turb_power("all", turb = 1)[-1]
p_les3_cor = sim3_cor.read_turb_power("all", turb = 1)[-1]
p_les4_cor = sim4_cor.read_turb_power("all", turb = 1)[-1]
p_les5_cor = sim5_cor.read_turb_power("all", turb = 1)[-1]
p_les6_cor = sim6_cor.read_turb_power("all", turb = 1)[-1]
p_les7_cor = sim7_cor.read_turb_power("all", turb = 1)[-1]
p_les8_cor = sim8_cor.read_turb_power("all", turb = 1)[-1]
p_les9_cor = sim9_cor.read_turb_power("all", turb = 1)[-1]
p_les10_cor = sim10_cor.read_turb_power("all", turb = 1)[-1]
p_les11_cor = sim11_cor.read_turb_power("all", turb = 1)[-1]
p_les12_cor = sim12_cor.read_turb_power("all", turb = 1)[-1]
p_les13_cor = sim13_cor.read_turb_power("all", turb = 1)[-1]
p_les14_cor = sim14_cor.read_turb_power("all", turb = 1)[-1]
p_les15_cor = sim15_cor.read_turb_power("all", turb = 1)[-1]
p_les16_cor = sim16_cor.read_turb_power("all", turb = 1)[-1]
p_les17_cor = sim17_cor.read_turb_power("all", turb = 1)[-1]

# Free Stream Velocities
# Uncorrected
u_inf1 = sim1.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2 = sim2.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3 = sim3.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4 = sim4.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5 = sim5.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6 = sim6.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7 = sim7.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8 = sim8.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9 = sim9.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10 = sim10.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11 = sim11.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12 = sim12.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13 = sim13.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14 = sim14.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15 = sim15.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16 = sim16.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17 = sim17.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Corrected
u_inf1_cor = sim1_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_cor = sim2_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_cor = sim3_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_cor = sim4_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_cor = sim5_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_cor = sim6_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_cor = sim7_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_cor = sim8_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_cor = sim9_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_cor = sim10_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_cor = sim11_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_cor = sim12_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_cor = sim13_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_cor = sim14_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_cor = sim15_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_cor = sim16_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_cor = sim17_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Power Coefficients
#Uncorrected
cp_les1 = p_les1 / (0.5*(np.pi/4)*(u_inf1**3))
cp_les2 = p_les2 / (0.5*(np.pi/4)*(u_inf2**3))
cp_les3 = p_les3 / (0.5*(np.pi/4)*(u_inf3**3))
cp_les4 = p_les4 / (0.5*(np.pi/4)*(u_inf4**3))
cp_les5 = p_les5 / (0.5*(np.pi/4)*(u_inf5**3))
cp_les6 = p_les6 / (0.5*(np.pi/4)*(u_inf6**3))
cp_les7 = p_les7 / (0.5*(np.pi/4)*(u_inf7**3))
cp_les8 = p_les8 / (0.5*(np.pi/4)*(u_inf8**3))
cp_les9 = p_les9 / (0.5*(np.pi/4)*(u_inf9**3))
cp_les10 = p_les10 / (0.5*(np.pi/4)*(u_inf10**3))
cp_les11 = p_les11 / (0.5*(np.pi/4)*(u_inf11**3))
cp_les12 = p_les12 / (0.5*(np.pi/4)*(u_inf12**3))
cp_les13 = p_les13 / (0.5*(np.pi/4)*(u_inf13**3))
cp_les14 = p_les14 / (0.5*(np.pi/4)*(u_inf14**3))
cp_les15 = p_les15 / (0.5*(np.pi/4)*(u_inf15**3))
cp_les16 = p_les16 / (0.5*(np.pi/4)*(u_inf16**3))
cp_les17 = p_les17 / (0.5*(np.pi/4)*(u_inf17**3))

# Correcteed
cp_les1_cor = p_les1_cor / (0.5*(np.pi/4)*(u_inf1_cor**3))
cp_les2_cor = p_les2_cor / (0.5*(np.pi/4)*(u_inf2_cor**3))
cp_les3_cor = p_les3_cor / (0.5*(np.pi/4)*(u_inf3_cor**3))
cp_les4_cor = p_les4_cor / (0.5*(np.pi/4)*(u_inf4_cor**3))
cp_les5_cor = p_les5_cor / (0.5*(np.pi/4)*(u_inf5_cor**3))
cp_les6_cor = p_les6_cor / (0.5*(np.pi/4)*(u_inf6_cor**3))
cp_les7_cor = p_les7_cor / (0.5*(np.pi/4)*(u_inf7_cor**3))
cp_les8_cor = p_les8_cor / (0.5*(np.pi/4)*(u_inf8_cor**3))
cp_les9_cor = p_les9_cor / (0.5*(np.pi/4)*(u_inf9_cor**3))
cp_les10_cor = p_les10_cor / (0.5*(np.pi/4)*(u_inf10_cor**3))
cp_les11_cor = p_les11_cor / (0.5*(np.pi/4)*(u_inf11_cor**3))
cp_les12_cor = p_les12_cor / (0.5*(np.pi/4)*(u_inf12_cor**3))
cp_les13_cor = p_les13_cor / (0.5*(np.pi/4)*(u_inf13_cor**3))
cp_les14_cor = p_les14_cor / (0.5*(np.pi/4)*(u_inf14_cor**3))
cp_les15_cor = p_les15_cor / (0.5*(np.pi/4)*(u_inf15_cor**3))
cp_les16_cor = p_les16_cor / (0.5*(np.pi/4)*(u_inf16_cor**3))
cp_les17_cor = p_les17_cor / (0.5*(np.pi/4)*(u_inf17_cor**3))

#Disk Velocities
#Uncorrected
ud_les1 = sim1.read_turb_uvel("all", steady = False)
ud_les1 = ud_les1[-1]
ud_les2 = sim2.read_turb_uvel("all", steady = False)
ud_les2 = ud_les2[-1]
ud_les3 = sim3.read_turb_uvel("all", steady = False)
ud_les3 = ud_les3[-1]
ud_les4 = sim4.read_turb_uvel("all", steady = False)
ud_les4 = ud_les4[-1]
ud_les5 = sim5.read_turb_uvel("all", steady = False)
ud_les5 = ud_les5[-1]
ud_les6 = sim6.read_turb_uvel("all", steady = False)
ud_les6 = ud_les6[-1]
ud_les7 = sim7.read_turb_uvel("all", steady = False)
ud_les7 = ud_les7[-1]
ud_les8 = sim8.read_turb_uvel("all", steady = False)
ud_les8 = ud_les8[-1]
ud_les9 = sim9.read_turb_uvel("all", steady = False)
ud_les9 = ud_les9[-1]
ud_les10 = sim10.read_turb_uvel("all", steady = False)
ud_les10 = ud_les10[-1]
ud_les11 = sim11.read_turb_uvel("all", steady = False)
ud_les11 = ud_les11[-1]
ud_les12 = sim12.read_turb_uvel("all", steady = False)
ud_les12 = ud_les12[-1]
ud_les13 = sim13.read_turb_uvel("all", steady = False)
ud_les13 = ud_les13[-1]
ud_les14 = sim14.read_turb_uvel("all", steady = False)
ud_les14 = ud_les14[-1]
ud_les15 = sim15.read_turb_uvel("all", steady = False)
ud_les15 = ud_les15[-1]
ud_les16 = sim16.read_turb_uvel("all", steady = False)
ud_les16 = ud_les16[-1]
ud_les17 = sim17.read_turb_uvel("all", steady = False)
ud_les17 = ud_les17[-1]

#Corrected
ud_les1_cor = sim1_cor.read_turb_uvel("all", steady = False)
ud_les1_cor = ud_les1_cor[-1]
ud_les2_cor = sim2_cor.read_turb_uvel("all", steady = False)
ud_les2_cor = ud_les2_cor[-1]
ud_les3_cor = sim3_cor.read_turb_uvel("all", steady = False)
ud_les3_cor = ud_les3_cor[-1]
ud_les4_cor = sim4_cor.read_turb_uvel("all", steady = False)
ud_les4_cor = ud_les4_cor[-1]
ud_les5_cor = sim5_cor.read_turb_uvel("all", steady = False)
ud_les5_cor = ud_les5_cor[-1]
ud_les6_cor = sim6_cor.read_turb_uvel("all", steady = False)
ud_les6_cor = ud_les6_cor[-1]
ud_les7_cor = sim7_cor.read_turb_uvel("all", steady = False)
ud_les7_cor = ud_les7_cor[-1]
ud_les8_cor = sim8_cor.read_turb_uvel("all", steady = False)
ud_les8_cor = ud_les8_cor[-1]
ud_les9_cor = sim9_cor.read_turb_uvel("all", steady = False)
ud_les9_cor = ud_les9_cor[-1]
ud_les10_cor = sim10_cor.read_turb_uvel("all", steady = False)
ud_les10_cor = ud_les10_cor[-1]
ud_les11_cor = sim11_cor.read_turb_uvel("all", steady = False)
ud_les11_cor = ud_les11_cor[-1]
ud_les12_cor = sim12_cor.read_turb_uvel("all", steady = False)
ud_les12_cor = ud_les12_cor[-1]
ud_les13_cor = sim13_cor.read_turb_uvel("all", steady = False)
ud_les13_cor = ud_les13_cor[-1]
ud_les14_cor = sim14_cor.read_turb_uvel("all", steady = False)
ud_les14_cor = ud_les14_cor[-1]
ud_les15_cor = sim15_cor.read_turb_uvel("all", steady = False)
ud_les15_cor = ud_les15_cor[-1]
ud_les16_cor = sim16_cor.read_turb_uvel("all", steady = False)
ud_les16_cor = ud_les16_cor[-1]
ud_les17_cor = sim17_cor.read_turb_uvel("all", steady = False)
ud_les17_cor = ud_les17_cor[-1]

#Thrust Force 
#Uncorrected
thrust_les1 = 2*(np.pi/4)*(ud_les1)*(u_inf1 - ud_les1)
thrust_les2 = 2*(np.pi/4)*(ud_les2)*(u_inf2 - ud_les2)
thrust_les3 = 2*(np.pi/4)*(ud_les3)*(u_inf3 - ud_les3)
thrust_les4 = 2*(np.pi/4)*(ud_les4)*(u_inf4 - ud_les4)
thrust_les5 = 2*(np.pi/4)*(ud_les5)*(u_inf5 - ud_les5)
thrust_les6 = 2*(np.pi/4)*(ud_les6)*(u_inf6 - ud_les6)
thrust_les7 = 2*(np.pi/4)*(ud_les7)*(u_inf7 - ud_les7)
thrust_les8 = 2*(np.pi/4)*(ud_les8)*(u_inf8 - ud_les8)
thrust_les9 = 2*(np.pi/4)*(ud_les9)*(u_inf9 - ud_les9)
thrust_les10 = 2*(np.pi/4)*(ud_les10)*(u_inf10 - ud_les10)
thrust_les11 = 2*(np.pi/4)*(ud_les11)*(u_inf11 - ud_les11)
thrust_les12 = 2*(np.pi/4)*(ud_les12)*(u_inf12 - ud_les12)
thrust_les13 = 2*(np.pi/4)*(ud_les13)*(u_inf13 - ud_les13)
thrust_les14 = 2*(np.pi/4)*(ud_les14)*(u_inf14 - ud_les14)
thrust_les15 = 2*(np.pi/4)*(ud_les15)*(u_inf15 - ud_les15)
thrust_les16 = 2*(np.pi/4)*(ud_les16)*(u_inf16 - ud_les16)
thrust_les17 = 2*(np.pi/4)*(ud_les17)*(u_inf17 - ud_les17)

#Corrected
thrust_les1_cor = 2*(np.pi/4)*(ud_les1_cor)*(u_inf1_cor - ud_les1_cor)
thrust_les2_cor = 2*(np.pi/4)*(ud_les2_cor)*(u_inf2_cor - ud_les2_cor)
thrust_les3_cor = 2*(np.pi/4)*(ud_les3_cor)*(u_inf3_cor - ud_les3_cor)
thrust_les4_cor = 2*(np.pi/4)*(ud_les4_cor)*(u_inf4_cor - ud_les4_cor)
thrust_les5_cor = 2*(np.pi/4)*(ud_les5_cor)*(u_inf5_cor - ud_les5_cor)
thrust_les6_cor = 2*(np.pi/4)*(ud_les6_cor)*(u_inf6_cor - ud_les6_cor)
thrust_les7_cor = 2*(np.pi/4)*(ud_les7_cor)*(u_inf7_cor - ud_les7_cor)
thrust_les8_cor = 2*(np.pi/4)*(ud_les8_cor)*(u_inf8_cor - ud_les8_cor)
thrust_les9_cor = 2*(np.pi/4)*(ud_les9_cor)*(u_inf9_cor - ud_les9_cor)
thrust_les10_cor = 2*(np.pi/4)*(ud_les10_cor)*(u_inf10_cor - ud_les10_cor)
thrust_les11_cor = 2*(np.pi/4)*(ud_les11_cor)*(u_inf11_cor - ud_les11_cor)
thrust_les12_cor = 2*(np.pi/4)*(ud_les12_cor)*(u_inf12_cor - ud_les12_cor)
thrust_les13_cor = 2*(np.pi/4)*(ud_les13_cor)*(u_inf13_cor - ud_les13_cor)
thrust_les14_cor = 2*(np.pi/4)*(ud_les14_cor)*(u_inf14_cor - ud_les14_cor)
thrust_les15_cor = 2*(np.pi/4)*(ud_les15_cor)*(u_inf15_cor - ud_les15_cor)
thrust_les16_cor = 2*(np.pi/4)*(ud_les16_cor)*(u_inf16_cor - ud_les16_cor)
thrust_les17_cor = 2*(np.pi/4)*(ud_les17_cor)*(u_inf17_cor - ud_les17_cor)

#Ct
#Uncorrected
ct_les1 = thrust_les1/(0.5*(np.pi/4)*(u_inf1**2))
ct_les2 = thrust_les2/(0.5*(np.pi/4)*(u_inf2**2))
ct_les3 = thrust_les3/(0.5*(np.pi/4)*(u_inf3**2))
ct_les4 = thrust_les4/(0.5*(np.pi/4)*(u_inf4**2))
ct_les5 = thrust_les5/(0.5*(np.pi/4)*(u_inf5**2))
ct_les6 = thrust_les6/(0.5*(np.pi/4)*(u_inf6**2))
ct_les7 = thrust_les7/(0.5*(np.pi/4)*(u_inf7**2))
ct_les8 = thrust_les8/(0.5*(np.pi/4)*(u_inf8**2))
ct_les9 = thrust_les9/(0.5*(np.pi/4)*(u_inf9**2))
ct_les10 = thrust_les10/(0.5*(np.pi/4)*(u_inf10**2))
ct_les11 = thrust_les11/(0.5*(np.pi/4)*(u_inf11**2))
ct_les12 = thrust_les12/(0.5*(np.pi/4)*(u_inf12**2))
ct_les13 = thrust_les13/(0.5*(np.pi/4)*(u_inf13**2))
ct_les14 = thrust_les14/(0.5*(np.pi/4)*(u_inf14**2))
ct_les15 = thrust_les15/(0.5*(np.pi/4)*(u_inf15**2))
ct_les16 = thrust_les16/(0.5*(np.pi/4)*(u_inf16**2))
ct_les17 = thrust_les17/(0.5*(np.pi/4)*(u_inf17**2))

#Corrected
ct_les1_cor = thrust_les1_cor/(0.5*(np.pi/4)*(u_inf1_cor**2))
ct_les2_cor = thrust_les2_cor/(0.5*(np.pi/4)*(u_inf2_cor**2))
ct_les3_cor = thrust_les3_cor/(0.5*(np.pi/4)*(u_inf3_cor**2))
ct_les4_cor = thrust_les4_cor/(0.5*(np.pi/4)*(u_inf4_cor**2))
ct_les5_cor = thrust_les5_cor/(0.5*(np.pi/4)*(u_inf5_cor**2))
ct_les6_cor = thrust_les6_cor/(0.5*(np.pi/4)*(u_inf6_cor**2))
ct_les7_cor = thrust_les7_cor/(0.5*(np.pi/4)*(u_inf7_cor**2))
ct_les8_cor = thrust_les8_cor/(0.5*(np.pi/4)*(u_inf8_cor**2))
ct_les9_cor = thrust_les9_cor/(0.5*(np.pi/4)*(u_inf9_cor**2))
ct_les10_cor = thrust_les10_cor/(0.5*(np.pi/4)*(u_inf10_cor**2))
ct_les11_cor = thrust_les11_cor/(0.5*(np.pi/4)*(u_inf11_cor**2))
ct_les12_cor = thrust_les12_cor/(0.5*(np.pi/4)*(u_inf12_cor**2))
ct_les13_cor = thrust_les13_cor/(0.5*(np.pi/4)*(u_inf13_cor**2))
ct_les14_cor = thrust_les14_cor/(0.5*(np.pi/4)*(u_inf14_cor**2))
ct_les15_cor = thrust_les15_cor/(0.5*(np.pi/4)*(u_inf15_cor**2))
ct_les16_cor = thrust_les16_cor/(0.5*(np.pi/4)*(u_inf16_cor**2))
ct_les17_cor = thrust_les17_cor/(0.5*(np.pi/4)*(u_inf17_cor**2))

#Induction Factors
#Uncorrected
a_les1 = 1-np.cbrt((p_les1/(0.5*(np.pi/4)*Ctprime1)))
a_les2 = 1-np.cbrt((p_les2/(0.5*(np.pi/4)*Ctprime2)))
a_les3 = 1-np.cbrt((p_les3/(0.5*(np.pi/4)*Ctprime3)))
a_les4 = 1-np.cbrt((p_les4/(0.5*(np.pi/4)*Ctprime4)))
a_les5 = 1-np.cbrt((p_les5/(0.5*(np.pi/4)*Ctprime5)))
a_les6 = 1-np.cbrt((p_les6/(0.5*(np.pi/4)*Ctprime6)))
a_les7 = 1-np.cbrt((p_les7/(0.5*(np.pi/4)*Ctprime7)))
a_les8 = 1-np.cbrt((p_les8/(0.5*(np.pi/4)*Ctprime8)))
a_les9 = 1-np.cbrt((p_les9/(0.5*(np.pi/4)*Ctprime9)))
a_les10 = 1-np.cbrt((p_les10/(0.5*(np.pi/4)*Ctprime10)))
a_les11 = 1-np.cbrt((p_les11/(0.5*(np.pi/4)*Ctprime11)))
a_les12 = 1-np.cbrt((p_les12/(0.5*(np.pi/4)*Ctprime12)))
a_les13 = 1-np.cbrt((p_les13/(0.5*(np.pi/4)*Ctprime13)))
a_les14 = 1-np.cbrt((p_les14/(0.5*(np.pi/4)*Ctprime14)))
a_les15 = 1-np.cbrt((p_les15/(0.5*(np.pi/4)*Ctprime15)))
a_les16 = 1-np.cbrt((p_les16/(0.5*(np.pi/4)*Ctprime16)))
a_les17 = 1-np.cbrt((p_les17/(0.5*(np.pi/4)*Ctprime17)))

#Corrected
a_les1_cor = 1-np.cbrt((p_les1_cor/(0.5*(np.pi/4)*Ctprime1)))
a_les2_cor = 1-np.cbrt((p_les2_cor/(0.5*(np.pi/4)*Ctprime2)))
a_les3_cor = 1-np.cbrt((p_les3_cor/(0.5*(np.pi/4)*Ctprime3)))
a_les4_cor = 1-np.cbrt((p_les4_cor/(0.5*(np.pi/4)*Ctprime4)))
a_les5_cor = 1-np.cbrt((p_les5_cor/(0.5*(np.pi/4)*Ctprime5)))
a_les6_cor = 1-np.cbrt((p_les6_cor/(0.5*(np.pi/4)*Ctprime6)))
a_les7_cor = 1-np.cbrt((p_les7_cor/(0.5*(np.pi/4)*Ctprime7)))
a_les8_cor = 1-np.cbrt((p_les8_cor/(0.5*(np.pi/4)*Ctprime8)))
a_les9_cor = 1-np.cbrt((p_les9_cor/(0.5*(np.pi/4)*Ctprime9)))
a_les10_cor = 1-np.cbrt((p_les10_cor/(0.5*(np.pi/4)*Ctprime10)))
a_les11_cor = 1-np.cbrt((p_les11_cor/(0.5*(np.pi/4)*Ctprime11)))
a_les12_cor = 1-np.cbrt((p_les12_cor/(0.5*(np.pi/4)*Ctprime12)))
a_les13_cor = 1-np.cbrt((p_les13_cor/(0.5*(np.pi/4)*Ctprime13)))
a_les14_cor = 1-np.cbrt((p_les14_cor/(0.5*(np.pi/4)*Ctprime14)))
a_les15_cor = 1-np.cbrt((p_les15_cor/(0.5*(np.pi/4)*Ctprime15)))
a_les16_cor = 1-np.cbrt((p_les16_cor/(0.5*(np.pi/4)*Ctprime16)))
a_les17_cor = 1-np.cbrt((p_les17_cor/(0.5*(np.pi/4)*Ctprime17)))

#Array for Theory Compare
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]

#Momentum Theory Values
#a
a_t = []
for i in range (17):
  if Ctprime_plot[i] == -4:
     a_t.append(0)
  else:
     a_t.append(Ctprime_plot[i]/(4+Ctprime_plot[i]))

#Cp
cp_t = []
for i in range(17):
   cp_t.append(4*a_t[i]*((1-a_t[i])**2))

#Ct
ct_t = []
for i in range(17):
   ct_t.append(Ctprime_plot[i]*((1-a_t[i])**2))

#Glauert Model
#Uncorrected V'
u_inf_block1 = u_inf1*((ud_les1/u_inf1)**2 + (ct_les1/4))/(ud_les1/u_inf1)
u_inf_block2 = u_inf2*((ud_les2/u_inf2)**2 + (ct_les2/4))/(ud_les2/u_inf2)
u_inf_block3 = u_inf3*((ud_les3/u_inf3)**2 + (ct_les3/4))/(ud_les3/u_inf3)
u_inf_block4 = u_inf4*((ud_les4/u_inf4)**2 + (ct_les4/4))/(ud_les4/u_inf4)
u_inf_block5 = u_inf5*((ud_les5/u_inf5)**2 + (ct_les5/4))/(ud_les5/u_inf5)
u_inf_block6 = u_inf6*((ud_les6/u_inf6)**2 + (ct_les6/4))/(ud_les6/u_inf6)
u_inf_block7 = u_inf7*((ud_les7/u_inf7)**2 + (ct_les7/4))/(ud_les7/u_inf7)
u_inf_block8 = u_inf8*((ud_les8/u_inf8)**2 + (ct_les8/4))/(ud_les8/u_inf8)
u_inf_block9 = u_inf9*((ud_les9/u_inf9)**2 + (ct_les9/4))/(ud_les9/u_inf9)
u_inf_block10 = u_inf10*((ud_les10/u_inf10)**2 + (ct_les10/4))/(ud_les10/u_inf10)
u_inf_block11 = u_inf11*((ud_les11/u_inf11)**2 + (ct_les11/4))/(ud_les11/u_inf11)
u_inf_block12 = u_inf12*((ud_les12/u_inf12)**2 + (ct_les12/4))/(ud_les12/u_inf12)
u_inf_block13 = u_inf13*((ud_les13/u_inf13)**2 + (ct_les13/4))/(ud_les13/u_inf13)
u_inf_block14 = u_inf14*((ud_les14/u_inf14)**2 + (ct_les14/4))/(ud_les14/u_inf14)
u_inf_block15 = u_inf15*((ud_les15/u_inf15)**2 + (ct_les15/4))/(ud_les15/u_inf15)
u_inf_block16 = u_inf16*((ud_les16/u_inf16)**2 + (ct_les16/4))/(ud_les16/u_inf16)

#Corrected V'
u_inf_block1_cor = u_inf1_cor*((ud_les1_cor/u_inf1_cor)**2 + (ct_les1_cor/4))/(ud_les1_cor/u_inf1_cor)
u_inf_block2_cor = u_inf2_cor*((ud_les2_cor/u_inf2_cor)**2 + (ct_les2_cor/4))/(ud_les2_cor/u_inf2_cor)
u_inf_block3_cor = u_inf3_cor*((ud_les3_cor/u_inf3_cor)**2 + (ct_les3_cor/4))/(ud_les3_cor/u_inf3_cor)
u_inf_block4_cor = u_inf4_cor*((ud_les4_cor/u_inf4_cor)**2 + (ct_les4_cor/4))/(ud_les4_cor/u_inf4_cor)
u_inf_block5_cor = u_inf5_cor*((ud_les5_cor/u_inf5_cor)**2 + (ct_les5_cor/4))/(ud_les5_cor/u_inf5_cor)
u_inf_block6_cor = u_inf6_cor*((ud_les6_cor/u_inf6_cor)**2 + (ct_les6_cor/4))/(ud_les6_cor/u_inf6_cor)
u_inf_block7_cor = u_inf7_cor*((ud_les7_cor/u_inf7_cor)**2 + (ct_les7_cor/4))/(ud_les7_cor/u_inf7_cor)
u_inf_block8_cor = u_inf8_cor*((ud_les8_cor/u_inf8_cor)**2 + (ct_les8_cor/4))/(ud_les8_cor/u_inf8_cor)
u_inf_block9_cor = u_inf9_cor*((ud_les9_cor/u_inf9_cor)**2 + (ct_les9_cor/4))/(ud_les9_cor/u_inf9_cor)
u_inf_block10_cor = u_inf10_cor*((ud_les10_cor/u_inf10_cor)**2 + (ct_les10_cor/4))/(ud_les10_cor/u_inf10_cor)
u_inf_block11_cor = u_inf11_cor*((ud_les11_cor/u_inf11_cor)**2 + (ct_les11_cor/4))/(ud_les11_cor/u_inf11_cor)
u_inf_block12_cor = u_inf12_cor*((ud_les12_cor/u_inf12_cor)**2 + (ct_les12_cor/4))/(ud_les12_cor/u_inf12_cor)
u_inf_block13_cor = u_inf13_cor*((ud_les13_cor/u_inf13_cor)**2 + (ct_les13_cor/4))/(ud_les13_cor/u_inf13_cor)
u_inf_block14_cor = u_inf14_cor*((ud_les14_cor/u_inf14_cor)**2 + (ct_les14_cor/4))/(ud_les14_cor/u_inf14_cor)
u_inf_block15_cor = u_inf15_cor*((ud_les15_cor/u_inf15_cor)**2 + (ct_les15_cor/4))/(ud_les15_cor/u_inf15_cor)
u_inf_block16_cor = u_inf16_cor*((ud_les16_cor/u_inf16_cor)**2 + (ct_les16_cor/4))/(ud_les16_cor/u_inf16_cor)

#Blockage Corrected Thery Values
#Cp
#Uncorrected
cp_block1 = cp_les1*((u_inf1/u_inf_block1)**3)
cp_block2 = cp_les2*((u_inf2/u_inf_block2)**3)
cp_block3 = cp_les3*((u_inf3/u_inf_block3)**3)
cp_block4 = cp_les4*((u_inf4/u_inf_block4)**3)
cp_block5 = cp_les5*((u_inf5/u_inf_block5)**3)
cp_block6 = cp_les6*((u_inf6/u_inf_block6)**3)
cp_block7 = cp_les7*((u_inf7/u_inf_block7)**3)
cp_block8 = cp_les8*((u_inf8/u_inf_block8)**3)
cp_block9 = cp_les9*((u_inf9/u_inf_block9)**3)
cp_block10 = cp_les10*((u_inf10/u_inf_block10)**3)
cp_block11 = cp_les11*((u_inf11/u_inf_block11)**3)
cp_block12 = cp_les12*((u_inf12/u_inf_block12)**3)
cp_block13 = cp_les13*((u_inf13/u_inf_block13)**3)
cp_block14 = cp_les14*((u_inf14/u_inf_block14)**3)
cp_block15 = cp_les15*((u_inf15/u_inf_block15)**3)
cp_block16 = cp_les16*((u_inf16/u_inf_block16)**3)

#Corrected
cp_block1_cor = cp_les1_cor*((u_inf1_cor/u_inf_block1_cor)**3)
cp_block2_cor = cp_les2_cor*((u_inf2_cor/u_inf_block2_cor)**3)
cp_block3_cor = cp_les3_cor*((u_inf3_cor/u_inf_block3_cor)**3)
cp_block4_cor = cp_les4_cor*((u_inf4_cor/u_inf_block4_cor)**3)
cp_block5_cor = cp_les5_cor*((u_inf5_cor/u_inf_block5_cor)**3)
cp_block6_cor = cp_les6_cor*((u_inf6_cor/u_inf_block6_cor)**3)
cp_block7_cor = cp_les7_cor*((u_inf7_cor/u_inf_block7_cor)**3)
cp_block8_cor = cp_les8_cor*((u_inf8_cor/u_inf_block8_cor)**3)
cp_block9_cor = cp_les9_cor*((u_inf9_cor/u_inf_block9_cor)**3)
cp_block10_cor = cp_les10_cor*((u_inf10_cor/u_inf_block10_cor)**3)
cp_block11_cor = cp_les11_cor*((u_inf11_cor/u_inf_block11_cor)**3)
cp_block12_cor = cp_les12_cor*((u_inf12_cor/u_inf_block12_cor)**3)
cp_block13_cor = cp_les13_cor*((u_inf13_cor/u_inf_block13_cor)**3)
cp_block14_cor = cp_les14_cor*((u_inf14_cor/u_inf_block14_cor)**3)
cp_block15_cor = cp_les15_cor*((u_inf15_cor/u_inf_block15_cor)**3)
cp_block16_cor = cp_les16_cor*((u_inf16_cor/u_inf_block16_cor)**3)

#Ct
#Uncorrected
ct_block1 = ct_les1*((u_inf1/u_inf_block1)**2)
ct_block2 = ct_les2*((u_inf2/u_inf_block2)**2)
ct_block3 = ct_les3*((u_inf3/u_inf_block3)**2)
ct_block4 = ct_les4*((u_inf4/u_inf_block4)**2)
ct_block5 = ct_les5*((u_inf5/u_inf_block5)**2)
ct_block6 = ct_les6*((u_inf6/u_inf_block6)**2)
ct_block7 = ct_les7*((u_inf7/u_inf_block7)**2)
ct_block8 = ct_les8*((u_inf8/u_inf_block8)**2)
ct_block9 = ct_les9*((u_inf9/u_inf_block9)**2)
ct_block10 = ct_les10*((u_inf10/u_inf_block10)**2)
ct_block11 = ct_les11*((u_inf11/u_inf_block11)**2)
ct_block12 = ct_les12*((u_inf12/u_inf_block12)**2)
ct_block13 = ct_les13*((u_inf13/u_inf_block13)**2)
ct_block14 = ct_les14*((u_inf14/u_inf_block14)**2)
ct_block15 = ct_les15*((u_inf15/u_inf_block15)**2)
ct_block16 = ct_les16*((u_inf16/u_inf_block16)**2)

#Corrected
ct_block1_cor = ct_les1_cor*((u_inf1_cor/u_inf_block1_cor)**2)
ct_block2_cor = ct_les2_cor*((u_inf2_cor/u_inf_block2_cor)**2)
ct_block2_cor = ct_les2_cor*((u_inf2_cor/u_inf_block2_cor)**2)
ct_block3_cor = ct_les3_cor*((u_inf3_cor/u_inf_block3_cor)**2)
ct_block4_cor = ct_les4_cor*((u_inf4_cor/u_inf_block4_cor)**2)
ct_block5_cor = ct_les5_cor*((u_inf5_cor/u_inf_block5_cor)**2)
ct_block6_cor = ct_les6_cor*((u_inf6_cor/u_inf_block6_cor)**2)
ct_block7_cor = ct_les7_cor*((u_inf7_cor/u_inf_block7_cor)**2)
ct_block8_cor = ct_les8_cor*((u_inf8_cor/u_inf_block8_cor)**2)
ct_block9_cor = ct_les9_cor*((u_inf9_cor/u_inf_block9_cor)**2)
ct_block10_cor = ct_les10_cor*((u_inf10_cor/u_inf_block10_cor)**2)
ct_block11_cor = ct_les11_cor*((u_inf11_cor/u_inf_block11_cor)**2)
ct_block12_cor = ct_les12_cor*((u_inf12_cor/u_inf_block12_cor)**2)
ct_block13_cor = ct_les13_cor*((u_inf13_cor/u_inf_block13_cor)**2)
ct_block14_cor = ct_les14_cor*((u_inf14_cor/u_inf_block14_cor)**2)
ct_block15_cor = ct_les15_cor*((u_inf15_cor/u_inf_block15_cor)**2)
ct_block16_cor = ct_les16_cor*((u_inf16_cor/u_inf_block16_cor)**2)

#Arrays for Plotting
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]
cp_les_plot = [cp_les1, cp_les2, cp_les3, cp_les4, cp_les5, cp_les6, cp_les7, cp_les8, cp_les9, cp_les10, cp_les11, cp_les12, cp_les13, cp_les14, cp_les15, cp_les16, cp_les17]
cp_les_plot_cor = [cp_les1_cor, cp_les2_cor, cp_les3_cor, cp_les4_cor, cp_les5_cor, cp_les6_cor, cp_les7_cor, cp_les8_cor, cp_les9_cor, cp_les10_cor, cp_les11_cor, cp_les12_cor, cp_les13_cor, cp_les14_cor, cp_les15_cor, cp_les16_cor, cp_les17_cor]
cp_block_plot = [ct_block1, ct_block2, ct_block3, ct_block4, ct_block5, ct_block6, ct_block7, ct_block8, ct_block9, ct_block10, ct_block11, ct_block12, ct_block13, ct_block14, ct_block15, ct_block16, ct_block16]
ct_les_plot = [ct_les1, ct_les2, ct_les3, ct_les4, ct_les5, ct_les6, ct_les7, ct_les8, ct_les9, ct_les10, ct_les11, ct_les12, ct_les13, ct_les14, ct_les15, ct_les16, ct_les17]
ct_les_cor_plot = [ct_les1_cor, ct_les2_cor, ct_les3_cor, ct_les4_cor, ct_les5_cor, ct_les6_cor, ct_les7_cor, ct_les8_cor, ct_les9_cor, ct_les10_cor, ct_les11_cor, ct_les12_cor, ct_les13_cor, ct_les14_cor, ct_les15_cor, ct_les16_cor, ct_les17_cor]
ct_block_plot = [ct_block1, ct_block2, ct_block3, ct_block4, ct_block5, ct_block6, ct_block7, ct_block8, ct_block9, ct_block10, ct_block11, ct_block12, ct_block13, ct_block14, ct_block15, ct_block16]
ct_block_cor_plot = [ct_block1_cor, ct_block2_cor, ct_block3_cor, ct_block4_cor, ct_block5_cor, ct_block5_cor, ct_block6_cor, ct_block7_cor, ct_block8_cor, ct_block9_cor, ct_block10_cor, ct_block11_cor, ct_block12_cor, ct_block13_cor, ct_block14_cor, ct_block15_cor, ct_block16_cor]
