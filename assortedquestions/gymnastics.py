k_n = list(map(int, input().strip().split(" ")))
orders = []
for i in range(k_n[0]):
    orders.append(list(map(int, input().strip().split(" "))))
q = k_n[1]
pairs = 0
while q > 0:
    inFrontOf = []
    isInFrontOf = True
    isFirstRound = True
    for order in orders:
        mini_order = order[order.index(q):]
        mini_order.remove(q)
        print(mini_order)
        if len(mini_order) == 0:
            isInFrontOf = False
            break
        else:
            if isFirstRound:
                inFrontOf = mini_order
            else:
                inFrontOf = list(set(inFrontOf).intersection(mini_order))
                print(inFrontOf)
                if len(inFrontOf) == 0:
                    isInFrontOf = False
                    break
        isFirstRound = False
    print("----------")
    print(len(inFrontOf))
    if isFirstRound:
        pairs += len(inFrontOf)
    q -= 1

print(pairs)