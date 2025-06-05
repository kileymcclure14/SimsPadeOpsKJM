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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# High Blocked, No Correction
sim1_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0000")
sim1_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0000", padeops = True, runid = 1, normalize_origin = "turbine")

sim2_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0001")
sim2_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0001", padeops = True, runid = 1, normalize_origin = "turbine")

sim3_folder_hblock = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0002")
sim3_hblock = pio.BudgetIO("Data/B_0002_Files/Sim_0002", padeops = True, runid = 1, normalize_origin = "turbine")

sim4_folder_block = os.path.join(au.DATA_PATH, "B_0002_Files/Sim_0003")
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

# High Blocked, Corrected
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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# High Blocked, No Correction
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

# High Blocked, Corrected
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

# Medium Blocked, No Correction
u_inf1_mblock = sim1_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_mblock = sim2_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_mblock = sim3_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_mblock = sim4_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_mblock = sim5_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_mblock = sim6_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_mblock = sim7_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_mblock = sim8_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_mblock = sim9_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_mblock = sim10_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_mblock = sim11_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_mblock = sim12_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_mblock = sim13_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_mblock = sim14_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_mblock = sim15_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_mblock = sim16_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_mblock = sim17_mblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# Medium Blocked, Corrected
u_inf1_mblock_cor = sim1_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_mblock_cor = sim2_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_mblock_cor = sim3_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_mblock_cor = sim4_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_mblock_cor = sim5_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_mblock_cor = sim6_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_mblock_cor = sim7_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_mblock_cor = sim8_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_mblock_cor = sim9_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_mblock_cor = sim10_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_mblock_cor = sim11_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_mblock_cor = sim12_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_mblock_cor = sim13_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_mblock_cor = sim14_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_mblock_cor = sim15_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_mblock_cor = sim16_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_mblock_cor = sim17_mblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# High Blocked, No Correction
u_inf1_hblock = sim1_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_hblock = sim2_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_hblock = sim3_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_hblock = sim4_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_hblock = sim5_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_hblock = sim6_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_hblock = sim7_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_hblock = sim8_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_hblock = sim9_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf10_hblock = sim10_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf11_hblock = sim11_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf12_hblock = sim12_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf13_hblock = sim13_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf14_hblock = sim14_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf15_hblock = sim15_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf16_hblock = sim16_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf17_hblock = sim17_hblock.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values

# High Blocked, Corrected
u_inf1_hblock_cor = sim1_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf2_hblock_cor = sim2_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf3_hblock_cor = sim3_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf4_hblock_cor = sim4_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf5_hblock_cor = sim5_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf6_hblock_cor = sim6_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf7_hblock_cor = sim7_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf8_hblock_cor = sim8_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
u_inf9_hblock_cor = sim9_hblock_cor.slice(field_terms=['u'], xlim = -5, zlim = 0)['u'].mean("y").values
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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# HighBlocked, Corrected
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

# Meidum Blocked, No Correction
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

# Medium Blocked, Corrected
ud_les1_mblock_cor = sim1_mblock_cor.read_turb_uvel("all", steady = False)
ud_les1_mblock_cor = ud_les1_mblock_cor[-1]
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

# High Blocked, No Correction
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

# High Blocked, Corrected
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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# High Blocked, No Correction
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

# High Blocked, Corrected
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

# Medium Blocked, No Correction
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

# Medium Blocked, Corrected
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

# High Blocked, No Correction
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

# High Blocked, Corrected
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

#Manual Inputs
#Blockage
mb = 0.1
hb = 0.35

#U2/U1 Manual Inputs/Guess
# Medium Uncorrected
u2_u1_m1 = 0.5
u2_u1_m2 = 0.5
u2_u1_m3 = 0.5
u2_u1_m4 = 0.5
u2_u1_m5 = 0.5
u2_u1_m6 = 0.5
u2_u1_m7 = 0.5
u2_u1_m8 = 0.5
u2_u1_m9 = 0.5
u2_u1_m10 = 0.5
u2_u1_m11 = 0.5
u2_u1_m12 = 0.5
u2_u1_m13 = 0.5
u2_u1_m14 = 0.5
u2_u1_m15 = 0.5
u2_u1_m16 = 0.5
u2_u1_m17 = 0.5

# Medium Corrected
u2_u1_m1_cor = 0.5
u2_u1_m2_cor = 0.5
u2_u1_m3_cor = 0.5
u2_u1_m4_cor = 0.5
u2_u1_m5_cor = 0.5
u2_u1_m6_cor = 0.5
u2_u1_m7_cor = 0.5
u2_u1_m8_cor = 0.5
u2_u1_m9_cor = 0.5
u2_u1_m10_cor = 0.5
u2_u1_m11_cor = 0.5
u2_u1_m12_cor = 0.5
u2_u1_m13_cor = 0.5
u2_u1_m14_cor = 0.5
u2_u1_m15_cor = 0.5
u2_u1_m16_cor = 0.5
u2_u1_m17_cor = 0.5

# High Uncorrected
u2_u1_h1 = 0.5
u2_u1_h2 = 0.5
u2_u1_h3 = 0.5
u2_u1_h4 = 0.5
u2_u1_h5 = 0.5
u2_u1_h6 = 0.5
u2_u1_h7 = 0.5
u2_u1_h8 = 0.5
u2_u1_h9 = 0.5
u2_u1_h10 = 0.5
u2_u1_h11 = 0.5
u2_u1_h12 = 0.5
u2_u1_h13 = 0.5
u2_u1_h14 = 0.5
u2_u1_h15 = 0.5
u2_u1_h16 = 0.5
u2_u1_h17 = 0.5

# High Corrected
u2_u1_h1_cor = 0.5
u2_u1_h2_cor = 0.5
u2_u1_h3_cor = 0.5
u2_u1_h4_cor = 0.5
u2_u1_h5_cor = 0.5
u2_u1_h6_cor = 0.5
u2_u1_h7_cor = 0.5
u2_u1_h8_cor = 0.5
u2_u1_h9_cor = 0.5
u2_u1_h10_cor = 0.5
u2_u1_h11_cor = 0.5
u2_u1_h12_cor = 0.5
u2_u1_h13_cor = 0.5
u2_u1_h14_cor = 0.5
u2_u1_h15_cor = 0.5
u2_u1_h16_cor = 0.5
u2_u1_h17_cor = 0.5

#Solving for Ut/U1
#Medium Uncorrected
ut_u1_m1 = (-1 + np.sqrt(1+mb*((u2_u1_m1**2)-1)))/(mb*(u2_u1_m1 -1))
ut_u1_m2 = (-1 + np.sqrt(1+mb*((u2_u1_m2**2)-1)))/(mb*(u2_u1_m2 -1))
ut_u1_m3 = (-1 + np.sqrt(1+mb*((u2_u1_m3**2)-1)))/(mb*(u2_u1_m3 -1))
ut_u1_m4 = (-1 + np.sqrt(1+mb*((u2_u1_m4**2)-1)))/(mb*(u2_u1_m4 -1))
ut_u1_m5 = (-1 + np.sqrt(1+mb*((u2_u1_m5**2)-1)))/(mb*(u2_u1_m5 -1))
ut_u1_m6 = (-1 + np.sqrt(1+mb*((u2_u1_m6**2)-1)))/(mb*(u2_u1_m6 -1))
ut_u1_m7 = (-1 + np.sqrt(1+mb*((u2_u1_m7**2)-1)))/(mb*(u2_u1_m7 -1))
ut_u1_m8 = (-1 + np.sqrt(1+mb*((u2_u1_m8**2)-1)))/(mb*(u2_u1_m8 -1))
ut_u1_m9 = (-1 + np.sqrt(1+mb*((u2_u1_m9**2)-1)))/(mb*(u2_u1_m9 -1))
ut_u1_m10 = (-1 + np.sqrt(1+mb*((u2_u1_m10**2)-1)))/(mb*(u2_u1_m10 -1))
ut_u1_m11 = (-1 + np.sqrt(1+mb*((u2_u1_m11**2)-1)))/(mb*(u2_u1_m11 -1))
ut_u1_m12 = (-1 + np.sqrt(1+mb*((u2_u1_m12**2)-1)))/(mb*(u2_u1_m12 -1))
ut_u1_m13 = (-1 + np.sqrt(1+mb*((u2_u1_m13**2)-1)))/(mb*(u2_u1_m13 -1))
ut_u1_m14 = (-1 + np.sqrt(1+mb*((u2_u1_m14**2)-1)))/(mb*(u2_u1_m14 -1))
ut_u1_m15 = (-1 + np.sqrt(1+mb*((u2_u1_m15**2)-1)))/(mb*(u2_u1_m15 -1))
ut_u1_m16 = (-1 + np.sqrt(1+mb*((u2_u1_m16**2)-1)))/(mb*(u2_u1_m16 -1))
ut_u1_m17 = (-1 + np.sqrt(1+mb*((u2_u1_m17**2)-1)))/(mb*(u2_u1_m17 -1))

# Medium Corrected
ut_u1_m1_cor = (-1 + np.sqrt(1+mb*((u2_u1_m1_cor**2)-1)))/(mb*(u2_u1_m1_cor -1))
ut_u1_m2_cor = (-1 + np.sqrt(1+mb*((u2_u1_m2_cor**2)-1)))/(mb*(u2_u1_m2_cor -1))
ut_u1_m3_cor = (-1 + np.sqrt(1+mb*((u2_u1_m3_cor**2)-1)))/(mb*(u2_u1_m3_cor -1))
ut_u1_m4_cor = (-1 + np.sqrt(1+mb*((u2_u1_m4_cor**2)-1)))/(mb*(u2_u1_m4_cor -1))
ut_u1_m5_cor = (-1 + np.sqrt(1+mb*((u2_u1_m5_cor**2)-1)))/(mb*(u2_u1_m5_cor -1))
ut_u1_m6_cor = (-1 + np.sqrt(1+mb*((u2_u1_m6_cor**2)-1)))/(mb*(u2_u1_m6_cor -1))
ut_u1_m7_cor = (-1 + np.sqrt(1+mb*((u2_u1_m7_cor**2)-1)))/(mb*(u2_u1_m7_cor -1))
ut_u1_m8_cor = (-1 + np.sqrt(1+mb*((u2_u1_m8_cor**2)-1)))/(mb*(u2_u1_m8_cor -1))
ut_u1_m9_cor = (-1 + np.sqrt(1+mb*((u2_u1_m9_cor**2)-1)))/(mb*(u2_u1_m9_cor -1))
ut_u1_m10_cor = (-1 + np.sqrt(1+mb*((u2_u1_m10_cor**2)-1)))/(mb*(u2_u1_m10_cor -1))
ut_u1_m11_cor = (-1 + np.sqrt(1+mb*((u2_u1_m11_cor**2)-1)))/(mb*(u2_u1_m11_cor -1))
ut_u1_m12_cor = (-1 + np.sqrt(1+mb*((u2_u1_m12_cor**2)-1)))/(mb*(u2_u1_m12_cor -1))
ut_u1_m13_cor = (-1 + np.sqrt(1+mb*((u2_u1_m13_cor**2)-1)))/(mb*(u2_u1_m13_cor -1))
ut_u1_m14_cor = (-1 + np.sqrt(1+mb*((u2_u1_m14_cor**2)-1)))/(mb*(u2_u1_m14_cor -1))
ut_u1_m15_cor = (-1 + np.sqrt(1+mb*((u2_u1_m15_cor**2)-1)))/(mb*(u2_u1_m15_cor -1))
ut_u1_m16_cor = (-1 + np.sqrt(1+mb*((u2_u1_m16_cor**2)-1)))/(mb*(u2_u1_m16_cor -1))
ut_u1_m17_cor = (-1 + np.sqrt(1+mb*((u2_u1_m17_cor**2)-1)))/(mb*(u2_u1_m17_cor -1))

#High Uncorrected
ut_u1_h1 = (-1 + np.sqrt(1+hb*((u2_u1_h1**2)-1)))/(hb*(u2_u1_h1 -1))
ut_u1_h2 = (-1 + np.sqrt(1+hb*((u2_u1_h2**2)-1)))/(hb*(u2_u1_h2 -1))
ut_u1_h3 = (-1 + np.sqrt(1+hb*((u2_u1_h3**2)-1)))/(hb*(u2_u1_h3 -1))
ut_u1_h4 = (-1 + np.sqrt(1+hb*((u2_u1_h4**2)-1)))/(hb*(u2_u1_h4 -1))
ut_u1_h5 = (-1 + np.sqrt(1+hb*((u2_u1_h5**2)-1)))/(hb*(u2_u1_h5 -1))
ut_u1_h6 = (-1 + np.sqrt(1+hb*((u2_u1_h6**2)-1)))/(hb*(u2_u1_h6 -1))
ut_u1_h7 = (-1 + np.sqrt(1+hb*((u2_u1_h7**2)-1)))/(hb*(u2_u1_h7 -1))
ut_u1_h8 = (-1 + np.sqrt(1+hb*((u2_u1_h8**2)-1)))/(hb*(u2_u1_h8 -1))
ut_u1_h9 = (-1 + np.sqrt(1+hb*((u2_u1_h9**2)-1)))/(hb*(u2_u1_h9 -1))
ut_u1_h10 = (-1 + np.sqrt(1+hb*((u2_u1_h10**2)-1)))/(hb*(u2_u1_h10 -1))
ut_u1_h11 = (-1 + np.sqrt(1+hb*((u2_u1_h11**2)-1)))/(hb*(u2_u1_h11 -1))
ut_u1_h12 = (-1 + np.sqrt(1+hb*((u2_u1_h12**2)-1)))/(hb*(u2_u1_h12 -1))
ut_u1_h13 = (-1 + np.sqrt(1+hb*((u2_u1_h13**2)-1)))/(hb*(u2_u1_h13 -1))
ut_u1_h14 = (-1 + np.sqrt(1+hb*((u2_u1_h14**2)-1)))/(hb*(u2_u1_h14 -1))
ut_u1_h15 = (-1 + np.sqrt(1+hb*((u2_u1_h15**2)-1)))/(hb*(u2_u1_h15 -1))
ut_u1_h16 = (-1 + np.sqrt(1+hb*((u2_u1_h16**2)-1)))/(hb*(u2_u1_h16 -1))
ut_u1_h17 = (-1 + np.sqrt(1+hb*((u2_u1_h17**2)-1)))/(hb*(u2_u1_h17 -1))

# High Corrected
ut_u1_h1_cor = (-1 + np.sqrt(1+hb*((u2_u1_h1_cor**2)-1)))/(hb*(u2_u1_m1_cor -1))
ut_u1_h2_cor = (-1 + np.sqrt(1+hb*((u2_u1_h2_cor**2)-1)))/(hb*(u2_u1_m2_cor -1))
ut_u1_h3_cor = (-1 + np.sqrt(1+hb*((u2_u1_h3_cor**2)-1)))/(hb*(u2_u1_m3_cor -1))
ut_u1_h4_cor = (-1 + np.sqrt(1+hb*((u2_u1_h4_cor**2)-1)))/(hb*(u2_u1_m4_cor -1))
ut_u1_h5_cor = (-1 + np.sqrt(1+hb*((u2_u1_h5_cor**2)-1)))/(hb*(u2_u1_m5_cor -1))
ut_u1_h6_cor = (-1 + np.sqrt(1+hb*((u2_u1_h6_cor**2)-1)))/(hb*(u2_u1_m6_cor -1))
ut_u1_h7_cor = (-1 + np.sqrt(1+hb*((u2_u1_h7_cor**2)-1)))/(hb*(u2_u1_m7_cor -1))
ut_u1_h8_cor = (-1 + np.sqrt(1+hb*((u2_u1_h8_cor**2)-1)))/(hb*(u2_u1_m8_cor -1))
ut_u1_h9_cor = (-1 + np.sqrt(1+hb*((u2_u1_h9_cor**2)-1)))/(hb*(u2_u1_m9_cor -1))
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
v0_U1_m1_22 = u2_u1_m1 - mb*(ut_u1_m1)*(u2_u1_m1 - 1)
v0_U1_m2_22 = u2_u1_m2 - mb*(ut_u1_m2)*(u2_u1_m2 - 1)
v0_U1_m3_22 = u2_u1_m3 - mb*(ut_u1_m3)*(u2_u1_m3 - 1)
v0_U1_m4_22 = u2_u1_m4 - mb*(ut_u1_m4)*(u2_u1_m4 - 1)
v0_U1_m5_22 = u2_u1_m5 - mb*(ut_u1_m5)*(u2_u1_m5 - 1)
v0_U1_m6_22 = u2_u1_m6 - mb*(ut_u1_m6)*(u2_u1_m6 - 1)
v0_U1_m7_22 = u2_u1_m7 - mb*(ut_u1_m7)*(u2_u1_m7 - 1)
v0_U1_m8_22 = u2_u1_m8 - mb*(ut_u1_m8)*(u2_u1_m8 - 1)
v0_U1_m9_22 = u2_u1_m9 - mb*(ut_u1_m9)*(u2_u1_m9 - 1)
v0_U1_m10_22 = u2_u1_m10 - mb*(ut_u1_m10)*(u2_u1_m10 - 1)
v0_U1_m11_22 = u2_u1_m11 - mb*(ut_u1_m11)*(u2_u1_m11 - 1)
v0_U1_m12_22 = u2_u1_m12 - mb*(ut_u1_m12)*(u2_u1_m12 - 1)
v0_U1_m13_22 = u2_u1_m13 - mb*(ut_u1_m13)*(u2_u1_m13 - 1)
v0_U1_m14_22 = u2_u1_m14 - mb*(ut_u1_m14)*(u2_u1_m14 - 1)
v0_U1_m15_22 = u2_u1_m15 - mb*(ut_u1_m15)*(u2_u1_m15 - 1)
v0_U1_m16_22 = u2_u1_m16 - mb*(ut_u1_m16)*(u2_u1_m16 - 1)
v0_U1_m17_22 = u2_u1_m17 - mb*(ut_u1_m17)*(u2_u1_m17 - 1)

# Medium Corrected, Eq 22 From Paper
v0_U1_m1_cor_22 = u2_u1_m1_cor - mb*(ut_u1_m1_cor)*(u2_u1_m1_cor - 1)
v0_U1_m2_cor_22 = u2_u1_m2_cor - mb*(ut_u1_m2_cor)*(u2_u1_m2_cor - 1)
v0_U1_m3_cor_22 = u2_u1_m3_cor - mb*(ut_u1_m3_cor)*(u2_u1_m3_cor - 1)
v0_U1_m4_cor_22 = u2_u1_m4_cor - mb*(ut_u1_m4_cor)*(u2_u1_m4_cor - 1)
v0_U1_m5_cor_22 = u2_u1_m5_cor - mb*(ut_u1_m5_cor)*(u2_u1_m5_cor - 1)
v0_U1_m6_cor_22 = u2_u1_m6_cor - mb*(ut_u1_m6_cor)*(u2_u1_m6_cor - 1)
v0_U1_m7_cor_22 = u2_u1_m7_cor - mb*(ut_u1_m7_cor)*(u2_u1_m7_cor - 1)
v0_U1_m8_cor_22 = u2_u1_m8_cor - mb*(ut_u1_m8_cor)*(u2_u1_m8_cor - 1)
v0_U1_m9_cor_22 = u2_u1_m9_cor - mb*(ut_u1_m9_cor)*(u2_u1_m9_cor - 1)
v0_U1_m10_cor_22 = u2_u1_m10_cor - mb*(ut_u1_m10_cor)*(u2_u1_m10_cor - 1)
v0_U1_m11_cor_22 = u2_u1_m11_cor - mb*(ut_u1_m11_cor)*(u2_u1_m11_cor - 1)
v0_U1_m12_cor_22 = u2_u1_m12_cor - mb*(ut_u1_m12_cor)*(u2_u1_m12_cor - 1)
v0_U1_m13_cor_22 = u2_u1_m13_cor - mb*(ut_u1_m13_cor)*(u2_u1_m13_cor - 1)
v0_U1_m14_cor_22 = u2_u1_m14_cor - mb*(ut_u1_m14_cor)*(u2_u1_m14_cor - 1)
v0_U1_m15_cor_22 = u2_u1_m15_cor - mb*(ut_u1_m15_cor)*(u2_u1_m15_cor - 1)
v0_U1_m16_cor_22 = u2_u1_m16_cor - mb*(ut_u1_m16_cor)*(u2_u1_m16_cor - 1)
v0_U1_m17_cor_22 = u2_u1_m17_cor - mb*(ut_u1_m17_cor)*(u2_u1_m17_cor - 1)

# High Uncorrected, Eq 22 From Paper
v0_U1_h1_22 = u2_u1_h1 - hb*(ut_u1_h1)*(u2_u1_h1 - 1)
v0_U1_h2_22 = u2_u1_h2 - hb*(ut_u1_h2)*(u2_u1_h2 - 1)
v0_U1_h3_22 = u2_u1_h3 - hb*(ut_u1_h3)*(u2_u1_h3 - 1)
v0_U1_h4_22 = u2_u1_h4 - hb*(ut_u1_h4)*(u2_u1_h4 - 1)
v0_U1_h5_22 = u2_u1_h5 - hb*(ut_u1_h5)*(u2_u1_h5 - 1)
v0_U1_h6_22 = u2_u1_h6 - hb*(ut_u1_h6)*(u2_u1_h6 - 1)
v0_U1_h7_22 = u2_u1_h7 - hb*(ut_u1_h7)*(u2_u1_h7 - 1)
v0_U1_h8_22 = u2_u1_h8 - hb*(ut_u1_h8)*(u2_u1_h8 - 1)
v0_U1_h9_22 = u2_u1_h9 - hb*(ut_u1_h9)*(u2_u1_h9 - 1)
v0_U1_h10_22 = u2_u1_h10 - hb*(ut_u1_h10)*(u2_u1_h10 - 1)
v0_U1_h11_22 = u2_u1_h11 - hb*(ut_u1_h11)*(u2_u1_h11 - 1)
v0_U1_h12_22 = u2_u1_h12 - hb*(ut_u1_h12)*(u2_u1_h12 - 1)
v0_U1_h13_22 = u2_u1_h13 - hb*(ut_u1_h13)*(u2_u1_h13 - 1)
v0_U1_h14_22 = u2_u1_h14 - hb*(ut_u1_h14)*(u2_u1_h14 - 1)
v0_U1_h15_22 = u2_u1_h15 - hb*(ut_u1_h15)*(u2_u1_h15 - 1)
v0_U1_h16_22 = u2_u1_h16 - hb*(ut_u1_h16)*(u2_u1_h16 - 1)
v0_U1_h17_22 = u2_u1_h17 - hb*(ut_u1_h17)*(u2_u1_h17 - 1)

# High Corrected, Eq 22 From Paper
v0_U1_h1_cor_22 = u2_u1_h1_cor - hb*(ut_u1_h1_cor)*(u2_u1_h1_cor - 1)
v0_U1_h2_cor_22 = u2_u1_h2_cor - hb*(ut_u1_h2_cor)*(u2_u1_h2_cor - 1)
v0_U1_h3_cor_22 = u2_u1_h3_cor - hb*(ut_u1_h3_cor)*(u2_u1_h3_cor - 1)
v0_U1_h4_cor_22 = u2_u1_h4_cor - hb*(ut_u1_h4_cor)*(u2_u1_h4_cor - 1)
v0_U1_h5_cor_22 = u2_u1_h5_cor - hb*(ut_u1_h5_cor)*(u2_u1_h5_cor - 1)
v0_U1_h6_cor_22 = u2_u1_h6_cor - hb*(ut_u1_h6_cor)*(u2_u1_h6_cor - 1)
v0_U1_h7_cor_22 = u2_u1_h7_cor - hb*(ut_u1_h7_cor)*(u2_u1_h7_cor - 1)
v0_U1_h8_cor_22 = u2_u1_h8_cor - hb*(ut_u1_h8_cor)*(u2_u1_h8_cor - 1)
v0_U1_h9_cor_22 = u2_u1_h9_cor - hb*(ut_u1_h9_cor)*(u2_u1_h9_cor - 1)
v0_U1_h10_cor_22 = u2_u1_h10_cor - hb*(ut_u1_h10_cor)*(u2_u1_h10_cor - 1)
v0_U1_h11_cor_22 = u2_u1_h11_cor - hb*(ut_u1_h11_cor)*(u2_u1_h11_cor - 1)
v0_U1_h12_cor_22 = u2_u1_h12_cor - hb*(ut_u1_h12_cor)*(u2_u1_h12_cor - 1)
v0_U1_h13_cor_22 = u2_u1_h13_cor - hb*(ut_u1_h13_cor)*(u2_u1_h13_cor - 1)
v0_U1_h14_cor_22 = u2_u1_h14_cor - hb*(ut_u1_h14_cor)*(u2_u1_h14_cor - 1)
v0_U1_h15_cor_22 = u2_u1_h15_cor - hb*(ut_u1_h15_cor)*(u2_u1_h15_cor - 1)
v0_U1_h16_cor_22 = u2_u1_h16_cor - hb*(ut_u1_h16_cor)*(u2_u1_h16_cor - 1)
v0_U1_h17_cor_22 = u2_u1_h17_cor - hb*(ut_u1_h17_cor)*(u2_u1_h17_cor - 1)

# Medium Uncorrected, Eq 23 From Paper
v0_U1_m1_23 = np.sqrt(((u2_u1_m1**2)-1)/ct_les1_mblock)
v0_U1_m2_23 = np.sqrt(((u2_u1_m2**2)-1)/ct_les2_mblock)
v0_U1_m3_23 = np.sqrt(((u2_u1_m3**2)-1)/ct_les3_mblock)
v0_U1_m4_23 = np.sqrt(((u2_u1_m4**2)-1)/ct_les4_mblock)
v0_U1_m5_23 = np.sqrt(((u2_u1_m5**2)-1)/ct_les5_mblock)
v0_U1_m6_23 = np.sqrt(((u2_u1_m6**2)-1)/ct_les6_mblock)
v0_U1_m7_23 = np.sqrt(((u2_u1_m7**2)-1)/ct_les7_mblock)
v0_U1_m8_23 = np.sqrt(((u2_u1_m8**2)-1)/ct_les8_mblock)
v0_U1_m9_23 = np.sqrt(((u2_u1_m9**2)-1)/ct_les9_mblock)
v0_U1_m10_23 = np.sqrt(((u2_u1_m10**2)-1)/ct_les10_mblock)
v0_U1_m11_23 = np.sqrt(((u2_u1_m11**2)-1)/ct_les11_mblock)
v0_U1_m12_23 = np.sqrt(((u2_u1_m12**2)-1)/ct_les12_mblock)
v0_U1_m13_23 = np.sqrt(((u2_u1_m13**2)-1)/ct_les13_mblock)
v0_U1_m14_23 = np.sqrt(((u2_u1_m14**2)-1)/ct_les14_mblock)
v0_U1_m15_23 = np.sqrt(((u2_u1_m15**2)-1)/ct_les15_mblock)
v0_U1_m16_23 = np.sqrt(((u2_u1_m16**2)-1)/ct_les16_mblock)
v0_U1_m17_23 = np.sqrt(((u2_u1_m17**2)-1)/ct_les17_mblock)

# Medium Corrected, Eq 23 From Paper
v0_U1_m1_cor_23 = np.sqrt(((u2_u1_m1_cor**2)-1)/ct_les1_mblock_cor)
v0_U1_m2_cor_23 = np.sqrt(((u2_u1_m2_cor**2)-1)/ct_les2_mblock_cor)
v0_U1_m3_cor_23 = np.sqrt(((u2_u1_m3_cor**2)-1)/ct_les3_mblock_cor)
v0_U1_m4_cor_23 = np.sqrt(((u2_u1_m4_cor**2)-1)/ct_les4_mblock_cor)
v0_U1_m5_cor_23 = np.sqrt(((u2_u1_m5_cor**2)-1)/ct_les5_mblock_cor)
v0_U1_m6_cor_23 = np.sqrt(((u2_u1_m6_cor**2)-1)/ct_les6_mblock_cor)
v0_U1_m7_cor_23 = np.sqrt(((u2_u1_m7_cor**2)-1)/ct_les7_mblock_cor)
v0_U1_m8_cor_23 = np.sqrt(((u2_u1_m8_cor**2)-1)/ct_les8_mblock_cor)
v0_U1_m9_cor_23 = np.sqrt(((u2_u1_m9_cor**2)-1)/ct_les9_mblock_cor)
v0_U1_m10_cor_23 = np.sqrt(((u2_u1_m10_cor**2)-1)/ct_les10_mblock_cor)
v0_U1_m11_cor_23 = np.sqrt(((u2_u1_m11_cor**2)-1)/ct_les11_mblock_cor)
v0_U1_m12_cor_23 = np.sqrt(((u2_u1_m12_cor**2)-1)/ct_les12_mblock_cor)
v0_U1_m13_cor_23 = np.sqrt(((u2_u1_m13_cor**2)-1)/ct_les13_mblock_cor)
v0_U1_m14_cor_23 = np.sqrt(((u2_u1_m14_cor**2)-1)/ct_les14_mblock_cor)
v0_U1_m15_cor_23 = np.sqrt(((u2_u1_m15_cor**2)-1)/ct_les15_mblock_cor)
v0_U1_m16_cor_23 = np.sqrt(((u2_u1_m16_cor**2)-1)/ct_les16_mblock_cor)
v0_U1_m17_cor_23 = np.sqrt(((u2_u1_m17_cor**2)-1)/ct_les17_mblock_cor)

# High Uncorrected, Eq 23 From Paper
v0_U1_h1_23 = np.sqrt(((u2_u1_h1**2)-1)/ct_les1_hblock)
v0_U1_h2_23 = np.sqrt(((u2_u1_h2**2)-1)/ct_les2_hblock)
v0_U1_h3_23 = np.sqrt(((u2_u1_h3**2)-1)/ct_les3_hblock)
v0_U1_h4_23 = np.sqrt(((u2_u1_h4**2)-1)/ct_les4_hblock)
v0_U1_h5_23 = np.sqrt(((u2_u1_h5**2)-1)/ct_les5_hblock)
v0_U1_h6_23 = np.sqrt(((u2_u1_h6**2)-1)/ct_les6_hblock)
v0_U1_h7_23 = np.sqrt(((u2_u1_h7**2)-1)/ct_les7_hblock)
v0_U1_h8_23 = np.sqrt(((u2_u1_h8**2)-1)/ct_les8_hblock)
v0_U1_h9_23 = np.sqrt(((u2_u1_h9**2)-1)/ct_les9_hblock)
v0_U1_h10_23 = np.sqrt(((u2_u1_h10**2)-1)/ct_les10_hblock)
v0_U1_h11_23 = np.sqrt(((u2_u1_h11**2)-1)/ct_les11_hblock)
v0_U1_h12_23 = np.sqrt(((u2_u1_h12**2)-1)/ct_les12_hblock)
v0_U1_h13_23 = np.sqrt(((u2_u1_h13**2)-1)/ct_les13_hblock)
v0_U1_h14_23 = np.sqrt(((u2_u1_h14**2)-1)/ct_les14_hblock)
v0_U1_h15_23 = np.sqrt(((u2_u1_h15**2)-1)/ct_les15_hblock)
v0_U1_h16_23 = np.sqrt(((u2_u1_h16**2)-1)/ct_les16_hblock)
v0_U1_h17_23 = np.sqrt(((u2_u1_h17**2)-1)/ct_les17_hblock)

# High Corrected, Eq 23 From Paper
v0_U1_h1_cor_23 = np.sqrt(((u2_u1_h1_cor**2)-1)/ct_les1_hblock_cor)
v0_U1_h2_cor_23 = np.sqrt(((u2_u1_h2_cor**2)-1)/ct_les2_hblock_cor)
v0_U1_h3_cor_23 = np.sqrt(((u2_u1_h3_cor**2)-1)/ct_les3_hblock_cor)
v0_U1_h4_cor_23 = np.sqrt(((u2_u1_h4_cor**2)-1)/ct_les4_hblock_cor)
v0_U1_h5_cor_23 = np.sqrt(((u2_u1_h5_cor**2)-1)/ct_les5_hblock_cor)
v0_U1_h6_cor_23 = np.sqrt(((u2_u1_h6_cor**2)-1)/ct_les6_hblock_cor)
v0_U1_h7_cor_23 = np.sqrt(((u2_u1_h7_cor**2)-1)/ct_les7_hblock_cor)
v0_U1_h8_cor_23 = np.sqrt(((u2_u1_h8_cor**2)-1)/ct_les8_hblock_cor)
v0_U1_h9_cor_23 = np.sqrt(((u2_u1_h9_cor**2)-1)/ct_les9_hblock_cor)
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
if np.absolute(v0_U1_m1_22 - v0_U1_m1_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0000")
else:
    v0_u1_m1 = np.mean([v0_U1_m1_22, v0_U1_m1_23])
    ut_v0_m1 = ut_u1_m1/v0_u1_m1
    v0_prime_m1 = (u_inf1_mblock*((ut_v0_m1**2 + (ct_les1_mblock/4))))/(ut_v0_m1)
    cp_prime_m1 = cp_les1_mblock*((u_inf1_mblock/v0_prime_m1)**3)
    ct_prime_m1 = ct_les1_mblock*((u_inf1_mblock/v0_prime_m1)**2)

if np.absolute(v0_U1_m2_22 - v0_U1_m2_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0001")
else:
    v0_u1_m2 = np.mean([v0_U1_m2_22, v0_U1_m2_23])
    ut_v0_m2 = ut_u1_m2/v0_u1_m2
    v0_prime_m2 = (u_inf2_mblock*((ut_v0_m2**2 + (ct_les2_mblock/4))))/(ut_v0_m2)
    cp_prime_m2 = cp_les2_mblock*((u_inf2_mblock/v0_prime_m2)**3)
    ct_prime_m2 = ct_les2_mblock*((u_inf2_mblock/v0_prime_m2)**2)

if np.absolute(v0_U1_m3_22 - v0_U1_m3_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0002")
else:
    v0_u1_m3 = np.mean([v0_U1_m3_22, v0_U1_m3_23])
    ut_v0_m3 = ut_u1_m3/v0_u1_m3
    v0_prime_m3 = (u_inf3_mblock*((ut_v0_m3**2 + (ct_les3_mblock/4))))/(ut_v0_m3)
    cp_prime_m3 = cp_les3_mblock*((u_inf3_mblock/v0_prime_m3)**3)
    ct_prime_m3 = ct_les3_mblock*((u_inf3_mblock/v0_prime_m3)**2)

if np.absolute(v0_U1_m4_22 - v0_U1_m4_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0003")
else:
    v0_u1_m4 = np.mean([v0_U1_m4_22, v0_U1_m4_23])
    ut_v0_m4 = ut_u1_m4/v0_u1_m4
    v0_prime_m4 = (u_inf4_mblock*((ut_v0_m4**2 + (ct_les4m_block/4))))/(ut_v0_m4)
    cp_prime_m4 = cp_les4_mblock*((u_inf4_mblock/v0_prime_m4)**3)
    ct_prime_m4 = ct_les4_mblock*((u_inf4_mblock/v0_prime_m4)**2)

if np.absolute(v0_U1_m5_22 - v0_U1_m5_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0004")
else:
    v0_u1_m5 = np.mean([v0_U1_m5_22, v0_U1_m5_23])
    ut_v0_m5 = ut_u1_m5/v0_u1_m5
    v0_prime_m5 = (u_inf5_mblock*((ut_v0_m5**2 + (ct_les5_mblock/4))))/(ut_v0_m5)
    cp_prime_m5 = cp_les5_mblock*((u_inf5_mblock/v0_prime_m5)**3)
    ct_prime_m5 = ct_les5_mblock*((u_inf5_mblock/v0_prime_m5)**2)

if np.absolute(v0_U1_m6_22 - v0_U1_m6_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0005")
else:
    v0_u1_m6 = np.mean([v0_U1_m6_22, v0_U1_m6_23])
    ut_v0_m6 = ut_u1_m6/v0_u1_m6
    v0_prime_m6 = (u_inf6_mblock*((ut_v0_m6**2 + (ct_les6_mblock/4))))/(ut_v0_m6)
    cp_prime_m6 = cp_les6_mblock*((u_inf6_mblock/v0_prime_m6)**3)
    ct_prime_m6 = ct_les6_mblock*((u_inf6_mblock/v0_prime_m6)**2)

if np.absolute(v0_U1_m7_22 - v0_U1_m7_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0006")
else:
    v0_u1_m7 = np.mean([v0_U1_m7_22, v0_U1_m7_23])
    ut_v0_m7 = ut_u1_m7/v0_u1_m7
    v0_prime_m7 = (u_inf7_mblock*((ut_v0_m7**2 + (ct_les7_mblock/4))))/(ut_v0_m7)
    cp_prime_m7 = cp_les7_mblock*((u_inf7_mblock/v0_prime_m7)**3)
    ct_prime_m7 = ct_les7_mblock*((u_inf7_mblock/v0_prime_m7)**2)

if np.absolute(v0_U1_m8_22 - v0_U1_m8_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0007")
else:
    v0_u1_m8 = np.mean([v0_U1_m8_22, v0_U1_m8_23])
    ut_v0_m8 = ut_u1_m8/v0_u1_m8
    v0_prime_m8 = (u_inf8_mblock*((ut_v0_m8**2 + (ct_les8_mblock/4))))/(ut_v0_m8)
    cp_prime_m8 = cp_les8_mblock*((u_inf8_mblock/v0_prime_m8)**3)
    ct_prime_m8 = ct_les8_mblock*((u_inf8_mblock/v0_prime_m8)**2)

if np.absolute(v0_U1_m9_22 - v0_U1_m9_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0008")
else:
    v0_u1_m9 = np.mean([v0_U1_m9_22, v0_U1_m9_23])
    ut_v0_m9 = ut_u1_m9/v0_u1_m9
    v0_prime_m9 = (u_inf9_mblock*((ut_v0_m9**2 + (ct_les9_mblock/4))))/(ut_v0_m9)
    cp_prime_m9 = cp_les9_mblock*((u_inf9_mblock/v0_prime_m9)**3)
    ct_prime_m9 = ct_les9_mblock*((u_inf9_mblock/v0_prime_m9)**2)

if np.absolute(v0_U1_m10_22 - v0_U1_m10_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0009")
else:
    v0_u1_m10 = np.mean([v0_U1_m10_22, v0_U1_m10_23])
    ut_v0_m10 = ut_u1_m10/v0_u1_m10
    v0_prime_m10 = (u_inf10_mblock*((ut_v0_m10**2 + (ct_les10_mblock/4))))/(ut_v0_m10)
    cp_prime_m10 = cp_les10_mblock*((u_inf10_mblock/v0_prime_m10)**3)
    ct_prime_m10 = ct_les10_mblock*((u_inf10_mblock/v0_prime_m10)**2)

if np.absolute(v0_U1_m11_22 - v0_U1_m11_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0010")
else:
    v0_u1_m11 = np.mean([v0_U1_m11_22, v0_U1_m11_23])
    ut_v0_m11 = ut_u1_m11/v0_u1_m11
    v0_prime_m11 = (u_inf11_mblock*((ut_v0_m11**2 + (ct_les11_mblock/4))))/(ut_v0_m11)
    cp_prime_m11 = cp_les11_mblock*((u_inf11_mblock/v0_prime_m11)**3)
    ct_prime_m11 = ct_les11_mblock*((u_inf11_mblock/v0_prime_m11)**2)

if np.absolute(v0_U1_m12_22 - v0_U1_m12_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0011")
else:
    v0_u1_m12 = np.mean([v0_U1_12_22, v0_U1_12_23])
    ut_v0_m12 = ut_u1_m12/v0_u1_m12
    v0_prime_m12 = (u_inf12_mblock*((ut_v0_m12**2 + (ct_les12_mblock/4))))/(ut_v0_m12)
    cp_prime_m12 = cp_les12_mblock*((u_inf12_mblock/v0_prime_m12)**3)
    ct_prime_m12 = ct_les12_mblock*((u_inf12_mblock/v0_prime_m12)**2)

if np.absolute(v0_U1_m13_22 - v0_U1_m13_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0012")
else:
    v0_u1_m13 = np.mean([v0_U1_m13_22, v0_U1_m13_23])
    ut_v0_m13 = ut_u1_m13/v0_u1_m13
    v0_prime_m13 = (u_inf13_mblock*((ut_v0_m13**2 + (ct_les13_mblock/4))))/(ut_v0_m13)
    cp_prime_m13 = cp_les13_mblock*((u_inf13_mblock/v0_prime_m13)**3)
    ct_prime_m13 = ct_les13_mblock*((u_inf13_mblock/v0_prime_m13)**2)

if np.absolute(v0_U1_m14_22 - v0_U1_m14_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0013")
else:
    v0_u1_m14 = np.mean([v0_U1_m14_22, v0_U1_m14_23])
    ut_v0_m14 = ut_u1_m14/v0_u1_m14
    v0_prime_m14 = (u_inf14_mblock*((ut_v0_m14**2 + (ct_les14_mblock/4))))/(ut_v0_m14)
    cp_prime_m14 = cp_les14_mblock*((u_inf14_mblock/v0_prime_m14)**3)
    ct_prime_m14 = ct_les14_mblock*((u_inf14_mblock/v0_prime_m14)**2)

if np.absolute(v0_U1_m15_22 - v0_U1_m15_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0014")
else:
    v0_u1_m15 = np.mean([v0_U1_m15_22, v0_U1_m15_23])
    ut_v0_m15 = ut_u1_m15/v0_u1_m15
    v0_prime_m15 = (u_inf15_mblock*((ut_v0_m15**2 + (ct_les15_mblock/4))))/(ut_v0_m15)
    cp_prime_m15 = cp_les15_mblock*((u_inf15_mblock/v0_prime_m15)**3)
    ct_prime_m15 = ct_les15_mblock*((u_inf15_mblock/v0_prime_m15)**2)

if np.absolute(v0_U1_m16_22 - v0_U1_1m6_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0015")
else:
    v0_u1_m16 = np.mean([v0_U1_m16_22, v0_U1_m16_23])
    ut_v0_m16 = ut_u1_m16/v0_u1_m16
    v0_prime_m16 = (u_inf16_mblock*((ut_v0_m16**2 + (ct_les16_mblock/4))))/(ut_v0_m16)
    cp_prime_m16 = cp_les16_mblock*((u_inf16_mblock/v0_prime_m16)**3)
    ct_prime_m16 = ct_les16_mblock*((u_inf16_mblock/v0_prime_m16)**2)

if np.absolute(v0_U1_m17_22 - v0_U1_m17_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0016")
else:
    v0_u1_m17 = np.mean([v0_U1_m17_22, v0_U1_m17_23])
    ut_v0_m17 = ut_u1_m17/v0_u1_m17
    v0_prime_m17 = (u_inf17_mblock*((ut_v0_m17**2 + (ct_les17_mblock/4))))/(ut_v0_m17)
    cp_prime_m17 = cp_les17_mblock*((u_inf17_mblock/v0_prime_m17)**3)
    ct_prime_m17 = ct_les17_mblock*((u_inf17_mblock/v0_prime_m17)**2)

# Medium Corrected
if np.absolute(v0_U1_1_cor_m22 - v0_U1_1_cor_m23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0000")
else:
    v0_u1_m1_cor = np.mean([v0_U1_m1_cor_22, v0_U1_m1_cor_23])
    ut_v0_m1_cor = ut_u1_m1_cor/v0_u1_m1_cor
    v0_prime_m1_cor = (u_inf1_mblock_cor*((ut_v0_m1_cor**2 + (ct_les1_mblock_cor/4))))/(ut_v0_m1_cor)
    cp_prime_m1_cor = cp_les1_mblock_cor*((u_inf1_mblock_cor/v0_prime_m1_cor)**3)
    ct_prime_m1_cor = ct_les1_mblock_cor*((u_inf1_mblock_cor/v0_prime_m1_cor)**2)

if np.absolute(v0_U1_m2_cor_22 - v0_U1_m2_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0001")
else:
    v0_u1_m2_cor = np.mean([v0_U1_m2_cor_22, v0_U1_m2_cor_23])
    ut_v0_m2_cor = ut_u1_m2_cor/v0_u1_m2_cor
    v0_prime_m2_cor = (u_inf2_mblock_cor*((ut_v0_m2_cor**2 + (ct_les2_mblock_cor/4))))/(ut_v0_m2_cor)
    cp_prime_m2_cor = cp_les2_mblock_cor*((u_inf2_mblock_cor/v0_prime_m2_cor)**3)
    ct_prime_m2_cor = ct_les2_mblock_cor*((u_inf2_mblock_cor/v0_prime_m2_cor)**2)

if np.absolute(v0_U1_m3_cor_22 - v0_U1_m3_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0002")
else:
    v0_u1_m3_cor = np.mean([v0_U1_m3_cor_22, v0_U1_m3_cor_23])
    ut_v0_m3_cor = ut_u1_m3_cor/v0_u1_m3_cor
    v0_prime_m3_cor = (u_inf3_mblock_cor*((ut_v0_m3_cor**2 + (ct_les3_mblock_cor/4))))/(ut_v0_m3_cor)
    cp_prime_m3_cor = cp_les3_mblock_cor*((u_inf3_mblock_cor/v0_prime_m3_cor)**3)
    ct_prime_m3_cor = ct_les3_mblock_cor*((u_inf3_mblock_cor/v0_prime_m3_cor)**2)

if np.absolute(v0_U1_m4_cor_22 - v0_U1_m4_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0003")
else:
    v0_u1_m4_cor = np.mean([v0_U1_m4_cor_22, v0_U1_m4_cor_23])
    ut_v0_m4_cor = ut_u1_m4_cor/v0_u1_m4_cor
    v0_prime_m4_cor = (u_inf4_mblock_cor*((ut_v0_m4_cor**2 + (ct_les4_mblock_cor/4))))/(ut_v0_m4_cor)
    cp_prime_m4_cor = cp_les4_mblock_cor*((u_inf4_mblock_cor/v0_prime_m4_cor)**3)
    ct_prime_m4_cor = ct_les4_mblock_cor*((u_inf4_mblock_cor/v0_prime_m4_cor)**2)

if np.absolute(v0_U1_m5_cor_22 - v0_U1_m5_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0004")
else:
    v0_u1_m5_cor = np.mean([v0_U1_m5_cor_22, v0_U1_m5_cor_23])
    ut_v0_m5_cor = ut_u1_m5_cor/v0_u1_m5_cor
    v0_prime_m5_cor = (u_inf5_mblock_cor*((ut_v0_m5_cor**2 + (ct_les5_mblock_cor/4))))/(ut_v0_m5_cor)
    cp_prime_m5_cor = cp_les5_mblock_cor*((u_inf5_mblock_cor/v0_prime_m5_cor)**3)
    ct_prime_m5_cor = ct_les5_mblock_cor*((u_inf5_mblock_cor/v0_prime_m5_cor)**2)

if np.absolute(v0_U1_m6_cor_22 - v0_U1_m6_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0005")
else:
    v0_u1_m6_cor = np.mean([v0_U1_m6_cor_22, v0_U1_m6_cor_23])
    ut_v0_m6_cor = ut_u1_m6_cor/v0_u1_m6_cor
    v0_prime_m6_cor = (u_inf6_mblock_cor*((ut_v0_m6_cor**2 + (ct_les6_mblock_cor/4))))/(ut_v0_m6_cor)
    cp_prime_m6_cor = cp_les6_mblock_cor*((u_inf6_mblock_cor/v0_prime_m6_cor)**3)
    ct_prime_m6_cor = ct_les6_mblock_cor*((u_inf6_mblock_cor/v0_prime_m6_cor)**2)

if np.absolute(v0_U1_m7_cor_22 - v0_U1_m7_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0006")
else:
    v0_u1_m7_cor = np.mean([v0_U1_m7_cor_22, v0_U1_m7_cor_23])
    ut_v0_m7_cor = ut_u1_m7_cor/v0_u1_m7_cor
    v0_prime_m7_cor = (u_inf7_mblock_cor*((ut_v0_m7_cor**2 + (ct_les7_mblock_cor/4))))/(ut_v0_m7_cor)
    cp_prime_m7_cor = cp_les7_mblock_cor*((u_inf7_mblock_cor/v0_prime_m7_cor)**3)
    ct_prime_m7_cor = ct_les7_mblock_cor*((u_inf7_mblock_cor/v0_prime_m7_cor)**2)

if np.absolute(v0_U1_m8_cor_22 - v0_U1_m8_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0007")
else:
    v0_u1_m8_cor = np.mean([v0_U1_m8_cor_22, v0_U1_m8_cor_23])
    ut_v0_m8_cor = ut_u1_m8_cor/v0_u1_m8_cor
    v0_prime_m8_cor = (u_inf8_mblock_cor*((ut_v0_m8_cor**2 + (ct_les8_mblock_cor/4))))/(ut_v0_m8_cor)
    cp_prime_m8_cor = cp_les8_mblock_cor*((u_inf8_mblock_cor/v0_prime_m8_cor)**3)
    ct_prime_m8_cor = ct_les8_mblock_cor*((u_inf8_mblock_cor/v0_prime_m8_cor)**2)

if np.absolute(v0_U1_m9_cor_22 - v0_U1_m9_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0008")
else:
    v0_u1_m9_cor = np.mean([v0_U1_m9_cor_22, v0_U1_m9_cor_23])
    ut_v0_m9_cor = ut_u1_m9_cor/v0_u1_m9_cor
    v0_prime_m9_cor = (u_inf9_mblock_cor*((ut_v0_m9_cor**2 + (ct_les9_mblock_cor/4))))/(ut_v0_m9_cor)
    cp_prime_m9_cor = cp_les9_mblock_cor*((u_inf9_mblock_cor/v0_prime_m9_cor)**3)
    ct_prime_m9_cor = ct_les9_mblock_cor*((u_inf9_mblock_cor/v0_prime_m9_cor)**2)

if np.absolute(v0_U1_m10_cor_22 - v0_U1_m10_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0009")
else:
    v0_u1_m10_cor = np.mean([v0_U1_m10_cor_22, v0_U1_m10_cor_23])
    ut_v0_m10_cor = ut_u1_m10_cor/v0_u1_10_cor
    v0_prime_m10_cor = (u_inf10_mblock_cor*((ut_v0_m10_cor**2 + (ct_les10_mblock_cor/4))))/(ut_v0_m10_cor)
    cp_prime_m10_cor = cp_les10_mblock_cor*((u_inf10_mblock_cor/v0_prime_m10_cor)**3)
    ct_prime_m10_cor = ct_les10_mblock_cor*((u_inf10_mblock_cor/v0_prime_m10_cor)**2)

if np.absolute(v0_U1_m11_cor_22 - v0_U1_m11_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0010")
else:
    v0_u1_m11_cor = np.mean([v0_U1_m11_cor_22, v0_U1_m11_cor_23])
    ut_v0_m11_cor = ut_u1_m11_cor/v0_u1_m11_cor
    v0_prime_m11_cor = (u_inf11_mblock_cor*((ut_v0_m11_cor**2 + (ct_les11_mblock_cor/4))))/(ut_v0_m11_cor)
    cp_prime_m11_cor = cp_les11_mblock_cor*((u_inf11_mblock_cor/v0_prime_m11_cor)**3)
    ct_prime_m11_cor = ct_les11_mblock_cor*((u_inf11_mblock_cor/v0_prime_m11_cor)**2)

if np.absolute(v0_U1_m12_cor_22 - v0_U1_m12_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0011")
else:
    v0_u1_m12_cor = np.mean([v0_U1_m12_cor_22, v0_U1_m12_cor_23])
    ut_v0_m12_cor = ut_u1_m12_cor/v0_u1_m12_cor
    v0_prime_m12_cor = (u_inf12_mblock_cor*((ut_v0_m12_cor**2 + (ct_les12_mblock_cor/4))))/(ut_v0_m12_cor)
    cp_prime_m12_cor = cp_les12_mblock_cor*((u_inf12_mblock_cor/v0_prime_m12_cor)**3)
    ct_prime_m12_cor = ct_les12_mblock_cor*((u_inf12_mblock_cor/v0_prime_m12_cor)**2)

if np.absolute(v0_U1_m13_cor_22 - v0_U1_m13_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0012")
else:
    v0_u1_m13_cor = np.mean([v0_U1_m13_cor_22, v0_U1_m13_cor_23])
    ut_v0_m13_cor = ut_u1_m13_cor/v0_u1_13_cor
    v0_prime_m13_cor = (u_inf13_mblock_cor*((ut_v0_m13_cor**2 + (ct_les13_mblock_cor/4))))/(ut_v0_m13_cor)
    cp_prime_m13_cor = cp_les13_mblock_cor*((u_inf13_mblock_cor/v0_prime_m13_cor)**3)
    ct_prime_m13_cor = ct_les13_mblock_cor*((u_inf13_mblock_cor/v0_prime_m13_cor)**2)

if np.absolute(v0_U1_m14_cor_22 - v0_U1_m14_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0013")
else:
    v0_u1_m14_cor = np.mean([v0_U1_m14_cor_22, v0_U1_m14_cor_23])
    ut_v0_m14_cor = ut_u1_m14_cor/v0_u1_m14_cor
    v0_prime_m14_cor = (u_inf14_mblock_cor*((ut_v0_m14_cor**2 + (ct_les14_mblock_cor/4))))/(ut_v0_m14_cor)
    cp_prime_m14_cor = cp_les14_mblock_cor*((u_inf14_mblock_cor/v0_prime_m14_cor)**3)
    ct_prime_m14_cor = ct_les14_mblock_cor*((u_inf14_mblock_cor/v0_prime_m14_cor)**2)

if np.absolute(v0_U1_m15_cor_22 - v0_U1_m15_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0014")
else:
    v0_u1_m15_cor = np.mean([v0_U1_m15_cor_22, v0_U1_m15_cor_23])
    ut_v0_m15_cor = ut_u1_m15_cor/v0_u1_m15_cor
    v0_prime_m15_cor = (u_inf15_mblock_cor*((ut_v0_m15_cor**2 + (ct_les15_mblock_cor/4))))/(ut_v0_m15_cor)
    cp_prime_m15_cor = cp_les15_mblock_cor*((u_inf15_mblock_cor/v0_prime_m15_cor)**3)
    ct_prime_m15_cor = ct_les15_mblock_cor*((u_inf15_mblock_cor/v0_prime_m15_cor)**2)

if np.absolute(v0_U1_m16_cor_22 - v0_U1_m16_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0015")
else:
    v0_u1_m16_cor = np.mean([v0_U1_m16_cor_22, v0_U1_m16_cor_23])
    ut_v0_m16_cor = ut_u1_m16_cor/v0_u1_m16_cor
    v0_prime_m16_cor = (u_inf16_mblock_cor*((ut_v0_m16_cor**2 + (ct_les16_mblock_cor/4))))/(ut_v0_m16_cor)
    cp_prime_m16_cor = cp_les16_mblock_cor*((u_inf16_mblock_cor/v0_prime_m16_cor)**3)
    ct_prime_m16_cor = ct_les16_mblock_cor*((u_inf16_mblock_cor/v0_prime_m16_cor)**2)

if np.absolute(v0_U1_m17_cor_22 - v0_U1_m17_cor_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Corrected Sim0016")
else:
    v0_u1_m17_cor = np.mean([v0_U1_m17_cor_22, v0_U1_m17_cor_23])
    ut_v0_m17_cor = ut_u1_m17_cor/v0_u1_m17_cor
    v0_prime_m17_cor = (u_inf17_mblock_cor*((ut_v0_m17_cor**2 + (ct_les17_mblock_cor/4))))/(ut_v0_m17_cor)
    cp_prime_m17_cor = cp_les17_mblock_cor*((u_inf17_mblock_cor/v0_prime_m17_cor)**3)
    ct_prime_m17_cor = ct_les17_mblock_cor*((u_inf17_mblock_cor/v0_prime_m17_cor)**2)

# High Uncorrected
if np.absolute(v0_U1_h1_22 - v0_U1_h1_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0000")
else:
    v0_u1_h1 = np.mean([v0_U1_h1_22, v0_U1_h1_23])
    ut_v0_h1 = ut_u1_h1/v0_u1_h1
    v0_prime_h1 = (u_inf1_hblock*((ut_v0_h1**2 + (ct_les1_hblock/4))))/(ut_v0_h1)
    cp_prime_h1 = cp_les1_hblock*((u_inf1_hblock/v0_prime_h1)**3)
    ct_prime_h1 = ct_les1_hblock*((u_inf1_hblock/v0_prime_h1)**2)

if np.absolute(v0_U1_h2_22 - v0_U1_h2_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0001")
else:
    v0_u1_h2 = np.mean([v0_U1_h2_22, v0_U1_h2_23])
    ut_v0_h2 = ut_u1_h2/v0_u1_h2
    v0_prime_h2 = (u_inf2_hblock*((ut_v0_h2**2 + (ct_les2_hblock/4))))/(ut_v0_h2)
    cp_prime_h2 = cp_les2_hblock*((u_inf2_hblock/v0_prime_h2)**3)
    ct_prime_h2 = ct_les2_hblock*((u_inf2_hblock/v0_prime_h2)**2)

if np.absolute(v0_U1_h3_22 - v0_U1_h3_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0002")
else:
    v0_u1_h3 = np.mean([v0_U1_h3_22, v0_U1_h3_23])
    ut_v0_h3 = ut_u1_h3/v0_u1_h3
    v0_prime_h3 = (u_inf3_hblock*((ut_v0_h3**2 + (ct_les3_hblock/4))))/(ut_v0_h3)
    cp_prime_h3 = cp_les3_hblock*((u_inf3_hblock/v0_prime_h3)**3)
    ct_prime_h3 = ct_les3_hblock*((u_inf3_hblock/v0_prime_h3)**2)

if np.absolute(v0_U1_h4_22 - v0_U1_h4_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0003")
else:
    v0_u1_h4 = np.mean([v0_U1_h4_22, v0_U1_h4_23])
    ut_v0_h4 = ut_u1_h4/v0_u1_h4
    v0_prime_h4 = (u_inf4_hblock*((ut_v0_h4**2 + (ct_les4_hblock/4))))/(ut_v0_h4)
    cp_prime_h4 = cp_les4_hblock*((u_inf4_hblock/v0_prime_h4)**3)
    ct_prime_h4 = ct_les4_hblock*((u_inf4_hblock/v0_prime_h4)**2)

if np.absolute(v0_U1_h5_22 - v0_U1_h5_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0004")
else:
    v0_u1_h5 = np.mean([v0_U1_h5_22, v0_U1_h5_23])
    ut_v0_h5 = ut_u1_h5/v0_u1_h5
    v0_prime_h5 = (u_inf5_hblock*((ut_v0_h5**2 + (ct_les5_hblock/4))))/(ut_v0_h5)
    cp_prime_h5 = cp_les5_hblock*((u_inf5_hblock/v0_prime_h5)**3)
    ct_prime_h5 = ct_les5_hblock*((u_inf5_hblock/v0_prime_h5)**2)

if np.absolute(v0_U1_h6_22 - v0_U1_h6_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0005")
else:
    v0_u1_h6 = np.mean([v0_U1_h6_22, v0_U1_h6_23])
    ut_v0_h6 = ut_u1_h6/v0_u1_h6
    v0_prime_h6 = (u_inf6_hblock*((ut_v0_h6**2 + (ct_les6_hblock/4))))/(ut_v0_h6)
    cp_prime_h6 = cp_les6_hblock*((u_inf6_hblock/v0_prime_h6)**3)
    ct_prime_h6 = ct_les6_hblock*((u_inf6_hblock/v0_prime_h6)**2)

if np.absolute(v0_U1_h7_22 - v0_U1_h7_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0006")
else:
    v0_u1_h7 = np.mean([v0_U1_h7_22, v0_U1_h7_23])
    ut_v0_h7 = ut_u1_h7/v0_u1_h7
    v0_prime_h7 = (u_inf7_hblock*((ut_v0_h7**2 + (ct_les7_hblock/4))))/(ut_v0_h7)
    cp_prime_h7 = cp_les7_hblock*((u_inf7_hblock/v0_prime_h7)**3)
    ct_prime_h7 = ct_les7_hblock*((u_inf7_hblock/v0_prime_h7)**2)

if np.absolute(v0_U1_h8_22 - v0_U1_h8_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0007")
else:
    v0_u1_h8 = np.mean([v0_U1_h8_22, v0_U1_h8_23])
    ut_v0_h8 = ut_u1_h8/v0_u1_h8
    v0_prime_h8 = (u_inf8_hblock*((ut_v0_h8**2 + (ct_les8_hblock/4))))/(ut_v0_h8)
    cp_prime_h8 = cp_les8_hblock*((u_inf8_hblock/v0_prime_h8)**3)
    ct_prime_h8 = ct_les8_hblock*((u_inf8_hblock/v0_prime_h8)**2)

if np.absolute(v0_U1_h9_22 - v0_U1_h9_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0008")
else:
    v0_u1_h9 = np.mean([v0_U1_h9_22, v0_U1_h9_23])
    ut_v0_h9 = ut_u1_h9/v0_u1_h9
    v0_prime_h9 = (u_inf9_hblock*((ut_v0_h9**2 + (ct_les9_hblock/4))))/(ut_v0_h9)
    cp_prime_h9 = cp_les9_hblock*((u_inf9_hblock/v0_prime_h9)**3)
    ct_prime_h9 = ct_les9_hblock*((u_inf9_hblock/v0_prime_h9)**2)

if np.absolute(v0_U1_h10_22 - v0_U1_h10_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0009")
else:
    v0_u1_h10 = np.mean([v0_U1_h10_22, v0_U1_h10_23])
    ut_v0_h10 = ut_u1_h10/v0_u1_h10
    v0_prime_h10 = (u_inf10_hblock*((ut_v0_h10**2 + (ct_les10_hblock/4))))/(ut_v0_h10)
    cp_prime_h10 = cp_les10_hblock*((u_inf10_hblock/v0_prime_h10)**3)
    ct_prime_h10 = ct_les10_hblock*((u_inf10_hblock/v0_prime_h10)**2)

if np.absolute(v0_U1_h11_22 - v0_U1_h11_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0010")
else:
    v0_u1_h11 = np.mean([v0_U1_h11_22, v0_U1_h11_23])
    ut_v0_h11 = ut_u1_h11/v0_u1_h11
    v0_prime_h11 = (u_inf11_hblock*((ut_v0_h11**2 + (ct_les11_hblock/4))))/(ut_v0_h11)
    cp_prime_h11 = cp_les11_hblock*((u_inf11_hblock/v0_prime_h11)**3)
    ct_prime_h11 = ct_les11_bhlock*((u_inf11_hblock/v0_prime_h11)**2)

if np.absolute(v0_U1_h12_22 - v0_U1_h12_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0011")
else:
    v0_u1_h12 = np.mean([v0_U1_h12_22, v0_U1_h12_23])
    ut_v0_h12 = ut_u1_h12/v0_u1_h12
    v0_prime_h12 = (u_inf12_hblock*((ut_v0_h12**2 + (ct_les12_hblock/4))))/(ut_v0_h12)
    cp_prime_h12 = cp_les12_hblock*((u_inf12_hblock/v0_prime_h12)**3)
    ct_prime_h12 = ct_les12_hblock*((u_inf12_hblock/v0_prime_h12)**2)

if np.absolute(v0_U1_h13_22 - v0_U1_h13_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0012")
else:
    v0_u1_h13 = np.mean([v0_U1_h13_22, v0_U1_h13_23])
    ut_v0_h13 = ut_u1_h13/v0_u1_h13
    v0_prime_h13 = (u_inf13_hblock*((ut_v0_h13**2 + (ct_les13_hblock/4))))/(ut_v0_h13)
    cp_prime_h13 = cp_les13_hblock*((u_inf13_hblock/v0_prime_h13)**3)
    ct_prime_h13 = ct_les13_hblock*((u_inf13_hblock/v0_prime_h13)**2)

if np.absolute(v0_U1_h14_22 - v0_U1_h14_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0013")
else:
    v0_u1_h14 = np.mean([v0_U1_h14_22, v0_U1_h14_23])
    ut_v0_h14 = ut_u1_h14/v0_u1_h14
    v0_prime_h14 = (u_inf14_hblock*((ut_v0_h14**2 + (ct_les14_hblock/4))))/(ut_v0_h14)
    cp_prime_h14 = cp_les14_hblock*((u_inf14_hblock/v0_prime_h14)**3)
    ct_prime_h14 = ct_les14_hblock*((u_inf14_hblock/v0_prime_h14)**2)

if np.absolute(v0_U1_h15_22 - v0_U1_h15_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0014")
else:
    v0_u1_h15 = np.mean([v0_U1_h15_22, v0_U1_h15_23])
    ut_v0_h15 = ut_u1_h15/v0_u1_h15
    v0_prime_h15 = (u_inf15_hblock*((ut_v0_h15**2 + (ct_les15_hblock/4))))/(ut_v0_h15)
    cp_prime_h15 = cp_les15_hblock*((u_inf15_hblock/v0_prime_h15)**3)
    ct_prime_h15 = ct_les15_hblock*((u_inf15_hblock/v0_prime_h15)**2)

if np.absolute(v0_U1_h16_22 - v0_U1_h16_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0015")
else:
    v0_u1_h16 = np.mean([v0_U1_h16_22, v0_U1_h16_23])
    ut_v0_h16 = ut_u1_h16/v0_u1_h16
    v0_prime_h16 = (u_inf16_hblock*((ut_v0_h16**2 + (ct_les16_hblock/4))))/(ut_v0_h16)
    cp_prime_h16 = cp_les16_hblock*((u_inf16_hblock/v0_prime_h16)**3)
    ct_prime_h16 = ct_les16_hblock*((u_inf16_hblock/v0_prime_h16)**2)

if np.absolute(v0_U1_h17_22 - v0_U1_h17_23) > 0.01:
    print(f"Enter a new guess for U2/U1 for Uncorrected Sim0016")
else:
    v0_u1_h17 = np.mean([v0_U1_h17_22, v0_U1_h17_23])
    ut_v0_h17 = ut_u1_h17/v0_u1_h17
    v0_phrme_h17 = (u_inf17_hblock*((ut_v0_h17**2 + (ct_les17_hblock/4))))/(ut_v0_h17)
    cp_prime_h17 = cp_les17_hblock*((u_inf17_hblock/v0_prime_h17)**3)
    ct_prime_1h7 = ct_les17_hblock*((u_inf17_hblock/v0_prime_h17)**2)

# High Corrected
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