from vpython import *

display(width = 1300, height =1000)
projectile = sphere(pos=vector(-5,0,0),radius=0.5, color=color.white,
                    make_trail = True)
 
projectile.mass = 1
projectile.angle = 45*3.1414/180
projectile.speed = 10
projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                             projectile.speed*sin(projectile.angle),0)
grav_acceleration = 9.8
dt=0.01
time = 0

while (projectile.pos.y >=0):
    rate(100)
# calculate force
    grav_force = vector(0, -projectile.mass*grav_acceleration,0)

# velocity after ejection

    projectile.velocity = projectile.velocity + grav_force/projectile.mass*dt

# position after ejection

    projectile.pos = projectile.pos + projectile.velocity*dt

# update time

    time = time + dt

