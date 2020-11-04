import math


def main():
    
    n = int(input("Enter number of tosses :"))
    k = int(input("Enter number of heads :"))

    a = 2**n
    
    probability = (math.comb(n,k))/a
        
    print("Probability of getting head is",probability, "times")
        
if __name__ == "__main__":
    main()