import numpy as np

# writing a function to calculate the escape velocity

G  = 6.673e-11  #gravitational constant, unit-Nm**2/kg**2

c =  299792458  #meter/second

M = float(input("Enter mass of Object in kg :"))
r = float(input("Enter radius of object in meter :"))

def escape_velocity(M,r):
    
    return np.sqrt(2*G*M/r)

# writing a function to calculate the schwarzchild radius

# will calculate distance if event horizon from center

def s_radius(M):
    return 2*G*M/c**2







