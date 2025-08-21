import numpy as np
from scipy.optimize import fsolve, least_squares
import math

def BC_residuals_ctprime(x, Ctp, yaw, beta):
    """
    Residuals for system in terms of Ct'
    Variables: an, us, u4, v4, A4
    """
    an, us, u4, v4, A4 = x

    r1 = 1 - np.sqrt(np.clip((us**2 - u4**2 - v4**2) / (Ctp*(np.cos(yaw)**2) + 1e-9), 0, 1e6)) - an
    r2 = np.sqrt(np.clip((beta*Ctp*((1-an)**2)*(np.cos(yaw)**3) + 2*beta*(u4**2)*A4 - 1) /
                         (2*A4*beta - 1 + 1e-9), 0, 1e6)) - us
    r3 = (1 - an)*np.cos(yaw) - u4*A4
    r4 = -(1/4)*Ctp*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2) - v4
    r5 = (us - 1) / (us - u4 + 1e-9) / beta - A4

    return [r1, r2, r3, r4, r5]

def model_BC_ctprime(Ctprime, yaw, beta):
    guesses = [
        [0.3, 1.0, 0.4, 0.0, 1.0],
        [0.2, 0.8, 0.3, 0.1, 0.8],
        [0.4, 1.2, 0.5, -0.1, 1.2]
    ]

    for guess in guesses:
        sol, info, ier, msg = fsolve(
            lambda x: BC_residuals_ctprime(x, Ctprime, yaw, beta),
            guess, full_output=True
        )
        residuals = BC_residuals_ctprime(sol, Ctprime, yaw, beta)
        if ier == 1 and np.linalg.norm(residuals) < 1e-6:
            return sol, "fsolve converged", residuals

    # fallback
    ls_sol = least_squares(
        lambda x: BC_residuals_ctprime(x, Ctprime, yaw, beta),
        guesses[0]
    )
    return ls_sol.x, "least_squares fallback", BC_residuals_ctprime(ls_sol.x, Ctprime, yaw, beta)

# Actual run
Ctprime =  1.370383
yaw = math.radians(10)
beta = 0.000001

solution, status, residuals = model_BC_ctprime(Ctprime, yaw, beta)
variables = ["an", "us", "u4", "v4", "A4"]

print("Solver status:", status)
print("\nSolution for the system of equations:")
for name, value in zip(variables, solution):
    print(f"  {name:6s} = {value:.6f}")

print("\nResiduals at solution (should be near zero):")
for i, res in enumerate(residuals, start=1):
    print(f"  r{i} = {res:.3e}")

# --- New: Compute CT and CP ---
an = solution[0]
CT = 4 * an * (1 - an)
CP = 4 * an * (1 - an)**2

print(f"  an (axial induction factor) = {an:.6f}")
print(f"\nDerived aerodynamic coefficients:")
print(f"  Ct (thrust coefficient)  = {CT:.6f}")
print(f"  Cp (power coefficient)  = {CP:.6f}")


