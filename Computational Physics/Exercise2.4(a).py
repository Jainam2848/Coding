import numpy as np

d = int(input("Enter Distance of planet :"))
v = float(input("Enter Velocty of spaceship :"))
c = 1
# t is stationary time
t = d/v
# T is Dilated time

a = v**2 /c
b = 1 - a
T = t* np.sqrt(b)
print("The time taken by spaceship is :", T, "light years")