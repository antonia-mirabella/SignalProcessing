import numpy as np
import matplotlib.pyplot as plt

#  A + B

t = np.arange(0, 0.03, 0.0005)
xt = np.cos(520 * np.pi * t +  np.pi / 3)
yt = np.cos(280 * np.pi * t - np.pi / 3)
zt = np.cos(120 * np.pi * t +  np.pi / 3)

fig, axs = plt.subplots(3)
fig.suptitle('Afisare semnale continue')
axs[0].plot(t,xt)
axs[1].plot(t,yt)
axs[2].plot(t,zt)

plt.savefig('Lab1Ex1b.pdf')
plt.show()

#  C

tc = np.arange(0, 0.03, 1/ 200)
xc = np.cos(520 * np.pi * tc +  np.pi / 3)
yc = np.cos(280 * np.pi * tc - np.pi / 3)
zc = np.cos(120 * np.pi * tc +  np.pi / 3)

fig, axs = plt.subplots(3)
fig.suptitle('Afisare semnale esantionate cu frec 200')
axs[0].stem(tc,xc)
axs[1].stem(tc,yc)
axs[2].stem(tc,zc)

axs[0].plot(t,xt)
axs[1].plot(t,yt)
axs[2].plot(t,zt)

plt.savefig('Lab1Ex1c.pdf')
plt.show()