import numpy as np 
G = 6.67e-11
M = 5.97e24
R = 6.371e6
#Use values of T--> 90min, 45min, 1day(in seconds)
T = float(input("Enter the value of time: "))
H = ((G*M*T**2)/(4.0*np.pi**2))**(1.0/3) - R
  

print("Altitude of satellite is : ", H)  