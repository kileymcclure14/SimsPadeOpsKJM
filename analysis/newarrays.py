import numpy as np

# ct_05 = np.load("ct_0_5_35_model.npy")
# ct_1 = np.load("ct_1_35_model.npy")
# ct_15 = np.load("ct_1_5_35_model.npy")
# ct_2 = np.load("ct_2_35_model.npy")
# ct_25 = np.load("ct_2_5_35_model.npy")
# ct_3 = np.load("ct_3_35_model.npy")
# ct_35 = np.load("ct_3_5_35_model.npy")
# ct_4 = np.load("ct_4_35_model.npy")

# ct_10deg_35_model = [ct_05[1], ct_1[1], ct_15[1], ct_2[1], ct_25[1], ct_3[1], ct_35[1], ct_4[1]]

# cp_05 = np.load("cp_0_5_35_model.npy")
# cp_1 = np.load("cp_1_35_model.npy")
# cp_15 = np.load("cp_1_5_35_model.npy")
# cp_2 = np.load("cp_2_35_model.npy")
# cp_25 = np.load("cp_2_5_35_model.npy")
# cp_3 = np.load("cp_3_35_model.npy")
# cp_35 = np.load("cp_3_5_35_model.npy")
# cp_4 = np.load("cp_4_35_model.npy")

# cp_10deg_35_model = [cp_05[1], cp_1[1], cp_15[1], cp_2[1], cp_25[1], cp_3[1], cp_35[1], cp_4[1]]

# a_05 = np.load("a_0_5_35_model.npy")
# a_1 = np.load("a_1_35_model.npy")
# a_15 = np.load("a_1_5_35_model.npy")
# a_2 = np.load("a_2_35_model.npy")
# a_25 = np.load("a_2_5_35_model.npy")
# a_3 = np.load("a_3_35_model.npy")
# a_35 = np.load("a_3_5_35_model.npy")
# a_4 = np.load("a_4_35_model.npy")

# a_10deg_35_model = [a_05[1], a_1[1], a_15[1], a_2[1], a_25[1], a_3[1], a_35[1], a_4[1]]

# np.save("ct_10deg_35_model.npy", ct_10deg_35_model)
# np.save("cp_10deg_35_model.npy", cp_10deg_35_model)
# np.save("a_10deg_35_model.npy", a_10deg_35_model)

a0 = np.load('a_0deg_10.npy')
a10 = np.load('a_10deg_10.npy')
a20 = np.load('a_20deg_10.npy')
a30 = np.load('a_30deg_10.npy')
a40 = np.load('a_40deg_10.npy')
a50 = np.load('a_50deg_10.npy')
a60 = np.load('a_60deg_10.npy')
a70 = np.load('a_70deg_10.npy')
a80 = np.load('a_80deg_10.npy')


a05 = [a0[0], a10[0], a20[0], a30[0], a40[0], a50[0], a60[0], a70[0], a80[0]]
a1 = [a0[1], a10[1], a20[1], a30[1], a40[1], a50[1], a60[1], a70[1], a80[1]]
a15 = [a0[2], a10[2], a20[2], a30[2], a40[2], a50[2], a60[2], a70[2], a80[2]]
a2 = [a0[3], a10[3], a20[3], a30[3], a40[3], a50[3], a60[3], a70[3], a80[3]]
a25 = [a0[4], a10[4], a20[4], a30[4], a40[4], a50[4], a60[4], a70[4], a80[4]]
a3 = [a0[5], a10[5], a20[5], a30[5], a40[5], a50[5], a60[5], a70[5], a80[5]]
a35 = [a0[6], a10[6], a20[6], a30[6], a40[6], a50[6], a60[6], a70[6], a80[6]]
a4 = [a0[7], a10[7], a20[7], a30[7], a40[7], a50[7], a60[7], a70[7], a80[7]]

np.save('a_0_5_10.npy', a05)
np.save('a_1_10.npy', a1)
np.save('a_1_5_10.npy', a15)
np.save('a_2_10.npy', a2)
np.save('a_2_5_10.npy', a25)
np.save('a_3_10.npy', a3)
np.save('a_3_5_10.npy', a35)
np.save('a_4_10.npy', a4)