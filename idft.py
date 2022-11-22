import numpy as np


def idft1_sum(k,x,N):
	xi=0
	for n in range(N):
		xi+=x[n] * np.exp(1j*2*np.pi*n*k/N)
	return xi
	
def idft1(x,N):
	res=np.zeros(len(x),dtype=np.cdouble)
	for k in range(N):
		res[k]=idft1_sum(k,x,N)
	return np.round(res)/N
	
def idft2(x,N):
	tf=np.empty((N,N),dtype=np.cdouble)
	for n in range(N):
		for k in range(N):
			tf[n,k]=np.exp(-1j*2*np.pi*n*k/N)
	return np.round(np.conj(tf) @ np.reshape(x,(-1,1))).flatten()/N
	
k=idft1(np.arange(1,9),8)
print(k)
