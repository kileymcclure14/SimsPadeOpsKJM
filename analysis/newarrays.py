import numpy as np

ct_05 = np.load("ct_0_5_35_model_new.npy")
ct_1 = np.load("ct_1_35_model_new.npy")
ct_15 = np.load("ct_1_5_35_model_new.npy")
ct_2 = np.load("ct_2_35_model_new.npy")
ct_25 = np.load("ct_2_5_35_model_new.npy")
ct_3 = np.load("ct_3_35_model_new.npy")
ct_35 = np.load("ct_3_5_35_model_new.npy")
ct_4 = np.load("ct_4_35_model_new.npy")

ct_0deg_35_model = [ct_05[0], ct_1[0], ct_15[0], ct_2[0], ct_25[0], ct_3[0], ct_35[0], ct_4[0]]

cp_05 = np.load("cp_0_5_35_model_new.npy")
cp_1 = np.load("cp_1_35_model_new.npy")
cp_15 = np.load("cp_1_5_35_model_new.npy")
cp_2 = np.load("cp_2_35_model_new.npy")
cp_25 = np.load("cp_2_5_35_model_new.npy")
cp_3 = np.load("cp_3_35_model_new.npy")
cp_35 = np.load("cp_3_5_35_model_new.npy")
cp_4 = np.load("cp_4_35_model_new.npy")

cp_0deg_35_model = [cp_05[0], cp_1[0], cp_15[0], cp_2[0], cp_25[0], cp_3[0], cp_35[0], cp_4[0]]

np.save("ct_0deg_35_model_new.npy", ct_0deg_35_model)
np.save("cp_0deg_35_model_new.npy", cp_0deg_35_model)