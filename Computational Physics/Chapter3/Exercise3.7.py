import numpy as np
import matplotlib.pylab as plt
import functools

x, y = np.ogrid[-2:2:1000j, -2:2.5:1000j]

# More iterations means more clear image
iterations = 100

c = x + 1j*y

z = functools.reduce(lambda x, y: x**2 + c, [1] * iterations, c)

plt.figure(figsize=(10, 10))
plt.imshow(np.log(np.abs(z)));
plt.title("Mandelbrot set")
plt.gray()
plt.show()
