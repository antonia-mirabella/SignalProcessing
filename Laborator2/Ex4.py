import numpy as np
import matplotlib.pyplot as plt

tb = np.arange(0, 3, 1 / 8000)
xb = np.sin(2 * np.pi * 800 * tb)

xc = np.mod(240 * tb, 1) * 2 - 1

xsum = xb + xc

fig, axs = plt.subplots(3)
fig.suptitle('Sinus semnal, semna sawtooth si suma lor')

axs[0].plot(tb[:200], xb[:200])
axs[1].plot(tb[:200], xc[:200])
axs[2].plot(tb[:200], xsum[:200])

axs[2].set_xlabel('timp (s)')

plt.savefig('Lab2Ex4.pdf')
plt.show()
