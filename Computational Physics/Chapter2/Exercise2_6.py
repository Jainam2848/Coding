import numpy as np

#Mass of sun
M = 1.9891e30 
# Gravitational constant
G = 6.6738e-11

def main():
# l1 and v1 would be entered by user and are for perihelion

    l1 = float(input("Enter distance of perihelion :"))
    v1 = float(input("Enter velocity at perihelion :"))

# l2 and v2 are lengths and veloctiy at aphelion
#calculate v2.
    v2 = (2*G*M/l1*v1) - v1

#calculate l2 from l1v1 = l2v2
    l2 = l1*v1/v2

# a = length of semi-major axis
    a = (l1+l2)/2

# b = length of semi-minor axis
    b = np.sqrt(l1*l2)

# T = orbital period
    T = (2*np.pi*a*b)/(l1*v1)

#orbital eccentricity
    e = (l2-l1)/(l2+l1)


    print(f"The length of aphelion is : {l2}")

    print(f"The velocity of planet at aphelion is : {v2}")

    print(f"The orbital period of planet is : {T}")

    print(f"The orbital eccentricity of planet is : {e}")
if __name__ == "__main__":
    main()
