import numpy as np
import matplotlib.pyplot as plt

#overlap add method
      

def overlap_add(x,h):

    M=len(h)
    L=M
    N=L+M-1
    x=np.append(x,np.zeros(M-1))
    h=np.append(h,np.zeros(M-1))
    j=np.array_split(x,M-1)
    y=[]
    for i in j:
        i=np.append(i,np.zeros(M-1))
        y.append(circular_convolution(i,h))

    for i in range(len(y)-1):
        u=np.array(y[i][0:M])
        v=np.array(y[i][M:M+2])
        e=np.array(y[i+1][0:M-1])
        t= np.concatenate((u,np.add(v,e),np.array(y[i+1][M-1:M+2])),axis=0)

    req_len=len(x)+M-1
    if len(t)==req_len:
        return t
    elif len(t)>req_len:
        index=[r for r in range(req_len+1,len(t))]
        t=np.delete(t,index)
        return t

x=np.array([1,2,3,4])
h=np.array([1,1,1])
print(overlap_add(x,h))