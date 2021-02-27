from numpy import sqrt
a = float(input('Enter value of a :'))
b = float(input('Enter value of b :'))
c = float(input('Enter value of c :'))


def main():
#4.1(a)
    x = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    print("The first solution using standard formula is :", x)
    print("The second solution using standard formula is :", y)

#4.2(b)    
    x1 =  2*c/(-b - sqrt(b**2 - 4*a*c))
    y2 =  2*c/(-b + sqrt(b**2 - 4*a*c))
    
    print("The first solution with alternative formula is :", x1)
    print("The second solution with alternative formula is :", y2)
    
if __name__ == "__main__":
    main()