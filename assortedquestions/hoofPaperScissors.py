n = int(input())
k = int(input())
fj = []
dp = [[[0 for i in range(n+1)] for j in range(k+1)] for m in range(3)]

HOOF = 1
PAPER = 0
SCISSORS = 2


def hasWon(a, b):
    if a == HOOF and b == SCISSORS:
        return True
    if a == SCISSORS and b == PAPER:
        return True
    if a == PAPER and b == HOOF:
        return True
    return False


for p in range(n-1):
    p += 1
    dp[n][][]
