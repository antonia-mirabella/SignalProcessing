import matplotlib.pyplot as plt
import numpy as np

# t = np.arange(1000) / 2000
t = np.arange(0, 1, 1/1000)
x = np.cos(2*np.pi* 25 * t) + np.sin(2*np.pi* 55 * t) + np.cos(2*np.pi* 40 * t)
N = len(x); n = np.arange(N)  # noqa: E702

X = np.array([np.sum(x * np.e ** (-2 * np.pi *1j * m * n /N )) for m in range(N)])

# print(np.allclose(X, np.fft.fft(x)))
#  A
fig, axs = plt.subplots(2)

axs[0].plot(t, x)
axs[0].set_xlabel('timp (s)')
axs[0].set_ylabel('x')

freqs = np.arange(N) * 1000 / N

axs[1].stem(freqs[:100], np.abs(X[:100]))
axs[1].set_xlabel('frecventa (Hz)')
axs[1].set_ylabel('|X|')

plt.savefig('Lab3Ex3.pdf')
plt.show()


# B
