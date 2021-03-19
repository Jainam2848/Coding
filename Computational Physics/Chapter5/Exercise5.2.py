import numpy as np

def f(x):
    return x**4 - 2*x + 1

b = 2
a = 0
N = 10
h = (b-a)/N
s0 = (f(a) + f(b))
s1 = 0.0
s2 = 0.0
x = int(N/2)
for k in range(2, N,2):    #even
    s1 += 2*f( a+ k*h )
    
for k in range(1,N, 2):    #odd
    s2 += 4*f( a+ k*h )
    
s = (1/3)*h*(s0 + s1 + s2)   
print(s)
