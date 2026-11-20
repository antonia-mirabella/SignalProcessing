import numpy as np
import matplotlib.pyplot as plt

t = np.arange(256) / 128

x = np.sin(2 * np.pi * 10 * t)
y = np.sin(2 * np.pi * 25 * t)
z = np.sin(2 * np.pi * 40 * t)

fig, axs = plt.subplots(4, figsize=(8, 8))
fig.suptitle('Aliasing example (signal freq 10 - 25 - 40 and sampling 15s)')

axs[0].plot(t, x, color='tab:purple', label='Signal x')
axs[1].plot(t, x, color='tab:purple', label='Signal x')
axs[2].plot(t, y, color='tab:red', label='Signal y')
axs[3].plot(t, z, color='tab:orange', label='Signal z')

sample = np.arange(int(t[-1] * 15) + 1) / 15
xs = np.sin(2 * np.pi * 10 * sample)
ys = np.sin(2 * np.pi * 25 * sample)
zs = np.sin(2 * np.pi * 40 * sample)

axs[1].stem(sample, xs, linefmt='C4-', markerfmt='C4o', label='Samples x')
axs[2].stem(sample, ys, linefmt='C3-', markerfmt='C3o', label='Samples y')
axs[3].stem(sample, zs, linefmt='C1-', markerfmt='C1o', label='Samples z')

for ax in axs:
    ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1))
axs[-1].set_xlabel('Time (s)')
fig.tight_layout()
plt.savefig('Lab4Ex2.pdf')
plt.show()