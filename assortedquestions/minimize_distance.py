num_tests = int(input())
n_and_k = []
depots = []
for i in range(num_tests):
    temp_n = input()
    n_and_k.append(list(map(int, temp_n.strip().split(" "))))
    temp_depot = list(map(int, input().strip().split(" ")))
    depots.append(temp_depot)


p = 0
for depot_list in depots:
    depot_list.sort()
    while 0 in depot_list:
        depot_list.remove(0)
    maxDist = max(max(depot_list), -max(depot_list), min(depot_list), -min(depot_list))
    k_val = n_and_k[p][1]
    travelled = 0
    if max(depot_list) <= 0 and min(depot_list) <= 0:
        m = 0
        for val in depot_list:
            depot_list[m] = val * -1
            m += 1
    if max(depot_list) >= 0 and min(depot_list) >= 0:
        q = 0
        while q < len(depot_list):
            if q == len(depot_list) - 1:
                travelled += depot_list[q]
            else:
                if (q+1) % k_val == 0:
                    travelled += 2 * depot_list[q]
            q += 1
    elif max(depot_list) + min(depot_list) > 0 > min(depot_list):
        lessZeroList = []
        moreZeroList = []
        for val in depot_list:
            if val < 0:
                lessZeroList.append(val)
            else:
                moreZeroList.append(val)
        u = 0
        for val in lessZeroList:
            if (u + 1) % k_val == 0:
                travelled += -2 * val
            elif u == len(lessZeroList) - 1:
                travelled += -2 * val
            u += 1
        u = 0
        for val in moreZeroList:
            if u == len(lessZeroList) - 1:
                travelled += val
            elif (u + 1) % k_val == 0:
                travelled += 2 * val
            u += 1
    elif max(depot_list) + min(depot_list) < 0:
        lessZeroList = []
        moreZeroList = []
        for val in depot_list:
            if val < 0:
                lessZeroList.append(val)
            else:
                moreZeroList.append(val)
        u = 0
        for val in moreZeroList:
            if (u + 1) % k_val == 0:
                travelled += 2 * val
            elif u == len(moreZeroList) - 1:
                travelled += 2 * val
            u += 1
        u = 0
        lessZeroList.reverse()
        for val in lessZeroList:
            if u == len(lessZeroList) - 1:
                travelled += -1 * val
            elif (u + 1) % k_val == 0:
                travelled += -2 * val
            u += 1
    print(travelled)
    p += 1
