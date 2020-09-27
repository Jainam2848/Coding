#Free fall
from numpy import *
h = float(input("Enter height of tower :"))
x = float(input("Enter height of ball :"))
g = 9.8
a = sqrt(h)
b = sqrt(g)
c = sqrt(2)
t = c*a/b

print("The time taken by ball is", t, )