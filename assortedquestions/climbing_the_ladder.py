#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def generate_ranks(arr):
    rankCount = 0
    ranks = []
    i = 0
    while i < len(arr):
        if arr[i-1] != arr[i] or i == 0:
            rankCount += 1
        ranks.append(rankCount)
        i += 1
    return ranks


def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    newRanks = []
    for noob in player:
        rankedTemp = ranked
        rankedTemp.append(noob)
        rankedTemp = list(set(rankedTemp))
        i = 0
        if len(rankedTemp) > len(ranked):
            while i < len(rankedTemp):
                if noob >= rankedTemp[i]:
                    rankedTemp.insert(noob, i)
                i += 1
        rankedPositions = generate_ranks(ranked)
        newRanks.append(rankedPositions[rankedTemp.index(noob)])
    return newRanks


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
