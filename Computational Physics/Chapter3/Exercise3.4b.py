import vpython as v
import numpy as np

# 3.4 (b)
# Green -- the atoms on the lattices of the cube
# blue  -- the atoms on the face of the cube. Run this for small value such as 1 to see the cube
L = 3
R = 0.2
count = 1
for i in range(-2*L, 2*L+1):
    for j in range(-2*L, 2*L+1):
        for k in range(-2*L, 2*L+1):
            if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
                v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.green)
            if i % 2 != 0 and j % 2 != 0 and k % 2 == 0:
                v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.blue)
            if i % 2 != 0 and j % 2 == 0 and k % 2 != 0:
                v.sphere(pos=v.vector(i, j, k),
                         radius=R,  color=v.color.blue)
            if i % 2 == 0 and j % 2 != 0 and k % 2 != 0:
                v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.blue)
            count += 1

        #print(i, j, k)
