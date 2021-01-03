import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
from array import array

# Graph of Average temperature vs years.

data = np.loadtxt("Temperature.txt")
x = data[:, 0]  # Years
y = data[:, 1]  # Average temperature

plt.xlabel("Years")
plt.ylabel("Average Temperature")
plt.title("Graph of Average Temperature since 1880")
plt.grid(True)
plt.plot(x, y)

plt.show()

# Graph of sunspots vs years

Data = np.loadtxt('sunspot.txt')
a = Data[:, 0]
b = Data[:, 1]

plt.xlabel("Number of years")
plt.ylabel("Number of sunspots")
plt.title("Graph of Sunspots")
plt.grid(True)
plt.plot(a, b)
plt.show()

# Graph of sunspots vs temperature

plt.xlabel("Temperature")
plt.ylabel("Sunspots")
plt.title("Effect of sunspots on Global average Temperature")
plt.grid(True)
plt.plot(y, b[:140], 'k.')
plt.show()

# 3D plot of temperature and sunspots as a function of years.
