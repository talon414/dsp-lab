import numpy as np
from fft import *

def ifft(x):
	n = len(x)
	if n==1:
		return x
	else:
		xe=ifft(x[::2])
		xo=ifft(x[1::2])
		fac=np.exp(2j*np.pi*np.arange(n)/n)
		
		X=np.concatenate((xe+fac[:int(n/2)]*xo,xe+fac[int(n/2):]*xo))
	return X
	
def IFFT(x):
	return ifft(x)/len(x)
		
print(IFFT(FFT(np.arange(1,9))))
