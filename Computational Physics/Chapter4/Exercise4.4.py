import  numpy as np
N = 100
h = 2/N
x = np.linspace(-1,1,N)
print(x)
y = np.sqrt(1 - x**2)
print(y)
yk = sum(y)
I = h*yk
print('The value of integral is :', I)

