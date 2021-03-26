# Question (a): Solving the integral representation of a Bessel function of the first kind

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# set up Bessel integral to be called later for calculation


def f(m, x, theta):

    return (1.0/np.pi) * np.cos(m * theta - x * np.sin(theta))

# set up a the Bessel function integral in a separate function


def Bessel(m, x):

    # set up limits and steps
    a = 0.0
    b = np.pi
    N = 1000
    h = (b - a)/(N)

    # write out theta range
    theta = np.arange(a+h, b, h)

    # use function for the Bessel integral and theta range
    y = sum(f(m, x, theta))

    # return the entire integral solution
    return 0.5 * h * (f(m, x, a) + f(m, x, b)) + h * y


# set up initial values for x range
x1 = 0.0
x2 = 10.0
N = 10000
h = (x2 - x1)/N

# set up arrays
x = np.empty(N+1)
bessel_func1 = np.empty(N+1)
bessel_func2 = np.empty(N+1)
bessel_func3 = np.empty(N+1)

# prepare for accuracy checks
print('Bessel functions J_0(x), J_1(x), J_2(x): ')

# for loop to calculate all of the integral slices
for i in range(N+1):
    x[i] = x1 + i*h
    bessel_func1[i] = Bessel(0.0, x[i])
    bessel_func2[i] = Bessel(1.0, x[i])
    bessel_func3[i] = Bessel(2.0, x[i])

# check for accuracy of program
    if i % 1000 == 0:
        print(f"x = {x[i]:1.1f}, J_0(x) = {bessel_func1[i]:1.6f}, J_1(x) = {bessel_func2[i]:1.6f}, J_2(x) = {bessel_func3[i]:1.6f}")

# set up plot
figure = plt.figure(figsize=(10, 5), dpi=200)
ax = plt.axes()
ax.axis([0, 10, -1.2, 1.2])
ax.set_xlabel('x')
ax.set_ylabel('J(x)')
ax.set_title('Bessel Functions of the First Kind')

# plot the three Bessel functions and set a legend
ax.plot(x, bessel_func1, '-b', label='m = 0')
ax.plot(x, bessel_func2, '-r', label='m = 1')
ax.plot(x, bessel_func3, '-g', label='m = 2')
leg = ax.legend()

# Question (b): Density plot of diffraction pattern

# set initial variables
k = (2.0 * np.pi)/0.5  # using 0.5 microns as the wavelength
r1 = 0.0  # 0 microns (starting point in r)
r2 = 1.0  # 1 micron (ending point in r)
N = 500
h = (r2 - r1)/N

# set up array
intensity = np.empty([N+1, N+1])

# use two for loops to generate the Bessel functions and intensity values
for i in range(N+1):
    x = h*(i - N/2)

    for j in range(N+1):
        y = h*(j - N/2)
        r = np.sqrt(x**2.0 + y**2.0)  # define a radius using distance formula

        if r == 0.0:
            intensity[i, j] = 0.5
        else:
            intensity[i, j] = (Bessel(1, k*r)/(k*r))**2.0

# plot the intensity on a density plot
sns.set_style("dark")
figure = plt.figure(figsize=(5, 5), dpi=200)
ax2 = plt.axes()
ax2.set_xlabel('x ($\mu m$)')
ax2.set_ylabel('y ($\mu m$)')
ax2.set_title('Intensity Diffraction Pattern')
plt.imshow(intensity, vmax=0.01, cmap='hot')
plt.savefig("Rings.pdf")
plt.show()
