array = [[] * 13]
while True:
    val = input()
    if val == '':
        break
    else:
        i = 0
        for c in val.strip():
            array[i].append(c)
            i += 1

gamma = max(array[0]) + max(array[1]) + max(array[2]) + max(array[3]) + max(array[4]) + max(array[5]) + max(array[6]) + max(array[7]) + max(array[8]) + max(array[9]) + max(array[10]) + max(array[11])
epsilon = min(array[0]) + min(array[1]) + min(array[2]) + min(array[3]) + min(array[4]) + min(array[5]) + min(array[6]) + min(array[7]) + min(array[8]) + min(array[9]) + min(array[10]) + min(array[11])
print(int(bin(gamma) + bin(epsilon)))

len_item = len(array[0])

