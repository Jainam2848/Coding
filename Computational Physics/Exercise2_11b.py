import math

N = int(input("Enter a number :"))
def Binomial(n,k):
    Binomial = math.comb(n,k)
    for n in range(N):
        for k in range(n):
            print(Binomial(n,k), " ")
            print("\n")
    
    Binomial(n,k) 