from math import comb

charArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

n = int(input())


def findStr(k, tar, ans=""):
    if tar == 0:
        return ans
    if ans:
        start = charArr.index(ans[-1]) + 1
    else:
        start = 0
    for i in range(start, 36):
        p = comb(36 - i - 1, tar - 1)
        if p >= k:
            return findStr(k, tar - 1, ans + charArr[i])
        k -= p




strLen = 1
while comb(36, strLen) < n:
    n -= comb(36, strLen)
    strLen += 1

print(findStr(n, strLen))