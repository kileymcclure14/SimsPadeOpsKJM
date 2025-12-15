import numpy as np
import polars as pl
from scipy.interpolate import LinearNDInterpolator
import utils
from scipy.optimize import root
from UnifiedMomentumModel.Momentum import UnifiedMomentum

@utils.cache_polars(utils.CACHEDIR / "robust_solver_table_2.csv")
def generate_table():
    betas = np.linspace(0.005, 0.4, 10)
    ctprimes = np.linspace(0.1, 10, 10)
    yaw_angles = np.radians(np.linspace(-45, 45, 10))
    results = []
    for beta in betas:
        for ctprime in ctprimes:
            for yaw in yaw_angles:
                model = BlockageModel(ctprime, yaw=yaw, beta=beta)
                an = model[0]
                dPstar = model[1]
                us = model[2]
                A4 = model[3]
                u4 = model[4]
                v4 = model[5]
                ct = ctprime * ((1 - an) * np.cos(yaw)) ** 2
                _df = pl.DataFrame({
                    "beta": [beta],
                    "ctprime": [ctprime],
                    "yaw": [yaw],
                    "ct": [ct],
                    "an": [an],
                    "dPstar": [dPstar],
                    "us": [us],
                    "A4": [A4],
                    "u4": [u4],
                    "v4": [v4]
                })
                results.append(_df)
    return pl.concat(results)

def _blockage_residual_ct(x, Ct, yaw, beta):
    '''
    Inputs:
        x: Input vector [an, dPstar, us, A4, Ctp, u4, v4]
        Ct : Thrust coefficient
        yaw : Yaw angle in radians
        beta : Blockage ratio

    Returns:
        Residuals of the system of equations
    '''
    an, dPstar, us, A4, Ctp, u4, v4 = x

    Ctp = np.clip(Ctp, 1e-3, 20)
    u4 = np.clip(u4, 0.0001, 1.01)
    an = np.clip(an, 0.0001, 0.999)
    # print(Ctp)

    umm_model = UnifiedMomentum()
    umm_sol = umm_model(Ctp, yaw)
    dp_UMM = umm_sol.dp
    dpw = - (1 - beta) * dp_UMM

    r1 = -0.5*Ctp*((1-an)**2)*(np.cos(yaw)**3) + (1/beta) *dPstar + A4*dpw - A4*u4**2 - ((1/beta) - A4)*us**2 + (1/beta)
    r2 = 1 - np.sqrt(np.clip(
        ((1 - u4**2 - v4**2) / (Ctp*(np.cos(yaw)**2) + 1e-6)) + 
        ((dPstar + dpw) / (0.5*Ctp*(np.cos(yaw)**2))), 0, 1e6)
        ) - an
    r3 = - dPstar + 0.5*us**2 - 0.5
    r4 = (1/beta)*((1 - us) / (u4 - us)) - A4
    r5 = (Ct / ((1-an)**2 * np.cos(yaw)**2 + 1e-6)) - Ctp
    r6 = - (1/4)*Ctp*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2) - v4
    r7 = (1 - an)*np.cos(yaw) - u4*A4

    return [r1, r2, r3, r4, r5, r6, r7]


def ThrustBasedBlockageModel(Ct, yaw, beta, return_success=False):
    '''
    Inputs:
    - Ct : Thrust coefficient
    - yaw : Yaw angle in radians
    - beta : Blockage ratio

    Returns:
    - an : Axial induction factor
    - dPstar : Non-dimensional pressure drop across the rotor
    - us : Bypass velocity
    - A4 : Wake area
    - Ctp : Local thrust coefficient
    - u4 : Streamwise velocity at the far wake
    - v4 : Spanwise velocity at the far wake
    '''
    df = generate_table()
    axes = df.select(['ct', 'yaw', 'beta']).to_numpy()
    an_data = df['an'].to_numpy()
    dPstar_data = df['dPstar'].to_numpy()
    us_data = df['us'].to_numpy()
    A4_data = df['A4'].to_numpy()
    ctprime_data = df['ctprime'].to_numpy()
    u4_data = df['u4'].to_numpy()
    v4_data = df['v4'].to_numpy()

    an_interp = LinearNDInterpolator(axes, an_data)
    dPstar_interp = LinearNDInterpolator(axes, dPstar_data)
    us_interp = LinearNDInterpolator(axes, us_data)
    A4_interp = LinearNDInterpolator(axes, A4_data)
    ctprime_interp = LinearNDInterpolator(axes, ctprime_data)
    u4_interp = LinearNDInterpolator(axes, u4_data)
    v4_interp = LinearNDInterpolator(axes, v4_data)

    an_0 = an_interp(Ct, yaw, beta)
    dPstar_0 = dPstar_interp(Ct, yaw, beta)
    us_0 = us_interp(Ct, yaw, beta)
    A4_0 = A4_interp(Ct, yaw, beta)
    ctprime_0 = ctprime_interp(Ct, yaw, beta)
    u4_0 = u4_interp(Ct, yaw, beta)
    v4_0 = v4_interp(Ct, yaw, beta)


    initial_guess = np.array([an_0, dPstar_0, us_0, A4_0, ctprime_0, u4_0, v4_0])
    sol = root((lambda x: _blockage_residual_ct(x, Ct, yaw, beta)), initial_guess, method = 'lm')
    print(f"Running model for Ct={Ct}, yaw={yaw}, beta={beta}")
    print("Success:", sol.success)
    print("Solution:", sol.x) 
    if return_success:
        return sol.x, sol.success
    else:
        return sol.x


def _blockage_residual_ctp(x, Ctp, yaw, beta):
    '''
    Inputs:
        x: Input vector [an, dPstar, us, A4, u4, v4]
        Ctp : Local thrust coefficient
        yaw : Yaw angle in radians
        beta : Blockage ratio

    Returns:
        Residuals of the system of equations
    '''
    an, dPstar, us, A4, u4, v4 = x

    umm_model = UnifiedMomentum()
    umm_sol = umm_model(Ctp, yaw)
    dp_UMM = umm_sol.dp
    dpw = - (1 - beta) * dp_UMM

    r1 = -0.5*Ctp*((1-an)**2)*(np.cos(yaw)**3) + (1/beta) *dPstar + A4*dpw - A4*u4**2 - ((1/beta) - A4)*us**2 + (1/beta)
    r2 = 1 - np.sqrt(np.clip(
        ((1 - u4**2 - v4**2) / (Ctp*(np.cos(yaw)**2) + 1e-6)) + 
        ((dPstar + dpw) / (0.5*Ctp*(np.cos(yaw)**2))), 0, 1e6)
        ) - an
    r3 = - dPstar + 0.5*us**2 - 0.5
    r4 = (1/beta)*((1 - us) / (u4 - us)) - A4
    r5 = - (1/4)*Ctp*((1-an)**2)*np.sin(yaw)*(np.cos(yaw)**2) - v4
    r6 = (1 - an)*np.cos(yaw) - u4*A4

    return [r1, r2, r3, r4, r5, r6]

def BlockageModel(Ctp, yaw, beta, return_success=False):
    '''
    Inputs:
        Ctp : Local thrust coefficient
        yaw : Yaw angle in radians
        beta : Blockage ratio

    Returns:
        an : Axial induction factor
        dPstar : Non-dimensional pressure drop across the rotor
        us : Bypass velocity
        A4 : Wake area
        u4 : Streamwise velocity at the far wake
        v4 : Spanwise velocity at the far wake
    '''
    umm_model = UnifiedMomentum()
    umm_sol = umm_model(Ctp, yaw)
    initial_guess = [(1-beta)*umm_sol.an, 0.001, 1.01, 1, umm_sol.u4, umm_sol.v4]
    sol = root((lambda x: _blockage_residual_ctp(x, Ctp, yaw, beta)), initial_guess)
    print(f"Running model for Ctp={Ctp}, yaw={yaw}, beta={beta}")
    print("Success:", sol.success)
    print("Solution:", sol.x)
    if return_success:
        return sol.x, sol.success
    else:
        return sol.x