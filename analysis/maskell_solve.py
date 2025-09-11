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

b = 0.1
k = 0.3551 - 5.1050*b

ct_block = np.load("ct_0deg_10.npy")
cp_block = np.load("cp_0deg_10.npy")

V0_Vprime = np.sqrt(1-(b*ct_block*(1/k)))

cp_mask = cp_block*((V0_Vprime)**3)

np.save('cp_maskell_10_U.npy', cp_mask)