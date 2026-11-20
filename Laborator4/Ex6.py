import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv

def specto(signal):
    n = len(signal)
    group = int(0.01 * n)
    overlap = group // 2

    num = (n - group) // overlap + 1

    S = np.zeros((group // 2 + 1, num))
    for i in range(num):
        start = i * overlap
        segment = signal[start:start + group]
        S[:, i] = np.abs(np.fft.fft(segment))[:group // 2 + 1]

    return S

data = {}
for vowel in ['a', 'e', 'i', 'o', 'u']:
    fs, signal = wv.read(f"vocala_{vowel}.wav")
    data[vowel] = {'fs': fs, 'signal': signal.astype(float)}
    data[vowel]['specto'] = specto(data[vowel]['signal'])

fig, axs = plt.subplots(5, figsize=(8, 12))
fig.suptitle('Spectrograms of the vowels')


for ax, vowel in zip(axs, data):
    fs = data[vowel]['fs']
    t = len(data[vowel]['signal']) / fs
    S_db = 20 * np.log10(data[vowel]['specto'] + 1e-10)

    im = ax.imshow(S_db, origin='lower', aspect='auto',extent=[0, t, 0, fs / 2],vmin=S_db.max() - 80, vmax=S_db.max())
    ax.set_ylim(0, 5000)
    ax.set_xlim(0,0.5)
    ax.set_title(f'Vowel {vowel}')
    ax.set_ylabel('Freq (Hz)')
    fig.colorbar(im, ax=ax, label='dB')

axs[-1].set_xlabel('Time (s)')
fig.tight_layout()
fig.savefig('Lab4Ex6.pdf')
plt.show()
