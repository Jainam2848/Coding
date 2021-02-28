from numpy import sqrt
a = float(input('Enter value of a :'))
b = float(input('Enter value of b :'))
c = float(input('Enter value of c :'))


def main():
#4.1(a)
    x = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a) #correct value
    
    print("The first solution using standard formula is :", x)
    print("The second solution using standard formula is :", y)

#4.2(b)    
    x1 =  2*c/(-b - sqrt(b**2 - 4*a*c))  #correct value
    y2 =  2*c/(-b + sqrt(b**2 - 4*a*c))
    
    print("")
    print("The first solution with method B is :", x1)
    print("The second solution with method B  is :", y2)
    
#4.2(c)   
    print('')
    print("The correct root values are :" , y,",", x1)
    
if __name__ == "__main__":
    main()