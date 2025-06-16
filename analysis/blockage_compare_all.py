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
#Uncorrected
a_les1 = 1-np.cbrt((p_les1/(0.5*(np.pi/4)*Ctprime1)))
a_les2 = 1-np.cbrt((p_les2/(0.5*(np.pi/4)*Ctprime2)))
a_les3 = 1-np.cbrt((p_les3/(0.5*(np.pi/4)*Ctprime3)))
a_les4 = 1-np.cbrt((p_les4/(0.5*(np.pi/4)*Ctprime4)))
a_les5 = 1-np.cbrt((p_les5/(0.5*(np.pi/4)*Ctprime5)))
a_les6 = 1-np.cbrt((p_les6/(0.5*(np.pi/4)*Ctprime6)))
a_les7 = 1-np.cbrt((p_les7/(0.5*(np.pi/4)*Ctprime7)))
a_les8 = 1-np.cbrt((p_les8/(0.5*(np.pi/4)*Ctprime8)))
#a_les9 = 1-np.cbrt((p_les9/(0.5*(np.pi/4)*Ctprime9)))
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
#a_les9_cor = 1-np.cbrt((p_les9_cor/(0.5*(np.pi/4)*Ctprime9)))
a_les10_cor = 1-np.cbrt((p_les10_cor/(0.5*(np.pi/4)*Ctprime10)))
a_les11_cor = 1-np.cbrt((p_les11_cor/(0.5*(np.pi/4)*Ctprime11)))
a_les12_cor = 1-np.cbrt((p_les12_cor/(0.5*(np.pi/4)*Ctprime12)))
a_les13_cor = 1-np.cbrt((p_les13_cor/(0.5*(np.pi/4)*Ctprime13)))
a_les14_cor = 1-np.cbrt((p_les14_cor/(0.5*(np.pi/4)*Ctprime14)))
a_les15_cor = 1-np.cbrt((p_les15_cor/(0.5*(np.pi/4)*Ctprime15)))
a_les16_cor = 1-np.cbrt((p_les16_cor/(0.5*(np.pi/4)*Ctprime16)))
a_les17_cor = 1-np.cbrt((p_les17_cor/(0.5*(np.pi/4)*Ctprime17)))

# Med Blocked, No Correction
a_les1_mblock = 1-np.cbrt((p_les1_mblock/(0.5*(np.pi/4)*Ctprime1)))
a_les2_mblock = 1-np.cbrt((p_les2_mblock/(0.5*(np.pi/4)*Ctprime2)))
a_les3_mblock = 1-np.cbrt((p_les3_mblock/(0.5*(np.pi/4)*Ctprime3)))
a_les4_mblock = 1-np.cbrt((p_les4_mblock/(0.5*(np.pi/4)*Ctprime4)))
a_les5_mblock = 1-np.cbrt((p_les5_mblock/(0.5*(np.pi/4)*Ctprime5)))
a_les6_mblock = 1-np.cbrt((p_les6_mblock/(0.5*(np.pi/4)*Ctprime6)))
a_les7_mblock = 1-np.cbrt((p_les7_mblock/(0.5*(np.pi/4)*Ctprime7)))
a_les8_mblock = 1-np.cbrt((p_les8_mblock/(0.5*(np.pi/4)*Ctprime8)))
#a_les9_mblock = 1-np.cbrt((p_les9_mblock/(0.5*(np.pi/4)*Ctprime9)))
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
#a_les9_mblock_cor = 1-np.cbrt((p_les9_mblock_cor/(0.5*(np.pi/4)*Ctprime9)))
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
#a_les9_hblock = 1-np.cbrt((p_les9_hblock/(0.5*(np.pi/4)*Ctprime9)))
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
#a_les9_hblock_cor = 1-np.cbrt((p_les9_hblock_cor/(0.5*(np.pi/4)*Ctprime9)))
a_les10_hblock_cor = 1-np.cbrt((p_les10_hblock_cor/(0.5*(np.pi/4)*Ctprime10)))
a_les11_hblock_cor = 1-np.cbrt((p_les11_hblock_cor/(0.5*(np.pi/4)*Ctprime11)))
a_les12_hblock_cor = 1-np.cbrt((p_les12_hblock_cor/(0.5*(np.pi/4)*Ctprime12)))
a_les13_hblock_cor = 1-np.cbrt((p_les13_hblock_cor/(0.5*(np.pi/4)*Ctprime13)))
a_les14_hblock_cor = 1-np.cbrt((p_les14_hblock_cor/(0.5*(np.pi/4)*Ctprime14)))
a_les15_hblock_cor = 1-np.cbrt((p_les15_hblock_cor/(0.5*(np.pi/4)*Ctprime15)))
a_les16_hblock_cor = 1-np.cbrt((p_les16_hblock_cor/(0.5*(np.pi/4)*Ctprime16)))
a_les17_hblock_cor = 1-np.cbrt((p_les17_hblock_cor/(0.5*(np.pi/4)*Ctprime17)))

# Arrays
Ctprime_plot = [Ctprime1, Ctprime2, Ctprime3, Ctprime4, Ctprime5, Ctprime6, Ctprime7, Ctprime8, Ctprime9, Ctprime10, Ctprime11, Ctprime12, Ctprime13, Ctprime14, Ctprime15, Ctprime16, Ctprime17]
cp_plot = [cp_les1, cp_les2, cp_les3, cp_les4, cp_les5, cp_les6, cp_les7, cp_les8, cp_les9, cp_les10, cp_les11, cp_les12, cp_les13, cp_les14, cp_les15, cp_les16, cp_les17]
cp_plot_cor = [cp_les1_cor, cp_les2_cor, cp_les3_cor, cp_les4_cor, cp_les5_cor, cp_les6_cor, cp_les7_cor, cp_les8_cor, cp_les9_cor, cp_les10_cor, cp_les11_cor, cp_les12_cor, cp_les13_cor, cp_les14_cor, cp_les15_cor, cp_les16_cor, cp_les17_cor] 
cp_plot_mblock = [cp_les1_mblock, cp_les2_mblock, cp_les3_mblock, cp_les4_mblock, cp_les5_mblock, cp_les6_mblock, cp_les7_mblock, cp_les8_mblock, cp_les9_mblock, cp_les10_mblock, cp_les11_mblock, cp_les12_mblock, cp_les13_mblock, cp_les14_mblock, cp_les15_mblock, cp_les16_mblock, cp_les17_mblock]    
cp_plot_mblock_cor = [cp_les1_mblock_cor, cp_les2_mblock_cor, cp_les3_mblock_cor, cp_les4_mblock_cor, cp_les5_mblock_cor, cp_les6_mblock_cor, cp_les7_mblock_cor, cp_les8_mblock_cor, cp_les9_mblock_cor, cp_les10_mblock_cor, cp_les11_mblock_cor, cp_les12_mblock_cor, cp_les13_mblock_cor, cp_les14_mblock_cor, cp_les15_mblock_cor, cp_les16_mblock_cor, cp_les17_mblock_cor]  
cp_plot_hblock = [cp_les1_hblock, cp_les2_hblock, cp_les3_hblock, cp_les4_hblock, cp_les5_hblock, cp_les6_hblock, cp_les7_hblock, cp_les8_hblock, cp_les9_hblock, cp_les10_hblock, cp_les11_hblock, cp_les12_hblock, cp_les13_hblock, cp_les14_hblock, cp_les15_hblock, cp_les16_hblock, cp_les17_hblock]
cp_plot_hblock_cor = [cp_les1_hblock_cor, cp_les2_hblock_cor, cp_les3_hblock_cor, cp_les4_hblock_cor, cp_les5_hblock_cor, cp_les6_hblock_cor, cp_les7_hblock_cor, cp_les8_hblock_cor, cp_les9_hblock_cor, cp_les10_hblock_cor, cp_les11_hblock_cor, cp_les12_hblock_cor, cp_les13_hblock_cor, cp_les14_hblock_cor, cp_les15_hblock_cor, cp_les16_hblock_cor, cp_les17_hblock_cor]   
ct_plot = [ct_les1, ct_les2, ct_les3, ct_les4, ct_les5, ct_les6, ct_les7, ct_les8, ct_les9, ct_les10, ct_les11, ct_les12, ct_les13, ct_les14, ct_les15, ct_les16, ct_les17] 
ct_plot_cor = [ct_les1_cor, ct_les2_cor, ct_les3_cor, ct_les4_cor, ct_les5_cor, ct_les6_cor, ct_les7_cor, ct_les8_cor, ct_les9_cor, ct_les10_cor, ct_les11_cor, ct_les12_cor, ct_les13_cor, ct_les14_cor, ct_les15_cor, ct_les16_cor, ct_les17_cor] 
ct_plot_mblock = [ct_les1_mblock, ct_les2_mblock, ct_les3_mblock, ct_les4_mblock, ct_les5_mblock, ct_les6_mblock, ct_les7_mblock, ct_les8_mblock, ct_les9_mblock, ct_les10_mblock, ct_les11_mblock, ct_les12_mblock, ct_les13_mblock, ct_les14_mblock, ct_les15_mblock, ct_les16_mblock, ct_les17_mblock]   
ct_plot_mblock_cor = [ct_les1_mblock_cor, ct_les2_mblock_cor, ct_les3_mblock_cor, ct_les4_mblock_cor, ct_les5_mblock_cor, ct_les6_mblock_cor, ct_les7_mblock_cor, ct_les8_mblock_cor, ct_les9_mblock_cor, ct_les10_mblock_cor, ct_les11_mblock_cor, ct_les12_mblock_cor, ct_les13_mblock_cor, ct_les14_mblock_cor, ct_les15_mblock_cor, ct_les16_mblock_cor, ct_les17_mblock_cor]   
ct_plot_hblock = [ct_les1_hblock, ct_les2_hblock, ct_les3_hblock, ct_les4_hblock, ct_les5_hblock, ct_les6_hblock, ct_les7_hblock, ct_les8_hblock, ct_les9_hblock, ct_les10_hblock, ct_les11_hblock, ct_les12_hblock, ct_les13_hblock, ct_les14_hblock, ct_les15_hblock, ct_les16_hblock, ct_les17_hblock]   
ct_plot_hblock_cor = [ct_les1_hblock_cor, ct_les2_hblock_cor, ct_les3_hblock_cor, ct_les4_hblock_cor, ct_les5_hblock_cor, ct_les6_hblock_cor, ct_les7_hblock_cor, ct_les8_hblock_cor, ct_les9_hblock_cor, ct_les10_hblock_cor, ct_les11_hblock_cor, ct_les12_hblock_cor, ct_les13_hblock_cor, ct_les14_hblock_cor, ct_les15_hblock_cor, ct_les16_hblock_cor, ct_les17_hblock_cor]   
a_plot = [a_les1, a_les2, a_les3, a_les4, a_les5, a_les6, a_les7, a_les8, 0, a_les10, a_les11, a_les12, a_les13, a_les14, a_les15, a_les16, a_les17]   
a_plot_cor = [a_les1_cor, a_les2_cor, a_les3_cor, a_les4_cor, a_les5_cor, a_les6_cor, a_les7_cor, a_les8_cor, 0, a_les10_cor, a_les11_cor, a_les12_cor, a_les13_cor, a_les14_cor, a_les15_cor, a_les16_cor, a_les17_cor]   
a_plot_mblock = [a_les1_mblock, a_les2_mblock, a_les3_mblock, a_les4_mblock, a_les5_mblock, a_les6_mblock, a_les7_mblock, a_les8_mblock, 0, a_les10_mblock, a_les11_mblock, a_les12_mblock, a_les13_mblock, a_les14_mblock, a_les15_mblock, a_les16_mblock, a_les17_mblock] 
a_plot_mblock_cor = [a_les1_mblock_cor, a_les2_mblock_cor, a_les3_mblock_cor, a_les4_mblock_cor, a_les5_mblock_cor, a_les6_mblock_cor, a_les7_mblock_cor, a_les8_mblock_cor, 0, a_les10_mblock_cor, a_les11_mblock_cor, a_les12_mblock_cor, a_les13_mblock_cor, a_les14_mblock_cor, a_les15_mblock_cor, a_les16_mblock_cor, a_les17_mblock_cor] 
a_plot_hblock = [a_les1_hblock, a_les2_hblock, a_les3_hblock, a_les4_hblock, a_les5_hblock, a_les6_hblock, a_les7_hblock, a_les8_hblock, 0, a_les10_hblock, a_les11_hblock, a_les12_hblock, a_les13_hblock, a_les14_hblock, a_les15_hblock, a_les16_hblock, a_les17_hblock] 
a_plot_hblock_cor = [a_les1_hblock_cor, a_les2_hblock_cor, a_les3_hblock_cor, a_les4_hblock_cor, a_les5_hblock_cor, a_les6_hblock_cor, a_les7_hblock_cor, a_les8_hblock_cor, 0, a_les10_hblock_cor, a_les11_hblock_cor, a_les12_hblock_cor, a_les13_hblock_cor, a_les14_hblock_cor, a_les15_hblock_cor, a_les16_hblock_cor, a_les17_hblock_cor] 

#Theory Values
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

#Plotting
#a
plt.figure(figsize = (9,6))
#plt.scatter(Ctprime_plot[1:16], a_plot[1:16], marker = 'o', color ='blue', label = 'Unblocked, No Correction')
#plt.scatter(Ctprime_plot[1:16], a_plot_cor[1:16], marker = 'o', color = 'red', label = 'Unblocked, Corrected')
plt.scatter(Ctprime_plot[1:16], a_plot_mblock[1:16], marker = 'o', color = 'green', label = '10% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], a_plot_mblock_cor[1:16], marker = 'o', color = 'orange', label = '10% Blockage, Corrected')
plt.scatter(Ctprime_plot[1:16], a_plot_hblock[1:16], marker = 'o', color ='magenta', label = '35% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], a_plot_hblock_cor[1:16], marker = 'o', color = 'purple', label = '35% Blockage, Corrected')
plt.plot(Ctprime_plot[1:16], a_t[1:16], color = 'black', label = 'ADM Theory')
plt.title('LES Results Blocked, Unblocked, and ADM Theory: Induction Factor')
plt.xlabel('Ct Prime')
plt.ylabel('Induction Factor')
plt.legend()
plt.ylim(-1, 1)
plt.savefig('./a_compare_all')

#Cp
plt.figure(figsize = (9,6))
plt.scatter(Ctprime_plot[1:16], cp_plot[1:16], marker = 'o', color = 'blue', label = 'Unblocked, No Correction')
plt.scatter(Ctprime_plot[1:16], cp_plot_cor[1:16], marker = 'o', color = 'red', label = 'Unblocked, Corrected')
plt.scatter(Ctprime_plot[1:16], cp_plot_mblock[1:16], marker = 'o', color = 'green', label = '10% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], cp_plot_mblock_cor[1:16], marker = 'o', color = 'orange', label = '10% Blockage, Corrected')
plt.scatter(Ctprime_plot[1:16], cp_plot_hblock[1:16], marker = 'o', color = 'magenta', label = '35% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], cp_plot_hblock_cor[1:16], marker = 'o', color = 'purple', label = '35% Blockage, Corrected')
plt.plot(Ctprime_plot[1:16], cp_t[1:16], color = 'black', label = 'ADM Theory')
plt.title('LES Results Blocked, Unblocked, and ADM Theory: Power Coefficient')
plt.xlabel('Ct Prime')
plt.ylabel('Power Coefficient')
plt.legend()
plt.ylim(-1, 1)
plt.savefig('./cp_compare_all')

#Ct
plt.figure(figsize = (9,6))
plt.scatter(Ctprime_plot[1:16], ct_plot[1:16], marker = 'o', color = 'blue', label = 'Unblocked, No Correction')
plt.scatter(Ctprime_plot[1:16], ct_plot_cor[1:16], marker = 'o', color = 'red', label = 'Unblocked, Corrected')
plt.scatter(Ctprime_plot[1:16], ct_plot_mblock[1:16], marker = 'o', color = 'green', label = '10% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], ct_plot_mblock_cor[1:16], marker = 'o', color = 'orange', label = '10% Blockage, Corrected')
plt.scatter(Ctprime_plot[1:16], ct_plot_hblock[1:16], marker = 'o', color = 'magenta', label = '35% Blockage, No Correction')
plt.scatter(Ctprime_plot[1:16], ct_plot_hblock_cor[1:16], marker = 'o', color = 'purple', label = '35% Blockage, Corrected')
plt.plot(Ctprime_plot[1:16], ct_t[1:16], color = 'black', label = 'ADM Theory')
plt.title('LES Results Blocked, Unblocked, and ADM Theory: Thrust Coefficient')
plt.xlabel('Ct Prime')
plt.ylabel('Thrust Coefficient')
plt.legend()
plt.ylim(-1, 1)
plt.savefig('./ct_compare_all')

#Export Data
np.save("cp_unblocked.npy", cp_plot[1:16])
np.save("cp_unblocked_cor.npy", cp_plot_cor[1:16])
np.save("ct_unblocked.npy", ct_plot[1:16])
np.save("ct_unblocked_cor.npy", ct_plot_cor[1:16])

