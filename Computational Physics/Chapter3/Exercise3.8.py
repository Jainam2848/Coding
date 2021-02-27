import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('http://www-personal.umich.edu/~mejn/cp/data/millikan.txt', float)
x = data[:, 0]
y = data[:, 1]
N = x.size

Ex = 1/N * sum(x)
Ey = 1/N * sum(y)
Exx = 1/N * sum(x**2)
Exy = 1/N * np.dot(x, y)
m = (Exy - Ex * Ey)/(Exx - Ex**2)
c = (Exx * Ey - Ex * Exy)/(Exx - Ex**2)

y1 = np.empty(N, float)
for i in range(0, N):
    y1[i] = m * x[i] + c
 
e = 1.602e-19
#h = m*e
#print(m)
#print(y)

print(f"estimated value for h = {m * e} J s")

plt.plot(x, y, 'ko')
plt.plot(x, y1, 'k')
plt.xlabel(" (Hz)")
plt.ylabel("Voltage (V)")
plt.show()