import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine
import streamtube

sim2 = pio.BudgetIO("Data/2_10_35_Files", padeops = True, normalize_origin = "turbine")
ds2 = sim2.slice(field_terms = 'u')
vel2 = ds2['u'].slice(zlim = 0, xlim = 0)

sim25 = pio.BudgetIO("Data/2_5_10_35_Files", padeops = True, normalize_origin = "turbine")
ds25 = sim25.slice(field_terms = 'u')
vel25 = ds25['u'].slice(zlim = 0, xlim = 0)

sim3 = pio.BudgetIO("Data/3_10_35_Files", padeops = True, normalize_origin = "turbine")
ds3 = sim3.slice(field_terms = 'u')
vel3 = ds3['u'].slice(zlim = 0, xlim = 0)

plt.figure(figsize = (3,4))
plt.plot(ds2.y, vel2)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 2 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_2_10_35.png', bbox_inches='tight', dpi = 300)

plt.figure(figsize = (3,4))
plt.plot(ds25.y, vel25)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 2.5 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_2_5_10_35.png', bbox_inches='tight', dpi = 300)

plt.figure(figsize = (3,4))
plt.plot(ds3.y, vel3)
plt.xlabel('y/D')
plt.ylabel('Velocity')
plt.title('Rotor View for 3 Ct Prime, 10 Degree Yaw, 35% Blockage')
plt.savefig('rotor_3_10_35.png', bbox_inches='tight', dpi = 300)