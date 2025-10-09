from yawtheory import model_BC_ctprime
import numpy as np

beta = 0.00479
CtPrime = 4

yaw_degs = np.arange(0, 81, 10)
Ct_array = []
Cp_array = []
a_array = []

for yaw_deg in yaw_degs:
    yaw_rad = np.radians(yaw_deg)
    solution = model_BC_ctprime(CtPrime, yaw_rad, beta)
    an, u4, v4, us, dp, A4 = solution
    Ct = CtPrime * ((1 - an)**2) * (np.cos(yaw_rad)**2)
    Cp = CtPrime * ((1 - an)**3) * (np.cos(yaw_rad)**3)
    Ct_array.append(Ct)
    Cp_array.append(Cp)
    a_array.append(an)
    

Ct_array = np.array(Ct_array)
Cp_array = np.array(Cp_array)
a_array = np.array(a_array)

np.save("ct_4_U_model.npy", Ct_array)
np.save("cp_4_U_model.npy", Cp_array)
np.save("a_4_U_model.npy", a_array)
