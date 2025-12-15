from yawtheory2 import ThrustBasedBlockageModel, BlockageModel
from UnifiedMomentumModel.Momentum import ThrustBasedUnified, UnifiedMomentum
import numpy as np

ct_vals = np.load('C_CT_RP.npy')
yaw = 0
beta1 = 0.35

ctp_thrust = []
for i in range(21):
    sol_ct = ThrustBasedBlockageModel(ct_vals[i], yaw, beta1)
    ctp_thrust.append(sol_ct[4])


ctp_thrust = np.array(ctp_thrust)
np.save('CTP_Sol_RP.npy', ctp_thrust)

beta2 = 0.005

an_ctp = []
for i in range(21):
    sol_ctp = BlockageModel(ctp_thrust[i], yaw, beta2)
    an_ctp.append(sol_ctp[0])

an_ctp = np.array(an_ctp)
print(an_ctp)
print(ctp_thrust)

cp_cor = []
for i in range(21):
    cp_corr = ctp_thrust[i] * ((1 - an_ctp[i])**3) * (np.cos(yaw)**3)
    cp_cor.append(cp_corr)

ct_cor = []
for i in range(21):
    ct_corr = ctp_thrust[i] * ((1 - an_ctp[i])**2) * (np.cos(yaw)**2)
    ct_cor.append(ct_corr)

np.save('CT_RP_Cor.npy', np.array(ct_cor))
np.save('CP_RP_Cor.npy', np.array(cp_cor))