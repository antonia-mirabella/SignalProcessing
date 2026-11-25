import numpy as np
import matplotlib.pyplot as plt

# Download latest version
# path = kagglehub.dataset_download("lampubhutia/bullettrain-timeseries-data")

# print("Path to dataset files:", path)

x = np.genfromtxt('1/Train.csv', delimiter=',', skip_header=1, usecols=2)

# Ex a -> 1 per hour => freq = 1 / 3600 Hz = 0.0002777777777777778 Hz
# #x b -> 18288 / 24 = 762.0 days
# Ex c (Nyquist) 0.0002777777777777778 / 2 = 0.0001388888888888889 Hz


thours = np.arange(18288)

X = np.fft.fft(x)
X = abs(X / 18288)
X = X[:int(18288 / 2)]

freq = 1 / 3600 # Hz
f = freq * np.arange(18288 // 2) / 18288 

fig, axs = plt.subplots(2, figsize=(10, 8))

axs[0].plot(thours, x, label ='Signal over hours')
axs[1].plot(f, X, label = 'Fourier Spectrum')

for ax in axs:
    ax.legend(loc='upper left')

plt.savefig('Lab5Exc.pdf')
plt.show()

#  from the graph we can see the larger value at 0Hz which is the DC component by eliminating the mean from the signal
meanx = np.mean(x)
y = x - meanx
Y = np.fft.fft(y)
Y = abs(Y / 18288)
Y = Y[:int(18288 / 2)]

fig, axs = plt.subplots(3, figsize=(10, 8))
axs[0].plot(thours, y, label ='Signal over hours')
axs[1].plot(f, Y, label = 'Fourier Spectrum')
axs[2].plot(f[:12], Y[:12], label='Removed DC offset')

for ax in axs:
    ax.legend(loc='upper left')

plt.savefig('Lab5Exd.pdf')
plt.show()

#  f top values

def top_values(s, f):
    idx = np.argsort(s)[-4:][::-1]
    return s[idx], f[idx]

vals, freqs = top_values(Y, f)

for v, fr in zip(vals, freqs):
    hours = 1 / (fr * 3600)
    print(f"absolute Y = {v:.2f} at {fr:.3e} Hz, period = {hours:.1f} hours = {hours / 24:.2f} days")

# 24 days - > daily traffic, higher in the day
# 762 days ~ 381 * 2 ~ 254 * 3 is the growth trend

#  g 
start = 48 + 168 * 6 # Monday midnight is at sample 48, and then 168 hours each week, 6 * 168 > 1000
stop = start + 720
t_month = (np.arange(start, stop) - start) / 24 

plt.plot(t_month, x[start:stop], label = 'Traffic over the sixth month')
plt.xticks(np.arange(0, 31, 7))
plt.xlabel('Days')

plt.savefig('Lab5MonthlyTraffic.pdf')
plt.show()


#  h
# 1. Would want to substract the growth with an average over the span of 7 days to get ~762/7=109 aligned weeks in total
# 2. Then , looking at traffic over 24 hours, set the 'starting point' of each day at the average lowest value (lower traffic at night)
# 3. For each day, separated according to 2, sum the traffic and fold them modulo 7 out of those 109 weeks to get an average for each 'unknown day' getting
#  5 higher days (weekdays) and 2 lower days (weekends). The first lower day is Saturday, then Sunday, and Monday.

#  this solution is really dependent on steps 2 'starting point' since it can be the time that traffic is at its lowest may differ from week to week 
#  and may not even be at midnight, but a few hours later. Also edge cases such as holidays break the pattern

#  i
# using 24h to remove components with a frequency shorter than 24h
kmax = 18288 // 24

Z = np.fft.fft(x)
Z[kmax + 1 : 18288 - kmax] = 0

xf = np.real(np.fft.ifft(Z)) 

Xf = abs(Z / 18288)
Xf = Xf[:int(18288 / 2)]

fig, axs = plt.subplots(2, figsize=(10, 8))
axs[0].plot(thours, x, label='Original signal')
axs[0].plot(thours, xf, label='Filtered signal')
axs[1].plot(f, Xf, label='Filtered spectrum')

for ax in axs:
    ax.legend(loc='upper left')

plt.savefig('Lab5Exi.pdf')
plt.show()