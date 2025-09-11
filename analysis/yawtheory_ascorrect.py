from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct
import numpy as np

ct = np.load("ct_0deg_10_n.npy")
beta1 = 0.10
yaw = 0
uinf = np.load("u_inf_0deg_10.npy")

ct_primes_sol = []
for i in range(8):
    sol_ct = model_BC_ct(ct[i], yaw, beta1)
    ct_primes_sol.append(sol_ct[6])

ct_primes_sol = np.array(ct_primes_sol)
beta2 = 0.00479

ud = []
for i in range(8):
    sol_ctprime = model_BC_ctprime(ct_primes_sol[i], yaw, beta2)
    ud.append(sol_ctprime[0])

ud = np.array(ud)

cp_10_U = []
for i in range(8):
    cp_10_U.append(ct_primes_sol[i]*((ud[i]/uinf[i])**3))

cp_10_U = np.array(cp_10_U)
np.save("cp_10_U.npy", cp_10_U)