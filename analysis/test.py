import matplotlib.pyplot as plt
import numpy as np

cp = np.load('cp_0deg_35.npy')
ctprimes = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4])

plt.figure(figsize=(9,6))
plt.plot(ctprimes, cp, marker='o')
plt.savefig('test')