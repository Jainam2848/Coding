from vpython import *
import numpy as np
import time

display(width = 1300, height = 1000)

MagneticField = 1e-5*vector(0,0,-5)

Electron = sphere(pos = vector(-5,0,0), radius = 0.1, color =color.white, make_trail = True)

Electron.m = 9.1e-31
Electron.charge = -1.6e-19
Electron.v = 7.5e6
Electron.p = Electron.m*Electron.v*vector(0,3,0)


t = 0
dt = 1e-9

while t<1e-6:
    rate(10000)
      
    Force = cross(Electron.charge* Electron.p/ Electron.m, MagneticField)
    # update momentum
    Electron.p = Electron.p+ Force*dt
    #update position
    Electron.pos = Electron.pos + Electron.p*dt/Electron.m

    t = t+dt
    time.sleep(0.01)
                                                                                                                                              