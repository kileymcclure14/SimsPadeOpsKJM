from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct
import numpy as np

ct = np.load("ct_0deg_10.npy")
beta1 = 0.10
yaw = 0
uinf = np.load("u_inf_0deg_10.npy")

ct_primes_sol = []
for i in range(8):
    sol_ct = model_BC_ct(ct[i], yaw, beta1)
    ct_primes_sol.append(sol_ct[6])

ct_primes_sol = np.array(ct_primes_sol)
beta2 = 0.00479

an = []
for i in range(8):
    sol_ctprime = model_BC_ctprime(ct_primes_sol[i], yaw, beta2)
    an.append(sol_ctprime[0])

an = np.array(an)

cp_10_U = []
for i in range(8):
    cp_10_U.append(ct_primes_sol[i] * ((1-an[i])**3) * (np.cos(yaw)**3))

cp_10_U = np.array(cp_10_U)
np.save("cp_10_Ut.npy", cp_10_U)