import math
import numpy as np

# n = int(input("Enter the number :"))
# a = [2]
# for i in range(2,n+1):
#     factorcount = 0
#     if n%i==0:
#         for j in range(2, int(i/2)+1):
#             if i%j==0:
#                 factorcount = 1
#                 break
#         if factorcount == 0:
#             print("The prime factors of n are : ",i)


# if i<=math.sqrt(n):
#     print("The number is non prime")

# else:
#     print("The number is prime")


def prime_list(N):
    """
    Returns a list of primes upto ten thousand
    """
    a = []
    for i in range(2, N):
        n = int(np.sqrt(i))
        factorcount = 0
        for j in range(2, n + 1):
            if i % j == 0:
                factorcount = 1
                break
        if factorcount == 0:
            a.append(i)
    return a


def prime_list1(N):
    """
    Returns a list of primes upto a given number N
    """
    a = [2]
    for i in range(3, N):
        n = int(np.sqrt(i))
        factorcount = 0
        for k in a:
            if k <= n and i % k == 0:
                factorcount = 1
                break
        if factorcount == 0:
            a.append(i)
    return a


def main():
    n = 100
    print("The list of primes using factors upto sqrt(n): ")
    print(prime_list(n))
    print("The list of primes using prime factors from the list of primes:")
    print(prime_list1(n))


if __name__ == "__main__":
    main()