from math import sqrt, floor
n = int(input().strip())


def get_factor_pairs(k):
    pairs = []
    for p in range(1, floor(sqrt(k)) + 1):
        if k / p == k // p:
            pairs.append([int(p), int(k / p)])
    return pairs


dp = [1, 2, 3, 4, 5, 5]
for i in range(7, n + 1):
    dp.append(0)

for i in range(7, n + 1):
    dp[i - 1] = dp[i - 2] + 1
    for pair in get_factor_pairs(i):
        dp[i - 1] = min(dp[i - 1], dp[pair[0] - 1] + dp[pair[1] - 1])

print(dp[n - 1])
