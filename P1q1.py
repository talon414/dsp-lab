import numpy as np
import matplotlib.pyplot as plt

def convol(x,h):
	l1=len(x)-1
	l2=len(h)-1
	x=np.append(x,np.zeros(l2,dtype=np.intc))
	h=np.append(h,np.zeros(l1,dtype=np.intc))
	res=np.zeros((len(x),len(x)))
	
	r1=np.append(h[0],h[1::][::-1])
	for i in range(len(x)):
		res[i]=r1
		r1=np.roll(r1,1)
		
	return (res @ np.reshape(x,(-1,1))).flatten()
	
x=[1,2,3]
h=[1,1,1,1]

print(convol(x,h))
print(np.convolve(x,h))
