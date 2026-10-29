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

Fourier8 = np.array([[np.cos(2 * np.pi * (m * k) / 8) - 1j * np.sin(2 * np.pi * m * k) for k in range(8)] for m in range(8)], dtype=complex)

# Fnew = np.divide(Fourier8, 1/ (np.sqrt(8)))

for m in range(8):
    for k in range(8):
        print(Fourier8[m][k])
    print()

print('------------------------------------------------------------------------------------------------')

Fh8 = np.conjugate(Fourier8)

IFourier8 = np.linalg.inv(Fourier8)

for m in range(8):
    for k in range(8):
        print(IFourier8[m][k])
    print()