# Free fall
import numpy as np
h = float(input("Enter height of tower :"))
x = float(input("Enter height of ball :"))
g = 9.8
a = np.sqrt(h)
b = np.sqrt(g)
c = np.sqrt(2)
t = c*a/b

print("The time taken by ball is", t, )
