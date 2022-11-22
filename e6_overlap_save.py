import numpy as np
import matplotlib.pyplot as plt

#overlap save method
def overlap_save(x,h):
    M=len(h)
    L=M
    N=L+M-1
    x=np.append(x,np.zeros(M-1))
    h=np.append(h,np.zeros(M-1))
    j=np.array_split(x,M-1)
    j[0]=np.insert(j[0],0,np.zeros(M-1))

    y=[]
    for i in range(1,len(j)):
        j[i]=np.insert(j[i],0,[x[i],x[i+1]])

    index=[u for u in range(M,N)]    
    for k in j:
        y=np.append(y,np.delete(circular_convolution(k,h),index))
        
    req_len=len(x)+M-1
    if len(y)<=req_len:
        return y
    elif len(y)>req_len:
        index=[r for r in range(req_len+1,len(y))]
        t=np.delete(y,index)
        return y

x=np.array([1,2,3,4])
h=np.array([1,1,1])
print(overlap_save(x,h))
