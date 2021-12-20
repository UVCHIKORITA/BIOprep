tests = int(input().strip())
for i in range(tests):
    val = input()
    # above value ignored
    costs = list(map(int, input().strip().split(" ")))
    mod3 = set()
    for cost in costs:
        mod3.add(cost % 3)
    try:
        mod3.remove(0)
    except:
        pass
    threepennies = max(costs) // 3
    if 1 not in costs and len(mod3) == 2:
        threepennies -= 1
    print(threepennies + len(mod3))
