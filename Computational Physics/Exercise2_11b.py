import math


def Binomial(N):
    for n in range(1, N+1):
        [print(math.comb(n, k), end=" ") for k in range(n+1)]
        print(end="\n")


def main():
    N = int(input("Enter a number :"))
    Binomial(N)


if __name__ == "__main__":
    main()
