from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct
import numpy as np

ct = np.load("ct_0_5_10.npy")
beta1 = 0.10
yaw = 0
uinf = np.load("u_inf_0deg_10.npy")

for i in range(8):
    sol_ct = model_BC_ct(ct[i], yaw, beta1)
    ct_primes_sol = sol_ct[6]

beta2 = 0.00479

for i in range(8):
    sol_ctprime = model_BC_ctprime(ct_primes_sol, yaw, beta2)
    ud = sol_ctprime[0]

cp_10_U = ct_primes_sol[i]*((ud[i]/uinf[i])**3)

np.save("cp_10_U.npy", cp_10_U)