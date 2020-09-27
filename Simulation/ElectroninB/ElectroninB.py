
from vpython import *
import numpy as np
import time
import math

running = False

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
    Electron.make_trail = True


bbutton = button(text="Run",pos=scene.title_anchor, bind=Run)


def Reset(c):
    global t, Electron
    t = 0
    Electron.pos = vector(0,-5,0)
    #Electron.pos = scene.mouse.pos
    Electron.p = Electron.m*Electron.v*vector(0,1,0)
    Electron.clear_trail()
    Electron.make_trail = False
    Electron.radius = 0.3

cbutton = button(text="Reset",pos=scene.title_anchor, bind=Reset)


#screen = display(title = "Motion of electron in magnetic field", width = 600, height = 200, make_trail=True)


MagneticField = 5e-5*vector(0,-5,-5)


#Let's add dragging properties
# drag = False
# Electron = None # declare Electron to be used below

# scene.bind("mousedown", def ():
#     global drag, Electron
#     Electron = sphere(pos=scene.mouse.pos,
#                 color=color.red,
#                 size=0.2*vec(1,1,1))
#     drag = True
#     scene.bind("mousemove", def ():
#         global drag, Electron
#         if drag: # mouse button is down
#         Electron.pos = scene.mouse.pos
        
#         scene.bind("mouseup", def ():
#             global drag, Electron
#             Electron.color = color.cyan
#             drag = False
#             )
#         )
#     )



Electron = sphere(pos = vector(0,-5,0), radius = 0.2, color = color.red, make_trail=False)

Electron.m = 9.1e-31
Electron.charge = -1.6e-19
Electron.v = float(input("enter velocity"))
Electron.p = Electron.m * Electron.v*vector(0, 3, 0)


t = 0
dt = 1e-9


while t<1e-5:
    rate(100)
    # if drag:
    #     R = scene.mouse.pos
    #     Electron.pos=R
    if running:
        rate(10000)
      
        Force = cross(Electron.charge * Electron.p/ Electron.m, MagneticField)
    # update momentum
        Electron.p = Electron.p + Force*dt
    #update position
        Electron.pos = Electron.pos + Electron.p*dt/Electron.m

        t = t+dt
        time.sleep(0.01)
     
