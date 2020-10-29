import math

def main():
    
    n = int(input("Enter number of tosses :"))
    
    for k in range(1,100):
        if(k>=60 or k<=100):
            probability = (math.comb(n,k))/(2**n)
        
    print("Probability of getting head is",probability, "times")
        
if __name__ == "__main__":
    main()