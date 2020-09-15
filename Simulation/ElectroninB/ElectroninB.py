from vpython import *
import numpy as np
import time

screen = display(title = "Motion of electron in magnetic field", width = 600, height = 200)

MagneticField = 5e-5*vector(0,-5,-5)

Electron = sphere(pos = vector(-5,0,0), radius = 0.1, color = color.red, make_trail = True)

Electron.m = 9.1e-31
Electron.charge = -1.6e-19
Electron.v = 7.5e6
Electron.p = Electron.m*Electron.v*vector(0,3,0)

running = False
def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"


bbutton = button(text="Run",pos=scene.title_anchor, bind=Run)


def Reset(c):
    global t, Electron
    t = 0
    Electron.pos = vector(-5,0,0)
    Electron.p = vector(0,0,0)
    Electron.make_trail = False
    Electron.radius = 0.1
    if Reset:screen.exit = True
cbutton = button(text="Reset",pos=scene.title_anchor, bind=Reset)

t = 0
dt = 1e-9

while t<1e-5:
    if running:
        rate(10000)
      
        Force = cross(Electron.charge* Electron.p/ Electron.m, MagneticField)
    # update momentum
        Electron.p = Electron.p+ Force*dt
    #update position
        Electron.pos = Electron.pos + Electron.p*dt/Electron.m

        t = t+dt
        time.sleep(0.01)
     
         
              

                                                               