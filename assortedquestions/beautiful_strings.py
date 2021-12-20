#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulStrings' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def beautifulStrings(s):
    # Write your code here
    length_s = len(s)
    i = 0
    m = 0
    d = 0
    p = 0
    while i < length_s:
        if i == 0:
            m = 1
        elif i > 0 and s[i] != s[i - 1]:
            m += 1
        if i >= 2 and s[i - 1] == s[i - 2]:
            d += 1
        if 0 < i < length_s - 1:
            if s[i - 1] == s[i + 1]:
                p += 1
        i += 1
    if s[length_s - 1] == s[length_s - 2]:
        d += 1
    return int(((m * (m - 1)) / 2) + d - p)



fptr = open(os.environ['OUTPUT_PATH'], 'w')

print("Enter some value here")
s = input()

result = beautifulStrings(s)


fptr.write(str(result) + '\n')

fptr.close()