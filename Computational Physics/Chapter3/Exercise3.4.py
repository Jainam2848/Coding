import vpython as v

# 3.4 (a)
L = 5
R = 0.3
count = 1
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if count % 2 == 0:
                v.sphere(pos=v.vector(i, j, k), radius=R,  color=v.color.red)
            else:
                # chlorine
                v.sphere(pos=v.vector(i, j, k), radius=R, color=v.color.blue)
            count += 1

        print(i, j, k)
