import numpy as np
import sounddevice

t = np.arange(0, 3, 1 / 8000)
xa = np.sin(2 * np.pi * 400 * t)
xb = np.sin(2 * np.pi * 800 * t)

x = np.concatenate((xa, xb))
sounddevice.play(x, 8000)
sounddevice.wait()
