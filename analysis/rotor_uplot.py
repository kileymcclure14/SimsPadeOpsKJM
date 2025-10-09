import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine
import streamtube

sim0 = pio.BudgetIO("Data/0_5_10_35_Files", padeops = True, normalize_origin = "turbine")
ds0 = sim0.slice(field_terms = 'u')
vel0 = ds0['u'].slice(zlim = 0, xlim = 0)

sim1 = pio.BudgetIO("Data/1_10_35_Files", padeops = True, normalize_origin = "turbine")
ds1 = sim1.slice(field_terms = 'u')
vel1 = ds1['u'].slice(zlim = 0, xlim = 0)

sim15 = pio.BudgetIO("Data/1_5_10_35_Files", padeops = True, normalize_origin = "turbine")
ds15 = sim15.slice(field_terms = 'u')
vel15 = ds15['u'].slice(zlim = 0, xlim = 0)

plt.figure(figsize = (3,4))
plt.plot(ds0.y, vel0)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 0.5 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_0_5_10_35.png', bbox_inches='tight', dpi = 300)

plt.figure(figsize = (3,4))
plt.plot(ds1.y, vel1)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 1 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_1_10_35.png', bbox_inches='tight', dpi = 300)

plt.figure(figsize = (3,4))
plt.plot(ds15.y, vel15)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 1.5 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_1_5_10_35.png', bbox_inches='tight', dpi = 300)