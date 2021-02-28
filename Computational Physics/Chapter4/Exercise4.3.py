import numpy as np

def f(x):
    f = x**2 - x
    return f

def derivatives(value_x, delta):
    x = value_x
    d = delta
    
    return (f(x+d)-f(x))/d


print(derivatives(1,1e-2))
print(derivatives(1,1e-4))
print(derivatives(1,1e-6))
print(derivatives(1,1e-8))
print(derivatives(1,1e-10))
print(derivatives(1,1e-12))
print(derivatives(1,1e-14))