import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine

# Load Data
sim3_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0002", padeops = True, runid = 0, normalize_origin = "turbine")
sim4_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0003", padeops = True, runid = 0, normalize_origin = "turbine")
sim5_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0004", padeops = True, runid = 0, normalize_origin = "turbine")
sim6_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0005", padeops = True, runid = 0, normalize_origin = "turbine")
sim7_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0006", padeops = True, runid = 0, normalize_origin = "turbine")
sim8_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0007", padeops = True, runid = 0, normalize_origin = "turbine")
sim9_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0008", padeops = True, runid = 0, normalize_origin = "turbine")
sim10_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0009", padeops = True, runid = 0, normalize_origin = "turbine")
sim11_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0010", padeops = True, runid = 0, normalize_origin = "turbine")
sim12_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0011", padeops = True, runid = 0, normalize_origin = "turbine")
sim13_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0012", padeops = True, runid = 0, normalize_origin = "turbine")
sim14_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0013", padeops = True, runid = 0, normalize_origin = "turbine")
sim15_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0014", padeops = True, runid = 0, normalize_origin = "turbine")
sim16_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0015", padeops = True, runid = 0, normalize_origin = "turbine")
sim17_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0016", padeops = True, runid = 0, normalize_origin = "turbine")

sim3_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0002", padeops = True, runid = 0, normalize_origin = "turbine")
sim4_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0003", padeops = True, runid = 0, normalize_origin = "turbine")
sim5_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0004", padeops = True, runid = 0, normalize_origin = "turbine")
sim6_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0005", padeops = True, runid = 0, normalize_origin = "turbine")
sim7_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0006", padeops = True, runid = 0, normalize_origin = "turbine")
sim8_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0007", padeops = True, runid = 0, normalize_origin = "turbine")
sim9_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0008", padeops = True, runid = 0, normalize_origin = "turbine")
sim10_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0009", padeops = True, runid = 0, normalize_origin = "turbine")
sim11_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0010", padeops = True, runid = 0, normalize_origin = "turbine")
sim12_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0011", padeops = True, runid = 0, normalize_origin = "turbine")
sim13_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0012", padeops = True, runid = 0, normalize_origin = "turbine")
sim14_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0013", padeops = True, runid = 0, normalize_origin = "turbine")
sim15_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0014", padeops = True, runid = 0, normalize_origin = "turbine")
sim16_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0015", padeops = True, runid = 0, normalize_origin = "turbine")
sim17_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0016", padeops = True, runid = 0, normalize_origin = "turbine")

# Set ds values
ds3m = sim3_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds4m = sim4_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds5m = sim5_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds6m = sim6_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds7m = sim7_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds8m = sim8_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds9m = sim9_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds10m = sim10_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds11m = sim11_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds12m = sim12_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds13m = sim13_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds14m = sim14_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds15m = sim15_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds16m = sim16_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds17m = sim17_mblock.slice(budget_terms = ["ubar", "vbar", "wbar"])

ds3h = sim3_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds4h = sim4_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds5h = sim5_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds6h = sim6_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds7h = sim7_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds8h = sim8_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds9h = sim9_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds10h = sim10_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds11h = sim11_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds12h = sim12_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds13h = sim13_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds14h = sim14_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds15h = sim15_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds16h = sim16_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])
ds17h = sim17_hblock.slice(budget_terms = ["ubar", "vbar", "wbar"])

#Z/D Views

#Med Blocked
ds3m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -3')
plt.savefig('./3m_z_d')

ds4m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -2.5')
plt.savefig('./4m_z_d')

ds5m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -2')
plt.savefig('./5m_z_d')

ds6m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -1.5')
plt.savefig('./6m_z_d')

ds7m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -1')
plt.savefig('./7m_z_d')

ds8m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = -0.5')
plt.savefig('./8m_z_d')

ds9m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 0')
plt.savefig('./9m_z_d')

ds10m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 0.5')
plt.savefig('./10m_z_d')

ds11m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 1')
plt.savefig('./11m_z_d')

ds12m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 1.5')
plt.savefig('./12m_z_d')

ds13m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 2')
plt.savefig('./13m_z_d')

ds14m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 2.5')
plt.savefig('./14m_z_d')

ds15m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 3')
plt.savefig('./15m_z_d')

ds16m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 3.5')
plt.savefig('./16m_z_d')    

ds17m['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 10% Blockage, Ct Prime = 4')
plt.savefig('./17m_z_d')

#High Blocked
ds3h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -3')
plt.savefig('./3h_z_d')

ds4h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -2.5')
plt.savefig('./4h_z_d')

ds5h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -2')
plt.savefig('./5h_z_d')

ds6h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -1.5')
plt.savefig('./6h_z_d')

ds7h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -1')
plt.savefig('./7h_z_d')

ds8h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = -0.5')
plt.savefig('./8h_z_d')

ds9h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 0')
plt.savefig('./9h_z_d')

ds10h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 0.5')
plt.savefig('./10h_z_d')

ds11h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 1')
plt.savefig('./11h_z_d')

ds12h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 1.5')
plt.savefig('./12h_z_d')

ds13h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 2')
plt.savefig('./13h_z_d')

ds14h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 2.5')
plt.savefig('./14h_z_d')

ds15h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 3')
plt.savefig('./15h_z_d')

ds16h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 3.5')
plt.savefig('./16h_z_d')

ds17h['ubar'].slice(ylim=0).imshow()
plt.title('Z/D View at 35% Blockage, Ct Prime = 4')
plt.savefig('./17h_z_d')