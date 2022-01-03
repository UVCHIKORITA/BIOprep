lol = input()
scores = sorted(list(map(int, input().strip().split(" "))))
lol_two = input()
target_list = list(map(int, input().strip().split(" ")))
for target in target_list:
    minways = [1]+[0]*target
    for score in scores:
        for i in range(score,target+1):
            if minways[i] == 0:
                minways[i] = minways[i - score] + 1
            else:
                minways[i] = min(minways[i], minways[i - score] + 1)
    if(minways[target] - 1 == -1):
        print("IMPOSSIBLE")
    else:
        print(minways[target] - 1)
