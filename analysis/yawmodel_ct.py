from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct
import numpy as np
import matplotlib.pyplot as plt

cts = np.load("ct_0deg_10.npy")
beta = 0.1
yaw = 0

Cp_array = []

for ct in cts:
    solution = model_BC_ct(ct, yaw, beta)
    an, u4, v4, us, dp, A4, Ctp = solution
    Cp = Ctp * ((1 - an)**3) * (np.cos(yaw)**3)
    Cp_array.append(Cp)

Cp_array = np.array(Cp_array)

les = np.load("cp_0deg_10.npy")
