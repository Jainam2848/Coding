import matplotlib.pyplot as plt
from numpy import loadtxt

data = loadtxt('http://www-personal.umich.edu/~mejn/cp/data/sunspots.txt')

x = data[:,0]
y = data[:,1]
plt.xlabel("Number of months since january 1749")
plt.ylabel("Number of sunspots")
plt.title("Graph of Sunspots")
plt.grid(True)
plt.plot(x,y)
plt.show()