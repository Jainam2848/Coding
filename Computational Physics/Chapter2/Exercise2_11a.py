import math
n = int(input("Enter value of n :"))

k = int(input("Enter value of k :"))
def main(n,k):
    Binomial = math.comb(n,k)

    print(Binomial)
    
if __name__ == "__main__":
    main(n,k)