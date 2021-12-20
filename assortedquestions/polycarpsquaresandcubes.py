from math import floor
from decimal import *
getcontext().prec = 2899

t = int(input().strip())
for i in range(t):
    num = int(input().strip())
    """
    print(floor((num ** (1 / 2))))
    print(floor((num ** (1 / 3))))
    print(floor((num ** (1 / 6))))"""

    print(int(floor(num**(1.0/float(2))) + floor(num**(1.0/float(3))) - floor(num**(1.0/float(6)))))