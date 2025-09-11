import matplotlib.pyplot as plt
import numpy as np

yaw = [0, 10, 20, 30, 40, 50, 60, 70, 80]
model = np.load("cp_4_10_model_new.npy")
les = np.load("cp_4_10.npy")

plt.figure(figsize = (3,4))
plt.plot(yaw, model, linestyle = '-', color = 'blue')
plt.plot(yaw, les[0:9], 'o', color = 'black')
plt.savefig('test')