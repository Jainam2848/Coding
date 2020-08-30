from vpython import *

screen = display(width = 4000, height =5000)

def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_unit = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_unit
    
    return force_vec
    
star = sphere( pos=vector(0,0,0), radius=0.5, color=color.yellow,
               mass = 1000, momentum=vector(0,0,0) )
               
planet1 = sphere( pos=vector(1,0,0), radius=0.05, color=color.green,
                  mass = 1, momentum=vector(0,30,0) )

planet2 = sphere( pos=vector(0,3,0), radius=0.075, color=color.red,
                  mass = 2, momentum=vector(-35,0,0) )
                  
planet3 = sphere( pos=vector(0,-4,0), radius=0.1, color=color.blue,
                  mass = 10, momentum=vector(160,0,0) )
               
planet4 = sphere( pos=vector(0,-5,0), radius=0.04, color=color.white,
                  mass = 8, momentum=vector(180,0,0) )

planet5 = sphere( pos=vector(0,6,0), radius=0.3, color=color.yellow,
                  mass = 15, momentum=vector(150,0,0) )

dt = 0.0001
t = 0
while (True):
    rate(1000)
    
    # Calculate forces.
    star.force = gforce(star,planet1)+gforce(star,planet2)+gforce(star,planet3)+gforce(star,planet4)+gforce(star,planet5)
    planet1.force = gforce(planet1,star)+gforce(planet1,planet2)+gforce(planet1,planet3)+gforce(planet1,planet4)+gforce(planet1,planet5)
    planet2.force = gforce(planet2,star)+gforce(planet2,planet1)+gforce(planet2,planet3)+gforce(planet2,planet4)+gforce(planet2,planet5)
    planet3.force = gforce(planet3,star)+gforce(planet3,planet1)+gforce(planet3,planet2)+gforce(planet3,planet4)+gforce(planet3,planet5)
    planet4.force = gforce(planet4,star)+gforce(planet4,planet1)+gforce(planet4,planet2)+gforce(planet4,planet3)+gforce(planet4,planet5)
    planet5.force = gforce(planet5,star)+gforce(planet5,planet1)+gforce(planet5,planet2)+gforce(planet5,planet3)+gforce(planet5,planet4)



    # Update momenta.
    star.momentum = star.momentum + star.force*dt
    planet1.momentum = planet1.momentum + planet1.force*dt
    planet2.momentum = planet2.momentum + planet2.force*dt
    planet3.momentum = planet3.momentum + planet3.force*dt
    planet4.momentum = planet4.momentum + planet4.force*dt
    planet5.momentum = planet5.momentum + planet5.force*dt
    
    # Update positions.
    star.pos = star.pos + star.momentum/star.mass*dt
    planet1.pos = planet1.pos + planet1.momentum/planet1.mass*dt
    planet2.pos = planet2.pos + planet2.momentum/planet2.mass*dt
    planet3.pos = planet3.pos + planet3.momentum/planet3.mass*dt
    planet4.pos = planet4.pos + planet4.momentum/planet4.mass*dt
    planet5.pos = planet5.pos + planet5.momentum/planet5.mass*dt

    #update time.
    t = t + dt