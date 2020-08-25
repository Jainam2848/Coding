import tkinter as tk
from tkinter import ttk
import math
import numpy as np
import time

class ProjectileMotion:
        
 
    def __init__(self, x, y, initialVelocity, initialAngle):
        self.x = x
        self.y = y
        self.mass= 10
        self.angle = initialAngle*np.pi/180.0
        self.v = initialVelocity
        self.vx = self.v*math.cos(self.angle)
        self.vy = self.v*math.sin(self.angle)
        self.ax = 0
        self.ay = 9.8
        self.dt = 0.1
        self.time = 0

    # define force   
    def grav_force(self):
        self.force.y = self.mass*self.ay
        self.force.x = 0
            
    #update velocity
    def updatevx(self):
        self.vx += self.ax*self.dt
        return self.vx

    def updatevy(self):   
        self.vy -= self.ay*self.dt
        return self.vy


    def update_position(self): 
        self.x += self.vx*self.dt
        self.y -= self.vy*self.dt - 0.5*self.ay*(self.dt)**2
        return(self.x, self.y)

    #update time
    def update_time(self):  
        self.time += self.dt


def buttonPushed():
    global projectileScreen
    projectileScreen.destroy()
    


# Create circle
    x0 = 10
    y0 = 600
    myOval = my_canvas.create_oval(x0,y0,x0+25,y0+25,fill="white")
    
        
    
    
    
def draw_oval(x, y):
    my_canvas.create_oval(x,y, x+25, y+ 25, fill="white")

def del_oval(x, y):
    my_canvas.create_oval(x,y, x+25, y+ 25, fill="black")
    
def draw_point(x, y):
    my_canvas.create_oval(x, y, x+1, y+1, fill="#476042")

    
def retrieve_input(x0,y0):
    
    initialVelocity=float(textBox1.get("1.0","end-1c"))
    initialAngle=float(textBox2.get("1.0","end-1c"))
    y = y0
    x=x0
    p1 = ProjectileMotion(x0,y0,initialVelocity, initialAngle)
    
    while (y0 >= y >= 0.0 and x0 <= x <=650):
        del_oval(x, y)
        vx = p1.updatevx()
        vy = p1.updatevy()
        x, y = p1.update_position()
        dt = p1.update_time()
        draw_oval(x, y)
        draw_point(x,y)
        my_canvas.update()
        time.sleep(0.01)
        
projectileScreen = tk.Tk()
projectileScreen.title("Simulation")

w = tk.Label(projectileScreen,text="Projectile motion simulation")
w.pack()
#Create canvas
my_canvas = tk.Canvas(projectileScreen, width = 800, height =650,bg="black")
my_canvas.pack(padx=10, pady=10)

# Create circle
x0 = 10
y0 = 600
myOval = my_canvas.create_oval(x0,y0,x0+25,y0+25,fill="white")

#Create textbox

label1 = tk.Label(master=projectileScreen, text="Initial Velocity", bg="white")
label1.pack(side=tk.LEFT)
textBox1=tk.Text(projectileScreen, height=1, width=10)
textBox1.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(master=projectileScreen, text="Initial Angle (in degrees)", bg="white")
label2.pack(side=tk.LEFT)
textBox2=tk.Text(projectileScreen, height=1, width=10)
textBox2.pack(side=tk.LEFT, padx=10)


buttonCommit=tk.Button(projectileScreen, height=1, width=10, text="Simulate", relief=tk.GROOVE,
                    command=lambda: retrieve_input(x0,y0))

buttonCommit.pack(side=tk.LEFT, padx = 10)

#Create exit button

exitButton = tk.Button(projectileScreen,text="Exit", relief= tk.RIDGE, command=buttonPushed)
exitButton.pack(side=tk.RIGHT, padx=10)


def clearTextinput():
    textBox1.delete("1.0", "end")
    textBox2.delete("1.0", "end")
    my_canvas.delete("all")
    
#Create reset button
resetButton = tk.Button(projectileScreen,text="Reset", relief= tk.RIDGE,
                        command=clearTextinput)
resetButton.pack(side=tk.RIGHT, padx=10)
  

projectileScreen.mainloop()