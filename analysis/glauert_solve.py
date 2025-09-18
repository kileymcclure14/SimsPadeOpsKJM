import analysis_utils as au
from pathlib import Path
import os
import math
import cmath
import padeopsIO as pio
# from pathlib import Path
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from padeopsIO import turbine

cp_35 = np.load("cp_0deg_35.npy")
ct_35 = np.load("ct_0deg_35.npy")
ud = np.load("ud_0deg_35.npy")
uinf = np.load("uinf_0deg_35.npy")

vprime = (uinf*((ud/uinf)**2 + (ct_35/4)))/(ud/uinf)

cp_gl_35 = cp_35*((uinf/vprime)**3)
ct_gl_35 = ct_35*((uinf/vprime)**2)

np.save("cp_gl_35.npy", cp_gl_35)
np.save("ct_gl_35.npy", ct_gl_35)