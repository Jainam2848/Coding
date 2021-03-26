import numpy as np
import math
import matplotlib.pylab as plt


def f(t):
    return math.exp(-(t**2))


a = 0
N = 1000
h = 0.0

x = np.arange(0.0, 3.0, 0.1)
z = np.zeros(len(x))

for i in range(len(x)):
    b = x[i]
    h += (b-a)/N
    s = 0.5 * (f(a)+f(b))
    # print(h)

    for k in range(1, N):
        s += f(a + k*h)
    c = h*s
    z[i] = c
    print(z)
plt.plot(x, z, linestyle='-.')
plt.show()
