import numpy as np
import matplotlib.pyplot as plt
import time

vec = [128, 256, 512, 1024, 2048, 4096, 8192]

def fft(x):
    m = len(x)
    if m == 1:
        return x

    x_even = fft([x[k] for k in range(0, m, 2)])
    x_odd = fft([x[k] for k in range(1, m, 2)])
    
    X = np.zeros(m, dtype=complex)
    for i in range(m // 2):
        w = np.e ** (-2j * np.pi * (i/m)) * x_odd[i]
        X[i] = x_even[i] + w
        X[i+ (m//2)] = x_even[i] - w
    
    return X

def dft(x, n):
    # DFourier = np.array([[np.cos(2 * np.pi * m * k / n) - 1j * np.sin(2 * np.pi * m * k / n) for k in range(n)] for m in range(n)], dtype=complex)
    # X = DFourier @ x
    
    # return X
    k = np.arange(n)
    M = np.exp(-2j * np.pi * np.outer(k, k) / n)
    return M @ x


t_fft = []
t_np = []
t_dft = []

for n in vec:
    t = np.arange(n) / 100
    x = np.sin(2 * np.pi * 5 * t)

    start = time.process_time()
    X = fft(x)
    t_fft.append(time.process_time() - start)

    start = time.process_time()
    X_np = np.fft.fft(x)
    t_np.append(time.process_time() - start)
    
    start = time.process_time()
    dft(x,n)
    t_dft.append(time.process_time() - start)
    

plt.figure(figsize=(8, 5))
plt.plot(vec, t_fft, 'o-', label='own FFT implementation')
plt.plot(vec, t_np, 's-', label='numpy.fft.fft method')
plt.plot(vec, t_dft, 'D-', label='own DFT implementation')
plt.xscale('log', base=2)
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Execution time (s)')
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('Lab4Ex1.pdf')
plt.show()
