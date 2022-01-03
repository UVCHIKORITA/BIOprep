from itertools import combinations

s = input()

count = 0
for splits in range(1,len(s)):
    for pos in combinations(range(1, len(s)), splits):
        got = []
        last = 0
        for i in pos:
            got.append(s[last:i])
            last = i
        got.append(s[last:])

        if got==got[::-1]:
            count += 1
print(count)