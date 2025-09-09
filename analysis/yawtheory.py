import numpy as np
from UnifiedMomentumModel.Momentum import UnifiedMomentum, ThrustBasedUnified
from scipy.optimize import fsolve

def BC_residuals_ctprime(x, Ctprime, yaw, beta):
    an, u4, v4, us, dp, A4 = x
    r1 = 0.5*Ctprime*((1-an)**2)*(np.cos(yaw)**3) + (u4**2)*A4 + (us**2)*(1/beta - A4) - 1/beta + dp/beta
    r2 = 1 - np.sqrt(
        np.clip((1 - u4**2 - v4**2 - 2*dp), 0, 1e3) /
        (Ctprime*(np.cos(yaw)**2))
        ) - an
    r3 = 0.5 - dp - 0.5*us**2
    r4 = (1/beta) * ((1 - us) / (u4 - us)) - A4
    r6 = (1/A4) * (1 - an) * np.cos(yaw) - u4
    r7 = (-1/4)*Ctprime*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2) - v4
    return [r1, r2, r3, r4, r6, r7]

def model_BC_ctprime(Ctprime, yaw, beta):
    """
    an, u4, v4, us, dp, A4
    """
    umm_model = UnifiedMomentum()
    umm_sol = umm_model(Ctprime, yaw)
    initial_guess = [umm_sol.an, umm_sol.u4, umm_sol.v4, 0.99, -0.01, 1]
    root = fsolve((lambda x: BC_residuals_ctprime(x, Ctprime, yaw, beta)), initial_guess)
    return root

def BC_residuals_ct(x, Ct, yaw, beta):
    an, u4, v4, us, dp, A4, Ctprime = x
    r1 = 0.5*Ctprime*((1-an)**2)*(np.cos(yaw)**3) + (u4**2)*A4 + (us**2)*(1/beta - A4) - 1/beta + dp/beta
    r2 = 1 - np.sqrt(
        np.clip((1 - u4**2 - v4**2 - 2*dp) /
        (Ctprime*(np.cos(yaw)**2) + 1e-6)
        , 0, 1e3) ) - an
    r3 = 0.5 - dp - 0.5*us**2
    r4 = (1/beta) * ((1 - us) / (u4 - us)) - A4
    r6 = (1/A4) * (1 - an) * np.cos(yaw) - u4
    r7 = (-1/4)*Ctprime*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2) - v4
    r8 = (Ct / ((1-an)**2 * np.cos(yaw)**2 + 1e-6)) - Ctprime
    return [r1, r2, r3, r4, r6, r7, r8]

def model_BC_ct(Ct, yaw, beta):
    """
    an, u4, v4, us, dp, A4, Ctp
    """
    umm_model = ThrustBasedUnified()
    umm_sol = umm_model(Ct, yaw)
    Ctp_0 = Ct / ((1 - umm_sol.an)**2 * np.cos(yaw)**2 + 1e-6)
    initial_guess = [umm_sol.an, umm_sol.u4, umm_sol.v4, 1.001, -0.1, 1, 2]
    #initial_guess = [1/3, 0.5, 0.001, 1.001, -0.01, 1.1, 1]
    root = fsolve((lambda x: BC_residuals_ct(x, Ct, yaw, beta)), initial_guess)
    return root