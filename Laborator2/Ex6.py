import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 0.02, 1 / fs)

xa = np.sin(2 * np.pi * (fs / 2) * t)
xb = np.sin(2 * np.pi * (fs / 4) * t)
xc = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3)
fig.suptitle('Sinus si frecventa fs')

axs[0].stem(t, xa)
axs[1].stem(t, xb)
axs[2].stem(t, xc)

axs[2].set_xlabel('timp (s)')

plt.savefig('Lab2Ex6.pdf')
plt.show()