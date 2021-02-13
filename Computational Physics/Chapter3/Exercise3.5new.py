from vpython import *
import numpy as np
import math 

sun = sphere(pos=vector(0, 0, 0) , radius=1.8, color=color.yellow)

Mercury = sphere(pos = vector(5,0,0), radius = 0.6, color = color.green, make_trail = True)
Venus = sphere(pos=vector(10, 0, 0) , radius=0.6, color=color.magenta, make_trail = True)
Earth = sphere(pos=vector(15, 0, 0) , radius=0.9, color=color.blue, make_trail = True)
Mars = sphere(pos=vector(20, 0, 0) ,radius=0.7, color = color.red, make_trail = True)
Jupiter = sphere(pos=vector(25, 0, 0) ,radius=1.1, color = color.orange, make_trail = True)
Saturn = sphere(pos=vector(30, 0, 0) ,radius=1.0, color = color.brown, make_trail = True)


Mercuryomega = 2*3.14159/88
Vomega       = 2*3.14159/255
Eomega       = 2*3.14159/365
Marsomega    = 2*3.14159/687
Jupiteromega = 2*3.14159/4330
Saturnomega  = 2*3.14159/10756

while True:
    rate(50)
    Mercury.rotate(angle = Mercuryomega,  axis = vector(0,0,1),origin = vector(0,0,0))
    Venus.rotate(angle = Vomega,  axis = vector(0,0,4),  origin = vector(0,0,0))
    Earth.rotate(angle = Eomega,  axis = vector(0,0,7), origin = vector(0,0,0))
    Mars.rotate(angle = Marsomega,  axis = vector(0,0,9),origin = vector(0,0,0))
    Jupiter.rotate(angle = Jupiteromega,  axis = vector(0,0,13),origin = vector(0,0,0))
    Saturn.rotate(angle = Saturnomega,  axis = vector(0,0,17),origin = vector(0,0,0))
