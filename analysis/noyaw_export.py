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

#Load Data
sim1_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0000")
sim1_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0001")
sim2_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0002")
sim3_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0003")
sim4_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0004")
sim5_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0005")
sim6_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0006")
sim7_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0007")
sim8_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0008")
sim9_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0009")
sim10_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0010")
sim11_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0011")
sim12_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0012")
sim13_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0013")
sim14_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0014")
sim15_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0015")
sim16_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0016")
sim17_mblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

sim1_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0000")
sim1_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0001")
sim2_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0002")
sim3_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0003")
sim4_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0004")
sim5_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0005")
sim6_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0006")
sim7_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0007")
sim8_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0008")
sim9_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0009")
sim10_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0010")
sim11_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0011")
sim12_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0012")
sim13_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_mblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0013")
sim14_hblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0014")
sim15_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0015")
sim16_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0016")
sim17_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Calculate Values
Ctprime1 = sim1_mblock_cor.ta[0].ct
Ctprime2 = sim2_mblock_cor.ta[0].ct
Ctprime3 = sim3_mblock_cor.ta[0].ct
Ctprime4 = sim4_mblock_cor.ta[0].ct
Ctprime5 = sim5_mblock_cor.ta[0].ct
Ctprime6 = sim6_mblock_cor.ta[0].ct
Ctprime7 = sim7_mblock_cor.ta[0].ct
Ctprime8 = sim8_mblock_cor.ta[0].ct
Ctprime9 = sim9_mblock_cor.ta[0].ct
Ctprime10 = sim10_mblock_cor.ta[0].ct
Ctprime11 = sim11_mblock_cor.ta[0].ct
Ctprime12 = sim12_mblock_cor.ta[0].ct
Ctprime13 = sim13_mblock_cor.ta[0].ct
Ctprime14 = sim14_mblock_cor.ta[0].ct
Ctprime15 = sim15_mblock_cor.ta[0].ct
Ctprime16 = sim16_mblock_cor.ta[0].ct
Ctprime17 = sim17_mblock_cor.ta[0].ct

p_les1_mblock_cor = sim1_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les2_mblock_cor = sim2_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les3_mblock_cor = sim3_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les4_mblock_cor = sim4_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les5_mblock_cor = sim5_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les6_mblock_cor = sim6_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les7_mblock_cor = sim7_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les8_mblock_cor = sim8_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les9_mblock_cor = sim9_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les10_mblock_cor = sim10_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les11_mblock_cor = sim11_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les12_mblock_cor = sim12_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les13_mblock_cor = sim13_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les14_mblock_cor = sim14_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les15_mblock_cor = sim15_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les16_mblock_cor = sim16_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les17_mblock_cor = sim17_mblock_cor.read_turb_power("all", turb = 1)[-1]

p_les1_hblock_cor = sim1_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les2_hblock_cor = sim2_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les3_hblock_cor = sim3_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les4_hblock_cor = sim4_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les5_hblock_cor = sim5_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les6_hblock_cor = sim6_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les7_hblock_cor = sim7_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les8_hblock_cor = sim8_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les9_hblock_cor = sim9_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les10_hblock_cor = sim10_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les11_hblock_cor = sim11_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les12_hblock_cor = sim12_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les13_hblock_cor = sim13_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les14_hblock_cor = sim14_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les15_hblock_cor = sim15_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les16_hblock_cor = sim16_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les17_hblock_cor = sim17_hblock_cor.read_turb_power("all", turb = 1)[-1]

u_inf1_mblock_cor = sim1_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf2_mblock_cor = sim2_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf3_mblock_cor = sim3_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf4_mblock_cor = sim4_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf5_mblock_cor = sim5_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf6_mblock_cor = sim6_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf7_mblock_cor = sim7_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf8_mblock_cor = sim8_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf9_mblock_cor = sim9_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf10_mblock_cor = sim10_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf11_mblock_cor = sim11_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf12_mblock_cor = sim12_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf13_mblock_cor = sim13_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf14_mblock_cor = sim14_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf15_mblock_cor = sim15_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf16_mblock_cor = sim16_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf17_mblock_cor = sim17_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

u_inf1_hblock_cor = sim1_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf2_hblock_cor = sim2_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf3_hblock_cor = sim3_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf4_hblock_cor = sim4_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf5_hblock_cor = sim5_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf6_hblock_cor = sim6_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf7_hblock_cor = sim7_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf8_hblock_cor = sim8_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf9_hblock_cor = sim9_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf10_hblock_cor = sim10_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf11_hblock_cor = sim11_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf12_hblock_cor = sim12_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf13_hblock_cor = sim13_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf14_hblock_cor = sim14_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf15_hblock_cor = sim15_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf16_hblock_cor = sim16_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf17_hblock_cor = sim17_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

cp_les1_mblock_cor = p_les1_mblock_cor / (0.5*(np.pi/4)*(u_inf1_mblock_cor**3))
cp_les2_mblock_cor = p_les2_mblock_cor / (0.5*(np.pi/4)*(u_inf2_mblock_cor**3))
cp_les3_mblock_cor = p_les3_mblock_cor / (0.5*(np.pi/4)*(u_inf3_mblock_cor**3))
cp_les4_mblock_cor = p_les4_mblock_cor / (0.5*(np.pi/4)*(u_inf4_mblock_cor**3))
cp_les5_mblock_cor = p_les5_mblock_cor / (0.5*(np.pi/4)*(u_inf5_mblock_cor**3))
cp_les6_mblock_cor = p_les6_mblock_cor / (0.5*(np.pi/4)*(u_inf6_mblock_cor**3))
cp_les7_mblock_cor = p_les7_mblock_cor / (0.5*(np.pi/4)*(u_inf7_mblock_cor**3))
cp_les8_mblock_cor = p_les8_mblock_cor / (0.5*(np.pi/4)*(u_inf8_mblock_cor**3))
cp_les9_mblock_cor = p_les9_mblock_cor / (0.5*(np.pi/4)*(u_inf9_mblock_cor**3))
cp_les10_mblock_cor = p_les10_mblock_cor / (0.5*(np.pi/4)*(u_inf10_mblock_cor**3))
cp_les11_mblock_cor = p_les11_mblock_cor / (0.5*(np.pi/4)*(u_inf11_mblock_cor**3))
cp_les12_mblock_cor = p_les12_mblock_cor / (0.5*(np.pi/4)*(u_inf12_mblock_cor**3))
cp_les13_mblock_cor = p_les13_mblock_cor / (0.5*(np.pi/4)*(u_inf13_mblock_cor**3))
cp_les14_mblock_cor = p_les14_mblock_cor / (0.5*(np.pi/4)*(u_inf14_mblock_cor**3))
cp_les15_mblock_cor = p_les15_mblock_cor / (0.5*(np.pi/4)*(u_inf15_mblock_cor**3))
cp_les16_mblock_cor = p_les16_mblock_cor / (0.5*(np.pi/4)*(u_inf16_mblock_cor**3))
cp_les17_mblock_cor = p_les17_mblock_cor / (0.5*(np.pi/4)*(u_inf17_mblock_cor**3))

cp_les1_hblock_cor = p_les1_hblock_cor / (0.5*(np.pi/4)*(u_inf1_hblock_cor**3))
cp_les2_hblock_cor = p_les2_hblock_cor / (0.5*(np.pi/4)*(u_inf2_hblock_cor**3))
cp_les3_hblock_cor = p_les3_hblock_cor / (0.5*(np.pi/4)*(u_inf3_hblock_cor**3))
cp_les4_hblock_cor = p_les4_hblock_cor / (0.5*(np.pi/4)*(u_inf4_hblock_cor**3))
cp_les5_hblock_cor = p_les5_hblock_cor / (0.5*(np.pi/4)*(u_inf5_hblock_cor**3))
cp_les6_hblock_cor = p_les6_hblock_cor / (0.5*(np.pi/4)*(u_inf6_hblock_cor**3))
cp_les7_hblock_cor = p_les7_hblock_cor / (0.5*(np.pi/4)*(u_inf7_hblock_cor**3))
cp_les8_hblock_cor = p_les8_hblock_cor / (0.5*(np.pi/4)*(u_inf8_hblock_cor**3))
cp_les9_hblock_cor = p_les9_hblock_cor / (0.5*(np.pi/4)*(u_inf9_hblock_cor**3))
cp_les10_hblock_cor = p_les10_hblock_cor / (0.5*(np.pi/4)*(u_inf10_hblock_cor**3))
cp_les11_hblock_cor = p_les11_hblock_cor / (0.5*(np.pi/4)*(u_inf11_hblock_cor**3))
cp_les12_hblock_cor = p_les12_hblock_cor / (0.5*(np.pi/4)*(u_inf12_hblock_cor**3))
cp_les13_hblock_cor = p_les13_hblock_cor / (0.5*(np.pi/4)*(u_inf13_hblock_cor**3))
cp_les14_hblock_cor = p_les14_hblock_cor / (0.5*(np.pi/4)*(u_inf14_hblock_cor**3))
cp_les15_hblock_cor = p_les15_hblock_cor / (0.5*(np.pi/4)*(u_inf15_hblock_cor**3))
cp_les16_hblock_cor = p_les16_hblock_cor / (0.5*(np.pi/4)*(u_inf16_hblock_cor**3))
cp_les17_hblock_cor = p_les17_hblock_cor / (0.5*(np.pi/4)*(u_inf17_hblock_cor**3))

ud_les1_mblock_cor = sim1_mblock_cor.read_turb_uvel("all", steady = False)
ud_les1_block_cor = ud_les1_mblock_cor[-1]
ud_les2_mblock_cor = sim2_mblock_cor.read_turb_uvel("all", steady = False)
ud_les2_mblock_cor = ud_les2_mblock_cor[-1]
ud_les3_mblock_cor = sim3_mblock_cor.read_turb_uvel("all", steady = False)
ud_les3_mblock_cor = ud_les3_mblock_cor[-1]
ud_les4_mblock_cor = sim4_mblock_cor.read_turb_uvel("all", steady = False)
ud_les4_mblock_cor = ud_les4_mblock_cor[-1]
ud_les5_mblock_cor = sim5_mblock_cor.read_turb_uvel("all", steady = False)
ud_les5_mblock_cor = ud_les5_mblock_cor[-1]
ud_les6_mblock_cor = sim6_mblock_cor.read_turb_uvel("all", steady = False)
ud_les6_mblock_cor = ud_les6_mblock_cor[-1]
ud_les7_mblock_cor = sim7_mblock_cor.read_turb_uvel("all", steady = False)
ud_les7_mblock_cor = ud_les7_mblock_cor[-1]
ud_les8_mblock_cor = sim8_mblock_cor.read_turb_uvel("all", steady = False)
ud_les8_mblock_cor = ud_les8_mblock_cor[-1]
ud_les9_mblock_cor = sim9_mblock_cor.read_turb_uvel("all", steady = False)
ud_les9_mblock_cor = ud_les9_mblock_cor[-1]
ud_les10_mblock_cor = sim10_mblock_cor.read_turb_uvel("all", steady = False)
ud_les10_mblock_cor = ud_les10_mblock_cor[-1]
ud_les11_mblock_cor = sim11_mblock_cor.read_turb_uvel("all", steady = False)
ud_les11_mblock_cor = ud_les11_mblock_cor[-1]
ud_les12_mblock_cor = sim12_mblock_cor.read_turb_uvel("all", steady = False)
ud_les12_mblock_cor = ud_les12_mblock_cor[-1]
ud_les13_mblock_cor = sim13_mblock_cor.read_turb_uvel("all", steady = False)
ud_les13_mblock_cor = ud_les13_mblock_cor[-1]
ud_les14_mblock_cor = sim14_mblock_cor.read_turb_uvel("all", steady = False)
ud_les14_mblock_cor = ud_les14_mblock_cor[-1]
ud_les15_mblock_cor = sim15_mblock_cor.read_turb_uvel("all", steady = False)
ud_les15_mblock_cor = ud_les15_mblock_cor[-1]
ud_les16_mblock_cor = sim16_mblock_cor.read_turb_uvel("all", steady = False)
ud_les16_mblock_cor = ud_les16_mblock_cor[-1]
ud_les17_mblock_cor = sim17_mblock_cor.read_turb_uvel("all", steady = False)
ud_les17_mblock_cor = ud_les17_mblock_cor[-1]

ud_les1_hblock_cor = sim1_hblock_cor.read_turb_uvel("all", steady = False)
ud_les1_hblock_cor = ud_les1_hblock_cor[-1]
ud_les2_hblock_cor = sim2_hblock_cor.read_turb_uvel("all", steady = False)
ud_les2_hblock_cor = ud_les2_hblock_cor[-1]
ud_les3_hblock_cor = sim3_hblock_cor.read_turb_uvel("all", steady = False)
ud_les3_hblock_cor = ud_les3_hblock_cor[-1]
ud_les4_hblock_cor = sim4_hblock_cor.read_turb_uvel("all", steady = False)
ud_les4_hblock_cor = ud_les4_hblock_cor[-1]
ud_les5_hblock_cor = sim5_hblock_cor.read_turb_uvel("all", steady = False)
ud_les5_hblock_cor = ud_les5_hblock_cor[-1]
ud_les6_hblock_cor = sim6_hblock_cor.read_turb_uvel("all", steady = False)
ud_les6_hblock_cor = ud_les6_hblock_cor[-1]
ud_les7_hblock_cor = sim7_hblock_cor.read_turb_uvel("all", steady = False)
ud_les7_hblock_cor = ud_les7_hblock_cor[-1]
ud_les8_hblock_cor = sim8_hblock_cor.read_turb_uvel("all", steady = False)
ud_les8_hblock_cor = ud_les8_hblock_cor[-1]
ud_les9_hblock_cor = sim9_hblock_cor.read_turb_uvel("all", steady = False)
ud_les9_hblock_cor = ud_les9_hblock_cor[-1]
ud_les10_hblock_cor = sim10_hblock_cor.read_turb_uvel("all", steady = False)
ud_les10_hblock_cor = ud_les10_hblock_cor[-1]
ud_les11_hblock_cor = sim11_hblock_cor.read_turb_uvel("all", steady = False)
ud_les11_hblock_cor = ud_les11_hblock_cor[-1]
ud_les12_hblock_cor = sim12_hblock_cor.read_turb_uvel("all", steady = False)
ud_les12_hblock_cor = ud_les12_hblock_cor[-1]
ud_les13_hblock_cor = sim13_hblock_cor.read_turb_uvel("all", steady = False)
ud_les13_hblock_cor = ud_les13_hblock_cor[-1]
ud_les14_hblock_cor = sim14_hblock_cor.read_turb_uvel("all", steady = False)
ud_les14_hblock_cor = ud_les14_hblock_cor[-1]
ud_les15_hblock_cor = sim15_hblock_cor.read_turb_uvel("all", steady = False)
ud_les15_hblock_cor = ud_les15_hblock_cor[-1]
ud_les16_hblock_cor = sim16_hblock_cor.read_turb_uvel("all", steady = False)
ud_les16_hblock_cor = ud_les16_hblock_cor[-1]
ud_les17_hblock_cor = sim17_hblock_cor.read_turb_uvel("all", steady = False)
ud_les17_hblock_cor = ud_les17_hblock_cor[-1]

thrust_les1_mblock_cor = 2*(np.pi/4)*(ud_les1_mblock_cor)*(u_inf1_mblock_cor - ud_les1_mblock_cor)
thrust_les2_mblock_cor = 2*(np.pi/4)*(ud_les2_mblock_cor)*(u_inf2_mblock_cor - ud_les2_mblock_cor)
thrust_les3_mblock_cor = 2*(np.pi/4)*(ud_les3_mblock_cor)*(u_inf3_mblock_cor - ud_les3_mblock_cor)
thrust_les4_mblock_cor = 2*(np.pi/4)*(ud_les4_mblock_cor)*(u_inf4_mblock_cor - ud_les4_mblock_cor)
thrust_les5_mblock_cor = 2*(np.pi/4)*(ud_les5_mblock_cor)*(u_inf5_mblock_cor - ud_les5_mblock_cor)
thrust_les6_mblock_cor = 2*(np.pi/4)*(ud_les6_mblock_cor)*(u_inf6_mblock_cor - ud_les6_mblock_cor)
thrust_les7_mblock_cor = 2*(np.pi/4)*(ud_les7_mblock_cor)*(u_inf7_mblock_cor - ud_les7_mblock_cor)
thrust_les8_mblock_cor = 2*(np.pi/4)*(ud_les8_mblock_cor)*(u_inf8_mblock_cor - ud_les8_mblock_cor)
thrust_les9_mblock_cor = 2*(np.pi/4)*(ud_les9_mblock_cor)*(u_inf9_mblock_cor - ud_les9_mblock_cor)
thrust_les10_mblock_cor = 2*(np.pi/4)*(ud_les10_mblock_cor)*(u_inf10_mblock_cor - ud_les10_mblock_cor)
thrust_les11_mblock_cor = 2*(np.pi/4)*(ud_les11_mblock_cor)*(u_inf11_mblock_cor - ud_les11_mblock_cor)
thrust_les12_mblock_cor = 2*(np.pi/4)*(ud_les12_mblock_cor)*(u_inf12_mblock_cor - ud_les12_mblock_cor)
thrust_les13_mblock_cor = 2*(np.pi/4)*(ud_les13_mblock_cor)*(u_inf13_mblock_cor - ud_les13_mblock_cor)
thrust_les14_mblock_cor = 2*(np.pi/4)*(ud_les14_mblock_cor)*(u_inf14_mblock_cor - ud_les14_mblock_cor)
thrust_les15_mblock_cor = 2*(np.pi/4)*(ud_les15_mblock_cor)*(u_inf15_mblock_cor - ud_les15_mblock_cor)
thrust_les16_mblock_cor = 2*(np.pi/4)*(ud_les16_mblock_cor)*(u_inf16_mblock_cor - ud_les16_mblock_cor)
thrust_les17_mblock_cor = 2*(np.pi/4)*(ud_les17_mblock_cor)*(u_inf17_mblock_cor - ud_les17_mblock_cor)

thrust_les1_hblock_cor = 2*(np.pi/4)*(ud_les1_hblock_cor)*(u_inf1_hblock_cor - ud_les1_hblock_cor)
thrust_les2_hblock_cor = 2*(np.pi/4)*(ud_les2_hblock_cor)*(u_inf2_hblock_cor - ud_les2_hblock_cor)
thrust_les3_hblock_cor = 2*(np.pi/4)*(ud_les3_hblock_cor)*(u_inf3_hblock_cor - ud_les3_hblock_cor)
thrust_les4_hblock_cor = 2*(np.pi/4)*(ud_les4_hblock_cor)*(u_inf4_hblock_cor - ud_les4_hblock_cor)
thrust_les5_hblock_cor = 2*(np.pi/4)*(ud_les5_hblock_cor)*(u_inf5_hblock_cor - ud_les5_hblock_cor)
thrust_les6_hblock_cor = 2*(np.pi/4)*(ud_les6_hblock_cor)*(u_inf6_hblock_cor - ud_les6_hblock_cor)
thrust_les7_hblock_cor = 2*(np.pi/4)*(ud_les7_hblock_cor)*(u_inf7_hblock_cor - ud_les7_hblock_cor)
thrust_les8_hblock_cor = 2*(np.pi/4)*(ud_les8_hblock_cor)*(u_inf8_hblock_cor - ud_les8_hblock_cor)
thrust_les9_hblock_cor = 2*(np.pi/4)*(ud_les9_hblock_cor)*(u_inf9_hblock_cor - ud_les9_hblock_cor)
thrust_les10_hblock_cor = 2*(np.pi/4)*(ud_les10_hblock_cor)*(u_inf10_hblock_cor - ud_les10_hblock_cor)
thrust_les11_hblock_cor = 2*(np.pi/4)*(ud_les11_hblock_cor)*(u_inf11_hblock_cor - ud_les11_hblock_cor)
thrust_les12_hblock_cor = 2*(np.pi/4)*(ud_les12_hblock_cor)*(u_inf12_hblock_cor - ud_les12_hblock_cor)
thrust_les13_hblock_cor = 2*(np.pi/4)*(ud_les13_hblock_cor)*(u_inf13_hblock_cor - ud_les13_hblock_cor)
thrust_les14_hblock_cor = 2*(np.pi/4)*(ud_les14_hblock_cor)*(u_inf14_hblock_cor - ud_les14_hblock_cor)
thrust_les15_hblock_cor = 2*(np.pi/4)*(ud_les15_hblock_cor)*(u_inf15_hblock_cor - ud_les15_hblock_cor)
thrust_les16_hblock_cor = 2*(np.pi/4)*(ud_les16_hblock_cor)*(u_inf16_hblock_cor - ud_les16_hblock_cor)
thrust_les17_hblock_cor = 2*(np.pi/4)*(ud_les17_hblock_cor)*(u_inf17_hblock_cor - ud_les17_hblock_cor)

ct_les1_mblock_cor = thrust_les1_mblock_cor/(0.5*(np.pi/4)*(u_inf1_mblock_cor**2))
ct_les2_mblock_cor = thrust_les2_mblock_cor/(0.5*(np.pi/4)*(u_inf2_mblock_cor**2))
ct_les3_mblock_cor = thrust_les3_mblock_cor/(0.5*(np.pi/4)*(u_inf3_mblock_cor**2))
ct_les4_mblock_cor = thrust_les4_mblock_cor/(0.5*(np.pi/4)*(u_inf4_mblock_cor**2))
ct_les5_mblock_cor = thrust_les5_mblock_cor/(0.5*(np.pi/4)*(u_inf5_mblock_cor**2))
ct_les6_mblock_cor = thrust_les6_mblock_cor/(0.5*(np.pi/4)*(u_inf6_mblock_cor**2))
ct_les7_mblock_cor = thrust_les7_mblock_cor/(0.5*(np.pi/4)*(u_inf7_mblock_cor**2))
ct_les8_mblock_cor = thrust_les8_mblock_cor/(0.5*(np.pi/4)*(u_inf8_mblock_cor**2))
ct_les9_mblock_cor = thrust_les9_mblock_cor/(0.5*(np.pi/4)*(u_inf9_mblock_cor**2))
ct_les10_mblock_cor = thrust_les10_mblock_cor/(0.5*(np.pi/4)*(u_inf10_mblock_cor**2))
ct_les11_mblock_cor = thrust_les11_mblock_cor/(0.5*(np.pi/4)*(u_inf11_mblock_cor**2))
ct_les12_mblock_cor = thrust_les12_mblock_cor/(0.5*(np.pi/4)*(u_inf12_mblock_cor**2))
ct_les13_mblock_cor = thrust_les13_mblock_cor/(0.5*(np.pi/4)*(u_inf13_mblock_cor**2))
ct_les14_mblock_cor = thrust_les14_mblock_cor/(0.5*(np.pi/4)*(u_inf14_mblock_cor**2))
ct_les15_mblock_cor = thrust_les15_mblock_cor/(0.5*(np.pi/4)*(u_inf15_mblock_cor**2))
ct_les16_mblock_cor = thrust_les16_mblock_cor/(0.5*(np.pi/4)*(u_inf16_mblock_cor**2))
ct_les17_mblock_cor = thrust_les17_mblock_cor/(0.5*(np.pi/4)*(u_inf17_mblock_cor**2))

ct_les1_hblock_cor = thrust_les1_hblock_cor/(0.5*(np.pi/4)*(u_inf1_hblock_cor**2))
ct_les2_hblock_cor = thrust_les2_hblock_cor/(0.5*(np.pi/4)*(u_inf2_hblock_cor**2))
ct_les3_hblock_cor = thrust_les3_hblock_cor/(0.5*(np.pi/4)*(u_inf3_hblock_cor**2))
ct_les4_hblock_cor = thrust_les4_hblock_cor/(0.5*(np.pi/4)*(u_inf4_hblock_cor**2))
ct_les5_hblock_cor = thrust_les5_hblock_cor/(0.5*(np.pi/4)*(u_inf5_hblock_cor**2))
ct_les6_hblock_cor = thrust_les6_hblock_cor/(0.5*(np.pi/4)*(u_inf6_hblock_cor**2))
ct_les7_hblock_cor = thrust_les7_hblock_cor/(0.5*(np.pi/4)*(u_inf7_hblock_cor**2))
ct_les8_hblock_cor = thrust_les8_hblock_cor/(0.5*(np.pi/4)*(u_inf8_hblock_cor**2))
ct_les9_hblock_cor = thrust_les9_hblock_cor/(0.5*(np.pi/4)*(u_inf9_hblock_cor**2))
ct_les10_hblock_cor = thrust_les10_hblock_cor/(0.5*(np.pi/4)*(u_inf10_hblock_cor**2))
ct_les11_hblock_cor = thrust_les11_hblock_cor/(0.5*(np.pi/4)*(u_inf11_hblock_cor**2))
ct_les12_hblock_cor = thrust_les12_hblock_cor/(0.5*(np.pi/4)*(u_inf12_hblock_cor**2))
ct_les13_hblock_cor = thrust_les13_hblock_cor/(0.5*(np.pi/4)*(u_inf13_hblock_cor**2))
ct_les14_hblock_cor = thrust_les14_hblock_cor/(0.5*(np.pi/4)*(u_inf14_hblock_cor**2))
ct_les15_hblock_cor = thrust_les15_hblock_cor/(0.5*(np.pi/4)*(u_inf15_hblock_cor**2))
ct_les16_hblock_cor = thrust_les16_hblock_cor/(0.5*(np.pi/4)*(u_inf16_hblock_cor**2))
ct_les17_hblock_cor = thrust_les17_hblock_cor/(0.5*(np.pi/4)*(u_inf17_hblock_cor**2))

#Appended Data Arrays
cp_mblock_0deg = [cp_les3_mblock_cor, cp_les5_mblock_cor, cp_les7_mblock_cor, cp_les10_mblock_cor, cp_les11_mblock_cor, cp_les12_mblock_cor, cp_les13_mblock_cor, cp_les14_mblock_cor, cp_les15_mblock_cor, cp_les16_mblock_cor, cp_les17_mblock_cor]
cp_hblock_0deg = [cp_les3_hblock_cor, cp_les5_hblock_cor, cp_les7_hblock_cor, cp_les10_hblock_cor, cp_les11_hblock_cor, cp_les12_hblock_cor, cp_les13_mblock_cor, cp_les14_mblock_cor, cp_les15_mblock_cor, cp_les16_mblock_cor, cp_les17_mblock_cor]
ct_mblock_0deg = [ct_les3_mblock_cor, ct_les5_mblock_cor, ct_les7_mblock_cor, ct_les10_mblock_cor, ct_les11_mblock_cor, ct_les12_mblock_cor, ct_les13_mblock_cor, ct_les14_mblock_cor, ct_les15_mblock_cor, ct_les16_mblock_cor, ct_les17_mblock_cor]
ct_hblock_0deg = [ct_les3_hblock_cor, ct_les5_hblock_cor, ct_les7_hblock_cor, ct_les10_hblock_cor, ct_les11_hblock_cor, ct_les12_hblock_cor, ct_les13_mblock_cor, ct_les14_mblock_cor, ct_les15_mblock_cor, ct_les16_mblock_cor, ct_les17_mblock_cor]
ctprime_yawstudy = [Ctprime3, Ctprime5, Ctprime7, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]

#Export Data
np.save("cp_mblock_0deg.npy", cp_mblock_0deg)
np.save("cp_hblock_0deg.npy", cp_hblock_0deg)
np.save("ct_mblock_0deg.npy", ct_mblock_0deg)
np.save("ct_hblock_0deg.npy", ct_hblock_0deg)
np.save("ctprime_yawstudy.npy", ctprime_yawstudy)
