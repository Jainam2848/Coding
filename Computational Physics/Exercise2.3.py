import numpy as np

x = float(input("Enter cartesian abssicca :"))
y = float(input("Enter cartesian ordinate :"))

r = np.sqrt(x**2 + y**2)
Theta = np.arctan(y/x)

print("The polar co-ordinates are :", r,"and", Theta)