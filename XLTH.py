import math as m
import numpy as np
a=[1,1,1,0,0,0,0,0,0,0]
N=input('Nhap N:')
N=int(N)
for i in range(N):
    s=s+m.cos(2*m.pi*i/N)