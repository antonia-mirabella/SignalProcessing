import numpy as np
import matplotlib.pyplot as plt


# F8 = [[] for k in range(8)]

# for m in range(8):
#     for k in range(8):
#         F8[m].append(np.cos(2 * np.pi * m * k) - 1j * np.sin(2 * np.pi * m * k))

# for m in range(8):
#     for k in range(8):
#         print(F8[m][k])
#     print()

Fourier8 = np.array([[np.cos(2 * np.pi * m * k / 8) - 1j * np.sin(2 * np.pi * m * k / 8) for k in range(8)] for m in range(8)], dtype=complex)
Fourier8 = np.divide(Fourier8, np.sqrt(8))


fig, axs = plt.subplots(8, sharey=True)
duration = np.linspace(0, stop=8, num=8)

axs[0].set_ylim(-2,2)
for i in range(8):

    axs[i].plot(duration, Fourier8[i].real, color = 'purple')
    axs[i].plot(duration, Fourier8[i].imag, linestyle='--', color = 'orange')

plt.tight_layout()
plt.savefig('Real & Imaginary Fourier 8.pdf')
plt.show()



# for m in range(8):
#     for k in range(8):
#         print(Fourier8[m][k])
#     print()

# IFourier8 = np.linalg.inv(Fourier8)

Fh = np.conjugate(Fourier8).T

# for m in range(8):
#     for k in range(8):
#         print(IFourier8[m][k])
#     print()

print(f'Is Fourier for N=8 unitary? : {np.allclose(Fourier8@Fh, np.eye(8))}')