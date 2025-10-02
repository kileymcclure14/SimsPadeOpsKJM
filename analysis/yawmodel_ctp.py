from yawtheory import model_BC_ctprime
import numpy as np

beta = 0.35
CtPrime = 0.5

yaw_degs = np.arange(0, 81, 10)
Ct_array = []
Cp_array = []

for yaw_deg in yaw_degs:
    yaw_rad = np.radians(yaw_deg)
    solution = model_BC_ctprime(CtPrime, yaw_rad, beta)
    an, u4, v4, us, dp, A4 = solution
    Ct = CtPrime * ((1 - an)**2) * (np.cos(yaw_rad)**2)
    Cp = CtPrime * ((1 - an)**3) * (np.cos(yaw_rad)**3)
    Ct_array.append(Ct)
    Cp_array.append(Cp)

Ct_array = np.array(Ct_array)
Cp_array = np.array(Cp_array)

np.save("ct_0_5_35_model.npy", Ct_array)
np.save("cp_0_5_35_model.npy", Cp_array)
