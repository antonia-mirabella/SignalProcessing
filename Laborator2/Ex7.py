import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 0.2, 1 / fs)
x = np.sin(40* 2 * np.pi  * t)

#  A

fig, axs = plt.subplots(2)
fig.suptitle('Semnalul si al 4-lea element din vectorul semnalului decimat')

axs[0].plot(t, x)

axs[1].stem(t[::4], x[::4])
axs[1].plot(t, x)

plt.savefig('Lab2Ex7a.pdf')
plt.show()

#  B

fig, axs = plt.subplots(1)
fig.suptitle('Semnal decimat la fs / 4 pornind de la al doilea element')

axs[0].stem(t[1::4], x[1::4])
axs[0].plot(t, x)


plt.savefig('Lab2Ex7b.pdf')
plt.show()