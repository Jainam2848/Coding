from vpython import *
import numpy as np
import math

display(width = 13000, height =10000)
sun = sphere(pos=vector(0, 0, 0), mass = 1000, radius=1.5, color=color.yellow)
G = 1   
class planets():    
    mercury = sphere(pos=vector(-5, 0, 0),  mass = 4 , radius=0.1, velocity = vector(5,10,0), color=color.orange)
    venus   = sphere(pos=vector(-10, 0, 0), mass = 10 ,radius=0.3, color=color.blue)
    earth   = sphere(pos=vector(0, 13, 0) , mass = 15, radius=0.5, color=color.red)

    def grav_force(planets, sun):
    # force on planets by sun
    # F = m1*m2/r**2
        G = 1
        r_vector = planets.pos-sun.pos
        r_mag = mag(r_vector)
        r_unit = r_vec/r_mag  # r caret
        force_mag = G*planets.mass*sun.mass/r_mag**2
        force_vec = -force_mag*r_unit #force is attractive
    
        return force_vec
    def move():
        pass
        
        #v = sqrt(G*sun.mass/planets.radius)
#radius = planets()
    #planets.v = math.sqrt(G*sun.mass/planets.radius)
dt = 0.1
t = 0
while (True):
    rate(50)