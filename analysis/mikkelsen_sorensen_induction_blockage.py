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

#Mediumn Blocked, Corrected
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

#High Blockage, Uncorrected
sim1_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0000")
sim1_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0001")
sim2_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0002")
sim3_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0003")
sim4_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0004")
sim5_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0005")
sim6_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0006")
sim7_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0007")
sim8_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0008")
sim9_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

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

#High Block, Corrected
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

#Ct Primes
Ctprime1 = sim1_mblock.ta[0].ct
Ctprime2 = sim2_mblock.ta[0].ct
Ctprime3 = sim3_mblock.ta[0].ct
Ctprime4 = sim4_mblock.ta[0].ct
Ctprime5 = sim5_mblock.ta[0].ct
Ctprime6 = sim6_mblock.ta[0].ct
Ctprime7 = sim7_mblock.ta[0].ct
Ctprime8 = sim8_mblock.ta[0].ct
Ctprime9 = sim9_mblock.ta[0].ct
Ctprime10 = sim10_mblock.ta[0].ct
Ctprime11 = sim11_mblock.ta[0].ct
Ctprime12 = sim12_mblock.ta[0].ct
Ctprime13 = sim13_mblock.ta[0].ct
Ctprime14 = sim14_mblock.ta[0].ct
Ctprime15 = sim15_mblock.ta[0].ct
Ctprime16 = sim16_mblock.ta[0].ct
Ctprime17 = sim17_mblock.ta[0].ct

#Turbine Power

#Med Blocked, No Correction
p_les1_mblock = sim1_mblock.read_turb_power("all", turb = 1)[-1]
p_les2_mblock = sim2_mblock.read_turb_power("all", turb = 1)[-1]
p_les3_mblock = sim3_mblock.read_turb_power("all", turb = 1)[-1]
p_les4_mblock = sim4_mblock.read_turb_power("all", turb = 1)[-1]
p_les5_mblock = sim5_mblock.read_turb_power("all", turb = 1)[-1]
p_les6_mblock = sim6_mblock.read_turb_power("all", turb = 1)[-1]
p_les7_mblock = sim7_mblock.read_turb_power("all", turb = 1)[-1]
p_les8_mblock = sim8_mblock.read_turb_power("all", turb = 1)[-1]
p_les9_mblock = sim9_mblock.read_turb_power("all", turb = 1)[-1]
p_les10_mblock = sim10_mblock.read_turb_power("all", turb = 1)[-1]
p_les11_mblock = sim11_mblock.read_turb_power("all", turb = 1)[-1]
p_les12_mblock = sim12_mblock.read_turb_power("all", turb = 1)[-1]
p_les13_mblock = sim13_mblock.read_turb_power("all", turb = 1)[-1]
p_les14_mblock = sim14_mblock.read_turb_power("all", turb = 1)[-1]
p_les15_mblock = sim15_mblock.read_turb_power("all", turb = 1)[-1]
p_les16_mblock = sim16_mblock.read_turb_power("all", turb = 1)[-1]
p_les17_mblock = sim17_mblock.read_turb_power("all", turb = 1)[-1]

#Med Blocked, Corrected
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

#High Block, No Correction
p_les1_hblock = sim1_hblock.read_turb_power("all", turb = 1)[-1]
p_les2_hblock = sim2_hblock.read_turb_power("all", turb = 1)[-1]
p_les3_hblock = sim3_hblock.read_turb_power("all", turb = 1)[-1]
p_les4_hblock = sim4_hblock.read_turb_power("all", turb = 1)[-1]
p_les5_hblock = sim5_hblock.read_turb_power("all", turb = 1)[-1]
p_les6_hblock = sim6_hblock.read_turb_power("all", turb = 1)[-1]
p_les7_hblock = sim7_hblock.read_turb_power("all", turb = 1)[-1]
p_les8_hblock = sim8_hblock.read_turb_power("all", turb = 1)[-1]
p_les9_hblock = sim9_hblock.read_turb_power("all", turb = 1)[-1]
p_les10_hblock = sim10_hblock.read_turb_power("all", turb = 1)[-1]
p_les11_hblock = sim11_hblock.read_turb_power("all", turb = 1)[-1]
p_les12_hblock = sim12_hblock.read_turb_power("all", turb = 1)[-1]
p_les13_hblock = sim13_hblock.read_turb_power("all", turb = 1)[-1]
p_les14_hblock = sim14_hblock.read_turb_power("all", turb = 1)[-1]
p_les15_hblock = sim15_hblock.read_turb_power("all", turb = 1)[-1]
p_les16_hblock = sim16_hblock.read_turb_power("all", turb = 1)[-1]
p_les17_hblock = sim17_hblock.read_turb_power("all", turb = 1)[-1]

#High Blockage, Corrected
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

#Free Stream Velocities

# Med Blocked, No Correction
u_inf1_mblock = sim1_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf2_mblock = sim2_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf3_mblock = sim3_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf4_mblock = sim4_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf5_mblock = sim5_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf6_mblock = sim6_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf7_mblock = sim7_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf8_mblock = sim8_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf9_mblock = sim9_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf10_mblock = sim10_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf11_mblock = sim11_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf12_mblock = sim12_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf13_mblock = sim13_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf14_mblock = sim14_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf15_mblock = sim15_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf16_mblock = sim16_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values
u_inf17_mblock = sim17_mblock.slice(field_terms=['u'], xlim = -5, zlim = 5)['u'].mean("y").values

# Med Blocked, Corrected
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

# High Blocked, Uncorrected
u_inf1_hblock = sim1_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf2_hblock = sim2_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf3_hblock = sim3_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf4_hblock = sim4_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf5_hblock = sim5_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf6_hblock = sim6_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf7_hblock = sim7_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf8_hblock = sim8_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf9_hblock = sim9_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf10_hblock = sim10_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf11_hblock = sim11_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf12_hblock = sim12_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf13_hblock = sim13_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf14_hblock = sim14_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf15_hblock = sim15_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf16_hblock = sim16_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values
u_inf17_hblock = sim17_hblock.slice(field_terms=['u'], xlim = -5, zlim = 1.4285)['u'].mean("y").values

# High Blocked, Corrected
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


#Power Coefficients

# Med Blocked, No Correction
cp_les1_mblock = p_les1_mblock / (0.5*(np.pi/4)*(u_inf1_mblock**3))
cp_les2_mblock = p_les2_mblock / (0.5*(np.pi/4)*(u_inf2_mblock**3))
cp_les3_mblock = p_les3_mblock / (0.5*(np.pi/4)*(u_inf3_mblock**3))
cp_les4_mblock = p_les4_mblock / (0.5*(np.pi/4)*(u_inf4_mblock**3))
cp_les5_mblock = p_les5_mblock / (0.5*(np.pi/4)*(u_inf5_mblock**3))
cp_les6_mblock = p_les6_mblock / (0.5*(np.pi/4)*(u_inf6_mblock**3))
cp_les7_mblock = p_les7_mblock / (0.5*(np.pi/4)*(u_inf7_mblock**3))
cp_les8_mblock = p_les8_mblock / (0.5*(np.pi/4)*(u_inf8_mblock**3))
cp_les9_mblock = p_les9_mblock / (0.5*(np.pi/4)*(u_inf9_mblock**3))
cp_les10_mblock = p_les10_mblock / (0.5*(np.pi/4)*(u_inf10_mblock**3))
cp_les11_mblock = p_les11_mblock / (0.5*(np.pi/4)*(u_inf11_mblock**3))
cp_les12_mblock = p_les12_mblock / (0.5*(np.pi/4)*(u_inf12_mblock**3))
cp_les13_mblock = p_les13_mblock / (0.5*(np.pi/4)*(u_inf13_mblock**3))
cp_les14_mblock = p_les14_mblock / (0.5*(np.pi/4)*(u_inf14_mblock**3))
cp_les15_mblock = p_les15_mblock / (0.5*(np.pi/4)*(u_inf15_mblock**3))
cp_les16_mblock = p_les16_mblock / (0.5*(np.pi/4)*(u_inf16_mblock**3))
cp_les17_mblock = p_les17_mblock / (0.5*(np.pi/4)*(u_inf17_mblock**3))

# Med Blocked, Corrected
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

# High Blocked, No Correction
cp_les1_hblock = p_les1_hblock / (0.5*(np.pi/4)*(u_inf1_hblock**3))
cp_les2_hblock = p_les2_hblock / (0.5*(np.pi/4)*(u_inf2_hblock**3))
cp_les3_hblock = p_les3_hblock / (0.5*(np.pi/4)*(u_inf3_hblock**3))
cp_les4_hblock = p_les4_hblock / (0.5*(np.pi/4)*(u_inf4_hblock**3))
cp_les5_hblock = p_les5_hblock / (0.5*(np.pi/4)*(u_inf5_hblock**3))
cp_les6_hblock = p_les6_hblock / (0.5*(np.pi/4)*(u_inf6_hblock**3))
cp_les7_hblock = p_les7_hblock / (0.5*(np.pi/4)*(u_inf7_hblock**3))
cp_les8_hblock = p_les8_hblock / (0.5*(np.pi/4)*(u_inf8_hblock**3))
cp_les9_hblock = p_les9_hblock / (0.5*(np.pi/4)*(u_inf9_hblock**3))
cp_les10_hblock = p_les10_hblock / (0.5*(np.pi/4)*(u_inf10_hblock**3))
cp_les11_hblock = p_les11_hblock / (0.5*(np.pi/4)*(u_inf11_hblock**3))
cp_les12_hblock = p_les12_hblock / (0.5*(np.pi/4)*(u_inf12_hblock**3))
cp_les13_hblock = p_les13_hblock / (0.5*(np.pi/4)*(u_inf13_hblock**3))
cp_les14_hblock = p_les14_hblock / (0.5*(np.pi/4)*(u_inf14_hblock**3))
cp_les15_hblock = p_les15_hblock / (0.5*(np.pi/4)*(u_inf15_hblock**3))
cp_les16_hblock = p_les16_hblock / (0.5*(np.pi/4)*(u_inf16_hblock**3))
cp_les17_hblock = p_les17_hblock / (0.5*(np.pi/4)*(u_inf17_hblock**3))

# High Blocked, Corrected
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

#Disk Velocities

# Med Blocked, No Correction
ud_les1_mblock = sim1_mblock.read_turb_uvel("all", steady = False)
ud_les1_mblock = ud_les1_mblock[-1]
ud_les2_mblock = sim2_mblock.read_turb_uvel("all", steady = False)
ud_les2_mblock = ud_les2_mblock[-1]
ud_les3_mblock = sim3_mblock.read_turb_uvel("all", steady = False)
ud_les3_mblock = ud_les3_mblock[-1]
ud_les4_mblock = sim4_mblock.read_turb_uvel("all", steady = False)
ud_les4_mblock = ud_les4_mblock[-1]
ud_les5_mblock = sim5_mblock.read_turb_uvel("all", steady = False)
ud_les5_mblock = ud_les5_mblock[-1]
ud_les6_mblock = sim6_mblock.read_turb_uvel("all", steady = False)
ud_les6_mblock = ud_les6_mblock[-1]
ud_les7_mblock = sim7_mblock.read_turb_uvel("all", steady = False)
ud_les7_mblock = ud_les7_mblock[-1]
ud_les8_mblock = sim8_mblock.read_turb_uvel("all", steady = False)
ud_les8_mblock = ud_les8_mblock[-1]
ud_les9_mblock = sim9_mblock.read_turb_uvel("all", steady = False)
ud_les9_mblock = ud_les9_mblock[-1]
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

# Med Blocked, Corrected
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

#High Blocked, No Correction
ud_les1_hblock = sim1_hblock.read_turb_uvel("all", steady = False)
ud_les1_hblock = ud_les1_hblock[-1]
ud_les2_hblock = sim2_hblock.read_turb_uvel("all", steady = False)
ud_les2_hblock = ud_les2_hblock[-1]
ud_les3_hblock = sim3_hblock.read_turb_uvel("all", steady = False)
ud_les3_hblock = ud_les3_hblock[-1]
ud_les4_hblock = sim4_hblock.read_turb_uvel("all", steady = False)
ud_les4_hblock = ud_les4_hblock[-1]
ud_les5_hblock = sim5_hblock.read_turb_uvel("all", steady = False)
ud_les5_hblock = ud_les5_hblock[-1]
ud_les6_hblock = sim6_hblock.read_turb_uvel("all", steady = False)
ud_les6_hblock = ud_les6_hblock[-1]
ud_les7_hblock = sim7_hblock.read_turb_uvel("all", steady = False)
ud_les7_hblock = ud_les7_hblock[-1]
ud_les8_hblock = sim8_hblock.read_turb_uvel("all", steady = False)
ud_les8_hblock = ud_les8_hblock[-1]
ud_les9_hblock = sim9_hblock.read_turb_uvel("all", steady = False)
ud_les9_hblock = ud_les9_hblock[-1]
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

#High Blocked, Corrected
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

#Thrust Force 

# Med Blocked, No Correction
thrust_les1_mblock = 2*(np.pi/4)*(ud_les1_mblock)*(u_inf1_mblock - ud_les1_mblock)
thrust_les2_mblock = 2*(np.pi/4)*(ud_les2_mblock)*(u_inf2_mblock - ud_les2_mblock)
thrust_les3_mblock = 2*(np.pi/4)*(ud_les3_mblock)*(u_inf3_mblock - ud_les3_mblock)
thrust_les4_mblock = 2*(np.pi/4)*(ud_les4_mblock)*(u_inf4_mblock - ud_les4_mblock)
thrust_les5_mblock = 2*(np.pi/4)*(ud_les5_mblock)*(u_inf5_mblock - ud_les5_mblock)
thrust_les6_mblock = 2*(np.pi/4)*(ud_les6_mblock)*(u_inf6_mblock - ud_les6_mblock)
thrust_les7_mblock = 2*(np.pi/4)*(ud_les7_mblock)*(u_inf7_mblock - ud_les7_mblock)
thrust_les8_mblock = 2*(np.pi/4)*(ud_les8_mblock)*(u_inf8_mblock - ud_les8_mblock)
thrust_les9_mblock = 2*(np.pi/4)*(ud_les9_mblock)*(u_inf9_mblock - ud_les9_mblock)
thrust_les10_mblock = 2*(np.pi/4)*(ud_les10_mblock)*(u_inf10_mblock - ud_les10_mblock)
thrust_les11_mblock = 2*(np.pi/4)*(ud_les11_mblock)*(u_inf11_mblock - ud_les11_mblock)
thrust_les12_mblock = 2*(np.pi/4)*(ud_les12_mblock)*(u_inf12_mblock - ud_les12_mblock)
thrust_les13_mblock = 2*(np.pi/4)*(ud_les13_mblock)*(u_inf13_mblock - ud_les13_mblock)
thrust_les14_mblock = 2*(np.pi/4)*(ud_les14_mblock)*(u_inf14_mblock - ud_les14_mblock)
thrust_les15_mblock = 2*(np.pi/4)*(ud_les15_mblock)*(u_inf15_mblock - ud_les15_mblock)
thrust_les16_mblock = 2*(np.pi/4)*(ud_les16_mblock)*(u_inf16_mblock - ud_les16_mblock)
thrust_les17_mblock = 2*(np.pi/4)*(ud_les17_mblock)*(u_inf17_mblock - ud_les17_mblock)

#Med Blocked, Corrected
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

#High Blocked, No Correction
thrust_les1_hblock = 2*(np.pi/4)*(ud_les1_hblock)*(u_inf1_hblock - ud_les1_hblock)
thrust_les2_hblock = 2*(np.pi/4)*(ud_les2_hblock)*(u_inf2_hblock - ud_les2_hblock)
thrust_les3_hblock = 2*(np.pi/4)*(ud_les3_hblock)*(u_inf3_hblock - ud_les3_hblock)
thrust_les4_hblock = 2*(np.pi/4)*(ud_les4_hblock)*(u_inf4_hblock - ud_les4_hblock)
thrust_les5_hblock = 2*(np.pi/4)*(ud_les5_hblock)*(u_inf5_hblock - ud_les5_hblock)
thrust_les6_hblock = 2*(np.pi/4)*(ud_les6_hblock)*(u_inf6_hblock - ud_les6_hblock)
thrust_les7_hblock = 2*(np.pi/4)*(ud_les7_hblock)*(u_inf7_hblock - ud_les7_hblock)
thrust_les8_hblock = 2*(np.pi/4)*(ud_les8_hblock)*(u_inf8_hblock - ud_les8_hblock)
thrust_les9_hblock = 2*(np.pi/4)*(ud_les9_hblock)*(u_inf9_hblock - ud_les9_hblock)
thrust_les10_hblock = 2*(np.pi/4)*(ud_les10_hblock)*(u_inf10_hblock - ud_les10_hblock)
thrust_les11_hblock = 2*(np.pi/4)*(ud_les11_hblock)*(u_inf11_hblock - ud_les11_hblock)
thrust_les12_hblock = 2*(np.pi/4)*(ud_les12_hblock)*(u_inf12_hblock - ud_les12_hblock)
thrust_les13_hblock = 2*(np.pi/4)*(ud_les13_hblock)*(u_inf13_hblock - ud_les13_hblock)
thrust_les14_hblock = 2*(np.pi/4)*(ud_les14_hblock)*(u_inf14_hblock - ud_les14_hblock)
thrust_les15_hblock = 2*(np.pi/4)*(ud_les15_hblock)*(u_inf15_hblock - ud_les15_hblock)
thrust_les16_hblock = 2*(np.pi/4)*(ud_les16_hblock)*(u_inf16_hblock - ud_les16_hblock)
thrust_les17_hblock = 2*(np.pi/4)*(ud_les17_hblock)*(u_inf17_hblock - ud_les17_hblock)

#High Blocked, Corrected
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

#Ct

# MedBlocked, No Correction
ct_les1_mblock = thrust_les1_mblock/(0.5*(np.pi/4)*(u_inf1_mblock**2))
ct_les2_mblock = thrust_les2_mblock/(0.5*(np.pi/4)*(u_inf2_mblock**2))
ct_les3_mblock = thrust_les3_mblock/(0.5*(np.pi/4)*(u_inf3_mblock**2))
ct_les4_mblock = thrust_les4_mblock/(0.5*(np.pi/4)*(u_inf4_mblock**2))
ct_les5_mblock = thrust_les5_mblock/(0.5*(np.pi/4)*(u_inf5_mblock**2))
ct_les6_mblock = thrust_les6_mblock/(0.5*(np.pi/4)*(u_inf6_mblock**2))
ct_les7_mblock = thrust_les7_mblock/(0.5*(np.pi/4)*(u_inf7_mblock**2))
ct_les8_mblock = thrust_les8_mblock/(0.5*(np.pi/4)*(u_inf8_mblock**2))
ct_les9_mblock = thrust_les9_mblock/(0.5*(np.pi/4)*(u_inf9_mblock**2))
ct_les10_mblock = thrust_les10_mblock/(0.5*(np.pi/4)*(u_inf10_mblock**2))
ct_les11_mblock = thrust_les11_mblock/(0.5*(np.pi/4)*(u_inf11_mblock**2))
ct_les12_mblock = thrust_les12_mblock/(0.5*(np.pi/4)*(u_inf12_mblock**2))
ct_les13_mblock = thrust_les13_mblock/(0.5*(np.pi/4)*(u_inf13_mblock**2))
ct_les14_mblock = thrust_les14_mblock/(0.5*(np.pi/4)*(u_inf14_mblock**2))
ct_les15_mblock = thrust_les15_mblock/(0.5*(np.pi/4)*(u_inf15_mblock**2))
ct_les16_mblock = thrust_les16_mblock/(0.5*(np.pi/4)*(u_inf16_mblock**2))
ct_les17_mblock = thrust_les17_mblock/(0.5*(np.pi/4)*(u_inf17_mblock**2))

# Med Blocked, Corrected
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

#High Blocked, No Correction
ct_les1_hblock = thrust_les1_hblock/(0.5*(np.pi/4)*(u_inf1_hblock**2))
ct_les2_hblock = thrust_les2_hblock/(0.5*(np.pi/4)*(u_inf2_hblock**2))
ct_les3_hblock = thrust_les3_hblock/(0.5*(np.pi/4)*(u_inf3_hblock**2))
ct_les4_hblock = thrust_les4_hblock/(0.5*(np.pi/4)*(u_inf4_hblock**2))
ct_les5_hblock = thrust_les5_hblock/(0.5*(np.pi/4)*(u_inf5_hblock**2))
ct_les6_hblock = thrust_les6_hblock/(0.5*(np.pi/4)*(u_inf6_hblock**2))
ct_les7_hblock = thrust_les7_hblock/(0.5*(np.pi/4)*(u_inf7_hblock**2))
ct_les8_hblock = thrust_les8_hblock/(0.5*(np.pi/4)*(u_inf8_hblock**2))
ct_les9_hblock = thrust_les9_hblock/(0.5*(np.pi/4)*(u_inf9_hblock**2))
ct_les10_hblock = thrust_les10_hblock/(0.5*(np.pi/4)*(u_inf10_hblock**2))
ct_les11_hblock = thrust_les11_hblock/(0.5*(np.pi/4)*(u_inf11_hblock**2))
ct_les12_hblock = thrust_les12_hblock/(0.5*(np.pi/4)*(u_inf12_hblock**2))
ct_les13_hblock = thrust_les13_hblock/(0.5*(np.pi/4)*(u_inf13_hblock**2))
ct_les14_hblock = thrust_les14_hblock/(0.5*(np.pi/4)*(u_inf14_hblock**2))
ct_les15_hblock = thrust_les15_hblock/(0.5*(np.pi/4)*(u_inf15_hblock**2))
ct_les16_hblock = thrust_les16_hblock/(0.5*(np.pi/4)*(u_inf16_hblock**2))
ct_les17_hblock = thrust_les17_hblock/(0.5*(np.pi/4)*(u_inf17_hblock**2))

#High Blocked, Corrected
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

#Induction Factors

# Med Blocked, No Correction
a_les1_mblock = 1-np.cbrt((p_les1_mblock/(0.5*(np.pi/4)*Ctprime1)))
a_les2_mblock = 1-np.cbrt((p_les2_mblock/(0.5*(np.pi/4)*Ctprime2)))
a_les3_mblock = 1-np.cbrt((p_les3_mblock/(0.5*(np.pi/4)*Ctprime3)))
a_les4_mblock = 1-np.cbrt((p_les4_mblock/(0.5*(np.pi/4)*Ctprime4)))
a_les5_mblock = 1-np.cbrt((p_les5_mblock/(0.5*(np.pi/4)*Ctprime5)))
a_les6_mblock = 1-np.cbrt((p_les6_mblock/(0.5*(np.pi/4)*Ctprime6)))
a_les7_mblock = 1-np.cbrt((p_les7_mblock/(0.5*(np.pi/4)*Ctprime7)))
a_les8_mblock = 1-np.cbrt((p_les8_mblock/(0.5*(np.pi/4)*Ctprime8)))
a_les9_mblock = 1
a_les10_mblock = 1-np.cbrt((p_les10_mblock/(0.5*(np.pi/4)*Ctprime10)))
a_les11_mblock = 1-np.cbrt((p_les11_mblock/(0.5*(np.pi/4)*Ctprime11)))
a_les12_mblock = 1-np.cbrt((p_les12_mblock/(0.5*(np.pi/4)*Ctprime12)))
a_les13_mblock = 1-np.cbrt((p_les13_mblock/(0.5*(np.pi/4)*Ctprime13)))
a_les14_mblock = 1-np.cbrt((p_les14_mblock/(0.5*(np.pi/4)*Ctprime14)))
a_les15_mblock = 1-np.cbrt((p_les15_mblock/(0.5*(np.pi/4)*Ctprime15)))
a_les16_mblock = 1-np.cbrt((p_les16_mblock/(0.5*(np.pi/4)*Ctprime16)))
a_les17_mblock = 1-np.cbrt((p_les17_mblock/(0.5*(np.pi/4)*Ctprime17)))

# Med Blocked, Corrected
a_les1_mblock_cor = 1-np.cbrt((p_les1_mblock_cor/(0.5*(np.pi/4)*Ctprime1)))
a_les2_mblock_cor = 1-np.cbrt((p_les2_mblock_cor/(0.5*(np.pi/4)*Ctprime2)))
a_les3_mblock_cor = 1-np.cbrt((p_les3_mblock_cor/(0.5*(np.pi/4)*Ctprime3)))
a_les4_mblock_cor = 1-np.cbrt((p_les4_mblock_cor/(0.5*(np.pi/4)*Ctprime4)))
a_les5_mblock_cor = 1-np.cbrt((p_les5_mblock_cor/(0.5*(np.pi/4)*Ctprime5)))
a_les6_mblock_cor = 1-np.cbrt((p_les6_mblock_cor/(0.5*(np.pi/4)*Ctprime6)))
a_les7_mblock_cor = 1-np.cbrt((p_les7_mblock_cor/(0.5*(np.pi/4)*Ctprime7)))
a_les8_mblock_cor = 1-np.cbrt((p_les8_mblock_cor/(0.5*(np.pi/4)*Ctprime8)))
a_les9_mblock_cor = 1
a_les10_mblock_cor = 1-np.cbrt((p_les10_mblock_cor/(0.5*(np.pi/4)*Ctprime10)))
a_les11_mblock_cor = 1-np.cbrt((p_les11_mblock_cor/(0.5*(np.pi/4)*Ctprime11)))
a_les12_mblock_cor = 1-np.cbrt((p_les12_mblock_cor/(0.5*(np.pi/4)*Ctprime12)))
a_les13_mblock_cor = 1-np.cbrt((p_les13_mblock_cor/(0.5*(np.pi/4)*Ctprime13)))
a_les14_mblock_cor = 1-np.cbrt((p_les14_mblock_cor/(0.5*(np.pi/4)*Ctprime14)))
a_les15_mblock_cor = 1-np.cbrt((p_les15_mblock_cor/(0.5*(np.pi/4)*Ctprime15)))
a_les16_mblock_cor = 1-np.cbrt((p_les16_mblock_cor/(0.5*(np.pi/4)*Ctprime16)))
a_les17_mblock_cor = 1-np.cbrt((p_les17_mblock_cor/(0.5*(np.pi/4)*Ctprime17)))

#High Blocked, No Correction
a_les1_hblock = 1-np.cbrt((p_les1_hblock/(0.5*(np.pi/4)*Ctprime1)))
a_les2_hblock = 1-np.cbrt((p_les2_hblock/(0.5*(np.pi/4)*Ctprime2)))
a_les3_hblock = 1-np.cbrt((p_les3_hblock/(0.5*(np.pi/4)*Ctprime3)))
a_les4_hblock = 1-np.cbrt((p_les4_hblock/(0.5*(np.pi/4)*Ctprime4)))
a_les5_hblock = 1-np.cbrt((p_les5_hblock/(0.5*(np.pi/4)*Ctprime5)))
a_les6_hblock = 1-np.cbrt((p_les6_hblock/(0.5*(np.pi/4)*Ctprime6)))
a_les7_hblock = 1-np.cbrt((p_les7_hblock/(0.5*(np.pi/4)*Ctprime7)))
a_les8_hblock = 1-np.cbrt((p_les8_hblock/(0.5*(np.pi/4)*Ctprime8)))
a_les9_hblock = 1
a_les10_hblock = 1-np.cbrt((p_les10_hblock/(0.5*(np.pi/4)*Ctprime10)))
a_les11_hblock = 1-np.cbrt((p_les11_hblock/(0.5*(np.pi/4)*Ctprime11)))
a_les12_hblock = 1-np.cbrt((p_les12_hblock/(0.5*(np.pi/4)*Ctprime12)))
a_les13_hblock = 1-np.cbrt((p_les13_hblock/(0.5*(np.pi/4)*Ctprime13)))
a_les14_hblock = 1-np.cbrt((p_les14_hblock/(0.5*(np.pi/4)*Ctprime14)))
a_les15_hblock = 1-np.cbrt((p_les15_hblock/(0.5*(np.pi/4)*Ctprime15)))
a_les16_hblock = 1-np.cbrt((p_les16_hblock/(0.5*(np.pi/4)*Ctprime16)))
a_les17_hblock = 1-np.cbrt((p_les17_hblock/(0.5*(np.pi/4)*Ctprime17)))

#High Blocked, Corrected
a_les1_hblock_cor = 1-np.cbrt((p_les1_hblock_cor/(0.5*(np.pi/4)*Ctprime1)))
a_les2_hblock_cor = 1-np.cbrt((p_les2_hblock_cor/(0.5*(np.pi/4)*Ctprime2)))
a_les3_hblock_cor = 1-np.cbrt((p_les3_hblock_cor/(0.5*(np.pi/4)*Ctprime3)))
a_les4_hblock_cor = 1-np.cbrt((p_les4_hblock_cor/(0.5*(np.pi/4)*Ctprime4)))
a_les5_hblock_cor = 1-np.cbrt((p_les5_hblock_cor/(0.5*(np.pi/4)*Ctprime5)))
a_les6_hblock_cor = 1-np.cbrt((p_les6_hblock_cor/(0.5*(np.pi/4)*Ctprime6)))
a_les7_hblock_cor = 1-np.cbrt((p_les7_hblock_cor/(0.5*(np.pi/4)*Ctprime7)))
a_les8_hblock_cor = 1-np.cbrt((p_les8_hblock_cor/(0.5*(np.pi/4)*Ctprime8)))
a_les9_hblock_cor = 1
a_les10_hblock_cor = 1-np.cbrt((p_les10_hblock_cor/(0.5*(np.pi/4)*Ctprime10)))
a_les11_hblock_cor = 1-np.cbrt((p_les11_hblock_cor/(0.5*(np.pi/4)*Ctprime11)))
a_les12_hblock_cor = 1-np.cbrt((p_les12_hblock_cor/(0.5*(np.pi/4)*Ctprime12)))
a_les13_hblock_cor = 1-np.cbrt((p_les13_hblock_cor/(0.5*(np.pi/4)*Ctprime13)))
a_les14_hblock_cor = 1-np.cbrt((p_les14_hblock_cor/(0.5*(np.pi/4)*Ctprime14)))
a_les15_hblock_cor = 1-np.cbrt((p_les15_hblock_cor/(0.5*(np.pi/4)*Ctprime15)))
a_les16_hblock_cor = 1-np.cbrt((p_les16_hblock_cor/(0.5*(np.pi/4)*Ctprime16)))
a_les17_hblock_cor = 1-np.cbrt((p_les17_hblock_cor/(0.5*(np.pi/4)*Ctprime17)))

#U Values

#Med Blocked, Uncorrected
U1_mblock = 1 - a_les1_mblock
U2_mblock = 1 - a_les2_mblock
U3_mblock = 1 - a_les3_mblock
U4_mblock = 1 - a_les4_mblock
U5_mblock = 1 - a_les5_mblock
U6_mblock = 1 - a_les6_mblock
U7_mblock = 1 - a_les7_mblock
U8_mblock = 1 - a_les8_mblock
U9_mblock = 1
U10_mblock = 1 - a_les10_mblock
U11_mblock = 1 - a_les11_mblock
U12_mblock = 1 - a_les12_mblock
U13_mblock = 1 - a_les13_mblock
U14_mblock = 1 - a_les14_mblock
U15_mblock = 1 - a_les15_mblock
U16_mblock = 1 - a_les16_mblock
U17_mblock = 1 - a_les17_mblock

#Med Blocked, Corrected
U1_mblock_cor = 1-a_les1_mblock_cor
U2_mblock_cor = 1-a_les2_mblock_cor
U3_mblock_cor = 1-a_les3_mblock_cor
U4_mblock_cor = 1-a_les4_mblock_cor
U5_mblock_cor = 1-a_les5_mblock_cor
U6_mblock_cor = 1-a_les6_mblock_cor
U7_mblock_cor = 1-a_les7_mblock_cor
U8_mblock_cor = 1-a_les8_mblock_cor
U9_mblock_cor = 1
U10_mblock_cor = 1-a_les10_mblock_cor
U11_mblock_cor = 1-a_les11_mblock_cor
U12_mblock_cor = 1-a_les12_mblock_cor
U13_mblock_cor = 1-a_les13_mblock_cor
U14_mblock_cor = 1-a_les14_mblock_cor
U15_mblock_cor = 1-a_les15_mblock_cor
U16_mblock_cor = 1-a_les16_mblock_cor
U17_mblock_cor = 1-a_les17_mblock_cor

#High Blocked, Uncorrected
U1_hblock = 1 - a_les1_hblock
U2_hblock = 1 - a_les2_hblock
U3_hblock = 1 - a_les3_hblock
U4_hblock = 1 - a_les4_hblock
U5_hblock = 1 - a_les5_hblock
U6_hblock = 1 - a_les6_hblock
U7_hblock = 1 - a_les7_hblock
U8_hblock = 1 - a_les8_hblock
U9_hblock = 1
U10_hblock = 1 - a_les10_hblock
U11_hblock = 1 - a_les11_hblock
U12_hblock = 1 - a_les12_hblock
U13_hblock = 1 - a_les13_hblock
U14_hblock = 1 - a_les14_hblock
U15_hblock = 1 - a_les15_hblock
U16_hblock = 1 - a_les16_hblock
U17_hblock = 1 - a_les17_hblock

#High Blocked, Corrected
U1_hblock_cor = 1 - a_les1_hblock_cor
U2_hblock_cor = 1 - a_les2_hblock_cor
U3_hblock_cor = 1 - a_les3_hblock_cor
U4_hblock_cor = 1 - a_les4_hblock_cor
U5_hblock_cor = 1 - a_les5_hblock_cor
U6_hblock_cor = 1 - a_les6_hblock_cor
U7_hblock_cor = 1 - a_les7_hblock_cor
U8_hblock_cor = 1 - a_les8_hblock_cor
U9_hblock_cor = 1
U10_hblock_cor = 1 - a_les10_hblock_cor
U11_hblock_cor = 1 - a_les11_hblock_cor
U12_hblock_cor = 1 - a_les12_hblock_cor
U13_hblock_cor = 1 - a_les13_hblock_cor
U14_hblock_cor = 1 - a_les14_hblock_cor
U15_hblock_cor = 1 - a_les15_hblock_cor
U16_hblock_cor = 1 - a_les16_hblock_cor
U17_hblock_cor = 1 - a_les17_hblock_cor

#V0/Vprime

#Unblocked, Uncorrected

#Med Blocked, Uncorrected
V0_Vp1_mblock = 1/(U1_mblock + (ct_les1_mblock/(4*U1_mblock)))
V0_Vp2_mblock = 1/(U2_mblock + (ct_les2_mblock/(4*U2_mblock)))
V0_Vp3_mblock = 1/(U3_mblock + (ct_les3_mblock/(4*U3_mblock)))
V0_Vp4_mblock = 1/(U4_mblock + (ct_les4_mblock/(4*U4_mblock)))
V0_Vp5_mblock = 1/(U5_mblock + (ct_les5_mblock/(4*U5_mblock)))
V0_Vp6_mblock = 1/(U6_mblock + (ct_les6_mblock/(4*U6_mblock)))
V0_Vp7_mblock = 1/(U7_mblock + (ct_les7_mblock/(4*U7_mblock)))
V0_Vp8_mblock = 1/(U8_mblock + (ct_les8_mblock/(4*U8_mblock)))
V0_Vp9_mblock = 1/(U9_mblock + (ct_les9_mblock/(4*U9_mblock)))
V0_Vp10_mblock = 1/(U10_mblock + (ct_les10_mblock/(4*U10_mblock)))
V0_Vp11_mblock = 1/(U11_mblock + (ct_les11_mblock/(4*U11_mblock)))
V0_Vp12_mblock = 1/(U12_mblock + (ct_les12_mblock/(4*U12_mblock)))
V0_Vp13_mblock = 1/(U13_mblock + (ct_les13_mblock/(4*U13_mblock)))
V0_Vp14_mblock = 1/(U14_mblock + (ct_les14_mblock/(4*U14_mblock)))
V0_Vp15_mblock = 1/(U15_mblock + (ct_les15_mblock/(4*U15_mblock)))
V0_Vp16_mblock = 1/(U16_mblock + (ct_les16_mblock/(4*U16_mblock)))
V0_Vp17_mblock = 1/(U17_mblock + (ct_les17_mblock/(4*U17_mblock)))

#Med Blocked, Corrected
V0_Vp1_mblock_cor = 1/(U1_mblock_cor + (ct_les1_mblock_cor/(4*U1_mblock_cor)))
V0_Vp2_mblock_cor = 1/(U2_mblock_cor + (ct_les2_mblock_cor/(4*U2_mblock_cor)))
V0_Vp3_mblock_cor = 1/(U3_mblock_cor + (ct_les3_mblock_cor/(4*U3_mblock_cor)))
V0_Vp4_mblock_cor = 1/(U4_mblock_cor + (ct_les4_mblock_cor/(4*U4_mblock_cor)))
V0_Vp5_mblock_cor = 1/(U5_mblock_cor + (ct_les5_mblock_cor/(4*U5_mblock_cor)))
V0_Vp6_mblock_cor = 1/(U6_mblock_cor + (ct_les6_mblock_cor/(4*U6_mblock_cor)))
V0_Vp7_mblock_cor = 1/(U7_mblock_cor + (ct_les7_mblock_cor/(4*U7_mblock_cor)))
V0_Vp8_mblock_cor = 1/(U8_mblock_cor + (ct_les8_mblock_cor/(4*U8_mblock_cor)))
V0_Vp9_mblock_cor = 1/(U9_mblock_cor + (ct_les9_mblock_cor/(4*U9_mblock_cor)))
V0_Vp10_mblock_cor = 1/(U10_mblock_cor + (ct_les10_mblock_cor/(4*U10_mblock_cor)))
V0_Vp11_mblock_cor = 1/(U11_mblock_cor + (ct_les11_mblock_cor/(4*U11_mblock_cor)))
V0_Vp12_mblock_cor = 1/(U12_mblock_cor + (ct_les12_mblock_cor/(4*U12_mblock_cor)))
V0_Vp13_mblock_cor = 1/(U13_mblock_cor + (ct_les13_mblock_cor/(4*U13_mblock_cor)))
V0_Vp14_mblock_cor = 1/(U14_mblock_cor + (ct_les14_mblock_cor/(4*U14_mblock_cor)))
V0_Vp15_mblock_cor = 1/(U15_mblock_cor + (ct_les15_mblock_cor/(4*U15_mblock_cor)))
V0_Vp16_mblock_cor = 1/(U16_mblock_cor + (ct_les16_mblock_cor/(4*U16_mblock_cor)))
V0_Vp17_mblock_cor = 1/(U17_mblock_cor + (ct_les17_mblock_cor/(4*U17_mblock_cor)))

#High Blocked, Uncorrected
V0_Vp1_hblock = 1/(U1_hblock + (ct_les1_hblock/(4*U1_hblock)))
V0_Vp2_hblock = 1/(U2_hblock + (ct_les2_hblock/(4*U2_hblock)))
V0_Vp3_hblock = 1/(U3_hblock + (ct_les3_hblock/(4*U3_hblock)))
V0_Vp4_hblock = 1/(U4_hblock + (ct_les4_hblock/(4*U4_hblock)))
V0_Vp5_hblock = 1/(U5_hblock + (ct_les5_hblock/(4*U5_hblock)))
V0_Vp6_hblock = 1/(U6_hblock + (ct_les6_hblock/(4*U6_hblock)))
V0_Vp7_hblock = 1/(U7_hblock + (ct_les7_hblock/(4*U7_hblock)))
V0_Vp8_hblock = 1/(U8_hblock + (ct_les8_hblock/(4*U8_hblock)))
V0_Vp9_hblock = 1/(U9_hblock + (ct_les9_hblock/(4*U9_hblock)))
V0_Vp10_hblock = 1/(U10_hblock + (ct_les10_hblock/(4*U10_hblock)))
V0_Vp11_hblock = 1/(U11_hblock + (ct_les11_hblock/(4*U11_hblock)))
V0_Vp12_hblock = 1/(U12_hblock + (ct_les12_hblock/(4*U12_hblock)))
V0_Vp13_hblock = 1/(U13_hblock + (ct_les13_hblock/(4*U13_hblock)))
V0_Vp14_hblock = 1/(U14_hblock + (ct_les14_hblock/(4*U14_hblock)))
V0_Vp15_hblock = 1/(U15_hblock + (ct_les15_hblock/(4*U15_hblock)))
V0_Vp16_hblock = 1/(U16_hblock + (ct_les16_hblock/(4*U16_hblock)))
V0_Vp17_hblock = 1/(U17_hblock + (ct_les17_hblock/(4*U17_hblock)))

#High Blocked, Corrected
V0_Vp1_hblock_cor = 1/(U1_hblock_cor + (ct_les1_hblock_cor/(4*U1_mblock_cor)))
V0_Vp2_hblock_cor = 1/(U2_hblock_cor + (ct_les2_hblock_cor/(4*U2_mblock_cor)))
V0_Vp3_hblock_cor = 1/(U3_hblock_cor + (ct_les3_hblock_cor/(4*U3_mblock_cor)))
V0_Vp4_hblock_cor = 1/(U4_hblock_cor + (ct_les4_hblock_cor/(4*U4_mblock_cor)))
V0_Vp5_hblock_cor = 1/(U5_hblock_cor + (ct_les5_hblock_cor/(4*U5_mblock_cor)))
V0_Vp6_hblock_cor = 1/(U6_hblock_cor + (ct_les6_hblock_cor/(4*U6_mblock_cor)))
V0_Vp7_hblock_cor = 1/(U7_hblock_cor + (ct_les7_hblock_cor/(4*U7_mblock_cor)))
V0_Vp8_hblock_cor = 1/(U8_hblock_cor + (ct_les8_hblock_cor/(4*U8_mblock_cor)))
V0_Vp9_hblock_cor = 1/(U9_hblock_cor + (ct_les9_hblock_cor/(4*U9_mblock_cor)))
V0_Vp10_hblock_cor = 1/(U10_hblock_cor + (ct_les10_hblock_cor/(4*U10_mblock_cor)))
V0_Vp11_hblock_cor = 1/(U11_hblock_cor + (ct_les11_hblock_cor/(4*U11_mblock_cor)))
V0_Vp12_hblock_cor = 1/(U12_hblock_cor + (ct_les12_hblock_cor/(4*U12_mblock_cor)))
V0_Vp13_hblock_cor = 1/(U13_hblock_cor + (ct_les13_hblock_cor/(4*U13_mblock_cor)))
V0_Vp14_hblock_cor = 1/(U14_hblock_cor + (ct_les14_hblock_cor/(4*U14_mblock_cor)))
V0_Vp15_hblock_cor = 1/(U15_hblock_cor + (ct_les15_hblock_cor/(4*U15_mblock_cor)))
V0_Vp16_hblock_cor = 1/(U16_hblock_cor + (ct_les16_hblock_cor/(4*U16_mblock_cor)))
V0_Vp17_hblock_cor = 1/(U17_hblock_cor + (ct_les17_hblock_cor/(4*U17_mblock_cor)))

#Cp Prime Values

#Med Blocked, No Correction
cp_prime1_mblock = cp_les1_mblock*(V0_Vp1_mblock**3)
cp_prime2_mblock = cp_les2_mblock*(V0_Vp2_mblock**3)
cp_prime3_mblock = cp_les3_mblock*(V0_Vp3_mblock**3)
cp_prime4_mblock = cp_les4_mblock*(V0_Vp4_mblock**3)
cp_prime5_mblock = cp_les5_mblock*(V0_Vp5_mblock**3)
cp_prime6_mblock = cp_les6_mblock*(V0_Vp6_mblock**3)
cp_prime7_mblock = cp_les7_mblock*(V0_Vp7_mblock**3)
cp_prime8_mblock = cp_les8_mblock*(V0_Vp8_mblock**3)
cp_prime9_mblock = cp_les9_mblock*(V0_Vp9_mblock**3)
cp_prime10_mblock = cp_les10_mblock*(V0_Vp10_mblock**3)
cp_prime11_mblock = cp_les11_mblock*(V0_Vp11_mblock**3)
cp_prime12_mblock = cp_les12_mblock*(V0_Vp12_mblock**3)
cp_prime13_mblock = cp_les13_mblock*(V0_Vp13_mblock**3)
cp_prime14_mblock = cp_les14_mblock*(V0_Vp14_mblock**3)
cp_prime15_mblock = cp_les15_mblock*(V0_Vp15_mblock**3)
cp_prime16_mblock = cp_les16_mblock*(V0_Vp16_mblock**3)
cp_prime17_mblock = cp_les17_mblock*(V0_Vp17_mblock*3)

#Med Blocked, Corrected
cp_prime1_mblock_cor = cp_les1_mblock_cor*(V0_Vp1_mblock_cor**3)
cp_prime2_mblock_cor = cp_les2_mblock_cor*(V0_Vp2_mblock_cor**3)
cp_prime3_mblock_cor = cp_les3_mblock_cor*(V0_Vp3_mblock_cor**3)
cp_prime4_mblock_cor = cp_les4_mblock_cor*(V0_Vp4_mblock_cor**3)
cp_prime5_mblock_cor = cp_les5_mblock_cor*(V0_Vp5_mblock_cor**3)
cp_prime6_mblock_cor = cp_les6_mblock_cor*(V0_Vp6_mblock_cor**3)
cp_prime7_mblock_cor = cp_les7_mblock_cor*(V0_Vp7_mblock_cor**3)
cp_prime8_mblock_cor = cp_les8_mblock_cor*(V0_Vp8_mblock_cor**3)
cp_prime9_mblock_cor = cp_les9_mblock_cor*(V0_Vp9_mblock_cor**3)
cp_prime10_mblock_cor = cp_les10_mblock_cor*(V0_Vp10_mblock_cor**3)
cp_prime11_mblock_cor = cp_les11_mblock_cor*(V0_Vp11_mblock_cor**3)
cp_prime12_mblock_cor = cp_les12_mblock_cor*(V0_Vp12_mblock_cor**3)
cp_prime13_mblock_cor = cp_les13_mblock_cor*(V0_Vp13_mblock_cor**3)
cp_prime14_mblock_cor = cp_les14_mblock_cor*(V0_Vp14_mblock_cor**3)
cp_prime15_mblock_cor = cp_les15_mblock_cor*(V0_Vp15_mblock_cor**3)
cp_prime16_mblock_cor = cp_les16_mblock_cor*(V0_Vp16_mblock_cor**3)
cp_prime17_mblock_cor = cp_les17_mblock_cor*(V0_Vp17_mblock_cor**3)

#High Blocked, Uncorrected
cp_prime1_hblock = cp_les1_hblock*(V0_Vp1_hblock**3)
cp_prime2_hblock = cp_les2_hblock*(V0_Vp2_hblock**3)
cp_prime3_hblock = cp_les3_hblock*(V0_Vp3_hblock**3)
cp_prime4_hblock = cp_les4_hblock*(V0_Vp4_hblock**3)
cp_prime5_hblock = cp_les5_hblock*(V0_Vp5_hblock**3)
cp_prime6_hblock = cp_les6_hblock*(V0_Vp6_hblock**3)
cp_prime7_hblock = cp_les7_hblock*(V0_Vp7_hblock**3)
cp_prime8_hblock = cp_les8_hblock*(V0_Vp8_hblock**3)
cp_prime9_hblock = cp_les9_hblock*(V0_Vp9_hblock**3)
cp_prime10_hblock = cp_les10_hblock*(V0_Vp10_hblock**3)
cp_prime11_hblock = cp_les11_hblock*(V0_Vp11_hblock**3)
cp_prime12_hblock = cp_les12_hblock*(V0_Vp12_hblock**3)
cp_prime13_hblock = cp_les13_hblock*(V0_Vp13_hblock**3)
cp_prime14_hblock = cp_les14_hblock*(V0_Vp14_hblock**3)
cp_prime15_hblock = cp_les15_hblock*(V0_Vp15_hblock**3)
cp_prime16_hblock = cp_les16_hblock*(V0_Vp16_hblock**3)
cp_prime17_hblock = cp_les17_hblock*(V0_Vp17_hblock**3)

#High Blocked, Corrected
cp_prime1_hblock_cor = cp_les1_hblock_cor*(V0_Vp1_hblock_cor**3)
cp_prime2_hblock_cor = cp_les2_hblock_cor*(V0_Vp2_hblock_cor**3)
cp_prime3_hblock_cor = cp_les3_hblock_cor*(V0_Vp3_hblock_cor**3)
cp_prime4_hblock_cor = cp_les4_hblock_cor*(V0_Vp4_hblock_cor**3)
cp_prime5_hblock_cor = cp_les5_hblock_cor*(V0_Vp5_hblock_cor**3)
cp_prime6_hblock_cor = cp_les6_hblock_cor*(V0_Vp6_hblock_cor**3)
cp_prime7_hblock_cor = cp_les7_hblock_cor*(V0_Vp7_hblock_cor**3)
cp_prime8_hblock_cor = cp_les8_hblock_cor*(V0_Vp8_hblock_cor**3)
cp_prime9_hblock_cor = cp_les9_hblock_cor*(V0_Vp9_hblock_cor**3)
cp_prime10_hblock_cor = cp_les10_hblock_cor*(V0_Vp10_hblock_cor**3)
cp_prime11_hblock_cor = cp_les11_hblock_cor*(V0_Vp11_hblock_cor**3)
cp_prime12_hblock_cor = cp_les12_hblock_cor*(V0_Vp12_hblock_cor**3)
cp_prime13_hblock_cor = cp_les13_hblock_cor*(V0_Vp13_hblock_cor**3)
cp_prime14_hblock_cor = cp_les14_hblock_cor*(V0_Vp14_hblock_cor**3)
cp_prime15_hblock_cor = cp_les15_hblock_cor*(V0_Vp15_hblock_cor**3)
cp_prime16_hblock_cor = cp_les16_hblock_cor*(V0_Vp16_hblock_cor**3)
cp_prime17_hblock_cor = cp_les17_hblock_cor*(V0_Vp17_hblock_cor**3)

#Ct Prime Values

#Med Blocked, No Correction
ct_prime1_mblock = ct_les1_mblock*(V0_Vp1_mblock**2)
ct_prime2_mblock = ct_les2_mblock*(V0_Vp2_mblock**2)
ct_prime3_mblock = ct_les3_mblock*(V0_Vp3_mblock**2)
ct_prime4_mblock = ct_les4_mblock*(V0_Vp4_mblock**2)
ct_prime5_mblock = ct_les5_mblock*(V0_Vp5_mblock**2)
ct_prime6_mblock = ct_les6_mblock*(V0_Vp6_mblock**2)
ct_prime7_mblock = ct_les7_mblock*(V0_Vp7_mblock**2)
ct_prime8_mblock = ct_les8_mblock*(V0_Vp8_mblock**2)
ct_prime9_mblock = ct_les9_mblock*(V0_Vp9_mblock**2)
ct_prime10_mblock = ct_les10_mblock*(V0_Vp10_mblock**2)
ct_prime11_mblock = ct_les11_mblock*(V0_Vp11_mblock**2)
ct_prime12_mblock = ct_les12_mblock*(V0_Vp12_mblock**2)
ct_prime13_mblock = ct_les13_mblock*(V0_Vp13_mblock**2)
ct_prime14_mblock = ct_les14_mblock*(V0_Vp14_mblock**2)
ct_prime15_mblock = ct_les15_mblock*(V0_Vp15_mblock**2)
ct_prime16_mblock = ct_les16_mblock*(V0_Vp16_mblock**2)
ct_prime17_mblock = ct_les17_mblock*(V0_Vp17_mblock*2)

#Med Blocked, Corrected
ct_prime1_mblock_cor = ct_les1_mblock_cor*(V0_Vp1_mblock_cor**2)
ct_prime2_mblock_cor = ct_les2_mblock_cor*(V0_Vp2_mblock_cor**2)
ct_prime3_mblock_cor = ct_les3_mblock_cor*(V0_Vp3_mblock_cor**2)
ct_prime4_mblock_cor = ct_les4_mblock_cor*(V0_Vp4_mblock_cor**2)
ct_prime5_mblock_cor = ct_les5_mblock_cor*(V0_Vp5_mblock_cor**2)
ct_prime6_mblock_cor = ct_les6_mblock_cor*(V0_Vp6_mblock_cor**2)
ct_prime7_mblock_cor = ct_les7_mblock_cor*(V0_Vp7_mblock_cor**2)
ct_prime8_mblock_cor = ct_les8_mblock_cor*(V0_Vp8_mblock_cor**2)
ct_prime9_mblock_cor = ct_les9_mblock_cor*(V0_Vp9_mblock_cor**2)
ct_prime10_mblock_cor = ct_les10_mblock_cor*(V0_Vp10_mblock_cor**2)
ct_prime11_mblock_cor = ct_les11_mblock_cor*(V0_Vp11_mblock_cor**2)
ct_prime12_mblock_cor = ct_les12_mblock_cor*(V0_Vp12_mblock_cor**2)
ct_prime13_mblock_cor = ct_les13_mblock_cor*(V0_Vp13_mblock_cor**2)
ct_prime14_mblock_cor = ct_les14_mblock_cor*(V0_Vp14_mblock_cor**2)
ct_prime15_mblock_cor = ct_les15_mblock_cor*(V0_Vp15_mblock_cor**2)
ct_prime16_mblock_cor = ct_les16_mblock_cor*(V0_Vp16_mblock_cor**2)
ct_prime17_mblock_cor = ct_les17_mblock_cor*(V0_Vp17_mblock_cor**2)

#High Blocked, Uncorrected
ct_prime1_hblock = ct_les1_hblock*(V0_Vp1_hblock**2)
ct_prime2_hblock = ct_les2_hblock*(V0_Vp2_hblock**2)
ct_prime3_hblock = ct_les3_hblock*(V0_Vp3_hblock**2)
ct_prime4_hblock = ct_les4_hblock*(V0_Vp4_hblock**2)
ct_prime5_hblock = ct_les5_hblock*(V0_Vp5_hblock**2)
ct_prime6_hblock = ct_les6_hblock*(V0_Vp6_hblock*2)
ct_prime7_hblock = ct_les7_hblock*(V0_Vp7_hblock**2)
ct_prime8_hblock = ct_les8_hblock*(V0_Vp8_hblock**2)
ct_prime9_hblock = ct_les9_hblock*(V0_Vp9_hblock**2)
ct_prime10_hblock = ct_les10_hblock*(V0_Vp10_hblock**2)
ct_prime11_hblock = ct_les11_hblock*(V0_Vp11_hblock**2)
ct_prime12_hblock = ct_les12_hblock*(V0_Vp12_hblock**2)
ct_prime13_hblock = ct_les13_hblock*(V0_Vp13_hblock**2)
ct_prime14_hblock = ct_les14_hblock*(V0_Vp14_hblock**2)
ct_prime15_hblock = ct_les15_hblock*(V0_Vp15_hblock**2)
ct_prime16_hblock = ct_les16_hblock*(V0_Vp16_hblock**2)
ct_prime17_hblock = ct_les17_hblock*(V0_Vp17_hblock**2)

#High Blocked, Corrected
ct_prime1_hblock_cor = ct_les1_hblock_cor*(V0_Vp1_hblock_cor**2)
ct_prime2_hblock_cor = ct_les2_hblock_cor*(V0_Vp2_hblock_cor**2)
ct_prime3_hblock_cor = ct_les3_hblock_cor*(V0_Vp3_hblock_cor**2)
ct_prime4_hblock_cor = ct_les4_hblock_cor*(V0_Vp4_hblock_cor**2)
ct_prime5_hblock_cor = ct_les5_hblock_cor*(V0_Vp5_hblock_cor**2)
ct_prime6_hblock_cor = ct_les6_hblock_cor*(V0_Vp6_hblock_cor**2)
ct_prime7_hblock_cor = ct_les7_hblock_cor*(V0_Vp7_hblock_cor**2)
ct_prime8_hblock_cor = ct_les8_hblock_cor*(V0_Vp8_hblock_cor**2)
ct_prime9_hblock_cor = ct_les9_hblock_cor*(V0_Vp9_hblock_cor**2)
ct_prime10_hblock_cor = ct_les10_hblock_cor*(V0_Vp10_hblock_cor**2)
ct_prime11_hblock_cor = ct_les11_hblock_cor*(V0_Vp11_hblock_cor**2)
ct_prime12_hblock_cor = ct_les12_hblock_cor*(V0_Vp12_hblock_cor**2)
ct_prime13_hblock_cor = ct_les13_hblock_cor*(V0_Vp13_hblock_cor**2)
ct_prime14_hblock_cor = ct_les14_hblock_cor*(V0_Vp14_hblock_cor**2)
ct_prime15_hblock_cor = ct_les15_hblock_cor*(V0_Vp15_hblock_cor**2)
ct_prime16_hblock_cor = ct_les16_hblock_cor*(V0_Vp16_hblock_cor**2)
ct_prime17_hblock_cor = ct_les17_hblock_cor*(V0_Vp17_hblock_cor**2)

#Arrays

# Arrays (homogeneous, no missing or inhomogeneous elements)
Ctprime_plot = [
    Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9,
    Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17
]
cp_prime_mblock_plot = [
    cp_prime1_mblock, cp_prime2_mblock, cp_prime3_mblock, cp_prime4_mblock, cp_prime5_mblock, cp_prime6_mblock, cp_prime7_mblock, cp_prime8_mblock, cp_prime9_mblock,
    cp_prime10_mblock, cp_prime11_mblock, cp_prime12_mblock, cp_prime13_mblock, cp_prime14_mblock, cp_prime15_mblock, cp_prime16_mblock, cp_prime17_mblock
]
cp_prime_mblock_cor_plot = [
    cp_prime1_mblock_cor, cp_prime2_mblock_cor, cp_prime3_mblock_cor, cp_prime4_mblock_cor, cp_prime5_mblock_cor, cp_prime6_mblock_cor, cp_prime7_mblock_cor, cp_prime8_mblock_cor, cp_prime9_mblock_cor,
    cp_prime10_mblock_cor, cp_prime11_mblock_cor, cp_prime12_mblock_cor, cp_prime13_mblock_cor, cp_prime14_mblock_cor, cp_prime15_mblock_cor, cp_prime16_mblock_cor, cp_prime17_mblock_cor
]
cp_prime_mblock_cor = np.hstack(cp_prime_mblock_cor_plot)
cp_prime_mblock_cor = cp_prime_mblock_cor[~np.isnan(cp_prime_mblock_cor)]

cp_prime_hblock_plot = [
    cp_prime1_hblock, cp_prime2_hblock, cp_prime3_hblock, cp_prime4_hblock, cp_prime5_hblock, cp_prime6_hblock, cp_prime7_hblock, cp_prime8_hblock, cp_prime9_hblock,
    cp_prime10_hblock, cp_prime11_hblock, cp_prime12_hblock, cp_prime13_hblock, cp_prime14_hblock, cp_prime15_hblock, cp_prime16_hblock, cp_prime17_hblock
]
cp_prime_hblock_cor_plot = [
    cp_prime1_hblock_cor, cp_prime2_hblock_cor, cp_prime3_hblock_cor, cp_prime4_hblock_cor, cp_prime5_hblock_cor, cp_prime6_hblock_cor, cp_prime7_hblock_cor, cp_prime8_hblock_cor, cp_prime9_hblock_cor,
    cp_prime10_hblock_cor, cp_prime11_hblock_cor, cp_prime12_hblock_cor, cp_prime13_hblock_cor, cp_prime14_hblock_cor, cp_prime15_hblock_cor, cp_prime16_hblock_cor, cp_prime17_hblock_cor
]
ct_prime_mblock_plot = [
    ct_prime1_mblock, ct_prime2_mblock, ct_prime3_mblock, ct_prime4_mblock, ct_prime5_mblock, ct_prime6_mblock, ct_prime7_mblock, ct_prime8_mblock, ct_prime9_mblock,
    ct_prime10_mblock, ct_prime11_mblock, ct_prime12_mblock, ct_prime13_mblock, ct_prime14_mblock, ct_prime15_mblock, ct_prime16_mblock, ct_prime17_mblock
]
ct_prime_mblock_cor_plot = [
    ct_prime1_mblock_cor, ct_prime2_mblock_cor, ct_prime3_mblock_cor, ct_prime4_mblock_cor, ct_prime5_mblock_cor, ct_prime6_mblock_cor, ct_prime7_mblock_cor, ct_prime8_mblock_cor, ct_prime9_mblock_cor,
    ct_prime10_mblock_cor, ct_prime11_mblock_cor, ct_prime12_mblock_cor, ct_prime13_mblock_cor, ct_prime14_mblock_cor, ct_prime15_mblock_cor, ct_prime16_mblock_cor, ct_prime17_mblock_cor
]
ct_prime_mblock_cor = np.hstack(ct_prime_mblock_cor_plot)
ct_prime_mblock_cor = ct_prime_mblock_cor[~np.isnan(ct_prime_mblock_cor)]

ct_prime_hblock_plot = [
    ct_prime1_hblock, ct_prime2_hblock, ct_prime3_hblock, ct_prime4_hblock, ct_prime5_hblock, ct_prime6_hblock, ct_prime7_hblock, ct_prime8_hblock, ct_prime9_hblock,
    ct_prime10_hblock, ct_prime11_hblock, ct_prime12_hblock, ct_prime13_hblock, ct_prime14_hblock, ct_prime15_hblock, ct_prime16_hblock, ct_prime17_hblock
]
ct_prime_hblock_cor_plot = [
    ct_prime1_hblock_cor, ct_prime2_hblock_cor, ct_prime3_hblock_cor, ct_prime4_hblock_cor, ct_prime5_hblock_cor, ct_prime6_hblock_cor, ct_prime7_hblock_cor, ct_prime8_hblock_cor, ct_prime9_hblock_cor,
    ct_prime10_hblock_cor, ct_prime11_hblock_cor, ct_prime12_hblock_cor, ct_prime13_hblock_cor, ct_prime14_hblock_cor, ct_prime15_hblock_cor, ct_prime16_hblock_cor, ct_prime17_hblock_cor
]

#Plotting
#Cp
plt.figure(figsize = (9,6))
plt.scatter(Ctprime_plot[1:16], cp_prime_mblock_plot[1:16], color = 'blue', label = '10 pct Blockage Uncorrected')
plt.scatter(Ctprime_plot[1:16], cp_prime_mblock_cor_plot[1:16], color = 'orange', label = '10 pct Blockage Corrected')
plt.scatter(Ctprime_plot[1:16], cp_prime_hblock_plot[1:16], color = 'green', label = '35 pct Blockage Uncorrected')
plt.scatter(Ctprime_plot[1:16], cp_prime_hblock_cor_plot[1:16], color = 'red', label = '35 pct Blockage Corrected')
plt.title('Emperical Blockage Correction Results (Mikkelsen/Sorensen 2002)')
plt.ylim(-1, 1)
plt.xlabel('Ct Prime')
plt.ylabel('Cp Prime (Equivalent Cp in Unblocked Flow)')
plt.legend()
plt.savefig('./cp_prime_comapare_ind')

#Ct
plt.figure(figsize = (9,6))
plt.scatter(Ctprime_plot[1:16], ct_prime_mblock_plot[1:16], color = 'blue', label = '10 pct Blockage Uncorrected')
plt.scatter(Ctprime_plot[1:16], ct_prime_mblock_cor_plot[1:16], color = 'orange', label = '10 pct Blockage Corrected')
plt.scatter(Ctprime_plot[1:16], ct_prime_hblock_plot[1:16], color = 'green', label = '35 pct Blockage Uncorrected')
plt.scatter(Ctprime_plot[1:16], ct_prime_hblock_cor_plot[1:16], color = 'red', label = '35 pct Blockage Corrected')
plt.title('Emperical Blockage Correction Results (Mikkelsen/Sorensen 2002)')
plt.ylim(-1, 1)
plt.xlabel('Ct Prime')
plt.ylabel('Ct Prime (Equivalent Ct in Unblocked Flow)')
plt.legend()
plt.savefig('./ct_prime_comapare_ind')

#Save Arrays
np.save('./CtPrime_Values', Ctprime_plot)
np.save('./cp_prime_mblock_ms', cp_prime_mblock_plot)
np.save('./ct_prime_mblock_ms', ct_prime_mblock_plot)
np.save('./cp_prime_mblock_cor_ms', cp_prime_mblock_cor)
np.save('./ct_prime_mblock_cor_ms', ct_prime_mblock_cor)
np.save('./cp_prime_hblock_ms', cp_prime_hblock_plot)
np.save('./ct_prime_hblock_ms', ct_prime_hblock_plot)
np.save('./cp_prime_hblock_cor_ms', cp_prime_hblock_cor_plot)
np.save('./ct_prime_hblock_cor_ms', ct_prime_hblock_cor_plot)

