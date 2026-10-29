import numpy as np
import matplotlib.pyplot as plt


time = np.arange(1000) / 2000
omega = 2 * np.pi * 12
x = (1/3) * np.sin(omega * time + 4/5)
samples = np.arange(len(x))

# Fig 1

n = np.linspace(0,1,num=1000)
y = x * np.e**(-2 *np.pi*1j*n)

fig, axs = plt.subplots(2)

# axs[0].plot(samples, x)
sc = axs[0].scatter(samples, x, c=np.abs(x), cmap='gist_rainbow')
fig.colorbar(sc, ax=axs[0], label='distanta')
axs[0].set_xlabel('timp masurat in esantioane')
axs[0].set_ylabel('amplitutdine')

# axs[1].plot(y.imag, y.real)
sc = axs[1].scatter(y.imag, y.real, c=np.abs(y), cmap='magma')
fig.colorbar(sc, ax=axs[1], label='distanta')
axs[1].set_xlabel('imaginar')
axs[1].set_ylabel('real')



plt.tight_layout()
plt.savefig('Lab3Ex2CercUnitateComplex.pdf')
plt.show()

# Fig 2

fig, axs = plt.subplots(4, figsize=(6,12))
for i,m in enumerate([1, 2, 5, 7]):
    z = x * np.e**(-2*np.pi*1j*m*n)
    axs[i].set_title(f'omega = {m}')
    axs[i].plot(z.imag, z.real)

    axs[i].set_xlim(-0.35, 0.35)
    axs[i].set_ylim(-0.35, 0.35)

plt.tight_layout()
plt.savefig('Lab3EEx2DiffOmega.pdf')
plt.show()

#  Animatie
import matplotlib.animation as animation  # noqa: E402

fig, axs = plt.subplots(4, figsize=(6, 12))
lines, zs = [], []
for i, m in enumerate([1, 2, 5, 7]):
    z = x * np.e**(-2*np.pi*1j*m*n)
    zs.append(z)

    ax = axs[i]
    ax.set_aspect('equal')
    ax.set_title(f'omega = {m}')
    ax.set_xlim(-0.35, 0.35)
    ax.set_ylim(-0.35, 0.35)

    line, = ax.plot([], [])
    lines.append(line)

def update(frame):
    for line, z in zip(lines, zs):
        line.set_data(z[:frame].imag, z[:frame].real)
    return lines

anim = animation.FuncAnimation(fig, update, frames=len(n), interval=10, blit=True)
plt.show()
anim.save('Lab3Ex2Animatie.gif', writer='pillow')
