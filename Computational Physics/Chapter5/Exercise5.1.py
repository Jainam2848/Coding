import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('http://www-personal.umich.edu/~mejn/cp/data/velocities.txt', float)

t = data[:, 0]
v = data[:, 1]

def f(x):
    f = v*t
    return f

    
n = 10   #number of slices
b = 100    #upper limit
a = 0      #lower limit
h = (b-a)/n

s = 0.5*f(a) + 0.5*f(b)

for k in range(1,n):
    s+= f(a+h*k)
print(h*s)
plt.plot(v,s)