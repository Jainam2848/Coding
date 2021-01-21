import matplotlib.pylab as plt
from numpy import loadtxt
data = loadtxt('http://www-personal.umich.edu/~mejn/cp/data/stm.txt',float)
plt.title(" Structure of Silicon Surface")
plt.imshow(data)
plt.show()
