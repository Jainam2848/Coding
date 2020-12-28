import numpy as np
import math

def catalan(n):
    if n==1:
        return 1
    else:
        return ((4*n-2)/(n+1)*catalan(n-1))
    
Ans= int(catalan(100))

print(Ans)