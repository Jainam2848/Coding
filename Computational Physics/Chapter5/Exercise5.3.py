import numpy as np
import math 
import matplotlib.pylab as plt


def f(t):
    return math.exp(-(t**2))

a = 0
N = 100
h = 0.0


for b in np.arange(0,3,0.1):
    h += (b-a)/N
    s = 0.5 *(f(a)+f(b))
    #print(h)
    
    for k in range(1,N):
        s+= f(a + k*h)
    c = h*s
    z = np.array([c])
    #print(z)
    y = np.arange(0, 3, 0.1)
    b = np.array([y])
    #print(b)
    plt.plot(z,b, linestyle='-.')
    plt.show()
