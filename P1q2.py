import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-10,11)
x=np.zeros_like(n)
x[n>-11]=0
x[n>-5]=1
x[n>8]=0
z=2*x+np.roll(x,-1)+0.5*np.roll(x,-2)

plt.stem(n,z)
plt.xticks(n)
plt.show()
'''
plt.stem(n,np.roll(x,-1))
plt.xticks(n)
plt.show()
'''
