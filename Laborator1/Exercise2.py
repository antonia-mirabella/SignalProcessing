import numpy as np
import matplotlib.pyplot as plt

def show(time, function, figureTitle, fileName):
    plt.figure()
    plt.plot(time, function)
    plt.title(figureTitle)
    plt.xlabel('time (s)') 
    plt.ylabel('func value') 
    plt.savefig(fileName)
    plt.show()

#  A

ta = np.arange(1600) / 8000 
x = np.sin(2 * np.pi * 400 * ta)

show(ta, x, "Sinusoidala cu 400 Hz, 1600 esantioane","Lab1Ex2a.pdf")

# B

tb = np.arange(0, 3, 1 / 8000)
x = np.sin(2 * np.pi * 800 * tb)

show(tb[:80], x[:80], "Sinusoidala cu 800 Hz, 3 secunde (zoomed in)","Lab1Ex2b.pdf")

#  C 

tc = np.linspace(0, 0.05, 5000)
x  = np.mod(240 * tc, 1) * 2 - 1

show(tc, x, "Sawtooth cu 240 Hz","Lab1Ex2c.pdf")

#  D

td = np.linspace(0, 0.05, 5000)
x = np.sign(np.sin(2 * np.pi * td * 300))

show(td, x, "Square cu 300 Hz","Lab1Ex2d.pdf")

semnal = np.random.rand(128,128)
plt.figure()
plt.title('Semnal 2D random') 
plt.savefig('Lab1Ex2f.pdf')
plt.imshow(semnal)

semnal = np.zeros((128, 128))
idx = np.arange(128)
semnal[idx, idx] = 1
semnal[idx, 127 - idx] = 1

plt.figure()
plt.imshow(semnal, cmap='gray')
plt.title('Semnal 2D in forma de X')
plt.savefig('Lab1Ex2e.pdf')
plt.show()