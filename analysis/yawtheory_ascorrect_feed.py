from yawtheory import BC_residuals_ctprime, model_BC_ctprime, BC_residuals_ct, model_BC_ct, model_BC_ct_feed
import numpy as np

ct = np.load("ct_0deg_35.npy")
beta1 = 0.35
yaw = 0
uinf = np.load("uinf_0deg_35.npy")

last_guess_vals = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

ct_primes_sol = []
for i in range(8):
    sol_ct = model_BC_ct_feed(ct[i], yaw, beta1, last_guess_vals[i])
    ct_primes_sol.append(sol_ct[6])
    
    

ct_primes_sol = np.array(ct_primes_sol)
beta2 = 0.00479

print("Ct Primes Solved from Ct:", ct_primes_sol)
an = []
for i in range(8):
    sol_ctprime = model_BC_ctprime(ct_primes_sol[i], yaw, beta2)
    an.append(sol_ctprime[0])

an = np.array(an)

cp_35_U = []
for i in range(8):
    cp_35_U.append(ct_primes_sol[i] * ((1-an[i])**3) * (np.cos(yaw)**3))

cp_35_U = np.array(cp_35_U)
np.save("cp_35_U_feed.npy", cp_35_U)