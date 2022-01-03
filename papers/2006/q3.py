# from math import factorial
from functools import lru_cache
inputs = list(map(int, input().strip().split(" ")))
s = inputs[0]
d = inputs[1]

"""
d_max = (inputs[0] - inputs[1] + 1) // 2
totalpos = 0

for i in range(d_max):
    j = i + 1
    try:
        if (inputs[0]-(j*2)) / 20 > inputs[1] - 1:
            continue
        else:
            totalpos += factorial(inputs[0]-(j*2)-1) / (factorial(inputs[1] - 2) * factorial(inputs[0]-(j*2)+1-inputs[1]))
    except:
        break

print(int(totalpos))
"""

@lru_cache(maxsize=None)
def findpos(a, b):
    if a / 20 > b:
        return 0
    if b == 0:
        if a == 0:
            return 1
        else:
            return 0
    if a <= 0:
        return 0
    pos = 0
    for i in range(1, 21):
        pos += findpos(a-i,b-1)
    return pos


totalPos = 0
for i in range(1, 21):
    totalPos += findpos(s - i * 2, d - 1)

print(totalPos)