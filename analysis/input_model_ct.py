import numpy as np
from scipy.optimize import fsolve, least_squares
import math

beta = 0.1
Ct = 0.8   
yaw = math.radians(10)

def BC_residuals_ct(x, Ct, yaw, beta):
    '''
    returns residuals for: an, dPstar, us, A4, Ctp, u4, v4
    '''
    an, dPstar, us, A4, Ctp, u4, v4 = x
    Uinf = 1
    beta = 1 / beta

    r1 = Ctp*((1-an)**2)*(np.cos(yaw)**3) + 2*((u4/Uinf)**2)*A4  + 2*((us/Uinf)**2)*(beta - A4) - 2*beta - beta*dPstar
    r2 = 1 - np.sqrt(np.clip(
        ((Uinf**2 - u4**2 - v4**2) / (Ctp*(np.cos(yaw)**2)*(Uinf**2) + 1e-6)) +
        (dPstar / (Ctp*(np.cos(yaw)**2)+1e-6))
    ,0, 1e6)) - an
    r3 = - dPstar + (us/Uinf)**2 - 1
    r4 = (((Uinf - us)*beta) / ((u4 - us))) - A4
    r5 = (Ct / ((1-an)**2 * np.cos(yaw)**2 + 1e-6)) - Ctp
    r6 = - (1/4)*Ctp*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2)*Uinf - v4
    r7 = (1 - an)*Uinf*np.cos(yaw) - u4*A4

    return [r1, r2, r3, r4, r5, r6, r7]

def model_BC_ct(Ct, yaw, beta):
    guesses = [
        [0.2, 0.1, 1.0, 1.0, Ct, 0.5, 0.0],
        [0.3, 0.5, 0.8, 0.8, Ct, 0.6, 0.1],
        [0.1, 0.01, 1.2, 1.5, Ct, 0.7, -0.1],
    ]
    for guess in guesses:
        sol, info, ier, msg = fsolve(
            lambda x: BC_residuals_ct(x, Ct, yaw, beta),
            guess, full_output=True
        )
        residuals = BC_residuals_ct(sol, Ct, yaw, beta)
        if ier == 1 and np.linalg.norm(residuals) < 1e-6:
            return sol, "fsolve converged", residuals

    # If none of the fsolve runs work → try least_squares
    ls_sol = least_squares(
        lambda x: BC_residuals_ct(x, Ct, yaw, beta),
        guesses[0]
    )
    return ls_sol.x, "least_squares fallback", BC_residuals_ct(ls_sol.x, Ct, yaw, beta)

# Run model
solution, status, residuals = model_BC_ct(Ct, yaw, beta)

variables = ["an", "dPstar", "us", "A4", "Ctp", "u4", "v4"]

print("Solver status:", status)
print("\nSolution for the system of equations:")
for name, value in zip(variables, solution):
    print(f"  {name:6s} = {value:.6f}")

print("\nResiduals at solution (should be near zero):")
for i, res in enumerate(residuals, start=1):
    print(f"  r{i} = {res:.3e}")

