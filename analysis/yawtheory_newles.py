from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct
import numpy as np
import pandas as pd

ct = np.load('ct_p3.npy')
beta1 = 0.3
yaw = 0
uinf = 1

ct_primes_sol = []
for i in range(5):
    sol_ct = model_BC_ct(ct[i], yaw, beta1)
    ct_primes_sol.append(sol_ct[6])

ct_primes_sol = np.array(ct_primes_sol)
np.save('ct_primes_sol_p3', ct_primes_sol)
beta2 = 0.005

an = []
for i in range(5):
    sol_ctprime = model_BC_ctprime(ct_primes_sol[i], yaw, beta2)
    an.append(sol_ctprime[0])

an = np.array(an)

cp_cor_p3_p05_newmod = []
for i in range(5):
    cp_cor_p3_p05_newmod.append(ct_primes_sol[i] * ((1-an[i])**3) * (np.cos(yaw)**3))

cp_cor_p3_p05_newmod = np.array(cp_cor_p3_p05_newmod)
np.save("cp_cor_p3_p05_newmod.npy", cp_cor_p3_p05_newmod)