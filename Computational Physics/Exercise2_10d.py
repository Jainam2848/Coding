import numpy as np
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2


def main():
    B = np.zeros(300)
    A1 = np.zeros(100)
    for Z in range(1, 100):
        for A in range(Z, 3*Z):
            if A % 2 != 0:
                a5 = 0.0
            else:
                if Z % 2 == 0:
                    a5 = 12.0
                else:
                    a5 = -12.0

        B[A] = a1*A - a2*A**(2/3) - a3*(Z**2)/A**(1/3) - \
            a4*((A-2*Z)**2)/A + a5/A**(1/2)

        A = np.where(B == np.max(B))[0][0]
        A1[Z] = A
    Z = np.where(A1 == np.max(A1))[0][0]

# question c
    print(f"The binding energy of atom is : {B[A]/A}")

    print(f"The value of A for most stable nucleus is : {A}")

    print(f"The value of Z for most stable nucleus is : {Z}")


if __name__ == "__main__":
    main()
