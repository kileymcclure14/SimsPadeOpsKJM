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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# High Blocked, No Correction
sim10_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0009")
sim10_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0010")
sim11_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0011")
sim12_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0012")
sim13_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0013")
sim14_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0014")
sim15_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0015")
sim16_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0016")
sim17_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

# High Blocked, Corrected
sim10_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0009")
sim10_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0010")
sim11_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0011")
sim12_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0012")
sim13_hblock_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0013")
sim14_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0014")
sim15_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0015")
sim16_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_hblock_cor = os.path.join(au.DATA_PATH, "B_0003_Files/Sim_0016")
sim17_hblock_cor = pio.BudgetIO("Data/B_0003_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Ct Primes
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
p_les10 = sim10.read_turb_power("all", turb =1)[-1]
p_les11 = sim11.read_turb_power("all", turb =1)[-1]
p_les12 = sim12.read_turb_power("all", turb =1)[-1]
p_les13 = sim13.read_turb_power("all", turb =1)[-1]
p_les14 = sim14.read_turb_power("all", turb =1)[-1]
p_les15 = sim15.read_turb_power("all", turb =1)[-1]
p_les16 = sim16.read_turb_power("all", turb =1)[-1]
p_les17 = sim17.read_turb_power("all", turb =1)[-1]

#Corrected
p_les10_cor = sim10_cor.read_turb_power("all", turb = 1)[-1]
p_les11_cor = sim11_cor.read_turb_power("all", turb = 1)[-1]
p_les12_cor = sim12_cor.read_turb_power("all", turb = 1)[-1]
p_les13_cor = sim13_cor.read_turb_power("all", turb = 1)[-1]
p_les14_cor = sim14_cor.read_turb_power("all", turb = 1)[-1]
p_les15_cor = sim15_cor.read_turb_power("all", turb = 1)[-1]
p_les16_cor = sim16_cor.read_turb_power("all", turb = 1)[-1]
p_les17_cor = sim17_cor.read_turb_power("all", turb = 1)[-1]

# Medium Blocked, No Correction
p_les10_mblock = sim10_mblock.read_turb_power("all", turb = 1)[-1]
p_les11_mblock = sim11_mblock.read_turb_power("all", turb = 1)[-1]
p_les12_mblock = sim12_mblock.read_turb_power("all", turb = 1)[-1]
p_les13_mblock = sim13_mblock.read_turb_power("all", turb = 1)[-1]
p_les14_mblock = sim14_mblock.read_turb_power("all", turb = 1)[-1]
p_les15_mblock = sim15_mblock.read_turb_power("all", turb = 1)[-1]
p_les16_mblock = sim16_mblock.read_turb_power("all", turb = 1)[-1]
p_les17_mblock = sim17_mblock.read_turb_power("all", turb = 1)[-1]

# Medium Blocked, Corrected
p_les10_mblock_cor = sim10_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les11_mblock_cor = sim11_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les12_mblock_cor = sim12_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les13_mblock_cor = sim13_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les14_mblock_cor = sim14_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les15_mblock_cor = sim15_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les16_mblock_cor = sim16_mblock_cor.read_turb_power("all", turb = 1)[-1]
p_les17_mblock_cor = sim17_mblock_cor.read_turb_power("all", turb = 1)[-1]

# High Blocked, No Correction
p_les10_hblock = sim10_hblock.read_turb_power("all", turb = 1)[-1]
p_les11_hblock = sim11_hblock.read_turb_power("all", turb = 1)[-1]
p_les12_hblock = sim12_hblock.read_turb_power("all", turb = 1)[-1]
p_les13_hblock = sim13_hblock.read_turb_power("all", turb = 1)[-1]
p_les14_hblock = sim14_hblock.read_turb_power("all", turb = 1)[-1]
p_les15_hblock = sim15_hblock.read_turb_power("all", turb = 1)[-1]
p_les16_hblock = sim16_hblock.read_turb_power("all", turb = 1)[-1]
p_les17_hblock = sim17_hblock.read_turb_power("all", turb = 1)[-1]

# High Blocked, Corrected
p_les10_hblock_cor = sim10_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les11_hblock_cor = sim11_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les12_hblock_cor = sim12_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les13_hblock_cor = sim13_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les14_hblock_cor = sim14_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les15_hblock_cor = sim15_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les16_hblock_cor = sim16_hblock_cor.read_turb_power("all", turb = 1)[-1]
p_les17_hblock_cor = sim17_hblock_cor.read_turb_power("all", turb = 1)[-1]

#Free Stream Velocities
# Uncorrected
u_inf10 = sim10.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11 = sim11.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12 = sim12.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13 = sim13.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14 = sim14.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15 = sim15.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16 = sim16.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17 = sim17.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Corrected
u_inf10_cor = sim10_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_cor = sim11_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_cor = sim12_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_cor = sim13_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_cor = sim14_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_cor = sim15_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_cor = sim16_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_cor = sim17_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Medium Blocked, No Correction
u_inf10_mblock = sim10_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_mblock = sim11_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_mblock = sim12_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_mblock = sim13_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_mblock = sim14_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_mblock = sim15_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_mblock = sim16_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_mblock = sim17_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Medium Blocked, Corrected
u_inf10_mblock_cor = sim10_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_mblock_cor = sim11_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_mblock_cor = sim12_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_mblock_cor = sim13_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_mblock_cor = sim14_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_mblock_cor = sim15_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_mblock_cor = sim16_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_mblock_cor = sim17_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# High Blocked, No Correction
u_inf10_hblock = sim10_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_hblock = sim11_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_hblock = sim12_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_hblock = sim13_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_hblock = sim14_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_hblock = sim15_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_hblock = sim16_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_hblock = sim17_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# High Blocked, Corrected
u_inf10_hblock_cor = sim10_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_hblock_cor = sim11_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_hblock_cor = sim12_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_hblock_cor = sim13_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_hblock_cor = sim14_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_hblock_cor = sim15_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_hblock_cor = sim16_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_hblock_cor = sim17_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

#Power Coefficients
#Uncorrected
cp_les10 = p_les10 / (0.5*(np.pi/4)*(u_inf10**3))
cp_les11 = p_les11 / (0.5*(np.pi/4)*(u_inf11**3))
cp_les12 = p_les12 / (0.5*(np.pi/4)*(u_inf12**3))
cp_les13 = p_les13 / (0.5*(np.pi/4)*(u_inf13**3))
cp_les14 = p_les14 / (0.5*(np.pi/4)*(u_inf14**3))
cp_les15 = p_les15 / (0.5*(np.pi/4)*(u_inf15**3))
cp_les16 = p_les16 / (0.5*(np.pi/4)*(u_inf16**3))
cp_les17 = p_les17 / (0.5*(np.pi/4)*(u_inf17**3))

# Correcteed
cp_les10_cor = p_les10_cor / (0.5*(np.pi/4)*(u_inf10_cor**3))
cp_les11_cor = p_les11_cor / (0.5*(np.pi/4)*(u_inf11_cor**3))
cp_les12_cor = p_les12_cor / (0.5*(np.pi/4)*(u_inf12_cor**3))
cp_les13_cor = p_les13_cor / (0.5*(np.pi/4)*(u_inf13_cor**3))
cp_les14_cor = p_les14_cor / (0.5*(np.pi/4)*(u_inf14_cor**3))
cp_les15_cor = p_les15_cor / (0.5*(np.pi/4)*(u_inf15_cor**3))
cp_les16_cor = p_les16_cor / (0.5*(np.pi/4)*(u_inf16_cor**3))
cp_les17_cor = p_les17_cor / (0.5*(np.pi/4)*(u_inf17_cor**3))

# Medium Blocked, No Correction
cp_les10_mblock = p_les10_mblock / (0.5*(np.pi/4)*(u_inf10_mblock**3))
cp_les11_mblock = p_les11_mblock / (0.5*(np.pi/4)*(u_inf11_mblock**3))
cp_les12_mblock = p_les12_mblock / (0.5*(np.pi/4)*(u_inf12_mblock**3))
cp_les13_mblock = p_les13_mblock / (0.5*(np.pi/4)*(u_inf13_mblock**3))
cp_les14_mblock = p_les14_mblock / (0.5*(np.pi/4)*(u_inf14_mblock**3))
cp_les15_mblock = p_les15_mblock / (0.5*(np.pi/4)*(u_inf15_mblock**3))
cp_les16_mblock = p_les16_mblock / (0.5*(np.pi/4)*(u_inf16_mblock**3))
cp_les17_mblock = p_les17_mblock / (0.5*(np.pi/4)*(u_inf17_mblock**3))

# Medium Blocked, Corrected
cp_les10_mblock_cor = p_les10_mblock_cor / (0.5*(np.pi/4)*(u_inf10_mblock_cor**3))
cp_les11_mblock_cor = p_les11_mblock_cor / (0.5*(np.pi/4)*(u_inf11_mblock_cor**3))
cp_les12_mblock_cor = p_les12_mblock_cor / (0.5*(np.pi/4)*(u_inf12_mblock_cor**3))
cp_les13_mblock_cor = p_les13_mblock_cor / (0.5*(np.pi/4)*(u_inf13_mblock_cor**3))
cp_les14_mblock_cor = p_les14_mblock_cor / (0.5*(np.pi/4)*(u_inf14_mblock_cor**3))
cp_les15_mblock_cor = p_les15_mblock_cor / (0.5*(np.pi/4)*(u_inf15_mblock_cor**3))
cp_les16_mblock_cor = p_les16_mblock_cor / (0.5*(np.pi/4)*(u_inf16_mblock_cor**3))
cp_les17_mblock_cor = p_les17_mblock_cor / (0.5*(np.pi/4)*(u_inf17_mblock_cor**3))

# High Blocked, No Correction
cp_les10_hblock = p_les10_hblock / (0.5*(np.pi/4)*(u_inf10_hblock**3))
cp_les11_hblock = p_les11_hblock / (0.5*(np.pi/4)*(u_inf11_hblock**3))
cp_les12_hblock = p_les12_hblock / (0.5*(np.pi/4)*(u_inf12_hblock**3))
cp_les13_hblock = p_les13_hblock / (0.5*(np.pi/4)*(u_inf13_hblock**3))
cp_les14_hblock = p_les14_hblock / (0.5*(np.pi/4)*(u_inf14_hblock**3))
cp_les15_hblock = p_les15_hblock / (0.5*(np.pi/4)*(u_inf15_hblock**3))
cp_les16_hblock = p_les16_hblock / (0.5*(np.pi/4)*(u_inf16_hblock**3))
cp_les17_hblock = p_les17_hblock / (0.5*(np.pi/4)*(u_inf17_hblock**3))

# HighBlocked, Corrected
cp_les10_hblock_cor = p_les10_hblock_cor / (0.5*(np.pi/4)*(u_inf10_hblock_cor**3))
cp_les11_hblock_cor = p_les11_hblock_cor / (0.5*(np.pi/4)*(u_inf11_hblock_cor**3))
cp_les12_hblock_cor = p_les12_hblock_cor / (0.5*(np.pi/4)*(u_inf12_hblock_cor**3))
cp_les13_hblock_cor = p_les13_hblock_cor / (0.5*(np.pi/4)*(u_inf13_hblock_cor**3))
cp_les14_hblock_cor = p_les14_hblock_cor / (0.5*(np.pi/4)*(u_inf14_hblock_cor**3))
cp_les15_hblock_cor = p_les15_hblock_cor / (0.5*(np.pi/4)*(u_inf15_hblock_cor**3))
cp_les16_hblock_cor = p_les16_hblock_cor / (0.5*(np.pi/4)*(u_inf16_hblock_cor**3))
cp_les17_hblock_cor = p_les17_hblock_cor / (0.5*(np.pi/4)*(u_inf17_hblock_cor**3))

#Disk Velocities
#Uncorrected
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

# Meidum Blocked, No Correction
ud_les10_mblock = sim10_mblock.read_turb_uvel("all", steady = False)
ud_les10_mblock = ud_les10_mblock[-1]
ud_les11_mblock = sim11_mblock.read_turb_uvel("all", steady = False)
ud_les11_mblock = ud_les11_mblock[-1]
ud_les12_mblock = sim12_mblock.read_turb_uvel("all", steady = False)
ud_les12_mblock = ud_les12_mblock[-1]
ud_les13_mblock = sim13_mblock.read_turb_uvel("all", steady = False)
ud_les13_mblock = ud_les13_mblock[-1]
ud_les14_mblock = sim14_mblock.read_turb_uvel("all", steady = False)
ud_les14_mblock = ud_les14_mblock[-1]
ud_les15_mblock = sim15_mblock.read_turb_uvel("all", steady = False)
ud_les15_mblock = ud_les15_mblock[-1]
ud_les16_mblock = sim16_mblock.read_turb_uvel("all", steady = False)
ud_les16_mblock = ud_les16_mblock[-1]
ud_les17_mblock = sim17_mblock.read_turb_uvel("all", steady = False)
ud_les17_mblock = ud_les17_mblock[-1]

# Medium Blocked, Corrected
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

# High Blocked, No Correction
ud_les10_hblock = sim10_hblock.read_turb_uvel("all", steady = False)
ud_les10_hblock = ud_les10_hblock[-1]
ud_les11_hblock = sim11_hblock.read_turb_uvel("all", steady = False)
ud_les11_hblock = ud_les11_hblock[-1]
ud_les12_hblock = sim12_hblock.read_turb_uvel("all", steady = False)
ud_les12_hblock = ud_les12_hblock[-1]
ud_les13_hblock = sim13_hblock.read_turb_uvel("all", steady = False)
ud_les13_hblock = ud_les13_hblock[-1]
ud_les14_hblock = sim14_hblock.read_turb_uvel("all", steady = False)
ud_les14_hblock = ud_les14_hblock[-1]
ud_les15_hblock = sim15_hblock.read_turb_uvel("all", steady = False)
ud_les15_hblock = ud_les15_hblock[-1]
ud_les16_hblock = sim16_hblock.read_turb_uvel("all", steady = False)
ud_les16_hblock = ud_les16_hblock[-1]
ud_les17_hblock = sim17_hblock.read_turb_uvel("all", steady = False)
ud_les17_hblock = ud_les17_hblock[-1]

# High Blocked, Corrected
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

#Thrust Force 
#Uncorrected
thrust_les10 = 2*(np.pi/4)*(ud_les10)*(u_inf10 - ud_les10)
thrust_les11 = 2*(np.pi/4)*(ud_les11)*(u_inf11 - ud_les11)
thrust_les12 = 2*(np.pi/4)*(ud_les12)*(u_inf12 - ud_les12)
thrust_les13 = 2*(np.pi/4)*(ud_les13)*(u_inf13 - ud_les13)
thrust_les14 = 2*(np.pi/4)*(ud_les14)*(u_inf14 - ud_les14)
thrust_les15 = 2*(np.pi/4)*(ud_les15)*(u_inf15 - ud_les15)
thrust_les16 = 2*(np.pi/4)*(ud_les16)*(u_inf16 - ud_les16)
thrust_les17 = 2*(np.pi/4)*(ud_les17)*(u_inf17 - ud_les17)

#Corrected
thrust_les10_cor = 2*(np.pi/4)*(ud_les10_cor)*(u_inf10_cor - ud_les10_cor)
thrust_les11_cor = 2*(np.pi/4)*(ud_les11_cor)*(u_inf11_cor - ud_les11_cor)
thrust_les12_cor = 2*(np.pi/4)*(ud_les12_cor)*(u_inf12_cor - ud_les12_cor)
thrust_les13_cor = 2*(np.pi/4)*(ud_les13_cor)*(u_inf13_cor - ud_les13_cor)
thrust_les14_cor = 2*(np.pi/4)*(ud_les14_cor)*(u_inf14_cor - ud_les14_cor)
thrust_les15_cor = 2*(np.pi/4)*(ud_les15_cor)*(u_inf15_cor - ud_les15_cor)
thrust_les16_cor = 2*(np.pi/4)*(ud_les16_cor)*(u_inf16_cor - ud_les16_cor)
thrust_les17_cor = 2*(np.pi/4)*(ud_les17_cor)*(u_inf17_cor - ud_les17_cor)

# Medium Blocked, No Correction
thrust_les10_mblock = 2*(np.pi/4)*(ud_les10_mblock)*(u_inf10_mblock - ud_les10_mblock)
thrust_les11_mblock = 2*(np.pi/4)*(ud_les11_mblock)*(u_inf11_mblock - ud_les11_mblock)
thrust_les12_mblock = 2*(np.pi/4)*(ud_les12_mblock)*(u_inf12_mblock - ud_les12_mblock)
thrust_les13_mblock = 2*(np.pi/4)*(ud_les13_mblock)*(u_inf13_mblock - ud_les13_mblock)
thrust_les14_mblock = 2*(np.pi/4)*(ud_les14_mblock)*(u_inf14_mblock - ud_les14_mblock)
thrust_les15_mblock = 2*(np.pi/4)*(ud_les15_mblock)*(u_inf15_mblock - ud_les15_mblock)
thrust_les16_mblock = 2*(np.pi/4)*(ud_les16_mblock)*(u_inf16_mblock - ud_les16_mblock)
thrust_les17_mblock = 2*(np.pi/4)*(ud_les17_mblock)*(u_inf17_mblock - ud_les17_mblock)

# Medium Blocked, Corrected
thrust_les10_mblock_cor = 2*(np.pi/4)*(ud_les10_mblock_cor)*(u_inf10_mblock_cor - ud_les10_mblock_cor)
thrust_les11_mblock_cor = 2*(np.pi/4)*(ud_les11_mblock_cor)*(u_inf11_mblock_cor - ud_les11_mblock_cor)
thrust_les12_mblock_cor = 2*(np.pi/4)*(ud_les12_mblock_cor)*(u_inf12_mblock_cor - ud_les12_mblock_cor)
thrust_les13_mblock_cor = 2*(np.pi/4)*(ud_les13_mblock_cor)*(u_inf13_mblock_cor - ud_les13_mblock_cor)
thrust_les14_mblock_cor = 2*(np.pi/4)*(ud_les14_mblock_cor)*(u_inf14_mblock_cor - ud_les14_mblock_cor)
thrust_les15_mblock_cor = 2*(np.pi/4)*(ud_les15_mblock_cor)*(u_inf15_mblock_cor - ud_les15_mblock_cor)
thrust_les16_mblock_cor = 2*(np.pi/4)*(ud_les16_mblock_cor)*(u_inf16_mblock_cor - ud_les16_mblock_cor)
thrust_les17_mblock_cor = 2*(np.pi/4)*(ud_les17_mblock_cor)*(u_inf17_mblock_cor - ud_les17_mblock_cor)

# High Blocked, No Correction
thrust_les10_hblock = 2*(np.pi/4)*(ud_les10_hblock)*(u_inf10_hblock - ud_les10_hblock)
thrust_les11_hblock = 2*(np.pi/4)*(ud_les11_hblock)*(u_inf11_hblock - ud_les11_hblock)
thrust_les12_hblock = 2*(np.pi/4)*(ud_les12_hblock)*(u_inf12_hblock - ud_les12_hblock)
thrust_les13_hblock = 2*(np.pi/4)*(ud_les13_hblock)*(u_inf13_hblock - ud_les13_hblock)
thrust_les14_hblock = 2*(np.pi/4)*(ud_les14_hblock)*(u_inf14_hblock - ud_les14_hblock)
thrust_les15_hblock = 2*(np.pi/4)*(ud_les15_hblock)*(u_inf15_hblock - ud_les15_hblock)
thrust_les16_hblock = 2*(np.pi/4)*(ud_les16_hblock)*(u_inf16_hblock - ud_les16_hblock)
thrust_les17_hblock = 2*(np.pi/4)*(ud_les17_hblock)*(u_inf17_hblock - ud_les17_hblock)

# High Blocked, Corrected
thrust_les10_hblock_cor = 2*(np.pi/4)*(ud_les10_hblock_cor)*(u_inf10_hblock_cor - ud_les10_hblock_cor)
thrust_les11_hblock_cor = 2*(np.pi/4)*(ud_les11_hblock_cor)*(u_inf11_hblock_cor - ud_les11_hblock_cor)
thrust_les12_hblock_cor = 2*(np.pi/4)*(ud_les12_hblock_cor)*(u_inf12_hblock_cor - ud_les12_hblock_cor)
thrust_les13_hblock_cor = 2*(np.pi/4)*(ud_les13_hblock_cor)*(u_inf13_hblock_cor - ud_les13_hblock_cor)
thrust_les14_hblock_cor = 2*(np.pi/4)*(ud_les14_hblock_cor)*(u_inf14_hblock_cor - ud_les14_hblock_cor)
thrust_les15_hblock_cor = 2*(np.pi/4)*(ud_les15_hblock_cor)*(u_inf15_hblock_cor - ud_les15_hblock_cor)
thrust_les16_hblock_cor = 2*(np.pi/4)*(ud_les16_hblock_cor)*(u_inf16_hblock_cor - ud_les16_hblock_cor)
thrust_les17_hblock_cor = 2*(np.pi/4)*(ud_les17_hblock_cor)*(u_inf17_hblock_cor - ud_les17_hblock_cor)

#Ct
#Uncorrected
ct_les10 = thrust_les10/(0.5*(np.pi/4)*(u_inf10**2))
ct_les11 = thrust_les11/(0.5*(np.pi/4)*(u_inf11**2))
ct_les12 = thrust_les12/(0.5*(np.pi/4)*(u_inf12**2))
ct_les13 = thrust_les13/(0.5*(np.pi/4)*(u_inf13**2))
ct_les14 = thrust_les14/(0.5*(np.pi/4)*(u_inf14**2))
ct_les15 = thrust_les15/(0.5*(np.pi/4)*(u_inf15**2))
ct_les16 = thrust_les16/(0.5*(np.pi/4)*(u_inf16**2))
ct_les17 = thrust_les17/(0.5*(np.pi/4)*(u_inf17**2))

#Corrected
ct_les10_cor = thrust_les10_cor/(0.5*(np.pi/4)*(u_inf10_cor**2))
ct_les11_cor = thrust_les11_cor/(0.5*(np.pi/4)*(u_inf11_cor**2))
ct_les12_cor = thrust_les12_cor/(0.5*(np.pi/4)*(u_inf12_cor**2))
ct_les13_cor = thrust_les13_cor/(0.5*(np.pi/4)*(u_inf13_cor**2))
ct_les14_cor = thrust_les14_cor/(0.5*(np.pi/4)*(u_inf14_cor**2))
ct_les15_cor = thrust_les15_cor/(0.5*(np.pi/4)*(u_inf15_cor**2))
ct_les16_cor = thrust_les16_cor/(0.5*(np.pi/4)*(u_inf16_cor**2))
ct_les17_cor = thrust_les17_cor/(0.5*(np.pi/4)*(u_inf17_cor**2))

# Medium Blocked, No Correction
ct_les10_mblock = thrust_les10_mblock/(0.5*(np.pi/4)*(u_inf10_mblock**2))
ct_les11_mblock = thrust_les11_mblock/(0.5*(np.pi/4)*(u_inf11_mblock**2))
ct_les12_mblock = thrust_les12_mblock/(0.5*(np.pi/4)*(u_inf12_mblock**2))
ct_les13_mblock = thrust_les13_mblock/(0.5*(np.pi/4)*(u_inf13_mblock**2))
ct_les14_mblock = thrust_les14_mblock/(0.5*(np.pi/4)*(u_inf14_mblock**2))
ct_les15_mblock = thrust_les15_mblock/(0.5*(np.pi/4)*(u_inf15_mblock**2))
ct_les16_mblock = thrust_les16_mblock/(0.5*(np.pi/4)*(u_inf16_mblock**2))
ct_les17_mblock = thrust_les17_mblock/(0.5*(np.pi/4)*(u_inf17_mblock**2))

# Medium Blocked, Corrected
ct_les10_mblock_cor = thrust_les10_mblock_cor/(0.5*(np.pi/4)*(u_inf10_mblock_cor**2))
ct_les11_mblock_cor = thrust_les11_mblock_cor/(0.5*(np.pi/4)*(u_inf11_mblock_cor**2))
ct_les12_mblock_cor = thrust_les12_mblock_cor/(0.5*(np.pi/4)*(u_inf12_mblock_cor**2))
ct_les13_mblock_cor = thrust_les13_mblock_cor/(0.5*(np.pi/4)*(u_inf13_mblock_cor**2))
ct_les14_mblock_cor = thrust_les14_mblock_cor/(0.5*(np.pi/4)*(u_inf14_mblock_cor**2))
ct_les15_mblock_cor = thrust_les15_mblock_cor/(0.5*(np.pi/4)*(u_inf15_mblock_cor**2))
ct_les16_mblock_cor = thrust_les16_mblock_cor/(0.5*(np.pi/4)*(u_inf16_mblock_cor**2))
ct_les17_mblock_cor = thrust_les17_mblock_cor/(0.5*(np.pi/4)*(u_inf17_mblock_cor**2))

# High Blocked, No Correction
ct_les10_hblock = thrust_les10_hblock/(0.5*(np.pi/4)*(u_inf10_hblock**2))
ct_les11_hblock = thrust_les11_hblock/(0.5*(np.pi/4)*(u_inf11_hblock**2))
ct_les12_hblock = thrust_les12_hblock/(0.5*(np.pi/4)*(u_inf12_hblock**2))
ct_les13_hblock = thrust_les13_hblock/(0.5*(np.pi/4)*(u_inf13_hblock**2))
ct_les14_hblock = thrust_les14_hblock/(0.5*(np.pi/4)*(u_inf14_hblock**2))
ct_les15_hblock = thrust_les15_hblock/(0.5*(np.pi/4)*(u_inf15_hblock**2))
ct_les16_hblock = thrust_les16_hblock/(0.5*(np.pi/4)*(u_inf16_hblock**2))
ct_les17_hblock = thrust_les17_hblock/(0.5*(np.pi/4)*(u_inf17_hblock**2))

# High Blocked, Corrected
ct_les10_hblock_cor = thrust_les10_hblock_cor/(0.5*(np.pi/4)*(u_inf10_hblock_cor**2))
ct_les11_hblock_cor = thrust_les11_hblock_cor/(0.5*(np.pi/4)*(u_inf11_hblock_cor**2))
ct_les12_hblock_cor = thrust_les12_hblock_cor/(0.5*(np.pi/4)*(u_inf12_hblock_cor**2))
ct_les13_hblock_cor = thrust_les13_hblock_cor/(0.5*(np.pi/4)*(u_inf13_hblock_cor**2))
ct_les14_hblock_cor = thrust_les14_hblock_cor/(0.5*(np.pi/4)*(u_inf14_hblock_cor**2))
ct_les15_hblock_cor = thrust_les15_hblock_cor/(0.5*(np.pi/4)*(u_inf15_hblock_cor**2))
ct_les16_hblock_cor = thrust_les16_hblock_cor/(0.5*(np.pi/4)*(u_inf16_hblock_cor**2))
ct_les17_hblock_cor = thrust_les17_hblock_cor/(0.5*(np.pi/4)*(u_inf17_hblock_cor**2))

#Manual Inputs
#Blockage
mb = 0.1
hb = 0.35

#U2/U1 Manual Inputs/Guess
# Medium Uncorrected
u2_u1_m10 = 1
u2_u1_m11 = 1
u2_u1_m12 = 1.01
u2_u1_m13 = 1.01
u2_u1_m14 = 1.01
u2_u1_m15 = 1.01
u2_u1_m16 = 1.01
u2_u1_m17 = 1.01

# Medium Corrected
u2_u1_m10_cor = 1
u2_u1_m11_cor = 1
u2_u1_m12_cor = 1
u2_u1_m13_cor = 1
u2_u1_m14_cor = 1.01
u2_u1_m15_cor = 1.01
u2_u1_m16_cor = 1.01
u2_u1_m17_cor = 1.01

# High Uncorrected
u2_u1_h10 = 1.01
u2_u1_h11 = 1.01
u2_u1_h12 = 1.01
u2_u1_h13 = 1.01
u2_u1_h14 = 1.01
u2_u1_h15 = 1.01
u2_u1_h16 = 1.01
u2_u1_h17 = 1.01

# High Corrected
u2_u1_h10_cor = 1.01
u2_u1_h11_cor = 1.01
u2_u1_h12_cor = 1.01
u2_u1_h13_cor = 1.01
u2_u1_h14_cor = 1.01
u2_u1_h15_cor = 1.01
u2_u1_h16_cor = 1.01
u2_u1_h17_cor = 1.01

#Solving for Ut/U1
#Medium Uncorrected
ut_u1_m10 = (-1 + np.sqrt(1+mb*((u2_u1_m10**2)-1)))/(mb*(u2_u1_m10 -1))
ut_u1_m11 = (-1 + np.sqrt(1+mb*((u2_u1_m11**2)-1)))/(mb*(u2_u1_m11 -1))
ut_u1_m12 = (-1 + np.sqrt(1+mb*((u2_u1_m12**2)-1)))/(mb*(u2_u1_m12 -1))
ut_u1_m13 = (-1 + np.sqrt(1+mb*((u2_u1_m13**2)-1)))/(mb*(u2_u1_m13 -1))
ut_u1_m14 = (-1 + np.sqrt(1+mb*((u2_u1_m14**2)-1)))/(mb*(u2_u1_m14 -1))
ut_u1_m15 = (-1 + np.sqrt(1+mb*((u2_u1_m15**2)-1)))/(mb*(u2_u1_m15 -1))
ut_u1_m16 = (-1 + np.sqrt(1+mb*((u2_u1_m16**2)-1)))/(mb*(u2_u1_m16 -1))
ut_u1_m17 = (-1 + np.sqrt(1+mb*((u2_u1_m17**2)-1)))/(mb*(u2_u1_m17 -1))

# Medium Corrected
ut_u1_m10_cor = (-1 + np.sqrt(1+mb*((u2_u1_m10_cor**2)-1)))/(mb*(u2_u1_m10_cor -1))
ut_u1_m11_cor = (-1 + np.sqrt(1+mb*((u2_u1_m11_cor**2)-1)))/(mb*(u2_u1_m11_cor -1))
ut_u1_m12_cor = (-1 + np.sqrt(1+mb*((u2_u1_m12_cor**2)-1)))/(mb*(u2_u1_m12_cor -1))
ut_u1_m13_cor = (-1 + np.sqrt(1+mb*((u2_u1_m13_cor**2)-1)))/(mb*(u2_u1_m13_cor -1))
ut_u1_m14_cor = (-1 + np.sqrt(1+mb*((u2_u1_m14_cor**2)-1)))/(mb*(u2_u1_m14_cor -1))
ut_u1_m15_cor = (-1 + np.sqrt(1+mb*((u2_u1_m15_cor**2)-1)))/(mb*(u2_u1_m15_cor -1))
ut_u1_m16_cor = (-1 + np.sqrt(1+mb*((u2_u1_m16_cor**2)-1)))/(mb*(u2_u1_m16_cor -1))
ut_u1_m17_cor = (-1 + np.sqrt(1+mb*((u2_u1_m17_cor**2)-1)))/(mb*(u2_u1_m17_cor -1))

#High Uncorrected
ut_u1_h10 = (-1 + np.sqrt(1+hb*((u2_u1_h10**2)-1)))/(hb*(u2_u1_h10 -1))
ut_u1_h11 = (-1 + np.sqrt(1+hb*((u2_u1_h11**2)-1)))/(hb*(u2_u1_h11 -1))
ut_u1_h12 = (-1 + np.sqrt(1+hb*((u2_u1_h12**2)-1)))/(hb*(u2_u1_h12 -1))
ut_u1_h13 = (-1 + np.sqrt(1+hb*((u2_u1_h13**2)-1)))/(hb*(u2_u1_h13 -1))
ut_u1_h14 = (-1 + np.sqrt(1+hb*((u2_u1_h14**2)-1)))/(hb*(u2_u1_h14 -1))
ut_u1_h15 = (-1 + np.sqrt(1+hb*((u2_u1_h15**2)-1)))/(hb*(u2_u1_h15 -1))
ut_u1_h16 = (-1 + np.sqrt(1+hb*((u2_u1_h16**2)-1)))/(hb*(u2_u1_h16 -1))
ut_u1_h17 = (-1 + np.sqrt(1+hb*((u2_u1_h17**2)-1)))/(hb*(u2_u1_h17 -1))

# High Corrected
ut_u1_h10_cor = (-1 + np.sqrt(1+hb*((u2_u1_h10_cor**2)-1)))/(hb*(u2_u1_m10_cor -1))
ut_u1_h11_cor = (-1 + np.sqrt(1+hb*((u2_u1_h11_cor**2)-1)))/(hb*(u2_u1_m11_cor -1))
ut_u1_h12_cor = (-1 + np.sqrt(1+hb*((u2_u1_h12_cor**2)-1)))/(hb*(u2_u1_m12_cor -1))
ut_u1_h13_cor = (-1 + np.sqrt(1+hb*((u2_u1_h13_cor**2)-1)))/(hb*(u2_u1_m13_cor -1))
ut_u1_h14_cor = (-1 + np.sqrt(1+hb*((u2_u1_h14_cor**2)-1)))/(hb*(u2_u1_m14_cor -1))
ut_u1_h15_cor = (-1 + np.sqrt(1+hb*((u2_u1_h15_cor**2)-1)))/(hb*(u2_u1_m15_cor -1))
ut_u1_h16_cor = (-1 + np.sqrt(1+hb*((u2_u1_h16_cor**2)-1)))/(hb*(u2_u1_m16_cor -1))
ut_u1_h17_cor = (-1 + np.sqrt(1+hb*((u2_u1_h17_cor**2)-1)))/(hb*(u2_u1_m17_cor -1))

#V0/U1 Eqs
# Meddium Uncorrected, Eq 22 From Paper
v0_U1_m10_22 = u2_u1_m10 - mb*(ut_u1_m10)*(u2_u1_m10 - 1)
v0_U1_m11_22 = u2_u1_m11 - mb*(ut_u1_m11)*(u2_u1_m11 - 1)
v0_U1_m12_22 = u2_u1_m12 - mb*(ut_u1_m12)*(u2_u1_m12 - 1)
v0_U1_m13_22 = u2_u1_m13 - mb*(ut_u1_m13)*(u2_u1_m13 - 1)
v0_U1_m14_22 = u2_u1_m14 - mb*(ut_u1_m14)*(u2_u1_m14 - 1)
v0_U1_m15_22 = u2_u1_m15 - mb*(ut_u1_m15)*(u2_u1_m15 - 1)
v0_U1_m16_22 = u2_u1_m16 - mb*(ut_u1_m16)*(u2_u1_m16 - 1)
v0_U1_m17_22 = u2_u1_m17 - mb*(ut_u1_m17)*(u2_u1_m17 - 1)

# Medium Corrected, Eq 22 From Paper
v0_U1_m10_cor_22 = u2_u1_m10_cor - mb*(ut_u1_m10_cor)*(u2_u1_m10_cor - 1)
v0_U1_m11_cor_22 = u2_u1_m11_cor - mb*(ut_u1_m11_cor)*(u2_u1_m11_cor - 1)
v0_U1_m12_cor_22 = u2_u1_m12_cor - mb*(ut_u1_m12_cor)*(u2_u1_m12_cor - 1)
v0_U1_m13_cor_22 = u2_u1_m13_cor - mb*(ut_u1_m13_cor)*(u2_u1_m13_cor - 1)
v0_U1_m14_cor_22 = u2_u1_m14_cor - mb*(ut_u1_m14_cor)*(u2_u1_m14_cor - 1)
v0_U1_m15_cor_22 = u2_u1_m15_cor - mb*(ut_u1_m15_cor)*(u2_u1_m15_cor - 1)
v0_U1_m16_cor_22 = u2_u1_m16_cor - mb*(ut_u1_m16_cor)*(u2_u1_m16_cor - 1)
v0_U1_m17_cor_22 = u2_u1_m17_cor - mb*(ut_u1_m17_cor)*(u2_u1_m17_cor - 1)

# High Uncorrected, Eq 22 From Paper
v0_U1_h10_22 = u2_u1_h10 - hb*(ut_u1_h10)*(u2_u1_h10 - 1)
v0_U1_h11_22 = u2_u1_h11 - hb*(ut_u1_h11)*(u2_u1_h11 - 1)
v0_U1_h12_22 = u2_u1_h12 - hb*(ut_u1_h12)*(u2_u1_h12 - 1)
v0_U1_h13_22 = u2_u1_h13 - hb*(ut_u1_h13)*(u2_u1_h13 - 1)
v0_U1_h14_22 = u2_u1_h14 - hb*(ut_u1_h14)*(u2_u1_h14 - 1)
v0_U1_h15_22 = u2_u1_h15 - hb*(ut_u1_h15)*(u2_u1_h15 - 1)
v0_U1_h16_22 = u2_u1_h16 - hb*(ut_u1_h16)*(u2_u1_h16 - 1)
v0_U1_h17_22 = u2_u1_h17 - hb*(ut_u1_h17)*(u2_u1_h17 - 1)

# High Corrected, Eq 22 From Paper
v0_U1_h10_cor_22 = u2_u1_h10_cor - hb*(ut_u1_h10_cor)*(u2_u1_h10_cor - 1)
v0_U1_h11_cor_22 = u2_u1_h11_cor - hb*(ut_u1_h11_cor)*(u2_u1_h11_cor - 1)
v0_U1_h12_cor_22 = u2_u1_h12_cor - hb*(ut_u1_h12_cor)*(u2_u1_h12_cor - 1)
v0_U1_h13_cor_22 = u2_u1_h13_cor - hb*(ut_u1_h13_cor)*(u2_u1_h13_cor - 1)
v0_U1_h14_cor_22 = u2_u1_h14_cor - hb*(ut_u1_h14_cor)*(u2_u1_h14_cor - 1)
v0_U1_h15_cor_22 = u2_u1_h15_cor - hb*(ut_u1_h15_cor)*(u2_u1_h15_cor - 1)
v0_U1_h16_cor_22 = u2_u1_h16_cor - hb*(ut_u1_h16_cor)*(u2_u1_h16_cor - 1)
v0_U1_h17_cor_22 = u2_u1_h17_cor - hb*(ut_u1_h17_cor)*(u2_u1_h17_cor - 1)

# Medium Uncorrected, Eq 23 From Paper
v0_U1_m10_23 = np.sqrt(((u2_u1_m10**2)-1)/ct_les10_mblock)
v0_U1_m11_23 = np.sqrt(((u2_u1_m11**2)-1)/ct_les11_mblock)
v0_U1_m12_23 = np.sqrt(((u2_u1_m12**2)-1)/ct_les12_mblock)
v0_U1_m13_23 = np.sqrt(((u2_u1_m13**2)-1)/ct_les13_mblock)
v0_U1_m14_23 = np.sqrt(((u2_u1_m14**2)-1)/ct_les14_mblock)
v0_U1_m15_23 = np.sqrt(((u2_u1_m15**2)-1)/ct_les15_mblock)
v0_U1_m16_23 = np.sqrt(((u2_u1_m16**2)-1)/ct_les16_mblock)
v0_U1_m17_23 = np.sqrt(((u2_u1_m17**2)-1)/ct_les17_mblock)

# Medium Corrected, Eq 23 From Paper
v0_U1_m10_cor_23 = np.sqrt(((u2_u1_m10_cor**2)-1)/ct_les10_mblock_cor)
v0_U1_m11_cor_23 = np.sqrt(((u2_u1_m11_cor**2)-1)/ct_les11_mblock_cor)
v0_U1_m12_cor_23 = np.sqrt(((u2_u1_m12_cor**2)-1)/ct_les12_mblock_cor)
v0_U1_m13_cor_23 = np.sqrt(((u2_u1_m13_cor**2)-1)/ct_les13_mblock_cor)
v0_U1_m14_cor_23 = np.sqrt(((u2_u1_m14_cor**2)-1)/ct_les14_mblock_cor)
v0_U1_m15_cor_23 = np.sqrt(((u2_u1_m15_cor**2)-1)/ct_les15_mblock_cor)
v0_U1_m16_cor_23 = np.sqrt(((u2_u1_m16_cor**2)-1)/ct_les16_mblock_cor)
v0_U1_m17_cor_23 = np.sqrt(((u2_u1_m17_cor**2)-1)/ct_les17_mblock_cor)

# High Uncorrected, Eq 23 From Paper
v0_U1_h10_23 = np.sqrt(((u2_u1_h10**2)-1)/ct_les10_hblock)
v0_U1_h11_23 = np.sqrt(((u2_u1_h11**2)-1)/ct_les11_hblock)
v0_U1_h12_23 = np.sqrt(((u2_u1_h12**2)-1)/ct_les12_hblock)
v0_U1_h13_23 = np.sqrt(((u2_u1_h13**2)-1)/ct_les13_hblock)
v0_U1_h14_23 = np.sqrt(((u2_u1_h14**2)-1)/ct_les14_hblock)
v0_U1_h15_23 = np.sqrt(((u2_u1_h15**2)-1)/ct_les15_hblock)
v0_U1_h16_23 = np.sqrt(((u2_u1_h16**2)-1)/ct_les16_hblock)
v0_U1_h17_23 = np.sqrt(((u2_u1_h17**2)-1)/ct_les17_hblock)

# High Corrected, Eq 23 From Paper
v0_U1_h10_cor_23 = np.sqrt(((u2_u1_h10_cor**2)-1)/ct_les10_hblock_cor)
v0_U1_h11_cor_23 = np.sqrt(((u2_u1_h11_cor**2)-1)/ct_les11_hblock_cor)
v0_U1_h12_cor_23 = np.sqrt(((u2_u1_h12_cor**2)-1)/ct_les12_hblock_cor)
v0_U1_h13_cor_23 = np.sqrt(((u2_u1_h13_cor**2)-1)/ct_les13_hblock_cor)
v0_U1_h14_cor_23 = np.sqrt(((u2_u1_h14_cor**2)-1)/ct_les14_hblock_cor)
v0_U1_h15_cor_23 = np.sqrt(((u2_u1_h15_cor**2)-1)/ct_les15_hblock_cor)
v0_U1_h16_cor_23 = np.sqrt(((u2_u1_h16_cor**2)-1)/ct_les16_hblock_cor)
v0_U1_h17_cor_23 = np.sqrt(((u2_u1_h17_cor**2)-1)/ct_les17_hblock_cor)

#Loops to Establish Convergence + Calculate V'0
# Medium Uncorrected
if np.absolute(v0_U1_m10_22 - v0_U1_m10_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim10")
else:
    v0_u1_m10 = np.mean([v0_U1_m10_22, v0_U1_m10_23])
    print(f"v0/u1 for Med Uncorrected Sim 10: {v0_u1_m10}")
    ut_v0_m10 = ut_u1_m10/v0_u1_m10
    v0_prime_m10 = (u_inf10_mblock*((ut_v0_m10**2 + (ct_les10_mblock/4))))/(ut_v0_m10)
    cp_prime_m10 = cp_les10_mblock*((u_inf10_mblock/v0_prime_m10)**3)
    ct_prime_m10 = ct_les10_mblock*((u_inf10_mblock/v0_prime_m10)**2)

if np.absolute(v0_U1_m11_22 - v0_U1_m11_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim11")
else:
    v0_u1_m11 = np.mean([v0_U1_m11_22, v0_U1_m11_23])
    print(f"v0/u1 for Med Uncorrected Sim 11: {v0_u1_m11}")
    ut_v0_m11 = ut_u1_m11/v0_u1_m11
    v0_prime_m11 = (u_inf11_mblock*((ut_v0_m11**2 + (ct_les11_mblock/4))))/(ut_v0_m11)
    cp_prime_m11 = cp_les11_mblock*((u_inf11_mblock/v0_prime_m11)**3)
    ct_prime_m11 = ct_les11_mblock*((u_inf11_mblock/v0_prime_m11)**2)

if np.absolute(v0_U1_m12_22 - v0_U1_m12_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim12")
else:
    v0_u1_m12 = np.mean([v0_U1_m12_22, v0_U1_m12_23])
    print(f"v0/u1 for Med Uncorrected Sim 12: {v0_u1_m12}")
    ut_v0_m12 = ut_u1_m12/v0_u1_m12
    v0_prime_m12 = (u_inf12_mblock*((ut_v0_m12**2 + (ct_les12_mblock/4))))/(ut_v0_m12)
    cp_prime_m12 = cp_les12_mblock*((u_inf12_mblock/v0_prime_m12)**3)
    ct_prime_m12 = ct_les12_mblock*((u_inf12_mblock/v0_prime_m12)**2)

if np.absolute(v0_U1_m13_22 - v0_U1_m13_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim13")
else:
    v0_u1_m13 = np.mean([v0_U1_m13_22, v0_U1_m13_23])
    print(f"v0/u1 for Med Uncorrected Sim 13: {v0_u1_m13}")
    ut_v0_m13 = ut_u1_m13/v0_u1_m13
    v0_prime_m13 = (u_inf13_mblock*((ut_v0_m13**2 + (ct_les13_mblock/4))))/(ut_v0_m13)
    cp_prime_m13 = cp_les13_mblock*((u_inf13_mblock/v0_prime_m13)**3)
    ct_prime_m13 = ct_les13_mblock*((u_inf13_mblock/v0_prime_m13)**2)

if np.absolute(v0_U1_m14_22 - v0_U1_m14_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim14")
else:
    v0_u1_m14 = np.mean([v0_U1_m14_22, v0_U1_m14_23])
    print(f"v0/u1 for Med Uncorrected Sim 14: {v0_u1_m14}")
    ut_v0_m14 = ut_u1_m14/v0_u1_m14
    v0_prime_m14 = (u_inf14_mblock*((ut_v0_m14**2 + (ct_les14_mblock/4))))/(ut_v0_m14)
    cp_prime_m14 = cp_les14_mblock*((u_inf14_mblock/v0_prime_m14)**3)
    ct_prime_m14 = ct_les14_mblock*((u_inf14_mblock/v0_prime_m14)**2)

if np.absolute(v0_U1_m15_22 - v0_U1_m15_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim15")
else:
    v0_u1_m15 = np.mean([v0_U1_m15_22, v0_U1_m15_23])
    print(f"v0/u1 for Med Uncorrected Sim 15: {v0_u1_m15}")
    ut_v0_m15 = ut_u1_m15/v0_u1_m15
    v0_prime_m15 = (u_inf15_mblock*((ut_v0_m15**2 + (ct_les15_mblock/4))))/(ut_v0_m15)
    cp_prime_m15 = cp_les15_mblock*((u_inf15_mblock/v0_prime_m15)**3)
    ct_prime_m15 = ct_les15_mblock*((u_inf15_mblock/v0_prime_m15)**2)

if np.absolute(v0_U1_m16_22 - v0_U1_m16_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim16")
else:
    v0_u1_m16 = np.mean([v0_U1_m16_22, v0_U1_m16_23])
    print(f"v0/u1 for Med Uncorrected Sim 16: {v0_u1_m16}")
    ut_v0_m16 = ut_u1_m16/v0_u1_m16
    v0_prime_m16 = (u_inf16_mblock*((ut_v0_m16**2 + (ct_les16_mblock/4))))/(ut_v0_m16)
    cp_prime_m16 = cp_les16_mblock*((u_inf16_mblock/v0_prime_m16)**3)
    ct_prime_m16 = ct_les16_mblock*((u_inf16_mblock/v0_prime_m16)**2)

if np.absolute(v0_U1_m17_22 - v0_U1_m17_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Uncorrected Sim17")
else:
    v0_u1_m17 = np.mean([v0_U1_m17_22, v0_U1_m17_23])
    print(f"v0/u1 for Med Uncorrected Sim 17: {v0_u1_m17}")
    ut_v0_m17 = ut_u1_m17/v0_u1_m17
    v0_prime_m17 = (u_inf17_mblock*((ut_v0_m17**2 + (ct_les17_mblock/4))))/(ut_v0_m17)
    cp_prime_m17 = cp_les17_mblock*((u_inf17_mblock/v0_prime_m17)**3)
    ct_prime_m17 = ct_les17_mblock*((u_inf17_mblock/v0_prime_m17)**2)

# Medium Corrected
if np.absolute(v0_U1_m10_cor_22 - v0_U1_m10_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Mecium Corrected Sim10")
else:
    v0_u1_m10_cor = np.mean([v0_U1_m10_cor_22, v0_U1_m10_cor_23])
    print(f"v0/u1 for Med Corrected Sim 10: {v0_u1_m10_cor}")
    ut_v0_m10_cor = ut_u1_m10_cor/v0_u1_m10_cor
    v0_prime_m10_cor = (u_inf10_mblock_cor*((ut_v0_m10_cor**2 + (ct_les10_mblock_cor/4))))/(ut_v0_m10_cor)
    cp_prime_m10_cor = cp_les10_mblock_cor*((u_inf10_mblock_cor/v0_prime_m10_cor)**3)
    ct_prime_m10_cor = ct_les10_mblock_cor*((u_inf10_mblock_cor/v0_prime_m10_cor)**2)

if np.absolute(v0_U1_m11_cor_22 - v0_U1_m11_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Corrected Sim11")
else:
    v0_u1_m11_cor = np.mean([v0_U1_m11_cor_22, v0_U1_m11_cor_23])
    print(f"v0/u1 for Med Corrected Sim 11: {v0_u1_m11_cor}")
    ut_v0_m11_cor = ut_u1_m11_cor/v0_u1_m11_cor
    v0_prime_m11_cor = (u_inf11_mblock_cor*((ut_v0_m11_cor**2 + (ct_les11_mblock_cor/4))))/(ut_v0_m11_cor)
    cp_prime_m11_cor = cp_les11_mblock_cor*((u_inf11_mblock_cor/v0_prime_m11_cor)**3)
    ct_prime_m11_cor = ct_les11_mblock_cor*((u_inf11_mblock_cor/v0_prime_m11_cor)**2)

if np.absolute(v0_U1_m12_cor_22 - v0_U1_m12_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Corrected Sim12")
else:
    v0_u1_m12_cor = np.mean([v0_U1_m12_cor_22, v0_U1_m12_cor_23])
    print(f"v0/u1 for Med Corrected Sim 12: {v0_u1_m12_cor}")
    ut_v0_m12_cor = ut_u1_m12_cor/v0_u1_m12_cor
    v0_prime_m12_cor = (u_inf12_mblock_cor*((ut_v0_m12_cor**2 + (ct_les12_mblock_cor/4))))/(ut_v0_m12_cor)
    cp_prime_m12_cor = cp_les12_mblock_cor*((u_inf12_mblock_cor/v0_prime_m12_cor)**3)
    ct_prime_m12_cor = ct_les12_mblock_cor*((u_inf12_mblock_cor/v0_prime_m12_cor)**2)

if np.absolute(v0_U1_m13_cor_22 - v0_U1_m13_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Corrected Sim13")
else:
    v0_u1_m13_cor = np.mean([v0_U1_m13_cor_22, v0_U1_m13_cor_23])
    print(f"v0/u1 for Med Corrected Sim 13: {v0_u1_m13_cor}")
    ut_v0_m13_cor = ut_u1_m13_cor/v0_u1_m13_cor
    v0_prime_m13_cor = (u_inf13_mblock_cor*((ut_v0_m13_cor**2 + (ct_les13_mblock_cor/4))))/(ut_v0_m13_cor)
    cp_prime_m13_cor = cp_les13_mblock_cor*((u_inf13_mblock_cor/v0_prime_m13_cor)**3)
    ct_prime_m13_cor = ct_les13_mblock_cor*((u_inf13_mblock_cor/v0_prime_m13_cor)**2)

if np.absolute(v0_U1_m14_cor_22 - v0_U1_m14_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Corrected Sim14")
else:
    v0_u1_m14_cor = np.mean([v0_U1_m14_cor_22, v0_U1_m14_cor_23])
    print(f"v0/u1 for Med Corrected Sim 14: {v0_u1_m14_cor}")
    ut_v0_m14_cor = ut_u1_m14_cor/v0_u1_m14_cor
    v0_prime_m14_cor = (u_inf14_mblock_cor*((ut_v0_m14_cor**2 + (ct_les14_mblock_cor/4))))/(ut_v0_m14_cor)
    cp_prime_m14_cor = cp_les14_mblock_cor*((u_inf14_mblock_cor/v0_prime_m14_cor)**3)
    ct_prime_m14_cor = ct_les14_mblock_cor*((u_inf14_mblock_cor/v0_prime_m14_cor)**2)

if np.absolute(v0_U1_m15_cor_22 - v0_U1_m15_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Medium Corrected Sim15")
else:
    v0_u1_m15_cor = np.mean([v0_U1_m15_cor_22, v0_U1_m15_cor_23])
    print(f"v0/u1 for Med Corrected Sim 15: {v0_u1_m15_cor}")
    ut_v0_m15_cor = ut_u1_m15_cor/v0_u1_m15_cor
    v0_prime_m15_cor = (u_inf15_mblock_cor*((ut_v0_m15_cor**2 + (ct_les15_mblock_cor/4))))/(ut_v0_m15_cor)
    cp_prime_m15_cor = cp_les15_mblock_cor*((u_inf15_mblock_cor/v0_prime_m15_cor)**3)
    ct_prime_m15_cor = ct_les15_mblock_cor*((u_inf15_mblock_cor/v0_prime_m15_cor)**2)

if np.absolute(v0_U1_m16_cor_22 - v0_U1_m16_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Meidum Corrected Sim16")
else:
    v0_u1_m16_cor = np.mean([v0_U1_m16_cor_22, v0_U1_m16_cor_23])
    print(f"v0/u1 for Med Corrected Sim 16: {v0_u1_m16_cor}")
    ut_v0_m16_cor = ut_u1_m16_cor/v0_u1_m16_cor
    v0_prime_m16_cor = (u_inf16_mblock_cor*((ut_v0_m16_cor**2 + (ct_les16_mblock_cor/4))))/(ut_v0_m16_cor)
    cp_prime_m16_cor = cp_les16_mblock_cor*((u_inf16_mblock_cor/v0_prime_m16_cor)**3)
    ct_prime_m16_cor = ct_les16_mblock_cor*((u_inf16_mblock_cor/v0_prime_m16_cor)**2)

if np.absolute(v0_U1_m17_cor_22 - v0_U1_m17_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Meidum Corrected Sim17")
else:
    v0_u1_m17_cor = np.mean([v0_U1_m17_cor_22, v0_U1_m17_cor_23])
    print(f"v0/u1 for Med Corrected Sim 17: {v0_u1_m17_cor}")
    ut_v0_m17_cor = ut_u1_m17_cor/v0_u1_m17_cor
    v0_prime_m17_cor = (u_inf17_mblock_cor*((ut_v0_m17_cor**2 + (ct_les17_mblock_cor/4))))/(ut_v0_m17_cor)
    cp_prime_m17_cor = cp_les17_mblock_cor*((u_inf17_mblock_cor/v0_prime_m17_cor)**3)
    ct_prime_m17_cor = ct_les17_mblock_cor*((u_inf17_mblock_cor/v0_prime_m17_cor)**2)

# High Uncorrected
if np.absolute(v0_U1_h10_22 - v0_U1_h10_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim10")
else:
    v0_u1_h10 = np.mean([v0_U1_h10_22, v0_U1_h10_23])
    print(f"v0/u1 for High uncorrected Sim 10: {v0_u1_h10}")
    ut_v0_h10 = ut_u1_h10/v0_u1_h10
    v0_prime_h10 = (u_inf10_hblock*((ut_v0_h10**2 + (ct_les10_hblock/4))))/(ut_v0_h10)
    cp_prime_h10 = cp_les10_hblock*((u_inf10_hblock/v0_prime_h10)**3)
    ct_prime_h10 = ct_les10_hblock*((u_inf10_hblock/v0_prime_h10)**2)

if np.absolute(v0_U1_h11_22 - v0_U1_h11_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim11")
else:
    v0_u1_h11 = np.mean([v0_U1_h11_22, v0_U1_h11_23])
    print(f"v0/u1 for High uncorrected Sim 11: {v0_u1_h11}")
    ut_v0_h11 = ut_u1_h11/v0_u1_h11
    v0_prime_h11 = (u_inf11_hblock*((ut_v0_h11**2 + (ct_les11_hblock/4))))/(ut_v0_h11)
    cp_prime_h11 = cp_les11_hblock*((u_inf11_hblock/v0_prime_h11)**3)
    ct_prime_h11 = ct_les11_hblock*((u_inf11_hblock/v0_prime_h11)**2)

if np.absolute(v0_U1_h12_22 - v0_U1_h12_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim12")
else:
    v0_u1_h12 = np.mean([v0_U1_h12_22, v0_U1_h12_23])
    print(f"v0/u1 for High uncorrected Sim 12: {v0_u1_h12}")
    ut_v0_h12 = ut_u1_h12/v0_u1_h12
    v0_prime_h12 = (u_inf12_hblock*((ut_v0_h12**2 + (ct_les12_hblock/4))))/(ut_v0_h12)
    cp_prime_h12 = cp_les12_hblock*((u_inf12_hblock/v0_prime_h12)**3)
    ct_prime_h12 = ct_les12_hblock*((u_inf12_hblock/v0_prime_h12)**2)

if np.absolute(v0_U1_h13_22 - v0_U1_h13_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim13")
else:
    v0_u1_h13 = np.mean([v0_U1_h13_22, v0_U1_h13_23])
    print(f"v0/u1 for High uncorrected Sim 13: {v0_u1_h13}")
    ut_v0_h13 = ut_u1_h13/v0_u1_h13
    v0_prime_h13 = (u_inf13_hblock*((ut_v0_h13**2 + (ct_les13_hblock/4))))/(ut_v0_h13)
    cp_prime_h13 = cp_les13_hblock*((u_inf13_hblock/v0_prime_h13)**3)
    ct_prime_h13 = ct_les13_hblock*((u_inf13_hblock/v0_prime_h13)**2)

if np.absolute(v0_U1_h14_22 - v0_U1_h14_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim14")
else:
    v0_u1_h14 = np.mean([v0_U1_h14_22, v0_U1_h14_23])
    print(f"v0/u1 for High uncorrected Sim 14: {v0_u1_h14}")
    ut_v0_h14 = ut_u1_h14/v0_u1_h14
    v0_prime_h14 = (u_inf14_hblock*((ut_v0_h14**2 + (ct_les14_hblock/4))))/(ut_v0_h14)
    cp_prime_h14 = cp_les14_hblock*((u_inf14_hblock/v0_prime_h14)**3)
    ct_prime_h14 = ct_les14_hblock*((u_inf14_hblock/v0_prime_h14)**2)

if np.absolute(v0_U1_h15_22 - v0_U1_h15_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim15")
else:
    v0_u1_h15 = np.mean([v0_U1_h15_22, v0_U1_h15_23])
    print(f"v0/u1 for High uncorrected Sim 15: {v0_u1_h15}")
    ut_v0_h15 = ut_u1_h15/v0_u1_h15
    v0_prime_h15 = (u_inf15_hblock*((ut_v0_h15**2 + (ct_les15_hblock/4))))/(ut_v0_h15)
    cp_prime_h15 = cp_les15_hblock*((u_inf15_hblock/v0_prime_h15)**3)
    ct_prime_h15 = ct_les15_hblock*((u_inf15_hblock/v0_prime_h15)**2)

if np.absolute(v0_U1_h16_22 - v0_U1_h16_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim16")
else:
    v0_u1_h16 = np.mean([v0_U1_h16_22, v0_U1_h16_23])
    print(f"v0/u1 for High uncorrected Sim 61: {v0_u1_h16}")
    ut_v0_h16 = ut_u1_h16/v0_u1_h16
    v0_prime_h16 = (u_inf16_hblock*((ut_v0_h16**2 + (ct_les16_hblock/4))))/(ut_v0_h16)
    cp_prime_h16 = cp_les16_hblock*((u_inf16_hblock/v0_prime_h16)**3)
    ct_prime_h16 = ct_les16_hblock*((u_inf16_hblock/v0_prime_h16)**2)

if np.absolute(v0_U1_h17_22 - v0_U1_h17_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Uncorrected Sim17")
else:
    v0_u1_h17 = np.mean([v0_U1_h17_22, v0_U1_h17_23])
    print(f"v0/u1 for High uncorrected Sim 17: {v0_u1_h17}")
    ut_v0_h17 = ut_u1_h17/v0_u1_h17
    v0_prime_h17 = (u_inf17_hblock*((ut_v0_h17**2 + (ct_les17_hblock/4))))/(ut_v0_h17)
    cp_prime_h17 = cp_les17_hblock*((u_inf17_hblock/v0_prime_h17)**3)
    ct_prime_1h7 = ct_les17_hblock*((u_inf17_hblock/v0_prime_h17)**2)

# High Corrected
if np.absolute(v0_U1_h10_cor_22 - v0_U1_h10_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim10")
else:
    v0_u1_h10_cor = np.mean([v0_U1_h10_cor_22, v0_U1_h10_cor_23])
    print(f"v0/u1 for High Corrected Sim 10: {v0_u1_h10_cor}")
    ut_v0_h10_cor = ut_u1_h10_cor/v0_u1_h10_cor
    v0_prime_h10_cor = (u_inf10_hblock_cor*((ut_v0_h10_cor**2 + (ct_les10_hblock_cor/4))))/(ut_v0_h10_cor)
    cp_prime_h10_cor = cp_les10_hblock_cor*((u_inf10_hblock_cor/v0_prime_h10_cor)**3)
    ct_prime_h10_cor = ct_les10_hblock_cor*((u_inf10_hblock_cor/v0_prime_h10_cor)**2)

if np.absolute(v0_U1_h11_cor_22 - v0_U1_h11_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim11")
else:
    v0_u1_h11_cor = np.mean([v0_U1_h11_cor_22, v0_U1_h11_cor_23])
    print(f"v0/u1 for High Corrected Sim 11: {v0_u1_h11_cor}")
    ut_v0_h11_cor = ut_u1_h11_cor/v0_u1_h11_cor
    v0_prime_h11_cor = (u_inf11_hblock_cor*((ut_v0_h11_cor**2 + (ct_les11_hblock_cor/4))))/(ut_v0_h11_cor)
    cp_prime_h11_cor = cp_les11_hblock_cor*((u_inf11_hblock_cor/v0_prime_h11_cor)**3)
    ct_prime_h11_cor = ct_les11_hblock_cor*((u_inf11_hblock_cor/v0_prime_h11_cor)**2)

if np.absolute(v0_U1_h12_cor_22 - v0_U1_h12_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim12")
else:
    v0_u1_h12_cor = np.mean([v0_U1_h12_cor_22, v0_U1_h12_cor_23])
    print(f"v0/u1 for High Corrected Sim 12: {v0_u1_h12_cor}")
    ut_v0_h12_cor = ut_u1_h12_cor/v0_u1_h12_cor
    v0_prime_h12_cor = (u_inf12_hblock_cor*((ut_v0_h12_cor**2 + (ct_les12_hblock_cor/4))))/(ut_v0_h12_cor)
    cp_prime_h12_cor = cp_les12_hblock_cor*((u_inf12_hblock_cor/v0_prime_h12_cor)**3)
    ct_prime_h12_cor = ct_les12_hblock_cor*((u_inf12_hblock_cor/v0_prime_h12_cor)**2)

if np.absolute(v0_U1_h13_cor_22 - v0_U1_h13_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim13")
else:
    v0_u1_h13_cor = np.mean([v0_U1_h13_cor_22, v0_U1_h13_cor_23])
    print(f"v0/u1 for High Corrected Sim 13: {v0_u1_h13_cor}")
    ut_v0_h13_cor = ut_u1_h13_cor/v0_u1_h13_cor
    v0_prime_h13_cor = (u_inf13_hblock_cor*((ut_v0_h13_cor**2 + (ct_les13_hblock_cor/4))))/(ut_v0_h13_cor)
    cp_prime_h13_cor = cp_les13_hblock_cor*((u_inf13_hblock_cor/v0_prime_h13_cor)**3)
    ct_prime_h13_cor = ct_les13_hblock_cor*((u_inf13_hblock_cor/v0_prime_h13_cor)**2)

if np.absolute(v0_U1_h14_cor_22 - v0_U1_h14_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim14")
else:
    v0_u1_h14_cor = np.mean([v0_U1_h14_cor_22, v0_U1_h14_cor_23])
    print(f"v0/u1 for High Corrected Sim 14: {v0_u1_h14_cor}")
    ut_v0_h14_cor = ut_u1_h14_cor/v0_u1_h14_cor
    v0_prime_h14_cor = (u_inf14_hblock_cor*((ut_v0_h14_cor**2 + (ct_les14_hblock_cor/4))))/(ut_v0_h14_cor)
    cp_prime_h14_cor = cp_les14_hblock_cor*((u_inf14_hblock_cor/v0_prime_h14_cor)**3)
    ct_prime_h14_cor = ct_les14_hblock_cor*((u_inf14_hblock_cor/v0_prime_h14_cor)**2)

if np.absolute(v0_U1_h15_cor_22 - v0_U1_h15_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim15")
else:
    v0_u1_h15_cor = np.mean([v0_U1_h15_cor_22, v0_U1_h15_cor_23])
    print(f"v0/u1 for High Corrected Sim 15: {v0_u1_h15_cor}")
    ut_v0_h15_cor = ut_u1_h15_cor/v0_u1_h15_cor
    v0_prime_h15_cor = (u_inf15_hblock_cor*((ut_v0_h15_cor**2 + (ct_les15_hblock_cor/4))))/(ut_v0_h15_cor)
    cp_prime_h15_cor = cp_les15_hblock_cor*((u_inf15_hblock_cor/v0_prime_h15_cor)**3)
    ct_prime_h15_cor = ct_les15_hblock_cor*((u_inf15_hblock_cor/v0_prime_h15_cor)**2)

if np.absolute(v0_U1_h16_cor_22 - v0_U1_h16_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim16")
else:
    v0_u1_h16_cor = np.mean([v0_U1_h16_cor_22, v0_U1_h16_cor_23])
    print(f"v0/u1 for High Corrected Sim 16: {v0_u1_h16_cor}")
    ut_v0_h16_cor = ut_u1_h16_cor/v0_u1_h16_cor
    v0_prime_h16_cor = (u_inf16_hblock_cor*((ut_v0_h16_cor**2 + (ct_les16_hblock_cor/4))))/(ut_v0_h16_cor)
    cp_prime_h16_cor = cp_les16_hblock_cor*((u_inf16_hblock_cor/v0_prime_h16_cor)**3)
    ct_prime_h16_cor = ct_les16_hblock_cor*((u_inf16_hblock_cor/v0_prime_h16_cor)**2)

if np.absolute(v0_U1_h17_cor_22 - v0_U1_h17_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for High Corrected Sim17")
else:
    v0_u1_h17_cor = np.mean([v0_U1_h17_cor_22, v0_U1_h17_cor_23])
    print(f"v0/u1 for High Corrected Sim 17: {v0_u1_h17_cor}")
    ut_v0_h17_cor = ut_u1_h17_cor/v0_u1_h17_cor
    v0_prime_h17_cor = (u_inf17_hblock_cor*((ut_v0_h17_cor**2 + (ct_les17_hblock_cor/4))))/(ut_v0_h17_cor)
    cp_prime_h17_cor = cp_les17_hblock_cor*((u_inf17_hblock_cor/v0_prime_h17_cor)**3)
    ct_prime_h17_cor = ct_les17_hblock_cor*((u_inf17_hblock_cor/v0_prime_h17_cor)**2)

#Velocity Fields to Help with Guess
#Medium Uncorrected
dsm10 = sim10_mblock.slice(field_terms = 'u', ylim = 5)
dsm10['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0009')

dsm11 = sim11_mblock.slice(field_terms = 'u', ylim = 5)
dsm11['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0010')

dsm12 = sim12_mblock.slice(field_terms = 'u', ylim = 5)
dsm12['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0011')

dsm13 = sim13_mblock.slice(field_terms = 'u', ylim = 5)
dsm13['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0012')

dsm14 = sim14_mblock.slice(field_terms = 'u', ylim = 5)
dsm14['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0013')

dsm15 = sim15_mblock.slice(field_terms = 'u', ylim = 5)
dsm15['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0014')

dsm16 = sim16_mblock.slice(field_terms = 'u', ylim = 5)
dsm16['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0015')

dsm17 = sim17_mblock.slice(field_terms = 'u', ylim = 5)
dsm17['u'].imshow()
plt.savefig('./u_field_B_0000_Sim_0016')

#Medium Corrected
dsm10_cor = sim10_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm10_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0009')

dsm11_cor = sim11_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm11_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0010')

dsm12_cor = sim12_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm12_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0011')

dsm13_cor = sim13_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm13_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0012')

dsm14_cor = sim14_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm14_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0013')

dsm15_cor = sim15_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm15_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0014')

dsm16_cor = sim16_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm16_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0015')

dsm17_cor = sim17_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsm17_cor['u'].imshow()
plt.savefig('./u_field_B_0001_Sim_0016')

#High Uncorrected
dsh10 = sim10_mblock.slice(field_terms = 'u', ylim = 5)
dsh10['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0009')

dsh11 = sim11_mblock.slice(field_terms = 'u', ylim = 5)
dsh11['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0010')

dsh12 = sim12_mblock.slice(field_terms = 'u', ylim = 5)
dsh12['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0011')

dsh13 = sim13_mblock.slice(field_terms = 'u', ylim = 5)
dsh13['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0012')

dsh14 = sim14_mblock.slice(field_terms = 'u', ylim = 5)
dsh14['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0013')

dsh15 = sim15_mblock.slice(field_terms = 'u', ylim = 5)
dsh15['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0014')

dsh16 = sim16_mblock.slice(field_terms = 'u', ylim = 5)
dsh16['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0015')

dsh17 = sim17_mblock.slice(field_terms = 'u', ylim = 5)
dsh17['u'].imshow()
plt.savefig('./u_field_B_0002_Sim_0016')

#High Corrected
dsh10_cor = sim10_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh10_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0009')

dsh11_cor = sim11_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh11_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0010')

dsh12_cor = sim12_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh12_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0011')

dsh13_cor = sim13_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh13_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0012')

dsh14_cor = sim14_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh14_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0013')

dsh15_cor = sim15_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh15_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0014')

dsh16_cor = sim16_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh16_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0015')

dsh17_cor = sim17_mblock_cor.slice(field_terms = 'u', ylim = 5)
dsh17_cor['u'].imshow()
plt.savefig('./u_field_B_0003_Sim_0016')
