from tkinter import *
import math
import numpy as np

projectile = Tk()
projectile.title("Simualtion")
projectile.geometry("5000x5000")

w = Label(projectile,text="Welcome")
w.pack()
#Create canvas
my_projectile = Canvas(projectile, width = 700, height =700,bg="black")
my_projectile.pack()


#Create circle(x1,y1,x2,y2)
my_projectile.create_oval(100,300,150,350,fill="white")

while (projectile.pos.y>=0):
        rate(100)

class projectile():
        
 
        def __init__(self):
                
                self.x  = 0
                self.y =0
                self.mass= 10
                self.angle = 60*3.1414/180
                self.v = 10
                self.vx = self.v*math.cos(self.angle)
                self.vy = self.v*math.sin(self.angle)
                self.ax = 0
                self.ay = -9.8
                self.dt = 0.001
                self.time = 0

# define force   
        def grav_force(self):
                self.force.y = -self.mass*self.ay
                self.force.x = 0
#update velocity
        def updatevx(self,dt):   

                self.vx = self.vx + self.ax*dt
                return self.vx
        
        def updatevy(self,dt):   

                self.vy = self.vy + self.ay*dt
                return self.vy



        def update_position(): 
                self.x = self.x + self.vx*dt

#update time
        def update_time():  
                self.time = self.time + self.dt

projectile(0,0)
    


def buttonPushed():
    global root
    root.destroy()    
    
mybutton = Button(root,text="Exit", command=buttonPushed)
mybutton.pack()
root.mainloop()
