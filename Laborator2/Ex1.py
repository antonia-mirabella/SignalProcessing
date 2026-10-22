import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0, 0.03, 0.0005)

x = 5 * np.sin(60 * 2 * np.pi * t + np.pi / 3)
y = 5 * np.cos(60 * 2 * np.pi * t+ np.pi / 3 - np.pi / 2)

fig, axs = plt.subplots(2)

axs[0].plot(t, x)
axs[1].plot(t, y)

fig.suptitle("Semnal sinus identic cu semnal cosinus")

plt.show()
plt.savefig('Lab2Ex1.pdf')
