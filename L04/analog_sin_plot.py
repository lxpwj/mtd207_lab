from numpy import linspace, sin, pi, absolute
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

# Sampling rate
fs = 100  # Hz
# the total lenght of the wave
length = 1  # 2 second
N = int(fs * length)
# time
t = linspace(0, length, num=N, endpoint=False)

# Generate a sinusoid at frequency f
f = 10  # Hz
f2 = 30  # Hz
#a = 5*sin(2 * pi * f * t)
a = 2* sin(2 * pi * f * t) + 2/3*sin(2 * pi * f2 * t)

# Plot signal, showing how endpoints wrap from one chunk to the next
plt.subplot(2, 1, 1)
plt.plot(t, a, '.-')
plt.plot(1, 1, 'r.')  # first sample of next chunk
plt.margins(0.1, 0.1)
plt.xlabel('Time [s]')
plt.axhline()
plt.axvline()
plt.axvline(x=1/f, c='r', marker=".")

# Use RFFT to get the amplitude of the one-sided spectrum
ampl = 1/N * absolute(rfft(a))
# RFFT frequency bins
freqs = rfftfreq(N, 1/fs)
# Plot spectrum
plt.subplot(2, 1, 2)
plt.stem(freqs, ampl)
plt.margins(0.1, 0.1)
plt.xlabel('Frequency [Hz]')
plt.tight_layout()
plt.show()


# Question 1:
# think about how to plot sum of two sine waveform
#

# Solution:
# uncomment Line 17, change f and f2 to get different results
