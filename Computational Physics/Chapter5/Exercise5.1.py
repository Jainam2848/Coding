import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt(
    'http://www-personal.umich.edu/~mejn/cp/data/velocities.txt', float)

t = data[:, 0]
v = data[:, 1]
#x = sum(v*t)


def f(v, t):
    return v * t


# print(x)
n = len(v)  # number of slices
b = 100  # upper limit
a = 0  # lower limit
h = (b - a) / n

s = 0.0
for k in range(n):
    print(v[k], t[k])
    s += f(v[k], t[k])

print(s)
plt.plot(t, v)
plt.show()
