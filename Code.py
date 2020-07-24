from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
f1=200000
w1=2*np.pi*f1
B, A=signal.iirfilter(2, w1,   btype='low', analog=True, ftype='butter', output='ba')
w, h = signal.freqs(B,A)
plt.plot(w/2/3.14, 20 * np.log10(abs(h)) ,  color='red', linewidth=2)
plt.xscale('log')
plt.title('Butterworth 2nd Order Low Pass Filter',fontsize=20)
plt.xlabel('Frequency [Hz]', fontsize=20)
plt.ylabel('Amplitude [dB]', fontsize=20)
plt.margins(0, 0.01)
plt.grid(which='both', axis='both')
plt.yticks( size=20)
plt.xticks( size=20)
plt.axvline(f1, color='blue', linewidth=2)
plt.show()
print ("a=", A)
print ("b=", B)
