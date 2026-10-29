import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.03, 0.0005)

fig, axs = plt.subplots(4)

x = 0
for i, phi in enumerate([ np.pi, np.pi / 2, np.pi / 3, -(np.pi / 3)]):
    x = np.sin(30 * 2 * np.pi * t + phi)

    axs[i].plot(t, x)
    plt.xlabel('timp (s)')
    axs[i].set_title(f'semnal {i + 1}')

fig.suptitle("4 semnale cu faze diferite")

plt.savefig("Lab2Ex2a.pdf")
plt.show()


fig, axs = plt.subplots(4, 1, sharex=True)

for i, ratio in enumerate([0.1, 1, 10, 100]):
    z = np.random.normal(size=x.shape)
    gamma = np.linalg.norm(x) / (np.sqrt(ratio) * np.linalg.norm(z))
    x += gamma * z

    axs[i].plot(t, x)
    axs[i].set_title(f"SNR {ratio}")

fig.suptitle('Semnal cu zgomot')
plt.savefig("Lab2Ex2b.pdf")
plt.show()
