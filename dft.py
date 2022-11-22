import numpy as np
import matplotlib.pyplot as plt

def dft1_sum(k,x,N):
	xi=0
	for n in range(N):
		xi+=x[n] * np.exp(-1j*2*np.pi*n*k/N)
	return xi
	
def dft1(x,N):
	res=np.zeros(len(x),dtype=np.cdouble)
	for k in range(N):
		res[k]=dft1_sum(k,x,N)
	return np.round(res)
	
def dft2(x,N):
	tf=np.empty((N,N),dtype=np.cdouble)
	for n in range(N):
		for k in range(N):
			tf[n,k]=np.exp(-1j*2*np.pi*n*k/N)
	return np.round(tf @ np.reshape(x,(-1,1))).flatten()
	
k=dft2(np.arange(1,5),4)
print(k)

plt.stem(np.arange(1,5),abs(k))
plt.show()

plt.stem(np.arange(1,5),np.angle(k))
plt.show()

