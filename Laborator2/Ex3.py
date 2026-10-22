import numpy as np
import scipy.io.wavfile
# import scipy.signal
import sounddevice


# A
ta = np.arange(0, 3, 1 / 8000)
xa = np.sin(2 * np.pi * 400 * ta)
sounddevice.play(xa, 8000)
sounddevice.wait()


# B
tb = np.arange(0, 3, 1 / 8000)
xb = np.sin(2 * np.pi * 800 * tb)
sounddevice.play(xb, 8000)
sounddevice.wait()


# C
tc = np.arange(0, 3, 1 / 100000)
xc = np.mod(240 * tc, 1) * 2 - 1
sounddevice.play(xc, 100000)
sounddevice.wait()


# D
td = np.arange(0, 3, 1 / 100000)
xd = np.sign(np.sin(2 * np.pi * td * 300))

rate = int(100000)
scipy.io.wavfile.write('Lab2Ex3d.wav', rate, xd)

rate, xd_read = scipy.io.wavfile.read('Lab2Ex3d.wav')
sounddevice.play(xd_read, rate)
sounddevice.wait()
