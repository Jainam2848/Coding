import numpy as np
import math
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

# now we have many value for a5
A = int(input("Enter value of A :"))
Z = int(input("Enter value of Z :"))

def main():
    
    if A%2!=0:  # A = 0
        a5 = 0.0
    else:
        if Z%2==0: # Z is even
            a5=12.0
        else: a5=-12.0
        
    B = float(a1*A - a2*A**(2/3)- a3*(Z**2)/A**(1/3) - a4*((A-2*Z)**2)/A + a5/A**(1/2))

    print(f"The binding energy of atom is : {B}")
    print(f"The binding energy of atom is : {B/A}")

if __name__ == "__main__":
    main()



