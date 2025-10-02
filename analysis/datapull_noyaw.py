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

sim0 = pio.BudgetIO("Data/0_5_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime0 = sim0.ta[0].ct
p0 = sim0.read_turb_power("all", turb = 1)[-1]
uinf0 = sim0.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp0 = p0/(0.5*(np.pi/4)*(uinf0**3))
ud0 = sim0.read_turb_uvel("all", steady = False)[-1]
ct0 = ctprime0*((ud0/uinf0)**2)

sim1 = pio.BudgetIO("Data/1_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime1 = sim1.ta[0].ct
p1 = sim1.read_turb_power("all", turb = 1)[-1]
uinf1 = sim1.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp1 = p1/(0.5*(np.pi/4)*(uinf1**3))
ud1 = sim1.read_turb_uvel("all", steady = False)[-1]
ct1 = ctprime1*((ud1/uinf1)**2)

sim2 = pio.BudgetIO("Data/1_5_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime2 = sim2.ta[0].ct
p2 = sim2.read_turb_power("all", turb = 1)[-1]
uinf2 = sim2.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp2 = p2/(0.5*(np.pi/4)*(uinf2**3))
ud2 = sim2.read_turb_uvel("all", steady = False)[-1]
ct2 = ctprime2*((ud2/uinf2)**2)

# sim3 = pio.BudgetIO("Data/2_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
# ctprime3 = sim3.ta[0].ct
# p3 = sim3.read_turb_power("all", turb = 1)[-1]
# uinf3 = sim3.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
# cp3 = p3/(0.5*(np.pi/4)*(uinf3**3))
# ud3 = sim3.read_turb_uvel("all", steady = False)[-1]
# ct3 = ctprime3*((ud3/uinf3)**2)

# sim4 = pio.BudgetIO("Data/2_5_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
# ctprime4 = sim4.ta[0].ct
# p4 = sim4.read_turb_power("all", turb = 1)[-1]
# uinf4 = sim4.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
# cp4 = p4/(0.5*(np.pi/4)*(uinf4**3))
# ud4 = sim4.read_turb_uvel("all", steady = False)[-1]
# ct4 = ctprime4*((ud4/uinf4)**2)

# sim5 = pio.BudgetIO("Data/3_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
# ctprime5 = sim5.ta[0].ct
# p5 = sim5.read_turb_power("all", turb = 1)[-1]
# uinf5 = sim5.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
# cp5 = p5/(0.5*(np.pi/4)*(uinf5**3))
# ud5 = sim5.read_turb_uvel("all", steady = False)[-1]
# ct5 = ctprime5*((ud5/uinf5)**2)

# sim6 = pio.BudgetIO("Data/3_5_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
# ctprime6 = sim6.ta[0].ct
# p6 = sim6.read_turb_power("all", turb = 1)[-1]
# uinf6 = sim6.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
# cp6 = p6/(0.5*(np.pi/4)*(uinf6**3))
# ud6 = sim6.read_turb_uvel("all", steady = False)[-1]
# ct6 = ctprime6*((ud6/uinf6)**2)

# sim7 = pio.BudgetIO("Data/4_10_35_Files", padeops = True, runid = 0, normalize_origin = "turbine")
# ctprime7 = sim7.ta[0].ct
# p7 = sim7.read_turb_power("all", turb = 1)[-1]
# uinf7 = sim7.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
# cp7 = p7/(0.5*(np.pi/4)*(uinf7**3))
# ud7 = sim7.read_turb_uvel("all", steady = False)[-1]
# ct7 = ctprime7*((ud7/uinf7)**2)

#cp_raw = [cp0, cp1, cp2, cp3, cp4, cp5, cp6, cp7]
cp_raw = [cp0, cp1, cp2]
np.save('cp_10deg_35_mini.npy', cp_raw)

ct_raw = [ct0, ct1, ct2]
np.save('ct_10deg_35_mini.npy', ct_raw)

uinf = [uinf0, uinf1, uinf2]
np.save('uinf_10deg_35_mini.npy', uinf)

ud = [ud0, ud1, ud2]
np.save('ud_10deg_35_mini.npy', ud)

p = [p0, p1, p2]
np.save('p_10deg_35_mini.npy', p)
