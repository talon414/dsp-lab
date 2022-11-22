import numpy as np
import matplotlib.pyplot as plt

def lincon(x,h):
	l1=len(x)-1
	l2=len(h)-1
	x=np.append(x,np.zeros(l2))
	h=np.append(h,np.zeros(l1))
	res=np.zeros((len(x),len(x)))
	
	r1=np.append(h[0],h[1::][::-1])
	for i in range(len(x)):
		res[i]=r1
		r1=np.roll(r1,1)
		
	return (res @ np.reshape(x,(-1,1))).flatten()

def correl(x1,x2):
	l1=len(x1)
	l2=len(x2)
	
	if l1>l2:
		x2=np.append(x2,np.zeros(l1-l2))
	elif l2>l1:
		x1=np.append(x1,np.zeros(l2-l1))
		
	x2=x2[::-1]
	
	return lincon(x1,x2)
	
	
x1=np.array([3,2,1,1])
x2=np.array([1,-1,1])

kel=correl(x2,x1)
kel1=np.correlate(x2,x1,"full")

print(kel)
print(kel1)
'''	
plt.stem(kel)
plt.show()
plt.stem(kel1)
plt.show()
'''
