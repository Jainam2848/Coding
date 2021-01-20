import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('http://www-personal.umich.edu/~mejn/cp/data/sunspots.txt')

x = data[:,0]  #months
y = data[:,1]  #sunspots
plt.xlabel("Number of months since january 1749")
plt.ylabel("Number of sunspots")
plt.title("Graph of Sunspots")
plt.grid(True)
plt.plot(x,y)
plt.show()

#part b and c

x,y = data[:1000,0], data[:1000,1]
#plt.plot(x,y)
r = 5
a = [sum(y[k-r:k+r]) for k in range(1000)]
c = np.array(a)
b = c/(2*r)

plt.plot(x,y,'g.')
plt.plot(x,b, label = 'average')
plt.show

