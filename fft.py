import numpy as np

def FFT(x):
	N=len(x)
	if N==1:
		return x
	else:
		x_eve=FFT(x[::2])
		x_o=FFT(x[1::2])
		fac=np.exp(-2j*np.pi*np.arange(N)/N)		
		X=np.concatenate((x_eve+fac[:int(N/2)]*x_o,x_eve+fac[int(N/2):]*x_o))
	return X


#print(FFT([1,2,3,4]))
