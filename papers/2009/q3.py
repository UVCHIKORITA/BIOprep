def find_sum(val):
    if val == 0:
        return 1
    return 2**(val-1)

sums = []
for i in range(32):
    sums.append(find_sum(i))

print(sums)


def find_qth_way(val, q):
    if q == sums[val]:
        return val
    i = int(val) - 1
    while i > 0:
        q -= sums[i]
        if q <= 0:
            q += sums[i]
            break
        i -= 1
    # :( :( :( :( :( :( :(
