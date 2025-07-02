import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine
import streamtube

sim1_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0000", padeops = True, runid = 0, normalize_origin = "turbine")
sim2_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0001", padeops = True, runid = 0, normalize_origin = "turbine")
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

sim1_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0000", padeops = True, runid = 0, normalize_origin = "turbine")
sim2_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0001", padeops = True, runid = 0, normalize_origin = "turbine")
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

ds1m = sim1_mblock.slice(budget_terms = "ubar")
ds2m = sim2_mblock.slice(budget_terms = "ubar")
ds3m = sim3_mblock.slice(budget_terms = "ubar")
ds4m = sim4_mblock.slice(budget_terms = "ubar")
ds5m = sim5_mblock.slice(budget_terms = "ubar")
ds6m = sim6_mblock.slice(budget_terms = "ubar")
ds7m = sim7_mblock.slice(budget_terms = "ubar")
ds8m = sim8_mblock.slice(budget_terms = "ubar")
ds9m = sim9_mblock.slice(budget_terms = "ubar")
ds10m = sim10_mblock.slice(budget_terms = "ubar")
ds11m = sim11_mblock.slice(budget_terms = "ubar")
ds12m = sim12_mblock.slice(budget_terms = "ubar")
ds13m = sim13_mblock.slice(budget_terms = "ubar")
ds14m = sim14_mblock.slice(budget_terms = "ubar")
ds15m = sim15_mblock.slice(budget_terms = "ubar")
ds16m = sim16_mblock.slice(budget_terms = "ubar")
ds17m = sim17_mblock.slice(budget_terms = "ubar")

ds1h = sim1_hblock.slice(budget_terms = "ubar")
ds2h = sim2_hblock.slice(budget_terms = "ubar")
ds3h = sim3_hblock.slice(budget_terms = "ubar")
ds4h = sim4_hblock.slice(budget_terms = "ubar")
ds5h = sim5_hblock.slice(budget_terms = "ubar")
ds6h = sim6_hblock.slice(budget_terms = "ubar")
ds7h = sim7_hblock.slice(budget_terms = "ubar")
ds8h = sim8_hblock.slice(budget_terms = "ubar")
ds9h = sim9_hblock.slice(budget_terms = "ubar")
ds10h = sim10_hblock.slice(budget_terms = "ubar")
ds11h = sim11_hblock.slice(budget_terms = "ubar")
ds12h = sim12_hblock.slice(budget_terms = "ubar")
ds13h = sim13_hblock.slice(budget_terms = "ubar")
ds14h = sim14_hblock.slice(budget_terms = "ubar")
ds15h = sim15_hblock.slice(budget_terms = "ubar")
ds16h = sim16_hblock.slice(budget_terms = "ubar")
ds17h = sim17_hblock.slice(budget_terms = "ubar")

#Set Up Wake Streamtubes and Wake Averaged Velocities
stream1m = streamtube.Streamtube(ds1m.x.to_numpy, ds1m.y.to_numpy(), ds1m.z.to_numpy(), ds1m["ubar"].to_numpy())
stream1m.compute_mask(R = 0.3)
ds1m['streamtube'] = stream1m.mask
ds1m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg1m = np.sum(ds1m['ubar'] * ds1m['streamtube'], axis=(1,2)), np.sum(ds1m['streamtube'], axis = (1,2))

stream2m = streamtube.Streamtube(ds2m.x.to_numpy, ds2m.y.to_numpy(), ds2m.z.to_numpy(), ds2m["ubar"].to_numpy())
stream2m.compute_mask(R = 0.3)
ds2m['streamtube'] = stream1m.mask
ds2m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg2m = np.sum(ds2m['ubar'] * ds2m['streamtube'], axis=(1,2)), np.sum(ds2m['streamtube'], axis = (1,2))

stream3m = streamtube.Streamtube(ds3m.x.to_numpy, ds3m.y.to_numpy(), ds3m.z.to_numpy(), ds3m["ubar"].to_numpy())
stream3m.compute_mask(R = 0.3)
ds3m['streamtube'] = stream3m.mask
ds3m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg3m = np.sum(ds3m['ubar'] * ds3m['streamtube'], axis=(1,2)), np.sum(ds3m['streamtube'], axis = (1,2))

stream4m = streamtube.Streamtube(ds4m.x.to_numpy, ds4m.y.to_numpy(), ds4m.z.to_numpy(), ds4m["ubar"].to_numpy())
stream4m.compute_mask(R = 0.3)
ds4m['streamtube'] = stream4m.mask
ds4m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg4m = np.sum(ds4m['ubar'] * ds4m['streamtube'], axis=(1,2)), np.sum(ds4m['streamtube'], axis = (1,2))

stream5m = streamtube.Streamtube(ds5m.x.to_numpy, ds5m.y.to_numpy(), ds5m.z.to_numpy(), ds5m["ubar"].to_numpy())
stream5m.compute_mask(R = 0.3)
ds5m['streamtube'] = stream5m.mask
ds5m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg5m = np.sum(ds5m['ubar'] * ds5m['streamtube'], axis=(1,2)), np.sum(ds5m['streamtube'], axis = (1,2))

stream1m = streamtube.Streamtube(ds1m.x.to_numpy, ds1m.y.to_numpy(), ds1m.z.to_numpy(), ds1m["ubar"].to_numpy())
stream1m.compute_mask(R = 0.3)
ds1m['streamtube'] = stream1m.mask
ds1m['streamtube'].slice(zlim = 0, xlim = [0.5, 5]).imshow #double check x limits on this
u_avg1m = np.sum(ds1m['ubar'] * ds1m['streamtube'], axis=(1,2)), np.sum(ds1m['streamtube'], axis = (1,2))