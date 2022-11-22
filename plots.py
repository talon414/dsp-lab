import numpy as np
import matplotlib.pyplot as plt

def fx(t):
    return 4*(t**2)-1


x=np.arange(0,2*np.pi,0.5)
y=[np.sin(x) for x in x]

z=fx(x)

l=[1,2,3,4,5,6]
k=[1,25,65,6,10,40]


# plt.plot(x,y)

# plt.stem(x,y)

plt.stem(l,k)

#plt.stem(x,z)
plt.xticks()

#plt.grid()
plt.show()


