import numpy as np

ct_05 = np.load("ct_0_5_35_model.npy")
ct_1 = np.load("ct_1_35_model.npy")
ct_15 = np.load("ct_1_5_35_model.npy")
ct_2 = np.load("ct_2_35_model.npy")
ct_25 = np.load("ct_2_5_35_model.npy")
ct_3 = np.load("ct_3_35_model.npy")
ct_35 = np.load("ct_3_5_35_model.npy")
ct_4 = np.load("ct_4_35_model.npy")

ct_10deg_35_model = [ct_05[1], ct_1[1], ct_15[1], ct_2[1], ct_25[1], ct_3[1], ct_35[1], ct_4[1]]

cp_05 = np.load("cp_0_5_35_model.npy")
cp_1 = np.load("cp_1_35_model.npy")
cp_15 = np.load("cp_1_5_35_model.npy")
cp_2 = np.load("cp_2_35_model.npy")
cp_25 = np.load("cp_2_5_35_model.npy")
cp_3 = np.load("cp_3_35_model.npy")
cp_35 = np.load("cp_3_5_35_model.npy")
cp_4 = np.load("cp_4_35_model.npy")

cp_10deg_35_model = [cp_05[1], cp_1[1], cp_15[1], cp_2[1], cp_25[1], cp_3[1], cp_35[1], cp_4[1]]

np.save("ct_10deg_35_model.npy", ct_10deg_35_model)
np.save("cp_10deg_35_model.npy", cp_10deg_35_model)