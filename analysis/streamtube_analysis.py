import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine
import streamtube

# sim1_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0000", padeops = True, runid = 0, normalize_origin = "turbine")
# sim2_mblock = pio.BudgetIO("Data/B_0004_Files/Sim_0001", padeops = True, runid = 0, normalize_origin = "turbine")
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

# sim1_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0000", padeops = True, runid = 0, normalize_origin = "turbine")
# sim2_hblock = pio.BudgetIO("Data/B_0005_Files/Sim_0001", padeops = True, runid = 0, normalize_origin = "turbine")
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

# ds1m = sim1_mblock.slice(budget_terms = "ubar")
# ds2m = sim2_mblock.slice(budget_terms = "ubar")
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

# ds1h = sim1_hblock.slice(budget_terms = "ubar")
# ds2h = sim2_hblock.slice(budget_terms = "ubar")
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

# Bypass Streamtubes
stream3m = streamtube.Streamtube(ds3m.x.to_numpy(), ds3m.y.to_numpy(), ds3m.z.to_numpy(), ds3m["ubar"].to_numpy())
stream3m.compute_mask(R = 0.1, orign = (0,0,9))
ds3m['streamtube'] = stream3m.mask
u_avg3mb = np.sum(ds3m['ubar'] * ds3m['streamtube'], axis = (1,2))/np.sum(ds3m['streamtube'], axis = (1,2))

stream4m = streamtube.Streamtube(ds4m.x.to_numpy(), ds4m.y.to_numpy(), ds4m.z.to_numpy(), ds4m["ubar"].to_numpy())
stream4m.compute_mask(R = 0.1, orign = (0,0,9))
ds4m['streamtube'] = stream4m.mask
u_avg4mb = np.sum(ds4m['ubar'] * ds4m['streamtube'], axis = (1,2))/np.sum(ds4m['streamtube'], axis = (1,2))

stream5m = streamtube.Streamtube(ds5m.x.to_numpy(), ds5m.y.to_numpy(), ds5m.z.to_numpy(), ds5m["ubar"].to_numpy())
stream5m.compute_mask(R = 0.1, orign = (0,0,9))
ds5m['streamtube'] = stream5m.mask
u_avg5mb = np.sum(ds5m['ubar'] * ds5m['streamtube'], axis = (1,2))/np.sum(ds5m['streamtube'], axis = (1,2))

stream6m = streamtube.Streamtube(ds6m.x.to_numpy(), ds6m.y.to_numpy(), ds6m.z.to_numpy(), ds6m["ubar"].to_numpy())
stream6m.compute_mask(R = 0.1, orign = (0,0,9))
ds6m['streamtube'] = stream6m.mask
u_avg6mb = np.sum(ds6m['ubar'] * ds6m['streamtube'], axis = (1,2))/np.sum(ds6m['streamtube'], axis = (1,2))

stream7m = streamtube.Streamtube(ds7m.x.to_numpy(), ds7m.y.to_numpy(), ds7m.z.to_numpy(), ds7m["ubar"].to_numpy())
stream7m.compute_mask(R = 0.1, orign = (0,0,9))
ds7m['streamtube'] = stream7m.mask
u_avg7mb = np.sum(ds7m['ubar'] * ds7m['streamtube'], axis = (1,2))/np.sum(ds7m['streamtube'], axis = (1,2))

stream8m = streamtube.Streamtube(ds8m.x.to_numpy(), ds8m.y.to_numpy(), ds8m.z.to_numpy(), ds8m["ubar"].to_numpy())
stream8m.compute_mask(R = 0.1, orign = (0,0,9))
ds8m['streamtube'] = stream8m.mask
u_avg8mb = np.sum(ds8m['ubar'] * ds8m['streamtube'], axis = (1,2))/np.sum(ds8m['streamtube'], axis = (1,2))

stream9m = streamtube.Streamtube(ds9m.x.to_numpy(), ds9m.y.to_numpy(), ds9m.z.to_numpy(), ds9m["ubar"].to_numpy())
stream9m.compute_mask(R = 0.1, orign = (0,0,9))
ds9m['streamtube'] = stream9m.mask
u_avg9mb = np.sum(ds9m['ubar'] * ds9m['streamtube'], axis = (1,2))/np.sum(ds9m['streamtube'], axis = (1,2))

stream10m = streamtube.Streamtube(ds10m.x.to_numpy(), ds10m.y.to_numpy(), ds10m.z.to_numpy(), ds10m["ubar"].to_numpy())
stream10m.compute_mask(R = 0.1, orign = (0,0,9))
ds10m['streamtube'] = stream10m.mask
u_avg10mb = np.sum(ds10m['ubar'] * ds10m['streamtube'], axis = (1,2))/np.sum(ds10m['streamtube'], axis = (1,2))

stream11m = streamtube.Streamtube(ds11m.x.to_numpy(), ds11m.y.to_numpy(), ds11m.z.to_numpy(), ds11m["ubar"].to_numpy())
stream11m.compute_mask(R = 0.1, orign = (0,0,9))
ds11m['streamtube'] = stream11m.mask
u_avg11mb = np.sum(ds11m['ubar'] * ds11m['streamtube'], axis = (1,2))/np.sum(ds11m['streamtube'], axis = (1,2))  

stream12m = streamtube.Streamtube(ds12m.x.to_numpy(), ds12m.y.to_numpy(), ds12m.z.to_numpy(), ds12m["ubar"].to_numpy())
stream12m.compute_mask(R = 0.1, orign = (0,0,9))
ds12m['streamtube'] = stream12m.mask
u_avg12mb = np.sum(ds12m['ubar'] * ds12m['streamtube'], axis = (1,2))/np.sum(ds12m['streamtube'], axis = (1,2))

stream13m = streamtube.Streamtube(ds13m.x.to_numpy(), ds13m.y.to_numpy(), ds13m.z.to_numpy(), ds13m["ubar"].to_numpy())
stream13m.compute_mask(R = 0.1, orign = (0,0,9))
ds13m['streamtube'] = stream13m.mask
u_avg13mb = np.sum(ds13m['ubar'] * ds13m['streamtube'], axis = (1,2))/np.sum(ds13m['streamtube'], axis = (1,2))

stream14m = streamtube.Streamtube(ds14m.x.to_numpy(), ds14m.y.to_numpy(), ds14m.z.to_numpy(), ds14m["ubar"].to_numpy())
stream14m.compute_mask(R = 0.1, orign = (0,0,9))
ds14m['streamtube'] = stream14m.mask
u_avg14mb = np.sum(ds14m['ubar'] * ds14m['streamtube'], axis = (1,2))/np.sum(ds14m['streamtube'], axis = (1,2))

stream15m = streamtube.Streamtube(ds15m.x.to_numpy(), ds15m.y.to_numpy(), ds15m.z.to_numpy(), ds15m["ubar"].to_numpy())
stream15m.compute_mask(R = 0.1, orign = (0,0,9))
ds15m['streamtube'] = stream15m.mask
u_avg15mb = np.sum(ds15m['ubar'] * ds15m['streamtube'], axis = (1,2))/np.sum(ds15m['streamtube'], axis = (1,2))

stream16m = streamtube.Streamtube(ds16m.x.to_numpy(), ds16m.y.to_numpy(), ds16m.z.to_numpy(), ds16m["ubar"].to_numpy())
stream16m.compute_mask(R = 0.1, orign = (0,0,9))
ds16m['streamtube'] = stream16m.mask
u_avg16mb = np.sum(ds16m['ubar'] * ds16m['streamtube'], axis = (1,2))/np.sum(ds16m['streamtube'], axis = (1,2))

stream17m = streamtube.Streamtube(ds17m.x.to_numpy(), ds17m.y.to_numpy(), ds17m.z.to_numpy(), ds17m["ubar"].to_numpy())
stream17m.compute_mask(R = 0.1, orign = (0,0,9))
ds17m['streamtube'] = stream17m.mask
u_avg17mb = np.sum(ds17m['ubar'] * ds17m['streamtube'], axis = (1,2))/np.sum(ds17m['streamtube'], axis = (1,2))

stream3h = streamtube.Streamtube(ds3h.x.to_numpy(), ds3h.y.to_numpy(), ds3h.z.to_numpy(), ds3h["ubar"].to_numpy())
stream3h.compute_mask(R = 0.1, orign = (0,0,9))
ds3h['streamtube'] = stream3h.mask
u_avg3hb = np.sum(ds3h['ubar'] * ds3h['streamtube'], axis = (1,2))/np.sum(ds3h['streamtube'], axis = (1,2))

stream4h = streamtube.Streamtube(ds4h.x.to_numpy(), ds4h.y.to_numpy(), ds4h.z.to_numpy(), ds4h["ubar"].to_numpy())
stream4h.compute_mask(R = 0.1, orign = (0,0,9))
ds4h['streamtube'] = stream4h.mask
u_avg4hb = np.sum(ds4h['ubar'] * ds4h['streamtube'], axis = (1,2))/np.sum(ds4h['streamtube'], axis = (1,2))

stream5h = streamtube.Streamtube(ds5h.x.to_numpy(), ds5h.y.to_numpy(), ds5h.z.to_numpy(), ds5h["ubar"].to_numpy())
stream5h.compute_mask(R = 0.1, orign = (0,0,9))
ds5h['streamtube'] = stream5h.mask
u_avg5hb = np.sum(ds5h['ubar'] * ds5h['streamtube'], axis = (1,2))/np.sum(ds5h['streamtube'], axis = (1,2))

stream6h = streamtube.Streamtube(ds6h.x.to_numpy(), ds6h.y.to_numpy(), ds6h.z.to_numpy(), ds6h["ubar"].to_numpy())
stream6h.compute_mask(R = 0.1, orign = (0,0,9))
ds6h['streamtube'] = stream6h.mask
u_avg6hb = np.sum(ds6h['ubar'] * ds6h['streamtube'], axis = (1,2))/np.sum(ds6h['streamtube'], axis = (1,2))

stream7h = streamtube.Streamtube(ds7h.x.to_numpy(), ds7h.y.to_numpy(), ds7h.z.to_numpy(), ds7h["ubar"].to_numpy())
stream7h.compute_mask(R = 0.1, orign = (0,0,9))
ds7h['streamtube'] = stream7h.mask
u_avg7hb = np.sum(ds7h['ubar'] * ds7h['streamtube'], axis = (1,2))/np.sum(ds7h['streamtube'], axis = (1,2))

stream8h = streamtube.Streamtube(ds8h.x.to_numpy(), ds8h.y.to_numpy(), ds8h.z.to_numpy(), ds8h["ubar"].to_numpy())
stream8h.compute_mask(R = 0.1, orign = (0,0,9))
ds8h['streamtube'] = stream8h.mask
u_avg8hb = np.sum(ds8h['ubar'] * ds8h['streamtube'], axis = (1,2))/np.sum(ds8h['streamtube'], axis = (1,2))

stream9h = streamtube.Streamtube(ds9h.x.to_numpy(), ds9h.y.to_numpy(), ds9h.z.to_numpy(), ds9h["ubar"].to_numpy())
stream9h.compute_mask(R = 0.1, orign = (0,0,9))
ds9h['streamtube'] = stream9h.mask
u_avg9hb = np.sum(ds9h['ubar'] * ds9h['streamtube'], axis = (1,2))/np.sum(ds9h['streamtube'], axis = (1,2))

stream10h = streamtube.Streamtube(ds10h.x.to_numpy(), ds10h.y.to_numpy(), ds10h.z.to_numpy(), ds10h["ubar"].to_numpy())
stream10h.compute_mask(R = 0.1, orign = (0,0,9))
ds10h['streamtube'] = stream10h.mask
u_avg10hb = np.sum(ds10h['ubar'] * ds10h['streamtube'], axis = (1,2))/np.sum(ds10h['streamtube'], axis = (1,2))

stream11h = streamtube.Streamtube(ds11h.x.to_numpy(), ds11h.y.to_numpy(), ds11h.z.to_numpy(), ds11h["ubar"].to_numpy())
stream11h.compute_mask(R = 0.1, orign = (0,0,9))
ds11h['streamtube'] = stream11h.mask
u_avg11hb = np.sum(ds11h['ubar'] * ds11h['streamtube'], axis = (1,2))/np.sum(ds11h['streamtube'], axis = (1,2))

stream12h = streamtube.Streamtube(ds12h.x.to_numpy(), ds12h.y.to_numpy(), ds12h.z.to_numpy(), ds12h["ubar"].to_numpy())
stream12h.compute_mask(R = 0.1, orign = (0,0,9))
ds12h['streamtube'] = stream12h.mask
u_avg12hb = np.sum(ds12h['ubar'] * ds12h['streamtube'], axis = (1,2))/np.sum(ds12h['streamtube'], axis = (1,2))

stream13h = streamtube.Streamtube(ds13h.x.to_numpy(), ds13h.y.to_numpy(), ds13h.z.to_numpy(), ds13h["ubar"].to_numpy())
stream13h.compute_mask(R = 0.1, orign = (0,0,9))
ds13h['streamtube'] = stream13h.mask
u_avg13hb = np.sum(ds13h['ubar'] * ds13h['streamtube'], axis = (1,2))/np.sum(ds13h['streamtube'], axis = (1,2))

stream14h = streamtube.Streamtube(ds14h.x.to_numpy(), ds14h.y.to_numpy(), ds14h.z.to_numpy(), ds14h["ubar"].to_numpy())
stream14h.compute_mask(R = 0.1, orign = (0,0,9))
ds14h['streamtube'] = stream14h.mask
u_avg14hb = np.sum(ds14h['ubar'] * ds14h['streamtube'], axis = (1,2))/np.sum(ds14h['streamtube'], axis = (1,2))

stream15h = streamtube.Streamtube(ds15h.x.to_numpy(), ds15h.y.to_numpy(), ds15h.z.to_numpy(), ds15h["ubar"].to_numpy())
stream15h.compute_mask(R = 0.1, orign = (0,0,9))
ds15h['streamtube'] = stream15h.mask
u_avg15hb = np.sum(ds15h['ubar'] * ds15h['streamtube'], axis = (1,2))/np.sum(ds15h['streamtube'], axis = (1,2))

stream16h = streamtube.Streamtube(ds16h.x.to_numpy(), ds16h.y.to_numpy(), ds16h.z.to_numpy(), ds16h["ubar"].to_numpy())
stream16h.compute_mask(R = 0.1, orign = (0,0,9))
ds16h['streamtube'] = stream16h.mask
u_avg16hb = np.sum(ds16h['ubar'] * ds16h['streamtube'], axis = (1,2))/np.sum(ds16h['streamtube'], axis = (1,2))

stream17h = streamtube.Streamtube(ds17h.x.to_numpy(), ds17h.y.to_numpy(), ds17h.z.to_numpy(), ds17h["ubar"].to_numpy())
stream17h.compute_mask(R = 0.1, orign = (0,0,9))
ds17h['streamtube'] = stream17h.mask
u_avg17hb = np.sum(ds17h['ubar'] * ds17h['streamtube'], axis = (1,2))/np.sum(ds17h['streamtube'], axis = (1,2))

#Wake Streamtubes
stream3m = streamtube.Streamtube(ds3m.x.to_numpy(), ds3m.y.to_numpy(), ds3m.z.to_numpy(), ds3m["ubar"].to_numpy())
stream3m.compute_mask(R = 0.3)
ds3m['streamtube'] = stream3m.mask
u_avg3mw = np.sum(ds3m['ubar'] * ds3m['streamtube'], axis = (1,2))/np.sum(ds3m['streamtube'], axis = (1,2))

stream4m = streamtube.Streamtube(ds4m.x.to_numpy(), ds4m.y.to_numpy(), ds4m.z.to_numpy(), ds4m["ubar"].to_numpy())
stream4m.compute_mask(R = 0.3)
ds4m['streamtube'] = stream4m.mask
u_avg4mw = np.sum(ds4m['ubar'] * ds4m['streamtube'], axis = (1,2))/np.sum(ds4m['streamtube'], axis = (1,2))

stream5m = streamtube.Streamtube(ds5m.x.to_numpy(), ds5m.y.to_numpy(), ds5m.z.to_numpy(), ds5m["ubar"].to_numpy())
stream5m.compute_mask(R = 0.3)
ds5m['streamtube'] = stream5m.mask
u_avg5mw = np.sum(ds5m['ubar'] * ds5m['streamtube'], axis = (1,2))/np.sum(ds5m['streamtube'], axis = (1,2))

stream6m = streamtube.Streamtube(ds6m.x.to_numpy(), ds6m.y.to_numpy(), ds6m.z.to_numpy(), ds6m["ubar"].to_numpy())
stream6m.compute_mask(R = 0.3)
ds6m['streamtube'] = stream6m.mask
u_avg6mw = np.sum(ds6m['ubar'] * ds6m['streamtube'], axis = (1,2))/np.sum(ds6m['streamtube'], axis = (1,2))

stream7m = streamtube.Streamtube(ds7m.x.to_numpy(), ds7m.y.to_numpy(), ds7m.z.to_numpy(), ds7m["ubar"].to_numpy())
stream7m.compute_mask(R = 0.3)
ds7m['streamtube'] = stream7m.mask
u_avg7mw = np.sum(ds7m['ubar'] * ds7m['streamtube'], axis = (1,2))/np.sum(ds7m['streamtube'], axis = (1,2))

stream8m = streamtube.Streamtube(ds8m.x.to_numpy(), ds8m.y.to_numpy(), ds8m.z.to_numpy(), ds8m["ubar"].to_numpy())
stream8m.compute_mask(R = 0.3)
ds8m['streamtube'] = stream8m.mask
u_avg8mw = np.sum(ds8m['ubar'] * ds8m['streamtube'], axis = (1,2))/np.sum(ds8m['streamtube'], axis = (1,2))

stream9m = streamtube.Streamtube(ds9m.x.to_numpy(), ds9m.y.to_numpy(), ds9m.z.to_numpy(), ds9m["ubar"].to_numpy())
stream9m.compute_mask(R = 0.3)
ds9m['streamtube'] = stream9m.mask
u_avg9mw = np.sum(ds9m['ubar'] * ds9m['streamtube'], axis = (1,2))/np.sum(ds9m['streamtube'], axis = (1,2))

stream10m = streamtube.Streamtube(ds10m.x.to_numpy(), ds10m.y.to_numpy(), ds10m.z.to_numpy(), ds10m["ubar"].to_numpy())
stream10m.compute_mask(R = 0.3)
ds10m['streamtube'] = stream10m.mask
u_avg10mw = np.sum(ds10m['ubar'] * ds10m['streamtube'], axis = (1,2))/np.sum(ds10m['streamtube'], axis = (1,2))

stream11m = streamtube.Streamtube(ds11m.x.to_numpy(), ds11m.y.to_numpy(), ds11m.z.to_numpy(), ds11m["ubar"].to_numpy())
stream11m.compute_mask(R = 0.3)
ds11m['streamtube'] = stream11m.mask
u_avg11mw = np.sum(ds11m['ubar'] * ds11m['streamtube'], axis = (1,2))/np.sum(ds11m['streamtube'], axis = (1,2))  

stream12m = streamtube.Streamtube(ds12m.x.to_numpy(), ds12m.y.to_numpy(), ds12m.z.to_numpy(), ds12m["ubar"].to_numpy())
stream12m.compute_mask(R = 0.3)
ds12m['streamtube'] = stream12m.mask
u_avg12mw = np.sum(ds12m['ubar'] * ds12m['streamtube'], axis = (1,2))/np.sum(ds12m['streamtube'], axis = (1,2))

stream13m = streamtube.Streamtube(ds13m.x.to_numpy(), ds13m.y.to_numpy(), ds13m.z.to_numpy(), ds13m["ubar"].to_numpy())
stream13m.compute_mask(R = 0.3)
ds13m['streamtube'] = stream13m.mask
u_avg13mw = np.sum(ds13m['ubar'] * ds13m['streamtube'], axis = (1,2))/np.sum(ds13m['streamtube'], axis = (1,2))

stream14m = streamtube.Streamtube(ds14m.x.to_numpy(), ds14m.y.to_numpy(), ds14m.z.to_numpy(), ds14m["ubar"].to_numpy())
stream14m.compute_mask(R = 0.3)
ds14m['streamtube'] = stream14m.mask
u_avg14mw = np.sum(ds14m['ubar'] * ds14m['streamtube'], axis = (1,2))/np.sum(ds14m['streamtube'], axis = (1,2))

stream15m = streamtube.Streamtube(ds15m.x.to_numpy(), ds15m.y.to_numpy(), ds15m.z.to_numpy(), ds15m["ubar"].to_numpy())
stream15m.compute_mask(R = 0.3)
ds15m['streamtube'] = stream15m.mask
u_avg15mw = np.sum(ds15m['ubar'] * ds15m['streamtube'], axis = (1,2))/np.sum(ds15m['streamtube'], axis = (1,2))

stream16m = streamtube.Streamtube(ds16m.x.to_numpy(), ds16m.y.to_numpy(), ds16m.z.to_numpy(), ds16m["ubar"].to_numpy())
stream16m.compute_mask(R = 0.3)
ds16m['streamtube'] = stream16m.mask
u_avg16mw = np.sum(ds16m['ubar'] * ds16m['streamtube'], axis = (1,2))/np.sum(ds16m['streamtube'], axis = (1,2))

stream17m = streamtube.Streamtube(ds17m.x.to_numpy(), ds17m.y.to_numpy(), ds17m.z.to_numpy(), ds17m["ubar"].to_numpy())
stream17m.compute_mask(R = 0.3)
ds17m['streamtube'] = stream17m.mask
u_avg17mw = np.sum(ds17m['ubar'] * ds17m['streamtube'], axis = (1,2))/np.sum(ds17m['streamtube'], axis = (1,2))

stream3h = streamtube.Streamtube(ds3h.x.to_numpy(), ds3h.y.to_numpy(), ds3h.z.to_numpy(), ds3h["ubar"].to_numpy())
stream3h.compute_mask(R = 0.3)
ds3h['streamtube'] = stream3h.mask
u_avg3hw = np.sum(ds3h['ubar'] * ds3h['streamtube'], axis = (1,2))/np.sum(ds3h['streamtube'], axis = (1,2))

stream4h = streamtube.Streamtube(ds4h.x.to_numpy(), ds4h.y.to_numpy(), ds4h.z.to_numpy(), ds4h["ubar"].to_numpy())
stream4h.compute_mask(R = 0.3)
ds4h['streamtube'] = stream4h.mask
u_avg4hw = np.sum(ds4h['ubar'] * ds4h['streamtube'], axis = (1,2))/np.sum(ds4h['streamtube'], axis = (1,2))

stream5h = streamtube.Streamtube(ds5h.x.to_numpy(), ds5h.y.to_numpy(), ds5h.z.to_numpy(), ds5h["ubar"].to_numpy())
stream5h.compute_mask(R = 0.3)
ds5h['streamtube'] = stream5h.mask
u_avg5hw = np.sum(ds5h['ubar'] * ds5h['streamtube'], axis = (1,2))/np.sum(ds5h['streamtube'], axis = (1,2))

stream6h = streamtube.Streamtube(ds6h.x.to_numpy(), ds6h.y.to_numpy(), ds6h.z.to_numpy(), ds6h["ubar"].to_numpy())
stream6h.compute_mask(R = 0.3)
ds6h['streamtube'] = stream6h.mask
u_avg6hw = np.sum(ds6h['ubar'] * ds6h['streamtube'], axis = (1,2))/np.sum(ds6h['streamtube'], axis = (1,2))

stream7h = streamtube.Streamtube(ds7h.x.to_numpy(), ds7h.y.to_numpy(), ds7h.z.to_numpy(), ds7h["ubar"].to_numpy())
stream7h.compute_mask(R = 0.3)
ds7h['streamtube'] = stream7h.mask
u_avg7hw = np.sum(ds7h['ubar'] * ds7h['streamtube'], axis = (1,2))/np.sum(ds7h['streamtube'], axis = (1,2))

stream8h = streamtube.Streamtube(ds8h.x.to_numpy(), ds8h.y.to_numpy(), ds8h.z.to_numpy(), ds8h["ubar"].to_numpy())
stream8h.compute_mask(R = 0.3)
ds8h['streamtube'] = stream8h.mask
u_avg8hw = np.sum(ds8h['ubar'] * ds8h['streamtube'], axis = (1,2))/np.sum(ds8h['streamtube'], axis = (1,2))

stream9h = streamtube.Streamtube(ds9h.x.to_numpy(), ds9h.y.to_numpy(), ds9h.z.to_numpy(), ds9h["ubar"].to_numpy())
stream9h.compute_mask(R = 0.3)
ds9h['streamtube'] = stream9h.mask
u_avg9hw = np.sum(ds9h['ubar'] * ds9h['streamtube'], axis = (1,2))/np.sum(ds9h['streamtube'], axis = (1,2))

stream10h = streamtube.Streamtube(ds10h.x.to_numpy(), ds10h.y.to_numpy(), ds10h.z.to_numpy(), ds10h["ubar"].to_numpy())
stream10h.compute_mask(R = 0.3)
ds10h['streamtube'] = stream10h.mask
u_avg10hw = np.sum(ds10h['ubar'] * ds10h['streamtube'], axis = (1,2))/np.sum(ds10h['streamtube'], axis = (1,2))

stream11h = streamtube.Streamtube(ds11h.x.to_numpy(), ds11h.y.to_numpy(), ds11h.z.to_numpy(), ds11h["ubar"].to_numpy())
stream11h.compute_mask(R = 0.3)
ds11h['streamtube'] = stream11h.mask
u_avg11hw = np.sum(ds11h['ubar'] * ds11h['streamtube'], axis = (1,2))/np.sum(ds11h['streamtube'], axis = (1,2))

stream12h = streamtube.Streamtube(ds12h.x.to_numpy(), ds12h.y.to_numpy(), ds12h.z.to_numpy(), ds12h["ubar"].to_numpy())
stream12h.compute_mask(R = 0.3)
ds12h['streamtube'] = stream12h.mask
u_avg12hw = np.sum(ds12h['ubar'] * ds12h['streamtube'], axis = (1,2))/np.sum(ds12h['streamtube'], axis = (1,2))

stream13h = streamtube.Streamtube(ds13h.x.to_numpy(), ds13h.y.to_numpy(), ds13h.z.to_numpy(), ds13h["ubar"].to_numpy())
stream13h.compute_mask(R = 0.3)
ds13h['streamtube'] = stream13h.mask
u_avg13hw = np.sum(ds13h['ubar'] * ds13h['streamtube'], axis = (1,2))/np.sum(ds13h['streamtube'], axis = (1,2))

stream14h = streamtube.Streamtube(ds14h.x.to_numpy(), ds14h.y.to_numpy(), ds14h.z.to_numpy(), ds14h["ubar"].to_numpy())
stream14h.compute_mask(R = 0.3)
ds14h['streamtube'] = stream14h.mask
u_avg14hw = np.sum(ds14h['ubar'] * ds14h['streamtube'], axis = (1,2))/np.sum(ds14h['streamtube'], axis = (1,2))

stream15h = streamtube.Streamtube(ds15h.x.to_numpy(), ds15h.y.to_numpy(), ds15h.z.to_numpy(), ds15h["ubar"].to_numpy())
stream15h.compute_mask(R = 0.3)
ds15h['streamtube'] = stream15h.mask
u_avg15hw = np.sum(ds15h['ubar'] * ds15h['streamtube'], axis = (1,2))/np.sum(ds15h['streamtube'], axis = (1,2))

stream16h = streamtube.Streamtube(ds16h.x.to_numpy(), ds16h.y.to_numpy(), ds16h.z.to_numpy(), ds16h["ubar"].to_numpy())
stream16h.compute_mask(R = 0.3)
ds16h['streamtube'] = stream16h.mask
u_avg16hw = np.sum(ds16h['ubar'] * ds16h['streamtube'], axis = (1,2))/np.sum(ds16h['streamtube'], axis = (1,2))

stream17h = streamtube.Streamtube(ds17h.x.to_numpy(), ds17h.y.to_numpy(), ds17h.z.to_numpy(), ds17h["ubar"].to_numpy())
stream17h.compute_mask(R = 0.3)
ds17h['streamtube'] = stream17h.mask
u_avg17hw = np.sum(ds17h['ubar'] * ds17h['streamtube'], axis = (1,2))/np.sum(ds17h['streamtube'], axis = (1,2))

#Plotting
plt.figure(figsize = (9,6))
plt.plot(ds3m.x, u_avg3mw, label = "Wake Averaged Velocity")
plt.plot(ds3m.x, u_avg3mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -3')
plt.savefig('./streamtube_3m')

plt.figure(figsize = (9,6))
plt.plot(ds3m.x, u_avg3hw, label = "Wake Averaged Velocity")
plt.plot(ds3m.x, u_avg3hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -3')
plt.savefig('./streamtube_3h')

plt.figure(figsize = (9,6))
plt.plot(ds4m.x, u_avg4mw, label = "Wake Averaged Velocity")
plt.plot(ds4m.x, u_avg4mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -2.5')
plt.savefig('./streamtube_4m')

plt.figure(figsize = (9,6))
plt.plot(ds4m.x, u_avg4hw, label = "Wake Averaged Velocity")
plt.plot(ds4m.x, u_avg4hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -2.5')
plt.savefig('./streamtube_4h')

plt.figure(figsize = (9,6))
plt.plot(ds5m.x, u_avg5mw, label = "Wake Averaged Velocity")
plt.plot(ds5m.x, u_avg5mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -2')
plt.savefig('./streamtube_5m')

plt.figure(figsize = (9,6))
plt.plot(ds5m.x, u_avg5hw, label = "Wake Averaged Velocity")
plt.plot(ds5m.x, u_avg5hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -2')
plt.savefig('./streamtube_5h')

plt.figure(figsize = (9,6))
plt.plot(ds6m.x, u_avg6mw, label = "Wake Averaged Velocity")
plt.plot(ds6m.x, u_avg6mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -1.5')
plt.savefig('./streamtube_6m')

plt.figure(figsize = (9,6))
plt.plot(ds6m.x, u_avg6hw, label = "Wake Averaged Velocity")
plt.plot(ds6m.x, u_avg6hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -1.5')
plt.savefig('./streamtube_6h')

plt.figure(figsize = (9,6))
plt.plot(ds7m.x, u_avg7mw, label = "Wake Averaged Velocity")
plt.plot(ds7m.x, u_avg7mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -1')
plt.savefig('./streamtube_7m')  

plt.figure(figsize = (9,6))
plt.plot(ds7m.x, u_avg7hw, label = "Wake Averaged Velocity")
plt.plot(ds7m.x, u_avg7hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -1')
plt.savefig('./streamtube_7h')

plt.figure(figsize = (9,6))
plt.plot(ds8m.x, u_avg8mw, label = "Wake Averaged Velocity")
plt.plot(ds8m.x, u_avg8mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = -0.5')
plt.savefig('./streamtube_8m')

plt.figure(figsize = (9,6))
plt.plot(ds8m.x, u_avg8hw, label = "Wake Averaged Velocity")
plt.plot(ds8m.x, u_avg8hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = -0.5')
plt.savefig('./streamtube_8h')  

plt.figure(figsize = (9,6))
plt.plot(ds9m.x, u_avg9mw, label = "Wake Averaged Velocity")
plt.plot(ds9m.x, u_avg9mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 0')
plt.savefig('./streamtube_9m')

plt.figure(figsize = (9,6))
plt.plot(ds9m.x, u_avg9hw, label = "Wake Averaged Velocity")
plt.plot(ds9m.x, u_avg9hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 0')
plt.savefig('./streamtube_9h')

plt.figure(figsize = (9,6))
plt.plot(ds10m.x, u_avg10mw, label = "Wake Averaged Velocity")
plt.plot(ds10m.x, u_avg10mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 0.5')
plt.savefig('./streamtube_10m') 

plt.figure(figsize = (9,6))
plt.plot(ds10m.x, u_avg10hw, label = "Wake Averaged Velocity")
plt.plot(ds10m.x, u_avg10hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 0.5')
plt.savefig('./streamtube_10h') 

plt.figure(figsize = (9,6))
plt.plot(ds11m.x, u_avg11mw, label = "Wake Averaged Velocity")
plt.plot(ds11m.x, u_avg11mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 1')
plt.savefig('./streamtube_11m') 

plt.figure(figsize = (9,6))
plt.plot(ds11m.x, u_avg11hw, label = "Wake Averaged Velocity")
plt.plot(ds11m.x, u_avg11hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 1')
plt.savefig('./streamtube_11h')

plt.figure(figsize = (9,6))
plt.plot(ds12m.x, u_avg12mw, label = "Wake Averaged Velocity")
plt.plot(ds12m.x, u_avg12mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 1.5')
plt.savefig('./streamtube_12m') 

plt.figure(figsize = (9,6))
plt.plot(ds12m.x, u_avg12hw, label = "Wake Averaged Velocity")
plt.plot(ds12m.x, u_avg12hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 1.5')
plt.savefig('./streamtube_12h')

plt.figure(figsize = (9,6))
plt.plot(ds13m.x, u_avg13mw, label = "Wake Averaged Velocity")
plt.plot(ds13m.x, u_avg13mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 2')
plt.savefig('./streamtube_13m')

plt.figure(figsize = (9,6))
plt.plot(ds13m.x, u_avg13hw, label = "Wake Averaged Velocity")
plt.plot(ds13m.x, u_avg13hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 2')
plt.savefig('./streamtube_13h')

plt.figure(figsize = (9,6))
plt.plot(ds14m.x, u_avg14mw, label = "Wake Averaged Velocity")
plt.plot(ds14m.x, u_avg14mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 2.5')
plt.savefig('./streamtube_14m')

plt.figure(figsize = (9,6))
plt.plot(ds14m.x, u_avg14hw, label = "Wake Averaged Velocity")
plt.plot(ds14m.x, u_avg14hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 2.5')
plt.savefig('./streamtube_14h')

plt.figure(figsize = (9,6))
plt.plot(ds15m.x, u_avg15mw, label = "Wake Averaged Velocity")
plt.plot(ds15m.x, u_avg15mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 3')
plt.savefig('./streamtube_15m')

plt.figure(figsize = (9,6))
plt.plot(ds15m.x, u_avg15hw, label = "Wake Averaged Velocity")
plt.plot(ds15m.x, u_avg15hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 3')
plt.savefig('./streamtube_15h')

plt.figure(figsize = (9,6))
plt.plot(ds16m.x, u_avg16mw, label = "Wake Averaged Velocity")
plt.plot(ds16m.x, u_avg16mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 3.5')
plt.savefig('./streamtube_16m')

plt.figure(figsize = (9,6))
plt.plot(ds16m.x, u_avg16hw, label = "Wake Averaged Velocity")
plt.plot(ds16m.x, u_avg16hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 3.5')
plt.savefig('./streamtube_16h')

plt.figure(figsize = (9,6))
plt.plot(ds17m.x, u_avg17mw, label = "Wake Averaged Velocity")
plt.plot(ds17m.x, u_avg17mb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 10% Blockage, Ct Prime = 4')
plt.savefig('./streamtube_17m')

plt.figure(figsize = (9,6))
plt.plot(ds17m.x, u_avg17hw, label = "Wake Averaged Velocity")
plt.plot(ds17m.x, u_avg17hb, label = "Bypass Averaged Velocity")
plt.legend()
plt.xlabel('X/D')
plt.ylabel('ubar')
plt.title('Streamtube Analysis at 35% Blockage, Ct Prime = 4')
plt.savefig('./streamtube_17h')
