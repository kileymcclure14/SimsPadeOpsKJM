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

#Blocked, No Correction
sim1_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0000")
sim1_block = pio.BudgetIO("Data/B_0000_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0001")
sim2_block = pio.BudgetIO("Data/B_0000_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0002")
sim3_block = pio.BudgetIO("Data/B_0000_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0003")
sim4_block = pio.BudgetIO("Data/B_0000_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0004")
sim5_block = pio.BudgetIO("Data/B_0000_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0005")
sim6_block = pio.BudgetIO("Data/B_0000_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0006")
sim7_block = pio.BudgetIO("Data/B_0000_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0007")
sim8_block = pio.BudgetIO("Data/B_0000_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0008")
sim9_block = pio.BudgetIO("Data/B_0000_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0009")
sim10_block = pio.BudgetIO("Data/B_0000_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0010")
sim11_block = pio.BudgetIO("Data/B_0000_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0011")
sim12_block = pio.BudgetIO("Data/B_0000_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0012")
sim13_block = pio.BudgetIO("Data/B_0000_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0013")
sim14_block = pio.BudgetIO("Data/B_0000_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0014")
sim15_block = pio.BudgetIO("Data/B_0000_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0015")
sim16_block = pio.BudgetIO("Data/B_0000_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_block = os.path.join(au.DATA_PATH, "B_0000_Files/Sim_0016")
sim17_block = pio.BudgetIO("Data/B_0000_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

#Blocked, Corrected
sim1_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0000")
sim1_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0001")
sim2_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0002")
sim3_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0003")
sim4_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0003", padeops = True, runid = 1, normalize_origin = "turbine")

sim5_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0004")
sim5_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0004", padeops = True, runid = 1, normalize_origin = "turbine")

sim6_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0005")
sim6_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0005", padeops = True, runid = 1, normalize_origin = "turbine")

sim7_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0006")
sim7_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0006", padeops = True, runid = 1, normalize_origin = "turbine")

sim8_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0007")
sim8_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0007", padeops = True, runid = 1, normalize_origin = "turbine")

sim9_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0008")
sim9_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0008", padeops = True, runid = 1, normalize_origin = "turbine")

sim10_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0009")
sim10_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0009", padeops = True, runid = 1, normalize_origin = "turbine")

sim11_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0010")
sim11_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0010", padeops = True, runid = 1, normalize_origin = "turbine")

sim12_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0011")
sim12_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0011", padeops = True, runid = 1, normalize_origin = "turbine")

sim13_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0012")
sim13_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0012", padeops = True, runid = 1, normalize_origin = "turbine")

sim14_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0013")
sim14_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0013", padeops = True, runid = 1, normalize_origin = "turbine")

sim15_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0014")
sim15_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0014", padeops = True, runid = 1, normalize_origin = "turbine")

sim16_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0015")
sim16_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0015", padeops = True, runid = 1, normalize_origin = "turbine")

sim17_folder_block_cor = os.path.join(au.DATA_PATH, "B_0001_Files/Sim_0016")
sim17_block_cor = pio.BudgetIO("Data/B_0001_Files/Sim_0016", padeops = True, runid = 1, normalize_origin = "turbine")

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

#Blocked, No Correction
p_les1_block = sim1_block.read_turb_power("all", turb = 1)[-1]
p_les2_block = sim2_block.read_turb_power("all", turb = 1)[-1]
p_les3_block = sim3_block.read_turb_power("all", turb = 1)[-1]
p_les4_block = sim4_block.read_turb_power("all", turb = 1)[-1]
p_les5_block = sim5_block.read_turb_power("all", turb = 1)[-1]
p_les6_block = sim6_block.read_turb_power("all", turb = 1)[-1]
p_les7_block = sim7_block.read_turb_power("all", turb = 1)[-1]
p_les8_block = sim8_block.read_turb_power("all", turb = 1)[-1]
p_les9_block = sim9_block.read_turb_power("all", turb = 1)[-1]
p_les10_block = sim10_block.read_turb_power("all", turb = 1)[-1]
p_les11_block = sim11_block.read_turb_power("all", turb = 1)[-1]
p_les12_block = sim12_block.read_turb_power("all", turb = 1)[-1]
p_les13_block = sim13_block.read_turb_power("all", turb = 1)[-1]
p_les14_block = sim14_block.read_turb_power("all", turb = 1)[-1]
p_les15_block = sim15_block.read_turb_power("all", turb = 1)[-1]
p_les16_block = sim16_block.read_turb_power("all", turb = 1)[-1]
p_les17_block = sim17_block.read_turb_power("all", turb = 1)[-1]

#Blocked, Corrected
p_les1_block_cor = sim1_block_cor.read_turb_power("all", turb = 1)[-1]
p_les2_block_cor = sim2_block_cor.read_turb_power("all", turb = 1)[-1]
p_les3_block_cor = sim3_block_cor.read_turb_power("all", turb = 1)[-1]
p_les4_block_cor = sim4_block_cor.read_turb_power("all", turb = 1)[-1]
p_les5_block_cor = sim5_block_cor.read_turb_power("all", turb = 1)[-1]
p_les6_block_cor = sim6_block_cor.read_turb_power("all", turb = 1)[-1]
p_les7_block_cor = sim7_block_cor.read_turb_power("all", turb = 1)[-1]
p_les8_block_cor = sim8_block_cor.read_turb_power("all", turb = 1)[-1]
p_les9_block_cor = sim9_block_cor.read_turb_power("all", turb = 1)[-1]
p_les10_block_cor = sim10_block_cor.read_turb_power("all", turb = 1)[-1]
p_les11_block_cor = sim11_block_cor.read_turb_power("all", turb = 1)[-1]
p_les12_block_cor = sim12_block_cor.read_turb_power("all", turb = 1)[-1]
p_les13_block_cor = sim13_block_cor.read_turb_power("all", turb = 1)[-1]
p_les14_block_cor = sim14_block_cor.read_turb_power("all", turb = 1)[-1]
p_les15_block_cor = sim15_block_cor.read_turb_power("all", turb = 1)[-1]
p_les16_block_cor = sim16_block_cor.read_turb_power("all", turb = 1)[-1]
p_les17_block_cor = sim17_block_cor.read_turb_power("all", turb = 1)[-1]

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

# Blocked, No Correction
u_inf1_block = sim1_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_block = sim2_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_block = sim3_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_block = sim4_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_block = sim5_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_block = sim6_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_block = sim7_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_block = sim8_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_block = sim9_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_block = sim10_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_block = sim11_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_block = sim12_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_block = sim13_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_block = sim14_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_block = sim15_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_block = sim16_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_block = sim17_block.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Blocked, Corrected
u_inf1_block_cor = sim1_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_block_cor = sim2_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_block_cor = sim3_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_block_cor = sim4_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_block_cor = sim5_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_block_cor = sim6_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_block_cor = sim7_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_block_cor = sim8_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_block_cor = sim9_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_block_cor = sim10_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_block_cor = sim11_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_block_cor = sim12_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_block_cor = sim13_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_block_cor = sim14_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_block_cor = sim15_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_block_cor = sim16_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_block_cor = sim17_block_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

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

#Blocked, No Correction
cp_les1_block = p_les1_block / (0.5*(np.pi/4)*(u_inf1_block**3))
cp_les2_block = p_les2_block / (0.5*(np.pi/4)*(u_inf2_block**3))
cp_les3_block = p_les3_block / (0.5*(np.pi/4)*(u_inf3_block**3))
cp_les4_block = p_les4_block / (0.5*(np.pi/4)*(u_inf4_block**3))
cp_les5_block = p_les5_block / (0.5*(np.pi/4)*(u_inf5_block**3))
cp_les6_block = p_les6_block / (0.5*(np.pi/4)*(u_inf6_block**3))
cp_les7_block = p_les7_block / (0.5*(np.pi/4)*(u_inf7_block**3))
cp_les8_block = p_les8_block / (0.5*(np.pi/4)*(u_inf8_block**3))
cp_les9_block = p_les9_block / (0.5*(np.pi/4)*(u_inf9_block**3))
cp_les10_block = p_les10_block / (0.5*(np.pi/4)*(u_inf10_block**3))
cp_les11_block = p_les11_block / (0.5*(np.pi/4)*(u_inf11_block**3))
cp_les12_block = p_les12_block / (0.5*(np.pi/4)*(u_inf12_block**3))
cp_les13_block = p_les13_block / (0.5*(np.pi/4)*(u_inf13_block**3))
cp_les14_block = p_les14_block / (0.5*(np.pi/4)*(u_inf14_block**3))
cp_les15_block = p_les15_block / (0.5*(np.pi/4)*(u_inf15_block**3))
cp_les16_block = p_les16_block / (0.5*(np.pi/4)*(u_inf16_block**3))
cp_les17_block = p_les17_block / (0.5*(np.pi/4)*(u_inf17_block**3))

#Blocked, Corrected
cp_les1_block_cor = p_les1_block_cor / (0.5*(np.pi/4)*(u_inf1_block_cor**3))
cp_les2_block_cor = p_les2_block_cor / (0.5*(np.pi/4)*(u_inf2_block_cor**3))
cp_les3_block_cor = p_les3_block_cor / (0.5*(np.pi/4)*(u_inf3_block_cor**3))
cp_les4_block_cor = p_les4_block_cor / (0.5*(np.pi/4)*(u_inf4_block_cor**3))
cp_les5_block_cor = p_les5_block_cor / (0.5*(np.pi/4)*(u_inf5_block_cor**3))
cp_les6_block_cor = p_les6_block_cor / (0.5*(np.pi/4)*(u_inf6_block_cor**3))
cp_les7_block_cor = p_les7_block_cor / (0.5*(np.pi/4)*(u_inf7_block_cor**3))
cp_les8_block_cor = p_les8_block_cor / (0.5*(np.pi/4)*(u_inf8_block_cor**3))
cp_les9_block_cor = p_les9_block_cor / (0.5*(np.pi/4)*(u_inf9_block_cor**3))
cp_les10_block_cor = p_les10_block_cor / (0.5*(np.pi/4)*(u_inf10_block_cor**3))
cp_les11_block_cor = p_les11_block_cor / (0.5*(np.pi/4)*(u_inf11_block_cor**3))
cp_les12_block_cor = p_les12_block_cor / (0.5*(np.pi/4)*(u_inf12_block_cor**3))
cp_les13_block_cor = p_les13_block_cor / (0.5*(np.pi/4)*(u_inf13_block_cor**3))
cp_les14_block_cor = p_les14_block_cor / (0.5*(np.pi/4)*(u_inf14_block_cor**3))
cp_les15_block_cor = p_les15_block_cor / (0.5*(np.pi/4)*(u_inf15_block_cor**3))
cp_les16_block_cor = p_les16_block_cor / (0.5*(np.pi/4)*(u_inf16_block_cor**3))
cp_les17_block_cor = p_les17_block_cor / (0.5*(np.pi/4)*(u_inf17_block_cor**3))

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

#Blocked, No Correction
ud_les1_block = sim1_block.read_turb_uvel("all", steady = False)
ud_les1_block = ud_les1_block[-1]
ud_les2_block = sim2_block.read_turb_uvel("all", steady = False)
ud_les2_block = ud_les2_block[-1]
ud_les3_block = sim3_block.read_turb_uvel("all", steady = False)
ud_les3_block = ud_les3_block[-1]
ud_les4_block = sim4_block.read_turb_uvel("all", steady = False)
ud_les4_block = ud_les4_block[-1]
ud_les5_block = sim5_block.read_turb_uvel("all", steady = False)
ud_les5_block = ud_les5_block[-1]
ud_les6_block = sim6_block.read_turb_uvel("all", steady = False)
ud_les6_block = ud_les6_block[-1]
ud_les7_block = sim7_block.read_turb_uvel("all", steady = False)
ud_les7_block = ud_les7_block[-1]
ud_les8_block = sim8_block.read_turb_uvel("all", steady = False)
ud_les8_block = ud_les8_block[-1]
ud_les9_block = sim9_block.read_turb_uvel("all", steady = False)
ud_les9_block = ud_les9_block[-1]
ud_les10_block = sim10_block.read_turb_uvel("all", steady = False)
ud_les10_block = ud_les10_block[-1]
ud_les11_block = sim11_block.read_turb_uvel("all", steady = False)
ud_les11_block = ud_les11_block[-1]
ud_les12_block = sim12_block.read_turb_uvel("all", steady = False)
ud_les12_block = ud_les12_block[-1]
ud_les13_block = sim13_block.read_turb_uvel("all", steady = False)
ud_les13_block = ud_les13_block[-1]
ud_les14_block = sim14_block.read_turb_uvel("all", steady = False)
ud_les14_block = ud_les14_block[-1]
ud_les15_block = sim15_block.read_turb_uvel("all", steady = False)
ud_les15_block = ud_les15_block[-1]
ud_les16_block = sim16_block.read_turb_uvel("all", steady = False)
ud_les16_block = ud_les16_block[-1]
ud_les17_block = sim17_block.read_turb_uvel("all", steady = False)
ud_les17_block = ud_les17_block[-1]

#Blocked, Corrected
ud_les1_block_cor = sim1_block_cor.read_turb_uvel("all", steady = False)
ud_les1_block_cor = ud_les1_block_cor[-1]
ud_les2_block_cor = sim2_block_cor.read_turb_uvel("all", steady = False)
ud_les2_block_cor = ud_les2_block_cor[-1]
ud_les3_block_cor = sim3_block_cor.read_turb_uvel("all", steady = False)
ud_les3_block_cor = ud_les3_block_cor[-1]
ud_les4_block_cor = sim4_block_cor.read_turb_uvel("all", steady = False)
ud_les4_block_cor = ud_les4_block_cor[-1]
ud_les5_block_cor = sim5_block_cor.read_turb_uvel("all", steady = False)
ud_les5_block_cor = ud_les5_block_cor[-1]
ud_les6_block_cor = sim6_block_cor.read_turb_uvel("all", steady = False)
ud_les6_block_cor = ud_les6_block_cor[-1]
ud_les7_block_cor = sim7_block_cor.read_turb_uvel("all", steady = False)
ud_les7_block_cor = ud_les7_block_cor[-1]
ud_les8_block_cor = sim8_block_cor.read_turb_uvel("all", steady = False)
ud_les8_block_cor = ud_les8_block_cor[-1]
ud_les9_block_cor = sim9_block_cor.read_turb_uvel("all", steady = False)
ud_les9_block_cor = ud_les9_block_cor[-1]
ud_les10_block_cor = sim10_block_cor.read_turb_uvel("all", steady = False)
ud_les10_block_cor = ud_les10_block_cor[-1]
ud_les11_block_cor = sim11_block_cor.read_turb_uvel("all", steady = False)
ud_les11_block_cor = ud_les11_block_cor[-1]
ud_les12_block_cor = sim12_block_cor.read_turb_uvel("all", steady = False)
ud_les12_block_cor = ud_les12_block_cor[-1]
ud_les13_block_cor = sim13_block_cor.read_turb_uvel("all", steady = False)
ud_les13_block_cor = ud_les13_block_cor[-1]
ud_les14_block_cor = sim14_block_cor.read_turb_uvel("all", steady = False)
ud_les14_block_cor = ud_les14_block_cor[-1]
ud_les15_block_cor = sim15_block_cor.read_turb_uvel("all", steady = False)
ud_les15_block_cor = ud_les15_block_cor[-1]
ud_les16_block_cor = sim16_block_cor.read_turb_uvel("all", steady = False)
ud_les16_block_cor = ud_les16_block_cor[-1]
ud_les17_block_cor = sim17_block_cor.read_turb_uvel("all", steady = False)
ud_les17_block_cor = ud_les17_block_cor[-1]

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

#Blocked, No Correction
thrust_les1_block = 2*(np.pi/4)*(ud_les1_block)*(u_inf1_block - ud_les1_block)
thrust_les2_block = 2*(np.pi/4)*(ud_les2_block)*(u_inf2_block - ud_les2_block)
thrust_les3_block = 2*(np.pi/4)*(ud_les3_block)*(u_inf3_block - ud_les3_block)
thrust_les4_block = 2*(np.pi/4)*(ud_les4_block)*(u_inf4_block - ud_les4_block)
thrust_les5_block = 2*(np.pi/4)*(ud_les5_block)*(u_inf5_block - ud_les5_block)
thrust_les6_block = 2*(np.pi/4)*(ud_les6_block)*(u_inf6_block - ud_les6_block)
thrust_les7_block = 2*(np.pi/4)*(ud_les7_block)*(u_inf7_block - ud_les7_block)
thrust_les8_block = 2*(np.pi/4)*(ud_les8_block)*(u_inf8_block - ud_les8_block)
thrust_les9_block = 2*(np.pi/4)*(ud_les9_block)*(u_inf9_block - ud_les9_block)
thrust_les10_block = 2*(np.pi/4)*(ud_les10_block)*(u_inf10_block - ud_les10_block)
thrust_les11_block = 2*(np.pi/4)*(ud_les11_block)*(u_inf11_block - ud_les11_block)
thrust_les12_block = 2*(np.pi/4)*(ud_les12_block)*(u_inf12_block - ud_les12_block)
thrust_les13_block = 2*(np.pi/4)*(ud_les13_block)*(u_inf13_block - ud_les13_block)
thrust_les14_block = 2*(np.pi/4)*(ud_les14_block)*(u_inf14_block - ud_les14_block)
thrust_les15_block = 2*(np.pi/4)*(ud_les15_block)*(u_inf15_block - ud_les15_block)
thrust_les16_block = 2*(np.pi/4)*(ud_les16_block)*(u_inf16_block - ud_les16_block)
thrust_les17_block = 2*(np.pi/4)*(ud_les17_block)*(u_inf17_block - ud_les17_block)

#Blocked, Corrected
thrust_les1_block_cor = 2*(np.pi/4)*(ud_les1_block_cor)*(u_inf1_block_cor - ud_les1_block_cor)
thrust_les2_block_cor = 2*(np.pi/4)*(ud_les2_block_cor)*(u_inf2_block_cor - ud_les2_block_cor)
thrust_les3_block_cor = 2*(np.pi/4)*(ud_les3_block_cor)*(u_inf3_block_cor - ud_les3_block_cor)
thrust_les4_block_cor = 2*(np.pi/4)*(ud_les4_block_cor)*(u_inf4_block_cor - ud_les4_block_cor)
thrust_les5_block_cor = 2*(np.pi/4)*(ud_les5_block_cor)*(u_inf5_block_cor - ud_les5_block_cor)
thrust_les6_block_cor = 2*(np.pi/4)*(ud_les6_block_cor)*(u_inf6_block_cor - ud_les6_block_cor)
thrust_les7_block_cor = 2*(np.pi/4)*(ud_les7_block_cor)*(u_inf7_block_cor - ud_les7_block_cor)
thrust_les8_block_cor = 2*(np.pi/4)*(ud_les8_block_cor)*(u_inf8_block_cor - ud_les8_block_cor)
thrust_les9_block_cor = 2*(np.pi/4)*(ud_les9_block_cor)*(u_inf9_block_cor - ud_les9_block_cor)
thrust_les10_block_cor = 2*(np.pi/4)*(ud_les10_block_cor)*(u_inf10_block_cor - ud_les10_block_cor)
thrust_les11_block_cor = 2*(np.pi/4)*(ud_les11_block_cor)*(u_inf11_block_cor - ud_les11_block_cor)
thrust_les12_block_cor = 2*(np.pi/4)*(ud_les12_block_cor)*(u_inf12_block_cor - ud_les12_block_cor)
thrust_les13_block_cor = 2*(np.pi/4)*(ud_les13_block_cor)*(u_inf13_block_cor - ud_les13_block_cor)
thrust_les14_block_cor = 2*(np.pi/4)*(ud_les14_block_cor)*(u_inf14_block_cor - ud_les14_block_cor)
thrust_les15_block_cor = 2*(np.pi/4)*(ud_les15_block_cor)*(u_inf15_block_cor - ud_les15_block_cor)
thrust_les16_block_cor = 2*(np.pi/4)*(ud_les16_block_cor)*(u_inf16_block_cor - ud_les16_block_cor)
thrust_les17_block_cor = 2*(np.pi/4)*(ud_les17_block_cor)*(u_inf17_block_cor - ud_les17_block_cor)

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

#Blocked, No Correction
ct_les1_block = thrust_les1_block/(0.5*(np.pi/4)*(u_inf1_block**2))
ct_les2_block = thrust_les2_block/(0.5*(np.pi/4)*(u_inf2_block**2))
ct_les3_block = thrust_les3_block/(0.5*(np.pi/4)*(u_inf3_block**2))
ct_les4_block = thrust_les4_block/(0.5*(np.pi/4)*(u_inf4_block**2))
ct_les5_block = thrust_les5_block/(0.5*(np.pi/4)*(u_inf5_block**2))
ct_les6_block = thrust_les6_block/(0.5*(np.pi/4)*(u_inf6_block**2))
ct_les7_block = thrust_les7_block/(0.5*(np.pi/4)*(u_inf7_block**2))
ct_les8_block = thrust_les8_block/(0.5*(np.pi/4)*(u_inf8_block**2))
ct_les9_block = thrust_les9_block/(0.5*(np.pi/4)*(u_inf9_block**2))
ct_les10_block = thrust_les10_block/(0.5*(np.pi/4)*(u_inf10_block**2))
ct_les11_block = thrust_les11_block/(0.5*(np.pi/4)*(u_inf11_block**2))
ct_les12_block = thrust_les12_block/(0.5*(np.pi/4)*(u_inf12_block**2))
ct_les13_block = thrust_les13_block/(0.5*(np.pi/4)*(u_inf13_block**2))
ct_les14_block = thrust_les14_block/(0.5*(np.pi/4)*(u_inf14_block**2))
ct_les15_block = thrust_les15_block/(0.5*(np.pi/4)*(u_inf15_block**2))
ct_les16_block = thrust_les16_block/(0.5*(np.pi/4)*(u_inf16_block**2))
ct_les17_block = thrust_les17_block/(0.5*(np.pi/4)*(u_inf17_block**2))

#Blocked, Corrected
ct_les1_block_cor = thrust_les1_block_cor/(0.5*(np.pi/4)*(u_inf1_block_cor**2))
ct_les2_block_cor = thrust_les2_block_cor/(0.5*(np.pi/4)*(u_inf2_block_cor**2))
ct_les3_block_cor = thrust_les3_block_cor/(0.5*(np.pi/4)*(u_inf3_block_cor**2))
ct_les4_block_cor = thrust_les4_block_cor/(0.5*(np.pi/4)*(u_inf4_block_cor**2))
ct_les5_block_cor = thrust_les5_block_cor/(0.5*(np.pi/4)*(u_inf5_block_cor**2))
ct_les6_block_cor = thrust_les6_block_cor/(0.5*(np.pi/4)*(u_inf6_block_cor**2))
ct_les7_block_cor = thrust_les7_block_cor/(0.5*(np.pi/4)*(u_inf7_block_cor**2))
ct_les8_block_cor = thrust_les8_block_cor/(0.5*(np.pi/4)*(u_inf8_block_cor**2))
ct_les9_block_cor = thrust_les9_block_cor/(0.5*(np.pi/4)*(u_inf9_block_cor**2))
ct_les10_block_cor = thrust_les10_block_cor/(0.5*(np.pi/4)*(u_inf10_block_cor**2))
ct_les11_block_cor = thrust_les11_block_cor/(0.5*(np.pi/4)*(u_inf11_block_cor**2))
ct_les12_block_cor = thrust_les12_block_cor/(0.5*(np.pi/4)*(u_inf12_block_cor**2))
ct_les13_block_cor = thrust_les13_block_cor/(0.5*(np.pi/4)*(u_inf13_block_cor**2))
ct_les14_block_cor = thrust_les14_block_cor/(0.5*(np.pi/4)*(u_inf14_block_cor**2))
ct_les15_block_cor = thrust_les15_block_cor/(0.5*(np.pi/4)*(u_inf15_block_cor**2))
ct_les16_block_cor = thrust_les16_block_cor/(0.5*(np.pi/4)*(u_inf16_block_cor**2))
ct_les17_block_cor = thrust_les17_block_cor/(0.5*(np.pi/4)*(u_inf17_block_cor**2))

#Manual Inputs
#Blockage
b = 0.1

#U2/U1 Manual Inputs/Guess
#Uncorrected
u2_u1_1 = 0.5
u2_u1_2 = 0.5
u2_u1_3 = 0.5
u2_u1_4 = 0.5
u2_u1_5 = 0.5
u2_u1_6 = 0.5
u2_u1_7 = 0.5
u2_u1_8 = 0.5
u2_u1_9 = 0.5
u2_u1_10 = 0.5
u2_u1_11 = 0.5
u2_u1_12 = 0.5
u2_u1_13 = 0.5
u2_u1_14 = 0.5
u2_u1_15 = 0.5
u2_u1_16 = 0.5
u2_u1_17 = 0.5

#Corrected
u2_u1_1_cor = 0.5
u2_u1_2_cor = 0.5
u2_u1_3_cor = 0.5
u2_u1_4_cor = 0.5
u2_u1_5_cor = 0.5
u2_u1_6_cor = 0.5
u2_u1_7_cor = 0.5
u2_u1_8_cor = 0.5
u2_u1_9_cor = 0.5
u2_u1_10_cor = 0.5
u2_u1_11_cor = 0.5
u2_u1_12_cor = 0.5
u2_u1_13_cor = 0.5
u2_u1_14_cor = 0.5
u2_u1_15_cor = 0.5
u2_u1_16_cor = 0.5
u2_u1_17_cor = 0.5

#Solving for Ut/U1
#Uncorrected
ut_u1_1 = (-1 + np.sqrt(1+b*((u2_u1_1**2)-1)))/(b*(u2_u1_1 -1))
ut_u1_2 = (-1 + np.sqrt(1+b*((u2_u1_2**2)-1)))/(b*(u2_u1_2 -1))
ut_u1_3 = (-1 + np.sqrt(1+b*((u2_u1_3**2)-1)))/(b*(u2_u1_3 -1))
ut_u1_4 = (-1 + np.sqrt(1+b*((u2_u1_4**2)-1)))/(b*(u2_u1_4 -1))
ut_u1_5 = (-1 + np.sqrt(1+b*((u2_u1_5**2)-1)))/(b*(u2_u1_5 -1))
ut_u1_6 = (-1 + np.sqrt(1+b*((u2_u1_6**2)-1)))/(b*(u2_u1_6 -1))
ut_u1_7 = (-1 + np.sqrt(1+b*((u2_u1_7**2)-1)))/(b*(u2_u1_7 -1))
ut_u1_8 = (-1 + np.sqrt(1+b*((u2_u1_8**2)-1)))/(b*(u2_u1_8 -1))
ut_u1_9 = (-1 + np.sqrt(1+b*((u2_u1_9**2)-1)))/(b*(u2_u1_9 -1))
ut_u1_10 = (-1 + np.sqrt(1+b*((u2_u1_10**2)-1)))/(b*(u2_u1_10 -1))
ut_u1_11 = (-1 + np.sqrt(1+b*((u2_u1_11**2)-1)))/(b*(u2_u1_11 -1))
ut_u1_12 = (-1 + np.sqrt(1+b*((u2_u1_12**2)-1)))/(b*(u2_u1_12 -1))
ut_u1_13 = (-1 + np.sqrt(1+b*((u2_u1_13**2)-1)))/(b*(u2_u1_13 -1))
ut_u1_14 = (-1 + np.sqrt(1+b*((u2_u1_14**2)-1)))/(b*(u2_u1_14 -1))
ut_u1_15 = (-1 + np.sqrt(1+b*((u2_u1_15**2)-1)))/(b*(u2_u1_15 -1))
ut_u1_16 = (-1 + np.sqrt(1+b*((u2_u1_16**2)-1)))/(b*(u2_u1_16 -1))
ut_u1_17 = (-1 + np.sqrt(1+b*((u2_u1_17**2)-1)))/(b*(u2_u1_17 -1))

#Corrected
ut_u1_1_cor = (-1 + np.sqrt(1+b*((u2_u1_1_cor**2)-1)))/(b*(u2_u1_1_cor -1))
ut_u1_2_cor = (-1 + np.sqrt(1+b*((u2_u1_2_cor**2)-1)))/(b*(u2_u1_2_cor -1))
ut_u1_3_cor = (-1 + np.sqrt(1+b*((u2_u1_3_cor**2)-1)))/(b*(u2_u1_3_cor -1))
ut_u1_4_cor = (-1 + np.sqrt(1+b*((u2_u1_4_cor**2)-1)))/(b*(u2_u1_4_cor -1))
ut_u1_5_cor = (-1 + np.sqrt(1+b*((u2_u1_5_cor**2)-1)))/(b*(u2_u1_5_cor -1))
ut_u1_6_cor = (-1 + np.sqrt(1+b*((u2_u1_6_cor**2)-1)))/(b*(u2_u1_6_cor -1))
ut_u1_7_cor = (-1 + np.sqrt(1+b*((u2_u1_7_cor**2)-1)))/(b*(u2_u1_7_cor -1))
ut_u1_8_cor = (-1 + np.sqrt(1+b*((u2_u1_8_cor**2)-1)))/(b*(u2_u1_8_cor -1))
ut_u1_9_cor = (-1 + np.sqrt(1+b*((u2_u1_9_cor**2)-1)))/(b*(u2_u1_9_cor -1))
ut_u1_10_cor = (-1 + np.sqrt(1+b*((u2_u1_10_cor**2)-1)))/(b*(u2_u1_10_cor -1))
ut_u1_11_cor = (-1 + np.sqrt(1+b*((u2_u1_11_cor**2)-1)))/(b*(u2_u1_11_cor -1))
ut_u1_12_cor = (-1 + np.sqrt(1+b*((u2_u1_12_cor**2)-1)))/(b*(u2_u1_12_cor -1))
ut_u1_13_cor = (-1 + np.sqrt(1+b*((u2_u1_13_cor**2)-1)))/(b*(u2_u1_13_cor -1))
ut_u1_14_cor = (-1 + np.sqrt(1+b*((u2_u1_14_cor**2)-1)))/(b*(u2_u1_14_cor -1))
ut_u1_15_cor = (-1 + np.sqrt(1+b*((u2_u1_15_cor**2)-1)))/(b*(u2_u1_15_cor -1))
ut_u1_16_cor = (-1 + np.sqrt(1+b*((u2_u1_16_cor**2)-1)))/(b*(u2_u1_16_cor -1))
ut_u1_17_cor = (-1 + np.sqrt(1+b*((u2_u1_17_cor**2)-1)))/(b*(u2_u1_17_cor -1))

#V0/U1 Eqs
#Uncorrected, Eq 22 From Paper
v0_U1_1_22 = u2_u1_1 - b*(ut_u1_1)*(u2_u1_1 - 1)
v0_U1_2_22 = u2_u1_2 - b*(ut_u1_2)*(u2_u1_2 - 1)
v0_U1_3_22 = u2_u1_3 - b*(ut_u1_3)*(u2_u1_3 - 1)
v0_U1_4_22 = u2_u1_4 - b*(ut_u1_4)*(u2_u1_4 - 1)
v0_U1_5_22 = u2_u1_5 - b*(ut_u1_5)*(u2_u1_5 - 1)
v0_U1_6_22 = u2_u1_6 - b*(ut_u1_6)*(u2_u1_6 - 1)
v0_U1_7_22 = u2_u1_7 - b*(ut_u1_7)*(u2_u1_7 - 1)
v0_U1_8_22 = u2_u1_8 - b*(ut_u1_8)*(u2_u1_8 - 1)
v0_U1_9_22 = u2_u1_9 - b*(ut_u1_9)*(u2_u1_9 - 1)
v0_U1_10_22 = u2_u1_10 - b*(ut_u1_10)*(u2_u1_10 - 1)
v0_U1_11_22 = u2_u1_11 - b*(ut_u1_11)*(u2_u1_11 - 1)
v0_U1_12_22 = u2_u1_12 - b*(ut_u1_12)*(u2_u1_12 - 1)
v0_U1_13_22 = u2_u1_13 - b*(ut_u1_13)*(u2_u1_13 - 1)
v0_U1_14_22 = u2_u1_14 - b*(ut_u1_14)*(u2_u1_14 - 1)
v0_U1_15_22 = u2_u1_15 - b*(ut_u1_15)*(u2_u1_15 - 1)
v0_U1_16_22 = u2_u1_16 - b*(ut_u1_16)*(u2_u1_16 - 1)
v0_U1_17_22 = u2_u1_17 - b*(ut_u1_17)*(u2_u1_17 - 1)

#Corrected, Eq 22 From Paper
v0_U1_1_cor_22 = u2_u1_1_cor - b*(ut_u1_1_cor)*(u2_u1_1_cor - 1)
v0_U1_2_cor_22 = u2_u1_2_cor - b*(ut_u1_2_cor)*(u2_u1_2_cor - 1)
v0_U1_3_cor_22 = u2_u1_3_cor - b*(ut_u1_3_cor)*(u2_u1_3_cor - 1)
v0_U1_4_cor_22 = u2_u1_4_cor - b*(ut_u1_4_cor)*(u2_u1_4_cor - 1)
v0_U1_5_cor_22 = u2_u1_5_cor - b*(ut_u1_5_cor)*(u2_u1_5_cor - 1)
v0_U1_6_cor_22 = u2_u1_6_cor - b*(ut_u1_6_cor)*(u2_u1_6_cor - 1)
v0_U1_7_cor_22 = u2_u1_7_cor - b*(ut_u1_7_cor)*(u2_u1_7_cor - 1)
v0_U1_8_cor_22 = u2_u1_8_cor - b*(ut_u1_8_cor)*(u2_u1_8_cor - 1)
v0_U1_9_cor_22 = u2_u1_9_cor - b*(ut_u1_9_cor)*(u2_u1_9_cor - 1)
v0_U1_10_cor_22 = u2_u1_10_cor - b*(ut_u1_10_cor)*(u2_u1_10_cor - 1)
v0_U1_11_cor_22 = u2_u1_11_cor - b*(ut_u1_11_cor)*(u2_u1_11_cor - 1)
v0_U1_12_cor_22 = u2_u1_12_cor - b*(ut_u1_12_cor)*(u2_u1_12_cor - 1)
v0_U1_13_cor_22 = u2_u1_13_cor - b*(ut_u1_13_cor)*(u2_u1_13_cor - 1)
v0_U1_14_cor_22 = u2_u1_14_cor - b*(ut_u1_14_cor)*(u2_u1_14_cor - 1)
v0_U1_15_cor_22 = u2_u1_15_cor - b*(ut_u1_15_cor)*(u2_u1_15_cor - 1)
v0_U1_16_cor_22 = u2_u1_16_cor - b*(ut_u1_16_cor)*(u2_u1_16_cor - 1)
v0_U1_17_cor_22 = u2_u1_17_cor - b*(ut_u1_17_cor)*(u2_u1_17_cor - 1)

#Uncorrected, Eq 23 From Paper
v0_U1_1_23 = np.sqrt(((u2_u1_1**2)-1)/ct_les1_block)
v0_U1_2_23 = np.sqrt(((u2_u1_2**2)-1)/ct_les2_block)
v0_U1_3_23 = np.sqrt(((u2_u1_3**2)-1)/ct_les3_block)
v0_U1_4_23 = np.sqrt(((u2_u1_4**2)-1)/ct_les4_block)
v0_U1_5_23 = np.sqrt(((u2_u1_5**2)-1)/ct_les5_block)
v0_U1_6_23 = np.sqrt(((u2_u1_6**2)-1)/ct_les6_block)
v0_U1_7_23 = np.sqrt(((u2_u1_7**2)-1)/ct_les7_block)
v0_U1_8_23 = np.sqrt(((u2_u1_8**2)-1)/ct_les8_block)
v0_U1_9_23 = np.sqrt(((u2_u1_9**2)-1)/ct_les9_block)
v0_U1_10_23 = np.sqrt(((u2_u1_10**2)-1)/ct_les10_block)
v0_U1_11_23 = np.sqrt(((u2_u1_11**2)-1)/ct_les11_block)
v0_U1_12_23 = np.sqrt(((u2_u1_12**2)-1)/ct_les12_block)
v0_U1_13_23 = np.sqrt(((u2_u1_13**2)-1)/ct_les13_block)
v0_U1_14_23 = np.sqrt(((u2_u1_14**2)-1)/ct_les14_block)
v0_U1_15_23 = np.sqrt(((u2_u1_15**2)-1)/ct_les15_block)
v0_U1_16_23 = np.sqrt(((u2_u1_16**2)-1)/ct_les16_block)
v0_U1_17_23 = np.sqrt(((u2_u1_17**2)-1)/ct_les17_block)

#Corrected, Eq 23 From Paper
v0_U1_1_cor_23 = np.sqrt(((u2_u1_1_cor**2)-1)/ct_les1_block_cor)
v0_U1_2_cor_23 = np.sqrt(((u2_u1_2_cor**2)-1)/ct_les2_block_cor)
v0_U1_3_cor_23 = np.sqrt(((u2_u1_3_cor**2)-1)/ct_les3_block_cor)
v0_U1_4_cor_23 = np.sqrt(((u2_u1_4_cor**2)-1)/ct_les4_block_cor)
v0_U1_5_cor_23 = np.sqrt(((u2_u1_5_cor**2)-1)/ct_les5_block_cor)
v0_U1_6_cor_23 = np.sqrt(((u2_u1_6_cor**2)-1)/ct_les6_block_cor)
v0_U1_7_cor_23 = np.sqrt(((u2_u1_7_cor**2)-1)/ct_les7_block_cor)
v0_U1_8_cor_23 = np.sqrt(((u2_u1_8_cor**2)-1)/ct_les8_block_cor)
v0_U1_9_cor_23 = np.sqrt(((u2_u1_9_cor**2)-1)/ct_les9_block_cor)
v0_U1_10_cor_23 = np.sqrt(((u2_u1_10_cor**2)-1)/ct_les10_block_cor)
v0_U1_11_cor_23 = np.sqrt(((u2_u1_11_cor**2)-1)/ct_les11_block_cor)
v0_U1_12_cor_23 = np.sqrt(((u2_u1_12_cor**2)-1)/ct_les12_block_cor)
v0_U1_13_cor_23 = np.sqrt(((u2_u1_13_cor**2)-1)/ct_les13_block_cor)
v0_U1_14_cor_23 = np.sqrt(((u2_u1_14_cor**2)-1)/ct_les14_block_cor)
v0_U1_15_cor_23 = np.sqrt(((u2_u1_15_cor**2)-1)/ct_les15_block_cor)
v0_U1_16_cor_23 = np.sqrt(((u2_u1_16_cor**2)-1)/ct_les16_block_cor)
v0_U1_17_cor_23 = np.sqrt(((u2_u1_17_cor**2)-1)/ct_les17_block_cor)

#Loops to Establish Convergence + Calculate V'0
#Uncorrected
if np.absolute(v0_U1_1_22 - v0_U1_1_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0000")
else:
    v0_u1_1 = np.mean([v0_U1_1_22, v0_U1_1_23])
    ut_v0_1 = ut_u1_1/v0_u1_1
    v0_prime_1 = (u_inf1_block*((ut_v0_1**2 + (ct_les1_block/4))))/(ut_v0_1)
    cp_prime_1 = cp_les1_block*((u_inf1_block/v0_prime_1)**3)
    ct_prime_1 = ct_les1_block*((u_inf1_block/v0_prime_1)**2)

if np.absolute(v0_U1_2_22 - v0_U1_2_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0001")
else:
    v0_u1_2 = np.mean([v0_U1_2_22, v0_U1_2_23])
    ut_v0_2 = ut_u1_2/v0_u1_2
    v0_prime_2 = (u_inf2_block*((ut_v0_2**2 + (ct_les2_block/4))))/(ut_v0_2)
    cp_prime_2 = cp_les2_block*((u_inf2_block/v0_prime_2)**3)
    ct_prime_2 = ct_les2_block*((u_inf2_block/v0_prime_2)**2)

if np.absolute(v0_U1_3_22 - v0_U1_3_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0002")
else:
    v0_u1_3 = np.mean([v0_U1_3_22, v0_U1_3_23])
    ut_v0_3 = ut_u1_3/v0_u1_3
    v0_prime_3 = (u_inf3_block*((ut_v0_3**2 + (ct_les3_block/4))))/(ut_v0_3)
    cp_prime_3 = cp_les3_block*((u_inf3_block/v0_prime_3)**3)
    ct_prime_3 = ct_les3_block*((u_inf3_block/v0_prime_3)**2)

if np.absolute(v0_U1_4_22 - v0_U1_4_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0003")
else:
    v0_u1_4 = np.mean([v0_U1_4_22, v0_U1_4_23])
    ut_v0_4 = ut_u1_4/v0_u1_4
    v0_prime_4 = (u_inf4_block*((ut_v0_4**2 + (ct_les4_block/4))))/(ut_v0_4)
    cp_prime_4 = cp_les4_block*((u_inf4_block/v0_prime_4)**3)
    ct_prime_4 = ct_les4_block*((u_inf4_block/v0_prime_4)**2)

if np.absolute(v0_U1_5_22 - v0_U1_5_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0004")
else:
    v0_u1_5 = np.mean([v0_U1_5_22, v0_U1_5_23])
    ut_v0_5 = ut_u1_5/v0_u1_5
    v0_prime_5 = (u_inf5_block*((ut_v0_5**2 + (ct_les5_block/4))))/(ut_v0_5)
    cp_prime_5 = cp_les5_block*((u_inf5_block/v0_prime_5)**3)
    ct_prime_5 = ct_les5_block*((u_inf5_block/v0_prime_5)**2)

if np.absolute(v0_U1_6_22 - v0_U1_6_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0005")
else:
    v0_u1_6 = np.mean([v0_U1_6_22, v0_U1_6_23])
    ut_v0_6 = ut_u1_6/v0_u1_6
    v0_prime_6 = (u_inf6_block*((ut_v0_6**2 + (ct_les6_block/4))))/(ut_v0_6)
    cp_prime_6 = cp_les6_block*((u_inf6_block/v0_prime_6)**3)
    ct_prime_6 = ct_les6_block*((u_inf6_block/v0_prime_6)**2)

if np.absolute(v0_U1_7_22 - v0_U1_7_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0006")
else:
    v0_u1_7 = np.mean([v0_U1_7_22, v0_U1_7_23])
    ut_v0_7 = ut_u1_7/v0_u1_7
    v0_prime_7 = (u_inf7_block*((ut_v0_7**2 + (ct_les7_block/4))))/(ut_v0_7)
    cp_prime_7 = cp_les7_block*((u_inf7_block/v0_prime_7)**3)
    ct_prime_7 = ct_les7_block*((u_inf7_block/v0_prime_7)**2)

if np.absolute(v0_U1_8_22 - v0_U1_8_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0007")
else:
    v0_u1_8 = np.mean([v0_U1_8_22, v0_U1_8_23])
    ut_v0_8 = ut_u1_8/v0_u1_8
    v0_prime_8 = (u_inf8_block*((ut_v0_8**2 + (ct_les8_block/4))))/(ut_v0_8)
    cp_prime_8 = cp_les8_block*((u_inf8_block/v0_prime_8)**3)
    ct_prime_8 = ct_les8_block*((u_inf8_block/v0_prime_8)**2)

if np.absolute(v0_U1_9_22 - v0_U1_9_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0008")
else:
    v0_u1_9 = np.mean([v0_U1_9_22, v0_U1_9_23])
    ut_v0_9 = ut_u1_9/v0_u1_9
    v0_prime_9 = (u_inf9_block*((ut_v0_9**2 + (ct_les9_block/4))))/(ut_v0_9)
    cp_prime_9 = cp_les9_block*((u_inf9_block/v0_prime_9)**3)
    ct_prime_9 = ct_les9_block*((u_inf9_block/v0_prime_9)**2)

if np.absolute(v0_U1_10_22 - v0_U1_10_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0009")
else:
    v0_u1_10 = np.mean([v0_U1_10_22, v0_U1_10_23])
    ut_v0_10 = ut_u1_10/v0_u1_10
    v0_prime_10 = (u_inf10_block*((ut_v0_10**2 + (ct_les10_block/4))))/(ut_v0_10)
    cp_prime_10 = cp_les10_block*((u_inf10_block/v0_prime_10)**3)
    ct_prime_10 = ct_les10_block*((u_inf10_block/v0_prime_10)**2)

if np.absolute(v0_U1_11_22 - v0_U1_11_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0010")
else:
    v0_u1_11 = np.mean([v0_U1_11_22, v0_U1_11_23])
    ut_v0_11 = ut_u1_11/v0_u1_11
    v0_prime_11 = (u_inf11_block*((ut_v0_11**2 + (ct_les11_block/4))))/(ut_v0_11)
    cp_prime_11 = cp_les11_block*((u_inf11_block/v0_prime_11)**3)
    ct_prime_11 = ct_les11_block*((u_inf11_block/v0_prime_11)**2)

if np.absolute(v0_U1_12_22 - v0_U1_12_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0011")
else:
    v0_u1_12 = np.mean([v0_U1_12_22, v0_U1_12_23])
    ut_v0_12 = ut_u1_12/v0_u1_12
    v0_prime_12 = (u_inf12_block*((ut_v0_12**2 + (ct_les12_block/4))))/(ut_v0_12)
    cp_prime_12 = cp_les12_block*((u_inf12_block/v0_prime_12)**3)
    ct_prime_12 = ct_les12_block*((u_inf12_block/v0_prime_12)**2)

if np.absolute(v0_U1_13_22 - v0_U1_13_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0012")
else:
    v0_u1_13 = np.mean([v0_U1_13_22, v0_U1_13_23])
    ut_v0_13 = ut_u1_13/v0_u1_13
    v0_prime_13 = (u_inf13_block*((ut_v0_13**2 + (ct_les13_block/4))))/(ut_v0_13)
    cp_prime_13 = cp_les13_block*((u_inf13_block/v0_prime_13)**3)
    ct_prime_13 = ct_les13_block*((u_inf13_block/v0_prime_13)**2)

if np.absolute(v0_U1_14_22 - v0_U1_14_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0013")
else:
    v0_u1_14 = np.mean([v0_U1_14_22, v0_U1_14_23])
    ut_v0_14 = ut_u1_14/v0_u1_14
    v0_prime_14 = (u_inf14_block*((ut_v0_14**2 + (ct_les14_block/4))))/(ut_v0_14)
    cp_prime_14 = cp_les14_block*((u_inf14_block/v0_prime_14)**3)
    ct_prime_14 = ct_les14_block*((u_inf14_block/v0_prime_14)**2)

if np.absolute(v0_U1_15_22 - v0_U1_15_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0014")
else:
    v0_u1_15 = np.mean([v0_U1_15_22, v0_U1_15_23])
    ut_v0_15 = ut_u1_15/v0_u1_15
    v0_prime_15 = (u_inf15_block*((ut_v0_15**2 + (ct_les15_block/4))))/(ut_v0_15)
    cp_prime_15 = cp_les15_block*((u_inf15_block/v0_prime_15)**3)
    ct_prime_15 = ct_les15_block*((u_inf15_block/v0_prime_15)**2)

if np.absolute(v0_U1_16_22 - v0_U1_16_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0015")
else:
    v0_u1_16 = np.mean([v0_U1_16_22, v0_U1_16_23])
    ut_v0_16 = ut_u1_16/v0_u1_16
    v0_prime_16 = (u_inf16_block*((ut_v0_16**2 + (ct_les16_block/4))))/(ut_v0_16)
    cp_prime_16 = cp_les16_block*((u_inf16_block/v0_prime_16)**3)
    ct_prime_16 = ct_les16_block*((u_inf16_block/v0_prime_16)**2)

if np.absolute(v0_U1_17_22 - v0_U1_17_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0016")
else:
    v0_u1_17 = np.mean([v0_U1_17_22, v0_U1_17_23])
    ut_v0_17 = ut_u1_17/v0_u1_17
    v0_prime_17 = (u_inf17_block*((ut_v0_17**2 + (ct_les17_block/4))))/(ut_v0_17)
    cp_prime_17 = cp_les17_block*((u_inf17_block/v0_prime_17)**3)
    ct_prime_17 = ct_les17_block*((u_inf17_block/v0_prime_17)**2)

#Corrected
if np.absolute(v0_U1_1_cor_22 - v0_U1_1_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0000")
else:
    v0_u1_1_cor = np.mean([v0_U1_1_cor_22, v0_U1_1_cor_23])
    ut_v0_1_cor = ut_u1_1_cor/v0_u1_1_cor
    v0_prime_1_cor = (u_inf1_block_cor*((ut_v0_1_cor**2 + (ct_les1_block_cor/4))))/(ut_v0_1_cor)
    cp_prime_1_cor = cp_les1_block_cor*((u_inf1_block_cor/v0_prime_1_cor)**3)
    ct_prime_1_cor = ct_les1_block_cor*((u_inf1_block_cor/v0_prime_1_cor)**2)

if np.absolute(v0_U1_2_cor_22 - v0_U1_2_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0001")
else:
    v0_u1_2_cor = np.mean([v0_U1_2_cor_22, v0_U1_2_cor_23])
    ut_v0_2_cor = ut_u1_2_cor/v0_u1_2_cor
    v0_prime_2_cor = (u_inf2_block_cor*((ut_v0_2_cor**2 + (ct_les2_block_cor/4))))/(ut_v0_2_cor)
    cp_prime_2_cor = cp_les2_block_cor*((u_inf2_block_cor/v0_prime_2_cor)**3)
    ct_prime_2_cor = ct_les2_block_cor*((u_inf2_block_cor/v0_prime_2_cor)**2)

if np.absolute(v0_U1_3_cor_22 - v0_U1_3_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0002")
else:
    v0_u1_3_cor = np.mean([v0_U1_3_cor_22, v0_U1_3_cor_23])
    ut_v0_3_cor = ut_u1_3_cor/v0_u1_3_cor
    v0_prime_3_cor = (u_inf3_block_cor*((ut_v0_3_cor**2 + (ct_les3_block_cor/4))))/(ut_v0_3_cor)
    cp_prime_3_cor = cp_les3_block_cor*((u_inf3_block_cor/v0_prime_3_cor)**3)
    ct_prime_3_cor = ct_les3_block_cor*((u_inf3_block_cor/v0_prime_3_cor)**2)

if np.absolute(v0_U1_4_cor_22 - v0_U1_4_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0003")
else:
    v0_u1_4_cor = np.mean([v0_U1_4_cor_22, v0_U1_4_cor_23])
    ut_v0_4_cor = ut_u1_4_cor/v0_u1_4_cor
    v0_prime_4_cor = (u_inf4_block_cor*((ut_v0_4_cor**2 + (ct_les4_block_cor/4))))/(ut_v0_4_cor)
    cp_prime_4_cor = cp_les4_block_cor*((u_inf4_block_cor/v0_prime_4_cor)**3)
    ct_prime_4_cor = ct_les4_block_cor*((u_inf4_block_cor/v0_prime_4_cor)**2)

if np.absolute(v0_U1_5_cor_22 - v0_U1_5_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0004")
else:
    v0_u1_5_cor = np.mean([v0_U1_5_cor_22, v0_U1_5_cor_23])
    ut_v0_5_cor = ut_u1_5_cor/v0_u1_5_cor
    v0_prime_5_cor = (u_inf5_block_cor*((ut_v0_5_cor**2 + (ct_les5_block_cor/4))))/(ut_v0_5_cor)
    cp_prime_5_cor = cp_les5_block_cor*((u_inf5_block_cor/v0_prime_5_cor)**3)
    ct_prime_5_cor = ct_les5_block_cor*((u_inf5_block_cor/v0_prime_5_cor)**2)

if np.absolute(v0_U1_6_cor_22 - v0_U1_6_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0005")
else:
    v0_u1_6_cor = np.mean([v0_U1_6_cor_22, v0_U1_6_cor_23])
    ut_v0_6_cor = ut_u1_6_cor/v0_u1_6_cor
    v0_prime_6_cor = (u_inf6_block_cor*((ut_v0_6_cor**2 + (ct_les6_block_cor/4))))/(ut_v0_6_cor)
    cp_prime_6_cor = cp_les6_block_cor*((u_inf6_block_cor/v0_prime_6_cor)**3)
    ct_prime_6_cor = ct_les6_block_cor*((u_inf6_block_cor/v0_prime_6_cor)**2)

if np.absolute(v0_U1_7_cor_22 - v0_U1_7_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0006")
else:
    v0_u1_7_cor = np.mean([v0_U1_7_cor_22, v0_U1_7_cor_23])
    ut_v0_7_cor = ut_u1_7_cor/v0_u1_7_cor
    v0_prime_7_cor = (u_inf7_block_cor*((ut_v0_7_cor**2 + (ct_les7_block_cor/4))))/(ut_v0_7_cor)
    cp_prime_7_cor = cp_les7_block_cor*((u_inf7_block_cor/v0_prime_7_cor)**3)
    ct_prime_7_cor = ct_les7_block_cor*((u_inf7_block_cor/v0_prime_7_cor)**2)

if np.absolute(v0_U1_8_cor_22 - v0_U1_8_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0007")
else:
    v0_u1_8_cor = np.mean([v0_U1_8_cor_22, v0_U1_8_cor_23])
    ut_v0_8_cor = ut_u1_8_cor/v0_u1_8_cor
    v0_prime_8_cor = (u_inf8_block_cor*((ut_v0_8_cor**2 + (ct_les8_block_cor/4))))/(ut_v0_8_cor)
    cp_prime_8_cor = cp_les8_block_cor*((u_inf8_block_cor/v0_prime_8_cor)**3)
    ct_prime_8_cor = ct_les8_block_cor*((u_inf8_block_cor/v0_prime_8_cor)**2)

if np.absolute(v0_U1_9_cor_22 - v0_U1_9_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0008")
else:
    v0_u1_9_cor = np.mean([v0_U1_9_cor_22, v0_U1_9_cor_23])
    ut_v0_9_cor = ut_u1_9_cor/v0_u1_9_cor
    v0_prime_9_cor = (u_inf9_block_cor*((ut_v0_9_cor**2 + (ct_les9_block_cor/4))))/(ut_v0_9_cor)
    cp_prime_9_cor = cp_les9_block_cor*((u_inf9_block_cor/v0_prime_9_cor)**3)
    ct_prime_9_cor = ct_les9_block_cor*((u_inf9_block_cor/v0_prime_9_cor)**2)

if np.absolute(v0_U1_10_cor_22 - v0_U1_10_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0009")
else:
    v0_u1_10_cor = np.mean([v0_U1_10_cor_22, v0_U1_10_cor_23])
    ut_v0_10_cor = ut_u1_10_cor/v0_u1_10_cor
    v0_prime_10_cor = (u_inf10_block_cor*((ut_v0_10_cor**2 + (ct_les10_block_cor/4))))/(ut_v0_10_cor)
    cp_prime_10_cor = cp_les10_block_cor*((u_inf10_block_cor/v0_prime_10_cor)**3)
    ct_prime_10_cor = ct_les10_block_cor*((u_inf10_block_cor/v0_prime_10_cor)**2)

if np.absolute(v0_U1_11_cor_22 - v0_U1_11_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0010")
else:
    v0_u1_11_cor = np.mean([v0_U1_11_cor_22, v0_U1_11_cor_23])
    ut_v0_11_cor = ut_u1_11_cor/v0_u1_11_cor
    v0_prime_11_cor = (u_inf11_block_cor*((ut_v0_11_cor**2 + (ct_les11_block_cor/4))))/(ut_v0_11_cor)
    cp_prime_11_cor = cp_les11_block_cor*((u_inf11_block_cor/v0_prime_11_cor)**3)
    ct_prime_11_cor = ct_les11_block_cor*((u_inf11_block_cor/v0_prime_11_cor)**2)

if np.absolute(v0_U1_12_cor_22 - v0_U1_12_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0011")
else:
    v0_u1_12_cor = np.mean([v0_U1_12_cor_22, v0_U1_12_cor_23])
    ut_v0_12_cor = ut_u1_12_cor/v0_u1_12_cor
    v0_prime_12_cor = (u_inf12_block_cor*((ut_v0_12_cor**2 + (ct_les12_block_cor/4))))/(ut_v0_12_cor)
    cp_prime_12_cor = cp_les12_block_cor*((u_inf12_block_cor/v0_prime_12_cor)**3)
    ct_prime_12_cor = ct_les12_block_cor*((u_inf12_block_cor/v0_prime_12_cor)**2)

if np.absolute(v0_U1_13_cor_22 - v0_U1_13_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0012")
else:
    v0_u1_13_cor = np.mean([v0_U1_13_cor_22, v0_U1_13_cor_23])
    ut_v0_13_cor = ut_u1_13_cor/v0_u1_13_cor
    v0_prime_13_cor = (u_inf13_block_cor*((ut_v0_13_cor**2 + (ct_les13_block_cor/4))))/(ut_v0_13_cor)
    cp_prime_13_cor = cp_les13_block_cor*((u_inf13_block_cor/v0_prime_13_cor)**3)
    ct_prime_13_cor = ct_les13_block_cor*((u_inf13_block_cor/v0_prime_13_cor)**2)

if np.absolute(v0_U1_14_cor_22 - v0_U1_14_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0013")
else:
    v0_u1_14_cor = np.mean([v0_U1_14_cor_22, v0_U1_14_cor_23])
    ut_v0_14_cor = ut_u1_14_cor/v0_u1_14_cor
    v0_prime_14_cor = (u_inf14_block_cor*((ut_v0_14_cor**2 + (ct_les14_block_cor/4))))/(ut_v0_14_cor)
    cp_prime_14_cor = cp_les14_block_cor*((u_inf14_block_cor/v0_prime_14_cor)**3)
    ct_prime_14_cor = ct_les14_block_cor*((u_inf14_block_cor/v0_prime_14_cor)**2)

if np.absolute(v0_U1_15_cor_22 - v0_U1_15_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0014")
else:
    v0_u1_15_cor = np.mean([v0_U1_15_cor_22, v0_U1_15_cor_23])
    ut_v0_15_cor = ut_u1_15_cor/v0_u1_15_cor
    v0_prime_15_cor = (u_inf15_block_cor*((ut_v0_15_cor**2 + (ct_les15_block_cor/4))))/(ut_v0_15_cor)
    cp_prime_15_cor = cp_les15_block_cor*((u_inf15_block_cor/v0_prime_15_cor)**3)
    ct_prime_15_cor = ct_les15_block_cor*((u_inf15_block_cor/v0_prime_15_cor)**2)

if np.absolute(v0_U1_16_cor_22 - v0_U1_16_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0015")
else:
    v0_u1_16_cor = np.mean([v0_U1_16_cor_22, v0_U1_16_cor_23])
    ut_v0_16_cor = ut_u1_16_cor/v0_u1_16_cor
    v0_prime_16_cor = (u_inf16_block_cor*((ut_v0_16_cor**2 + (ct_les16_block_cor/4))))/(ut_v0_16_cor)
    cp_prime_16_cor = cp_les16_block_cor*((u_inf16_block_cor/v0_prime_16_cor)**3)
    ct_prime_16_cor = ct_les16_block_cor*((u_inf16_block_cor/v0_prime_16_cor)**2)

if np.absolute(v0_U1_17_cor_22 - v0_U1_17_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0016")
else:
    v0_u1_17_cor = np.mean([v0_U1_17_cor_22, v0_U1_17_cor_23])
    ut_v0_17_cor = ut_u1_17_cor/v0_u1_17_cor
    v0_prime_17_cor = (u_inf17_block_cor*((ut_v0_17_cor**2 + (ct_les17_block_cor/4))))/(ut_v0_17_cor)
    cp_prime_17_cor = cp_les17_block_cor*((u_inf17_block_cor/v0_prime_17_cor)**3)
    ct_prime_17_cor = ct_les17_block_cor*((u_inf17_block_cor/v0_prime_17_cor)**2)

#Arrays for Plotting
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]
cp_plot = [
    cp_les1, cp_les2, cp_les3, cp_les4, cp_les5, cp_les6, cp_les7, cp_les8,
    cp_les9, cp_les10, cp_les11, cp_les12, cp_les13, cp_les14, cp_les15, cp_les16, cp_les17
]
ct_plot = [
    ct_les1, ct_les2, ct_les3, ct_les4, ct_les5, ct_les6, ct_les7, ct_les8,
    ct_les9, ct_les10, ct_les11, ct_les12, ct_les13, ct_les14, ct_les15, ct_les16, ct_les17
]
cp_plot_cor = [
    cp_les1_cor, cp_les2_cor, cp_les3_cor, cp_les4_cor, cp_les5_cor, cp_les6_cor, cp_les7_cor, cp_les8_cor,
    cp_les9_cor, cp_les10_cor, cp_les11_cor, cp_les12_cor, cp_les13_cor, cp_les14_cor, cp_les15_cor, cp_les16_cor, cp_les17_cor
]
ct_plot_cor = [
    ct_les1_cor, ct_les2_cor, ct_les3_cor, ct_les4_cor, ct_les5_cor, ct_les6_cor, ct_les7_cor, ct_les8_cor,
    ct_les9_cor, ct_les10_cor, ct_les11_cor, ct_les12_cor, ct_les13_cor, ct_les14_cor, ct_les15_cor, ct_les16_cor, ct_les17_cor
]
cp_block_plot = [
    cp_les1_block, cp_les2_block, cp_les3_block, cp_les4_block, cp_les5_block, cp_les6_block, cp_les7_block, cp_les8_block,
    cp_les9_block, cp_les10_block, cp_les11_block, cp_les12_block, cp_les13_block, cp_les14_block, cp_les15_block, cp_les16_block, cp_les17_block
]
ct_block_plot = [
    ct_les1_block, ct_les2_block, ct_les3_block, ct_les4_block, ct_les5_block, ct_les6_block, ct_les7_block, ct_les8_block,
    ct_les9_block, ct_les10_block, ct_les11_block, ct_les12_block, ct_les13_block, ct_les14_block, ct_les15_block, ct_les16_block, ct_les17_block
]

cp_block_cor= [
    cp_les1_block_cor, cp_les2_block_cor, cp_les3_block_cor, cp_les4_block_cor, cp_les5_block_cor, cp_les6_block_cor, cp_les7_block_cor, cp_les8_block_cor,
    cp_les9_block_cor, cp_les10_block_cor, cp_les11_block_cor, cp_les12_block_cor, cp_les13_block_cor, cp_les14_block_cor, cp_les15_block_cor, cp_les16_block_cor, cp_les17_block_cor
]
ct_block_cor = [
    ct_les1_block_cor, ct_les2_block_cor, ct_les3_block_cor, ct_les4_block_cor, ct_les5_block_cor, ct_les6_block_cor, ct_les7_block_cor, ct_les8_block_cor,
    ct_les9_block_cor, ct_les10_block_cor, ct_les11_block_cor, ct_les12_block_cor, ct_les13_block_cor, ct_les14_block_cor, ct_les15_block_cor, ct_les16_block_cor, ct_les17_block_cor
]

cp_prime_plot = [cp_prime_1, cp_prime_2, cp_prime_3, cp_prime_4, cp_prime_5, cp_prime_6, cp_prime_7, cp_prime_8, cp_prime_9, cp_prime_10, cp_prime_11, cp_prime_12, cp_prime_13, cp_prime_14, cp_prime_15, cp_prime_16, cp_prime_17]
ct_prime_plot = [ct_prime_1, ct_prime_2, ct_prime_3, ct_prime_4, ct_prime_5, ct_prime_6, ct_prime_7, ct_prime_8, ct_prime_9, ct_prime_10, ct_prime_11, ct_prime_12, ct_prime_13, ct_prime_14, ct_prime_15, ct_prime_16, ct_prime_17]
cp_prime_plot_cor = [cp_prime_1_cor, cp_prime_2_cor, cp_prime_3_cor, cp_prime_4_cor, cp_prime_5_cor, cp_prime_6_cor, cp_prime_7_cor, cp_prime_8_cor, cp_prime_9_cor, cp_prime_10_cor, cp_prime_11_cor, cp_prime_12_cor, cp_prime_13_cor, cp_prime_14_cor, cp_prime_15_cor, cp_prime_16_cor, cp_prime_17_cor]
ct_prime_plot_cor = [ct_prime_1_cor, ct_prime_2_cor, ct_prime_3_cor, ct_prime_4_cor, ct_prime_5_cor, ct_prime_6_cor, ct_prime_7_cor, ct_prime_8_cor, ct_prime_9_cor, ct_prime_10_cor, ct_prime_11_cor, ct_prime_12_cor, ct_prime_13_cor, ct_prime_14_cor, ct_prime_15_cor, ct_prime_16_cor, ct_prime_17_cor]

#Graphing
#Cp

#Ct
