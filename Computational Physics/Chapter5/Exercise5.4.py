import numpy as np
import matplotlib.pylab as plt
np.seterr(divide='ignore', invalid='ignore')

# part(a)


def J(m, x):

    def f(teta):
        return np.cos(m*teta - x*np.sin(teta))

    N = 1000
    a = 0.0
    b = np.pi
    h = (b-a)/N

    s = f(a) + f(b) 
    for k in range(1, N//2):
        s += 4*f(a + (2*k-1)*h) + 2*f(a+2*k*h)
    # print(s)
    j = h/3*s/np.pi
    # print(I)
    return j


x = np.linspace(0, 20)

plt.plot(x, J(0, x), label='J0')
plt.plot(x, J(1, x), label='J1')
plt.plot(x, J(2, x), label='J2')
plt.legend(("$J_0$", "$J_1$", "$J_2$"))
plt.show()

# part(b)

lamda = 500e-9
k = 2*np.pi/lamda
r = np.linspace(0, 1e-6)
I = (J(1, r*k)/k/r)**2
print(len(I))
I2 = np.reshape(I, (2,25))
#data = np.array([r, I])

plt.plot(I2)

#plt.imshow(I2)
plt.title(" Diffraction")
plt.show()











