from math import factorial
C = 1
n = 0
while C <= 1e9:
    print(f"The catalan numbers are: {C}")
    C = (factorial(2 * n)) / (factorial(n + 1) * factorial(n))
    n = n + 1