import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)
xsin = np.sin(alpha)

xtaylor = alpha
xpade = (alpha - 7 * alpha ** 3 / 60) / (1 + alpha ** 2 / 20)

eroaretaylor = np.abs(xsin - xtaylor)
eroarepade = np.abs(xsin - xpade)

#  A

plt.figure()
plt.plot(alpha, xsin, label='sin(x)')
plt.plot(alpha, xtaylor, label='x')
plt.title('sin(x) si x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('Lab2Ex8a.pdf')
plt.show()

#  B

plt.figure()
plt.plot(alpha, eroaretaylor)
plt.title('Eroarea dintre sin(x) si x')
plt.xlabel('alpha')
plt.ylabel('eroare')
plt.savefig('Lab2Ex8b.pdf')
plt.show()

#  C

fig, axs = plt.subplots(2)
fig.suptitle('sin(x) si aproximarea Pade')

axs[0].plot(alpha, xsin, label='sin(x)')
axs[0].plot(alpha, xpade, label='Pade')
axs[0].legend()

axs[1].plot(alpha, eroarepade, label='eroare Pade')
axs[1].legend()

axs[1].set_xlabel('alpha')

plt.savefig('Lab2Ex8c.pdf')
plt.show()

#  D

plt.figure()
plt.plot(alpha, eroaretaylor, label='eroare Taylor')
plt.plot(alpha, eroarepade, label='eroare Pade')
plt.yscale('log')
plt.title('Eroarea Taylor si Pade, axa Oy logaritmica')
plt.xlabel('x')
plt.ylabel('eroare')
plt.legend()
plt.savefig('Lab2Ex8d.pdf')
plt.show()
