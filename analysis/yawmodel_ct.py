from yawtheory2 import ThrustBasedBlockageModel
import numpy as np
import matplotlib.pyplot as plt
from UnifiedMomentumModel.Momentum import ThrustBasedUnified, UnifiedMomentum

cts = np.load('U_CT_RP.npy')
beta = 0.35
yaw = 0

Cp_array = []

ctp_thrust = []
an_thrust = []
for i in range(16):
    sol_ct = ThrustBasedBlockageModel(cts[i], yaw, beta)
    an_thrust.append(sol_ct[0])
    ctp_thrust.append(sol_ct[4])

ctp_thrust = np.array(ctp_thrust)
an_thrust = np.array(an_thrust)

CP_Cor_RP,= ctp_thrust * ((1-an_thrust)**3) * (np.cos(np.radians(yaw))**3)
np.save('U_CTP_Sol_RP.npy', np.array(ctp_thrust))


