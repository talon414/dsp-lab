import numpy as np
import matplotlib.pyplot as plt

def dft(x,N):
	tf=np.empty((N,N),dtype=np.cdouble)
	for n in range(N):
		for k in range(N):
			tf[n,k]=np.exp(-1j*2*np.pi*n*k/N)
	return (tf @ np.reshape(x,(-1,1))).flatten()
	
def idft(x,N):
	tf=np.empty((N,N),dtype=np.cdouble)
	for n in range(N):
		for k in range(N):
			tf[n,k]=np.exp(-1j*2*np.pi*n*k/N)
	return np.round(np.conj(tf) @ np.reshape(x,(-1,1))).flatten()/N
	
#6
t=np.arange(-10,10,1/200)

x1=2*np.sin(20*np.pi*t)+np.cos(40*np.pi*t)+np.cos(60*np.pi*t)+0.5*np.sin(80*np.pi*t)

#plt.plot(t,x1)
#plt.show()
#X=np.fft.fft(x1)
X=dft(x1,len(x1))
N=len(X)
k=np.arange(N)
T=N/200
fq=k/T

plt.plot(fq,abs(X))
plt.show()

plt.phase_spectrum(X)
plt.show()
