import math

n = int(input("Enter the number :"))
a = [2]
for i in range(2,n+1):
    factorcount = 0
    if n%i==0:
        for j in range(2, int(i/2)+1):
            if i%j==0:
                factorcount = 1
                break
        if factorcount == 0:
            print("The prime factors of n are : ",i)
            
            
if i<=math.sqrt(n):
    print("The number is non prime")
    
else:
    print("The number is prime")
    

