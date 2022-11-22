import numpy as np
import matplotlib.pyplot as plt

#computing 4 point dft
N=4
D=np.empty((N,N),dtype=np.cdouble)
W=np.exp(-1j*2*np.pi/N)

for k in np.arange(N):
	for n in np.arange(N):
		D[k,n]=W**(k*n)
		
np.round(D)

#input signal
x=np.array([[1,2,3,4]]).T

X=D @ x
np.round(X)

print("x= ",x)
print(f"{N} point dft of x ={X}")

mag_x=abs(X)
phase_x=[np.arctan(s.imag/s.real) for s in X]


#magnitude spectrum
plt.stem(mag_x)
plt.xticks()
plt.title("magnitude spectrum of X")
plt.savefig("e3dft_magnitude_spectrum.png")
plt.show()