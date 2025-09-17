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

b = 0.35
cp = np.load('cp_0deg_35.npy')
ct = np.load('ct_0deg_35.npy')

ct_werle = ct*((1-b)**2/(1+b))
cp_werle = cp*((1-b)**2)

np.save('cp_werle_35.npy', cp_werle)
np.save('ct_werle_35.npy', ct_werle)