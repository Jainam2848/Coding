import numpy as np


def warp_drive(n):
    if n <= 1:
        return 1
    else:
        return 1 + warp_drive(n / 2)


def time(D, T):
    x = D / T
    x = x / 31556952
    return x

def escape_velocity(M, r):
    return np.sqrt(2 * G * M / r)


def s_radius(M):
    return 2 * G * M / c ** 2


G = 6.673e-11  # gravitational constant, unit-Nm**2/kg**2

c = 299792458  # meters/second

earth_diameter = 12742e3 

# black holes

Messier_87_mass = 1.3 * 10e40  # kg
Messier_87_radius = 1.9 * 10e13  # meter

Sagitarius_mass = 8.2 * 10e36   #kg
Sagitarius_radius = 1.2 * 10e10 # meter

decision = input("(A). You want to know about objects escape velocity and its radius of event- horizon? or (B) \
 you wanna travel there ?").lower()

if decision == "a":
                
    ask_user = input("Do u want to enter the mass and radius manually (y/n)? ")

    if ask_user == 'y':
        M = float(input("Enter mass of Object in kg : "))
        r = float(input("Enter radius of object in meter : "))
        escape_velocity(M, r)
        s_radius(M)
        print("Escape Velocity for your planet is", escape_velocity(M, r), "m/s")
        print("Your Object has", s_radius(M), "meter big event horizon")
        
    else:

        lst = ['SMBH in Messier 87 (option a)', 'Sagitarius A (option b)']

        print("Please select anyone from below :")

        for a in lst:
            print(a)
        user_ask2 = input('Please type your choice :').lower()

        if user_ask2 == 'a':
            print("SMBH in Messier 87 has escape velocity of :", escape_velocity(Messier_87_mass, Messier_87_radius), "m/s")
            print("SMBH in Messier 87 has", s_radius(Messier_87_mass), "m big Event Horizon")
            print("SMBH in Messier 87 is", (Messier_87_radius*2)/earth_diameter, "times in diameter than Earth")
            
        if user_ask2 == 'b':
            print("Sagitarius A has escape velocity of :", escape_velocity(Sagitarius_mass, Sagitarius_radius), "m/s")
            print("Sagitarius A has ", s_radius(Sagitarius_mass), "m big Event Horizon")
            print("it will take whopping", warp_drive(2.42573e+20), "min for Warp Drive to travel to Sagittarius A")
            print("Fun Fact: we are revolving around sun which is revolving around this Super Massive Black Hole")
            print("Sagitarius A is", (Sagitarius_radius*2)/earth_diameter, "times in diameter than Earth")
            
elif decision=='b':
    
    print("Where do you wanna go first?")
    SMBH = ['a.Sagitarius A', 'b.SMBH in Messier 87']
    for a in SMBH:
        print(a)
    pick = input('Please pick where you want to go? as a or b : ').lower()

    if pick == 'a':
    
        space_ships = ['a.Warp Drive(very fast)', "b.Thanos's spaceship(literally teleports)",
                   "c.Parker Solar Probe(Fastest spaceship man has ever made)"]
        for s in space_ships:
            print(s)
        pick = input('Please pick which spaceship you want to use as a,b or c : ').lower()
        print()
        if pick == 'a':
            warp_drive(2.42573e+20)
            print("it will take whopping", warp_drive(2.42573e+20), "min for Warp Drive to travel to Sagittarius A")
        if pick == 'b':
            print("Yep, you got teleported almost instantly")
        if pick == 'c':
            print("Whoa! , how many generations died reaching Sagittarius in", time(2.42573e+20, 150000), "years?")
    
        print("SMBH in Messier 87 has escape velocity of :", escape_velocity(Messier_87_mass, Messier_87_radius), "m/s")
        print("SMBH in Messier 87 has", s_radius(Messier_87_mass), "m big Event Horizon")
        print("SMBH in Messier 87 is", (Messier_87_radius*2)/earth_diameter, "times in diameter than Earth")

    

    elif pick == 'b':
    
        space_ships = ['a.Warp Drive(very fast)', "b.Thanos's spaceship(literally teleports)",
                   "c.Parker Solar Probe(Fastest spaceship man has ever made)"]
        for s in space_ships:
            print(s)
        pick = input('Please pick which spaceship you want to use as a,b or c : ').lower()
    
        if pick == 'a':
            warp_drive(5.01418715e+23)
            print("it will take whopping", warp_drive(5.01418715e+23), "min for Warp Drive to travel to SMBH in Messier 87")
        if pick == 'b':
            print("Yep, you got teleported almost instantly")
        if pick == 'c':
            print("Sheesh!, how many generations will die reaching SMBH of Messier A in", time(5.01418715e+23, 150000),
              "years?")
    
        print("Sagitarius A has escape velocity of :", escape_velocity(Sagitarius_mass, Sagitarius_radius), "m/s")
        print("Sagitarius A has ", s_radius(Sagitarius_mass), "m big Event Horizon")
        print("Sagitarius A is", (Sagitarius_radius*2)/earth_diameter, "times in diameter than Earth")
        
        
        
        
        
        
        
        
        
        
        
        
        
