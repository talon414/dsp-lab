import numpy as np
import matplotlib.pyplot as plt

def signal(t):
	return np.sin(20*np.pi*t)+np.cos(30*np.pi*t)+np.sin(80*np.pi*t)

def wind(a,n):
	return a-(1-a)*np.cos(2*np.pi*n/100)
	
def sincf(t):
	return np.sinc(2*np.pi*t)
	
def build_fil(a,n,t):
	h= wind(a,n) * sincf(t)
	return h/h.sum()

#t=np.linspace(-10,10,100)
#plt.xticks(t)
t1=np.arange(0,1,1/200)

#plt.plot(t,signal(t))
#plt.show()

plt.stem(t1,signal(t1))
plt.show()

X=np.fft.fft(signal(t1))

plt.plot(t1,abs(X @ build_fil(0.54,np.arange(100),t1)))
plt.show()

