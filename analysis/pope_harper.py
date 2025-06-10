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
sim1_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0000")
sim1 = pio.BudgetIO("Data/U_0017_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0001")
sim2 = pio.BudgetIO("Data/U_0017_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0002")
sim3 = pio.BudgetIO("Data/U_0017_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0003")
sim4 = pio.BudgetIO("Data/U_0017_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0004")
sim5 = pio.BudgetIO("Data/U_0017_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0005")
sim6 = pio.BudgetIO("Data/U_0017_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0006")
sim7 = pio.BudgetIO("Data/U_0017_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0007")
sim8 = pio.BudgetIO("Data/U_0017_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0008")
sim9 = pio.BudgetIO("Data/U_0017_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0009")
sim10 = pio.BudgetIO("Data/U_0017_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0010")
sim11 = pio.BudgetIO("Data/U_0017_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0011")
sim12 = pio.BudgetIO("Data/U_0017_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0012")
sim13 = pio.BudgetIO("Data/U_0017_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0013")
sim14 = pio.BudgetIO("Data/U_0017_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0014")
sim15 = pio.BudgetIO("Data/U_0017_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0015")
sim16 = pio.BudgetIO("Data/U_0017_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder = os.path.join(au.DATA_PATH, "U_0017_Files/Sim_0016")
sim17 = pio.BudgetIO("Data/U_0017_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Corrected
sim1_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0000")
sim1_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0001")
sim2_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0002")
sim3_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0003")
sim4_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0004")
sim5_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0005")
sim6_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0006")
sim7_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0007")
sim8_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0008")
sim9_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0009")
sim10_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0010")
sim11_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0011")
sim12_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0012")
sim13_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0013")
sim14_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0014")
sim15_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0015")
sim16_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_cor = os.path.join(au.DATA_PATH, "U_0018_Files/Sim_0016")
sim17_cor = pio.BudgetIO("Data/U_0018_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Medium Blockage, Uncorrected
sim1_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0000")
sim1_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0001")
sim2_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0002")
sim3_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0003")
sim4_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0004")
sim5_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0005")
sim6_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0006")
sim7_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0007")
sim8_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0008")
sim9_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0009")
sim10_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0010")
sim11_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0011")
sim12_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0012")
sim13_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0013")
sim14_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0014")
sim15_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0015")
sim16_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_mblock = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0016")
sim17_mblock = pio.BudgetIO("Data/B_0000_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Primes
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

#Free Stream Velocities
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

#Blockage Amounts
mb = 0.1
hb = 0.35

#Epsilon Values
epsm = 1/(4*mb)
epsh = 1/(4*hb)

#UT/UF Values
ut_uf_m = 1/(1 + epsm)
ut_uf_h = 1/(1 + epsh)

#Cp Prime Values
#Medium Uncorrected
cp_prime1_m = cp_les1*(ut_uf_m**3)
cp_prime2_m = cp_les2*(ut_uf_m**3)
cp_prime3_m = cp_les3*(ut_uf_m**3)
cp_prime4_m = cp_les4*(ut_uf_m**3)
cp_prime5_m = cp_les5*(ut_uf_m**3)
cp_prime6_m = cp_les6*(ut_uf_m**3)
cp_prime7_m = cp_les7*(ut_uf_m**3)
cp_prime8_m = cp_les8*(ut_uf_m**3)
cp_prime9_m = cp_les9*(ut_uf_m**3)
cp_prime10_m = cp_les10*(ut_uf_m**3)
cp_prime11_m = cp_les11*(ut_uf_m**3)
cp_prime12_m = cp_les12*(ut_uf_m**3)
cp_prime13_m = cp_les13*(ut_uf_m**3)
cp_prime14_m = cp_les14*(ut_uf_m**3)
cp_prime15_m = cp_les15*(ut_uf_m**3)
cp_prime16_m = cp_les16*(ut_uf_m**3)
cp_prime17_m = cp_les17*(ut_uf_m**3)

#Medium Corrected
cp_prime1_m_cor = cp_les1_cor*(ut_uf_m**3)
cp_prime2_m_cor = cp_les2_cor*(ut_uf_m**3)
cp_prime3_m_cor = cp_les3_cor*(ut_uf_m**3)
cp_prime4_m_cor = cp_les4_cor*(ut_uf_m**3)
cp_prime5_m_cor = cp_les5_cor*(ut_uf_m**3)
cp_prime6_m_cor = cp_les6_cor*(ut_uf_m**3)
cp_prime7_m_cor = cp_les7_cor*(ut_uf_m**3)
cp_prime8_m_cor = cp_les8_cor*(ut_uf_m**3)
cp_prime9_m_cor = cp_les9_cor*(ut_uf_m**3)
cp_prime10_m_cor = cp_les10_cor*(ut_uf_m**3)
cp_prime11_m_cor = cp_les11_cor*(ut_uf_m**3)
cp_prime12_m_cor = cp_les12_cor*(ut_uf_m**3)
cp_prime13_m_cor = cp_les13_cor*(ut_uf_m**3)
cp_prime14_m_cor = cp_les14_cor*(ut_uf_m**3)
cp_prime15_m_cor = cp_les15_cor*(ut_uf_m**3)
cp_prime16_m_cor = cp_les16_cor*(ut_uf_m**3)
cp_prime17_m_cor = cp_les17_cor*(ut_uf_m**3)

#High Uncorrected
cp_prime1_h = cp_les1*(ut_uf_h**3)
cp_prime2_h = cp_les2*(ut_uf_h**3)
cp_prime3_h = cp_les3*(ut_uf_h**3)
cp_prime4_h = cp_les4*(ut_uf_h**3)
cp_prime5_h = cp_les5*(ut_uf_h**3)
cp_prime6_h = cp_les6*(ut_uf_h**3)
cp_prime7_h = cp_les7*(ut_uf_h**3)
cp_prime8_h = cp_les8*(ut_uf_h**3)
cp_prime9_h = cp_les9*(ut_uf_h**3)
cp_prime10_h = cp_les10*(ut_uf_h**3)
cp_prime11_h = cp_les11*(ut_uf_h**3)
cp_prime12_h = cp_les12*(ut_uf_h**3)
cp_prime13_h = cp_les13*(ut_uf_h**3)
cp_prime14_h = cp_les14*(ut_uf_h**3)
cp_prime15_h = cp_les15*(ut_uf_h**3)
cp_prime16_h = cp_les16*(ut_uf_h**3)
cp_prime17_h = cp_les17*(ut_uf_h**3)

#High Corrected
cp_prime1_h_cor = cp_les1_cor*(ut_uf_h**3)
cp_prime2_h_cor = cp_les2_cor*(ut_uf_h**3)
cp_prime3_h_cor = cp_les3_cor*(ut_uf_h**3)
cp_prime4_h_cor = cp_les4_cor*(ut_uf_h**3)
cp_prime5_h_cor = cp_les5_cor*(ut_uf_h**3)
cp_prime6_h_cor = cp_les6_cor*(ut_uf_h**3)
cp_prime7_h_cor = cp_les7_cor*(ut_uf_h**3)
cp_prime8_h_cor = cp_les8_cor*(ut_uf_h**3)
cp_prime9_h_cor = cp_les9_cor*(ut_uf_h**3)
cp_prime10_h_cor = cp_les10_cor*(ut_uf_h**3)
cp_prime11_h_cor = cp_les11_cor*(ut_uf_h**3)
cp_prime12_h_cor = cp_les12_cor*(ut_uf_h**3)
cp_prime13_h_cor = cp_les13_cor*(ut_uf_h**3)
cp_prime14_h_cor = cp_les14_cor*(ut_uf_h**3)    
cp_prime15_h_cor = cp_les15_cor*(ut_uf_h**3)
cp_prime16_h_cor = cp_les16_cor*(ut_uf_h**3)
cp_prime17_h_cor = cp_les17_cor*(ut_uf_h**3)

#Ct Prime Values
#Medium Uncorrected
ct_prime1_m = ct_les1*(ut_uf_m**2)
ct_prime2_m = ct_les2*(ut_uf_m**2)
ct_prime3_m = ct_les3*(ut_uf_m**2)
ct_prime4_m = ct_les4*(ut_uf_m**2)
ct_prime5_m = ct_les5*(ut_uf_m**2)
ct_prime6_m = ct_les6*(ut_uf_m**2)
ct_prime7_m = ct_les7*(ut_uf_m**2)
ct_prime8_m = ct_les8*(ut_uf_m**2)
ct_prime9_m = ct_les9*(ut_uf_m**2)
ct_prime10_m = ct_les10*(ut_uf_m**2)
ct_prime11_m = ct_les11*(ut_uf_m**2)
ct_prime12_m = ct_les12*(ut_uf_m**2)
ct_prime13_m = ct_les13*(ut_uf_m**2)
ct_prime14_m = ct_les14*(ut_uf_m**2)
ct_prime15_m = ct_les15*(ut_uf_m**2)
ct_prime16_m = ct_les16*(ut_uf_m**2)
ct_prime17_m = ct_les17*(ut_uf_m**2)

#Medium Corrected
ct_prime1_m_cor = ct_les1_cor*(ut_uf_m**2)
ct_prime2_m_cor = ct_les2_cor*(ut_uf_m**2)
ct_prime3_m_cor = ct_les3_cor*(ut_uf_m**2)
ct_prime4_m_cor = ct_les4_cor*(ut_uf_m**2)
ct_prime5_m_cor = ct_les5_cor*(ut_uf_m**2)
ct_prime6_m_cor = ct_les6_cor*(ut_uf_m**2)
ct_prime7_m_cor = ct_les7_cor*(ut_uf_m**2)
ct_prime8_m_cor = ct_les8_cor*(ut_uf_m**2)
ct_prime9_m_cor = ct_les9_cor*(ut_uf_m**2)
ct_prime10_m_cor = ct_les10_cor*(ut_uf_m**2)
ct_prime11_m_cor = ct_les11_cor*(ut_uf_m**2)
ct_prime12_m_cor = ct_les12_cor*(ut_uf_m**2)
ct_prime13_m_cor = ct_les13_cor*(ut_uf_m**2)
ct_prime14_m_cor = ct_les14_cor*(ut_uf_m**2)
ct_prime15_m_cor = ct_les15_cor*(ut_uf_m**2)
ct_prime16_m_cor = ct_les16_cor*(ut_uf_m**2)
ct_prime17_m_cor = ct_les17_cor*(ut_uf_m**2)

#High Uncorrected
ct_prime1_h = ct_les1*(ut_uf_h**2)
ct_prime2_h = ct_les2*(ut_uf_h**2)
ct_prime3_h = ct_les3*(ut_uf_h**2)
ct_prime4_h = ct_les4*(ut_uf_h**2)
ct_prime5_h = ct_les5*(ut_uf_h**2)
ct_prime6_h = ct_les6*(ut_uf_h**2)
ct_prime7_h = ct_les7*(ut_uf_h**2)
ct_prime8_h = ct_les8*(ut_uf_h**2)
ct_prime9_h = ct_les9*(ut_uf_h**2)
ct_prime10_h = ct_les10*(ut_uf_h**2)
ct_prime11_h = ct_les11*(ut_uf_h**2)
ct_prime12_h = ct_les12*(ut_uf_h**2)
ct_prime13_h = ct_les13*(ut_uf_h**2)
ct_prime14_h = ct_les14*(ut_uf_h**2)
ct_prime15_h = ct_les15*(ut_uf_h**2)
ct_prime16_h = ct_les16*(ut_uf_h**2)
ct_prime17_h = ct_les17*(ut_uf_h**2)

#High Corrected
ct_prime1_h_cor = ct_les1_cor*(ut_uf_h**2)
ct_prime2_h_cor = ct_les2_cor*(ut_uf_h**2)
ct_prime3_h_cor = ct_les3_cor*(ut_uf_h**2)
ct_prime4_h_cor = ct_les4_cor*(ut_uf_h**2)
ct_prime5_h_cor = ct_les5_cor*(ut_uf_h**2)
ct_prime6_h_cor = ct_les6_cor*(ut_uf_h**2)
ct_prime7_h_cor = ct_les7_cor*(ut_uf_h**2)
ct_prime8_h_cor = ct_les8_cor*(ut_uf_h**2)
ct_prime9_h_cor = ct_les9_cor*(ut_uf_h**2)
ct_prime10_h_cor = ct_les10_cor*(ut_uf_h**2)
ct_prime11_h_cor = ct_les11_cor*(ut_uf_h**2)
ct_prime12_h_cor = ct_les12_cor*(ut_uf_h**2)
ct_prime13_h_cor = ct_les13_cor*(ut_uf_h**2)
ct_prime14_h_cor = ct_les14_cor*(ut_uf_h**2)
ct_prime15_h_cor = ct_les15_cor*(ut_uf_h**2)
ct_prime16_h_cor = ct_les16_cor*(ut_uf_h**2)
ct_prime17_h_cor = ct_les17_cor*(ut_uf_h**2)

#Arrays for Plotting/Saving
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]
Cpprime_m = [cp_prime1_m, cp_prime2_m, cp_prime3_m, cp_prime4_m, cp_prime5_m, cp_prime6_m, cp_prime7_m, cp_prime8_m, cp_prime9_m, cp_prime10_m, cp_prime11_m, cp_prime12_m, cp_prime13_m, cp_prime14_m, cp_prime15_m, cp_prime16_m, cp_prime17_m]
Cpprime_m_cor = [cp_prime1_m_cor, cp_prime2_m_cor, cp_prime3_m_cor, cp_prime4_m_cor, cp_prime5_m_cor, cp_prime6_m_cor, cp_prime7_m_cor, cp_prime8_m_cor, cp_prime9_m_cor, cp_prime10_m_cor, cp_prime11_m_cor, cp_prime12_m_cor, cp_prime13_m_cor, cp_prime14_m_cor, cp_prime15_m_cor, cp_prime16_m_cor, cp_prime17_m_cor]
Cpprime_h = [cp_prime1_h, cp_prime2_h, cp_prime3_h, cp_prime4_h, cp_prime5_h, cp_prime6_h, cp_prime7_h, cp_prime8_h, cp_prime9_h, cp_prime10_h, cp_prime11_h, cp_prime12_h, cp_prime13_h, cp_prime14_h, cp_prime15_h, cp_prime16_h, cp_prime17_h]
Cpprime_h_cor = [cp_prime1_h_cor, cp_prime2_h_cor, cp_prime3_h_cor, cp_prime4_h_cor, cp_prime5_h_cor, cp_prime6_h_cor, cp_prime7_h_cor, cp_prime8_h_cor, cp_prime9_h_cor, cp_prime10_h_cor, cp_prime11_h_cor, cp_prime12_h_cor, cp_prime13_h_cor, cp_prime14_h_cor, cp_prime15_h_cor, cp_prime16_h_cor, cp_prime17_h_cor]
ctprime_m = [ct_prime1_m, ct_prime2_m, ct_prime3_m, ct_prime4_m, ct_prime5_m, ct_prime6_m, ct_prime7_m, ct_prime8_m, ct_prime9_m, ct_prime10_m, ct_prime11_m, ct_prime12_m, ct_prime13_m, ct_prime14_m, ct_prime15_m, ct_prime16_m, ct_prime17_m]
ctprime_m_cor = [ct_prime1_m_cor, ct_prime2_m_cor, ct_prime3_m_cor, ct_prime4_m_cor, ct_prime5_m_cor, ct_prime6_m_cor, ct_prime7_m_cor, ct_prime8_m_cor, ct_prime9_m_cor, ct_prime10_m_cor, ct_prime11_m_cor, ct_prime12_m_cor, ct_prime13_m_cor, ct_prime14_m_cor, ct_prime15_m_cor, ct_prime16_m_cor, ct_prime17_m_cor]
ctprime_h = [ct_prime1_h, ct_prime2_h, ct_prime3_h, ct_prime4_h, ct_prime5_h, ct_prime6_h, ct_prime7_h, ct_prime8_h, ct_prime9_h, ct_prime10_h, ct_prime11_h, ct_prime12_h, ct_prime13_h, ct_prime14_h, ct_prime15_h, ct_prime16_h, ct_prime17_h]
ctprime_h_cor = [ct_prime1_h_cor, ct_prime2_h_cor, ct_prime3_h_cor, ct_prime4_h_cor, ct_prime5_h_cor, ct_prime6_h_cor, ct_prime7_h_cor, ct_prime8_h_cor, ct_prime9_h_cor, ct_prime10_h_cor, ct_prime11_h_cor, ct_prime12_h_cor, ct_prime13_h_cor, ct_prime14_h_cor, ct_prime15_h_cor, ct_prime16_h_cor, ct_prime17_h_cor]

#Plotting
#Cp
plt.figure(figsize=(9,6))
plt.scatter(Ctprime_plot[1:16], Cpprime_m[1:16], label='10% Blockage Uncorrected', color='blue', marker='o')
plt.scatter(Ctprime_plot[1:16], Cpprime_m_cor[1:16], label='10% Blockage Corrected', color='orange', marker='o')
plt.scatter(Ctprime_plot[1:16], Cpprime_h[1:16], label='35% Blockage Uncorrected', color='green', marker='o')
plt.scatter(Ctprime_plot[1:16], Cpprime_h_cor[1:16], label='35% Blockage Corrected', color='red', marker='o')
plt.ylim(-1,1)
plt.legend()
plt.xlabel('Ct Prime')
plt.ylabel('Equivalent Unblocked Cp')
plt.title('Emperical Blockage Correction Results (Pope/Harper)')
plt.savefig('./cp_ph')

#Ct
plt.figure(figsize=(9,6))
plt.scatter(Ctprime_plot[1:16], ctprime_m[1:16], label='10% Blockage Uncorrected', color='blue', marker='o')
plt.scatter(Ctprime_plot[1:16], ctprime_m_cor[1:16], label='10% Blockage Corrected', color='orange', marker='o')
plt.scatter(Ctprime_plot[1:16], ctprime_h[1:16], label='35% Blockage Uncorrected', color='green', marker='o')
plt.scatter(Ctprime_plot[1:16], ctprime_h_cor[1:16], label='35% Blockage Corrected', color='red', marker='o')
plt.ylim(-1,1)
plt.legend()
plt.xlabel('Ct Prime')
plt.ylabel('Equivalent Unblocked Ct')
plt.title('Emperical Blockage Correction Results (Pope/Harper)')
plt.savefig('./ct_ph')

#Save Data
np.save('./cp_prime_m_ph', Cpprime_m)
np.save('./cp_prime_m_cor_ph', Cpprime_m_cor)
np.save('./cp_prime_h_ph', Cpprime_h)
np.save('./cp_prime_h_cor_ph', Cpprime_h_cor)
np.save('./ct_prime_m_ph', ctprime_m)
np.save('./ct_prime_m_cor_ph', ctprime_m_cor)
np.save('./ct_prime_h_ph', ctprime_h)
np.save('./ct_prime_h_cor_ph', ctprime_h_cor)


