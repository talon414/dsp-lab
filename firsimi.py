import numpy as np
import matplotlib.pyplot as plt

def sincf(fc,M):
	return np.sinc(2*fc*(np.arange(M+1)-M/2))

def hamming(a,M):
	return a-(1-a)*np.cos(2*np.pi*np.arange(M+1)/M)
	
def filter(a,fc,M,wind=None):
	if wind is None:
		h=sincf(fc,M)
	else:
		h=sincf(fc,M)*wind(a,M)
	return h/h.sum()
fs=200
M=100
fc=0.2
t=np.arange(-10,10,1/fs)
x=np.sin(20*np.pi*t)+np.cos(30*np.pi*t)+np.sin(80*np.pi*t)
	
X=np.fft.fft(x)

frq=np.arange(len(X))*fs/len(X)

plt.stem(frq,abs(X))
plt.show()

yk1=np.fft.fft(np.convolve(x,filter(0.54,fc,M,wind=hamming)))
yk2=np.fft.fft(np.convolve(x,filter(0.35,fc,M,wind=hamming)))

frq1=np.arange(len(yk1))*fs/len(yk1)
frq2=np.arange(len(yk2))*fs/len(yk2)

plt.stem(frq1,abs(yk1))
plt.show()
plt.stem(frq2,abs(yk2))
plt.show()
