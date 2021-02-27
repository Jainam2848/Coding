n = int(input("Enter a Number to find its factorial :"))
def factorial(n):
    fac = 1
    if n<0:
        print("The factorial does not exists")
    elif n==0:
        print("The factorial is 1")
    
    for i in range(n,0,-1):
        fac*=i
            
    return fac
print(factorial(n))
    
