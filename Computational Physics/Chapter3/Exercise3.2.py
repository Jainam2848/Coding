import numpy as np
import math
import matplotlib.pyplot as plt

# deltoid curve
theta = np.linspace(0,360)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)
print(x,y)
plt.plot(x,y)
plt.title('Deltoit Curve')
plt.show()

# Galilean spiral
theta2 = np.linspace(0,1800)
x2 = (theta2**2)*np.cos(theta2)
y2 = (theta2**2)*np.sin(theta2)
plt.plot(x2,y2)
plt.title('Galilean spiral')

plt.show()

#feys curve
theta3 = np.linspace(0,4320)

r = np.e**(np.cos(theta3)) - 2*np.cos(4*theta) \
                            + np.sin(theta/12)**5
        
x3 = r*np.cos(theta3)
y3 = r*np.sin(theta3)                    

plt.plot(x3,y3)
plt.title('Feys Curve')

plt.show()
