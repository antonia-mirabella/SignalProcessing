import numpy as np
import matplotlib.pyplot as plt

fs = 1600
# t = np.arange(0, 1, 1 / fs)
t = np.linspace(0, 3/ 16, int(fs/16))

xa = np.round(np.sin(2 * np.pi * (fs / 2) * t), 10)
xb = np.round(np.sin(2 * np.pi * (fs / 4) * t), 10)
xc = np.round(np.sin(2 * np.pi * 0 * t), 10)


sigs = [xa, xb, xc]

fig, axs = plt.subplots(3)
fig.suptitle('Sinus si frecventa fs (zoomed in)')

for i, sig in enumerate(sigs):
    axs[i].step(t, sig, color = 'purple', alpha = 0.7)

    # made the sample 'circle' smaller since it overlapped the previous step 'lines'
    markerline, stemlines, baseline = axs[i].stem(t, sig)
    markerline.set_markersize(3)


axs[2].set_xlabel('timp (s)')

plt.tight_layout
plt.savefig('Lab2Ex6.pdf')
plt.show()