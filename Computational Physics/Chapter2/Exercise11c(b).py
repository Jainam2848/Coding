import math

#binomial distribution formula
def main():
    n = 100 # number of tosses
    p = 0.5 # probability of getting head when coin is tossed once
    
    u = n*p #mean
    sigma = (u*(1-p))**(1/2)
    x = 60
    z = (x - u)/sigma # Standard normal random variable
    Z = 0.9772      # Value of z from z-table
    
    probability = 1 - Z
    
    print(probability)
    
if __name__ == "__main__":
    main()