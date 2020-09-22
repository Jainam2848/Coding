
import numpy as np
import time
import tkinter as tk
from tkinter import ttk
import math
from array import *

magneticScreen = tk.Tk()
magneticScreen.title("Simulation")

w = tk.Label(magneticScreen,text="Motion of electron in Magnetic field ")
w.pack()

my_canvas = tk.Canvas(magneticScreen, width = 800, height =650,bg="black")
my_canvas.pack(padx=10, pady=10)

MagneticField = np.array([[0,0,0],[0,-5,0],[0,0,5]])
Velocity = np.array([[0,0,0],[0,-3,0],[0,0,0]])
A = np.cross(MagneticField, Velocity)

class electronMotion:
    def __init__(self, x, y, Velocity, MagneticField):
        self.x = x
        self.y = y
        self.m= 9.1e-31
        self.v = Velocity
        self.charge = -1.6e-19
        self.dt = 1e-9
        self.time = 0
        self.MagneticField = MagneticField 
        self.p = self.m*self.v
        
    def force(self):
        self.force = np.dot(A, self.charge)
        return(force)        
        
    def updateMomemtum(self):
        self.p = self.p + self.force*self.dt
        return(self.p)

    def updatePosition(self):
        self.x = self.x + self.p*dt/self.m
        self.y = self.y + self.p*dt/self.m
        return(self.x, self.y)


    def updatetime(self):
        self.time+=self.dt
        
def retrieve_input(x0,y0):
    Velocity=float(textBox1.get("1.0","end-1c"))
    MagneticField=float(textBox2.get("1.0","end-1c"))
    p1 = electronMotion(x0,y0,Velocity, MagneticField)
    x = x0
    y = y0
    while (y0 >= y >= 0.0 and x0 <= x <=350):
        del_oval(x, y)
        p = p1.updateMomemtum()
        x, y = p1.updateposition()
        draw_oval(x, y)
        draw_point(x,y)
        my_canvas.update()
        time.sleep(0.01)

def del_oval(x, y):
    my_canvas.create_oval(x,y, x+25, y+ 25, fill="black")
    
def draw_point(x, y):
    my_canvas.create_oval(x, y, x+1, y+1, fill="#476042")

def buttonPushed():
    global magneticScreen
    magneticScreen.destroy() 

def draw_oval(x, y):
    my_canvas.create_oval(x,y, x+25, y+ 25, fill="white")
        
        
            

# creating oval        
x0 = 10
y0 = 300
myOval = my_canvas.create_oval(x0,y0,x0+25,y0+25,fill="white")

# Creating lables
label1 = tk.Label(master=magneticScreen, text="Velocity", bg="white")
label1.pack(side=tk.LEFT)

textBox1=tk.Text(magneticScreen, height=1, width=10)
textBox1.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(master=magneticScreen, text="Magnetic Field", bg="white")
label2.pack(side=tk.LEFT)

textBox2=tk.Text(magneticScreen, height=1, width=10)
textBox2.pack(side=tk.LEFT, padx=10)



buttonCommit=tk.Button(magneticScreen, height=1, width=10, text="Simulate", relief=tk.GROOVE,
                    command=lambda: retrieve_input(x0,y0))

buttonCommit.pack(side=tk.LEFT, padx = 10)

#Create exit button

exitButton = tk.Button(magneticScreen,text="Exit", relief= tk.RIDGE, command=buttonPushed)
exitButton.pack(side=tk.RIGHT, padx=10)


def clearTextinput():
    textBox1.delete("1.0", "end")
    textBox2.delete("1.0", "end")
    my_canvas.delete("all")
    
    
#Create reset button
resetButton = tk.Button(magneticScreen,text="Reset", relief= tk.RIDGE,
                        command=clearTextinput)
resetButton.pack(side=tk.RIGHT, padx=10)
  

magneticScreen.mainloop()





