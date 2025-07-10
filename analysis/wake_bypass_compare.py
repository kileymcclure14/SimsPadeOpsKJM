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

#Load Velocities
uavg_3hb = np.load("uavg_3hb.npy")
uavg_3mb = np.load("uavg_3mb.npy")
uavg_4hb = np.load("uavg_4hb.npy")
uavg_4mb = np.load("uavg_4mb.npy")
uavg_5hb = np.load("uavg_5hb.npy")
uavg_5mb = np.load("uavg_5mb.npy")
uavg_6hb = np.load("uavg_6hb.npy")
uavg_6mb = np.load("uavg_6mb.npy")
uavg_7hb = np.load("uavg_7hb.npy")
uavg_7mb = np.load("uavg_7mb.npy")
uavg_8hb = np.load("uavg_8hb.npy")
uavg_8mb = np.load("uavg_8mb.npy")
uavg_9hb = np.load("uavg_9hb.npy")
uavg_9mb = np.load("uavg_9mb.npy")
uavg_10hb = np.load("uavg_10hb.npy")
uavg_10mb = np.load("uavg_10mb.npy")
uavg_11hb = np.load("uavg_11hb.npy")
uavg_11mb = np.load("uavg_11mb.npy")
uavg_12hb = np.load("uavg_12hb.npy")
uavg_12mb = np.load("uavg_12mb.npy")
uavg_13hb = np.load("uavg_13hb.npy")
uavg_13mb = np.load("uavg_13mb.npy")
uavg_14hb = np.load("uavg_14hb.npy")
uavg_14mb = np.load("uavg_14mb.npy")
uavg_15hb = np.load("uavg_15hb.npy")
uavg_15mb = np.load("uavg_15mb.npy")
uavg_16hb = np.load("uavg_16hb.npy")
uavg_16mb = np.load("uavg_16mb.npy")
uavg_17hb = np.load("uavg_17hb.npy")
uavg_17mb = np.load("uavg_17mb.npy")
uavg_3hw = np.load("uavg_3hw.npy")
uavg_3mw = np.load("uavg_3mw.npy")
uavg_4hw = np.load("uavg_4hw.npy")
uavg_4mw = np.load("uavg_4mw.npy")
uavg_5hw = np.load("uavg_5hw.npy")
uavg_5mw = np.load("uavg_5mw.npy")
uavg_6hw = np.load("uavg_6hw.npy")
uavg_6mw = np.load("uavg_6mw.npy")
uavg_7hw = np.load("uavg_7hw.npy")
uavg_7mw = np.load("uavg_7mw.npy")
uavg_8hw = np.load("uavg_8hw.npy")
uavg_8mw = np.load("uavg_8mw.npy")
uavg_9hw = np.load("uavg_9hw.npy")
uavg_9mw = np.load("uavg_9mw.npy")
uavg_10hw = np.load("uavg_10hw.npy")
uavg_10mw = np.load("uavg_10mw.npy")
uavg_11hw = np.load("uavg_11hw.npy")
uavg_11mw = np.load("uavg_11mw.npy")
uavg_12hw = np.load("uavg_12hw.npy")
uavg_12mw = np.load("uavg_12mw.npy")
uavg_13hw = np.load("uavg_13hw.npy")
uavg_13mw = np.load("uavg_13mw.npy")
uavg_14hw = np.load("uavg_14hw.npy")
uavg_14mw = np.load("uavg_14mw.npy")
uavg_15hw = np.load("uavg_15hw.npy")
uavg_15mw = np.load("uavg_15mw.npy")
uavg_16hw = np.load("uavg_16hw.npy")
uavg_16mw = np.load("uavg_16mw.npy")
uavg_17hw = np.load("uavg_17hw.npy")
uavg_17mw = np.load("uavg_17mw.npy")
x = np.load("xvals.npy")

#Calculate U2/U1
u2_u1_3h = uavg_3hb / uavg_3hw
u2_u1_3m = uavg_3mb / uavg_3mw
u2_u1_4h = uavg_4hb / uavg_4hw
u2_u1_4m = uavg_4mb / uavg_4mw
u2_u1_5h = uavg_5hb / uavg_5hw
u2_u1_5m = uavg_5mb / uavg_5mw
u2_u1_6h = uavg_6hb / uavg_6hw
u2_u1_6m = uavg_6mb / uavg_6mw
u2_u1_7h = uavg_7hb / uavg_7hw
u2_u1_7m = uavg_7mb / uavg_7mw
u2_u1_8h = uavg_8hb / uavg_8hw
u2_u1_8m = uavg_8mb / uavg_8mw
u2_u1_9h = uavg_9hb / uavg_9hw
u2_u1_9m = uavg_9mb / uavg_9mw
u2_u1_10h = uavg_10hb / uavg_10hw
u2_u1_10m = uavg_10mb / uavg_10mw
u2_u1_11h = uavg_11hb / uavg_11hw
u2_u1_11m = uavg_11mb / uavg_11mw
u2_u1_12h = uavg_12hb / uavg_12hw
u2_u1_12m = uavg_12mb / uavg_12mw
u2_u1_13h = uavg_13hb / uavg_13hw
u2_u1_13m = uavg_13mb / uavg_13mw
u2_u1_14h = uavg_14hb / uavg_14hw
u2_u1_14m = uavg_14mb / uavg_14mw
u2_u1_15h = uavg_15hb / uavg_15hw
u2_u1_15m = uavg_15mb / uavg_15mw
u2_u1_16h = uavg_16hb / uavg_16hw
u2_u1_16m = uavg_16mb / uavg_16mw
u2_u1_17h = uavg_17hb / uavg_17hw
u2_u1_17m = uavg_17mb / uavg_17mw

#Plots
plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_3h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_3m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -3')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_3')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_4h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_4m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -2.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_4')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_5h, label = "35% Blockage ", color = 'blue')
plt.plot(x, u2_u1_5m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -2')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_5')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_6h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_6m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -1.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_6')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_7h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_7m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -1')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_7')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_8h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_8m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = -0.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_8')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_9h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_9m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 0')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_9')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_10h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_10m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 0.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_10')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_11h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_11m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 1')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_11')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_12h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_12m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 1.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_12')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_13h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_13m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 2')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_13')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_14h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_14m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 2.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_14')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_15h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_15m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 3')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_15')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_16h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_16m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 3.5')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_16')

plt.figure(figsize = (9,6))
plt.plot(x, u2_u1_17h, label = "35% Blockage", color = 'blue')
plt.plot(x, u2_u1_17m, label = '10% Blockage', color = 'red')
plt.title('Bypass/Wake Velocity at Ct Prime = 4')
plt.xlabel('x/D')
plt.ylabel('U2/U1')
plt.legend()
plt.savefig('./u2_u1_17')