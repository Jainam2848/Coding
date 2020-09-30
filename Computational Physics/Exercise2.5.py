import numpy as np


m = 9.11e-31
# h is planks constant
E = float(input("Enter Kinetic energy (in ev):"))
v = float(input("Enter potential step (in ev) :"))
h = 6.626e-34
H = h/2*np.pi

k1 = np.sqrt(2*m/E)/H
k2 = np.sqrt(2*m*(E - v))/H

# probability of transmission is :
    
T = 4*k1*k2/(k1 + k2)**2

# probability of reflection is :

R = ((k1 - k2)/(k1 + k2))**2


print(f"The probability of Transmission is :{T}") 
print(f"The probability of Reflection is :{R}")

