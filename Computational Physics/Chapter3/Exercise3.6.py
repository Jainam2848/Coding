import matplotlib.pylab as plt
from numpy import arange

def logistic_map(r,x=1./2,n=1000):
	for i in range(n):
		x = r*x*(1-x)
	return x
	
r = arange(1,4,0.01)
x = logistic_map(r)

plt.plot(r,x,'k.')
plt.xlabel('r')
plt.ylabel('x')
plt.title("Chaos and the Feigenbaum plot")