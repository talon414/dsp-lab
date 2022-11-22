import numpy as np
import matplotlib.pyplot as plt

#computing 4 point idft
N=4
D=np.empty((N,N),dtype=np.cdouble)
W=np.exp(1j*2*np.pi/N)

for k in np.arange(N):
	for n in np.arange(N):
		D[k,n]=W**(k*n)
		
np.round(D)

#input signal
x=np.array([[10,-2+2j,-2,-2-2j]]).T

X=(D @ x)/N
np.round(X)

print("x= ",x)
print(f"{N} point idft of x ={X}")