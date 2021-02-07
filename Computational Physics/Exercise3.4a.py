import vpython as v
# 3.4 (a)
L = 1
R = 0.2
count = 1
for i in range(-2*L, 2*L+1):
    for j in range(-2*L, 2*L+1):
        for k in range(-2*L, 2*L+1):
            v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.green)
            if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
                v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.blue)
