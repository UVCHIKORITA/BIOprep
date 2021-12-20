#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s.replace(" ", "")
    rows = 0
    columns = int(math.sqrt(len(s)) // 1)
    if columns < math.sqrt(len(s)):
        rows += 1
    rows += columns
    i = 0
    encodedstring = ""
    while i < len(s):
        encodedstring += s[i]
        if (i + 1) % columns == 0:
            encodedstring += "||"
        i += 1
    return encodedstring


if __name__ == '__main__':

    s = input()

    result = encryption(s)
    print(result)
