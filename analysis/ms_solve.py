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

Ctprimes = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
cp_35 = np.load("cp_0deg_35_f.npy")
ct_35 = np.load("ct_0deg_35_f.npy")
ud = np.load("ud_0deg_35_f.npy")
uinf = np.load("uinf_0deg_35_f.npy")
p = np.load("p_35_f.npy")
p = np.array(p)

a = 1-np.cbrt((p/(0.5*(np.pi/4)*Ctprimes)))

u = 1-a

v0_vp = 1/(u + (ct_35/(4*u)))

cp = cp_35*(v0_vp**3)
ct = ct_35*(v0_vp**2)

np.save("cp_ms_35_f.npy", cp)
np.save("ct_ms_35_f.npy", ct)