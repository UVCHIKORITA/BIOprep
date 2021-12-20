cases = int(input().strip())
for i in range(cases):
    nlrk = list(map(int, input().strip().split(" ")))
    bars = list(map(int, input().strip().split(" ")))
    bars.sort()
    bars = [x for x in bars if x >= nlrk[1] and x <= nlrk[2]]
    sum = 0
    bought = 0
    for bar in bars:
        sum += bar
        bought += 1
        if sum > nlrk[3]:
            bought -= 1
            break
    print(bought)