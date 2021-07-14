import numpy as np

# writing a function to calculate the escape velocity

G  = 6.673e-11  #gravitational constant, unit-Nm**2/kg**2

c =  299792458  #meters/second

ask_user = input("Do u want to enter the mass and radius manually (y/n) ?")

if ask_user == 'y':
    M = float(input("Enter mass of Object in kg :"))
    r = float(input("Enter radius of object in meter :"))

else:
    pass


#black holes

Messier_87_mass = 1.3*10e40  #kg
Messier_87_radius = 1.9*10e13  #meter

Sagitarius_mass = 8.2*10e36
Sagitarius_radius = 1.2*10e10

lst = ['Messier 87' , 'Sagitarius']

print("Please select anyone from below :")

for a in lst:
    print(a)
    
user_ask2 = input('Please type your choice :').lower()
    
def escape_velocity(M,r):
    
    return np.sqrt(2*G*M/r)

# writing a function to calculate the schwarzchild radius

# will calculate distance if event horizon from center

def s_radius(M):
    return 2*G*M/c**2

#for manually entered values of m and r

print('Escape Velocity would be :',escape_velocity(M, r), "m/s")
print("Schwarzchild radius would be :", s_radius(M))

if user_ask2 == 'messier 87':
    print("Messier 87 has escape velocity of :", escape_velocity(Messier_87_mass, Messier_87_radius), "m/s")
    print("Messier 87 has schwarzchild radius of :", s_radius(Messier_87_mass), "m") 

if user_ask2 == 'sagitarius':
    print("Sagitarius has escape velocity of :", escape_velocity(Sagitarius_mass, Sagitarius_radius), "m/s")
    print("Sagitarius has schwarzchild radius of :", s_radius(Sagitarius_mass), "m") 


