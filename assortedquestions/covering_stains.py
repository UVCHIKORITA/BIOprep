#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'coveringStains' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY coordinates
#

def coveringStains(k, coordinates):
    minX = math.inf
    maxX = -math.inf
    numberminX = 0
    numbermaxX = 0
    minY = math.inf
    maxY = -math.inf
    numberminY = 0
    numbermaxY = 0
    for coordinate in coordinates:
        if coordinate[0] < minX:
            minX = coordinate[0]
            numberminX = 1
        elif coordinate[0] == minX:
            numberminX += 1
        if coordinate[0] > maxX:
            maxX = coordinate[0]
            numbermaxX =1
        elif coordinate[0] == maxX:
            numbermaxX += 1
        if coordinate[1] < minY:
            minY = coordinate[1]
            numberminY = 1
        elif coordinate[1] == minY:
            numberminY += 1
        if coordinate[1] > maxY:
            maxY = coordinate[1]
            numbermaxY = 1
        elif coordinate[1] == maxY:
            numbermaxY += 1
    print(numberminX)
    print(numbermaxX)
    print(numberminY)
    print(numbermaxY)
    if numberminX > k and numbermaxX > k and numberminY > k and numbermaxY > k:
        return 0
    return ":("

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = coveringStains(k, coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
