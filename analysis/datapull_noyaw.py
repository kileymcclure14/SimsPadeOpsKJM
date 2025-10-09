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

sim0 = pio.BudgetIO("Data/U_0_Files/Sim_0000", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime0 = sim0.ta[0].ct
p0 = sim0.read_turb_power("all", turb = 1)[-1]
uinf0 = sim0.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp0 = p0/(0.5*(np.pi/4)*(uinf0**3))
ud0 = sim0.read_turb_uvel("all", steady = False)[-1]
ct0 = ctprime0*((ud0/uinf0)**2)
a0 = 1-np.cbrt((p0/(0.5*(np.pi/4)*ctprime0)))

sim1 = pio.BudgetIO("Data/U_0_Files/Sim_0001", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime1 = sim1.ta[0].ct
p1 = sim1.read_turb_power("all", turb = 1)[-1]
uinf1 = sim1.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp1 = p1/(0.5*(np.pi/4)*(uinf1**3))
ud1 = sim1.read_turb_uvel("all", steady = False)[-1]
ct1 = ctprime1*((ud1/uinf1)**2)
a1 = 1-np.cbrt((p1/(0.5*(np.pi/4)*ctprime1)))

sim2 = pio.BudgetIO("Data/U_0_Files/Sim_0002", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime2 = sim2.ta[0].ct
p2 = sim2.read_turb_power("all", turb = 1)[-1]
uinf2 = sim2.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp2 = p2/(0.5*(np.pi/4)*(uinf2**3))
ud2 = sim2.read_turb_uvel("all", steady = False)[-1]
ct2 = ctprime2*((ud2/uinf2)**2)
a2 = 1-np.cbrt((p2/(0.5*(np.pi/4)*ctprime2)))

sim3 = pio.BudgetIO("Data/U_0_Files/Sim_0003", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime3 = sim3.ta[0].ct
p3 = sim3.read_turb_power("all", turb = 1)[-1]
uinf3 = sim3.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp3 = p3/(0.5*(np.pi/4)*(uinf3**3))
ud3 = sim3.read_turb_uvel("all", steady = False)[-1]
ct3 = ctprime3*((ud3/uinf3)**2)
a3 = 1-np.cbrt((p3/(0.5*(np.pi/4)*ctprime3)))

sim4 = pio.BudgetIO("Data/U_0_Files/Sim_0004", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime4 = sim4.ta[0].ct
p4 = sim4.read_turb_power("all", turb = 1)[-1]
uinf4 = sim4.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp4 = p4/(0.5*(np.pi/4)*(uinf4**3))
ud4 = sim4.read_turb_uvel("all", steady = False)[-1]
ct4 = ctprime4*((ud4/uinf4)**2)
a4 = 1-np.cbrt((p4/(0.5*(np.pi/4)*ctprime4)))

sim5 = pio.BudgetIO("Data/U_0_Files/Sim_0005", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime5 = sim5.ta[0].ct
p5 = sim5.read_turb_power("all", turb = 1)[-1]
uinf5 = sim5.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp5 = p5/(0.5*(np.pi/4)*(uinf5**3))
ud5 = sim5.read_turb_uvel("all", steady = False)[-1]
ct5 = ctprime5*((ud5/uinf5)**2)
a5 = 1-np.cbrt((p5/(0.5*(np.pi/4)*ctprime5)))

sim6 = pio.BudgetIO("Data/U_0_Files/Sim_0006", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime6 = sim6.ta[0].ct
p6 = sim6.read_turb_power("all", turb = 1)[-1]
uinf6 = sim6.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp6 = p6/(0.5*(np.pi/4)*(uinf6**3))
ud6 = sim6.read_turb_uvel("all", steady = False)[-1]
ct6 = ctprime6*((ud6/uinf6)**2)
a6 = 1-np.cbrt((p6/(0.5*(np.pi/4)*ctprime6)))

sim7 = pio.BudgetIO("Data/U_0_Files/Sim_0007", padeops = True, runid = 0, normalize_origin = "turbine")
ctprime7 = sim7.ta[0].ct
p7 = sim7.read_turb_power("all", turb = 1)[-1]
uinf7 = sim7.slice(field_terms = ['u'], xlim = -5, zlim = 0)['u'].mean("y").values
cp7 = p7/(0.5*(np.pi/4)*(uinf7**3))
ud7 = sim7.read_turb_uvel("all", steady = False)[-1]
ct7 = ctprime7*((ud7/uinf7)**2)
a7 = 1-np.cbrt((p7/(0.5*(np.pi/4)*ctprime7)))

cp_raw = [cp0, cp1, cp2, cp3, cp4, cp5, cp6, cp7]
np.save('cp_0deg_U.npy', cp_raw)

ct_raw = [ct0, ct1, ct2, ct3, ct4, ct5, ct6, ct7]
np.save('ct_0deg_U.npy', ct_raw)

a_raw = [a0, a1, a2, a3, a4, a5, a6, a7]
np.save('a_0deg_U.npy', a_raw)