n = int(input())
arr_a = list(map(int, input().strip().split(" ")))

prev_possibilities = []
i = 0
total_possibilities = 1
for item in arr_a:
    if i + 1 < len(arr_a) and i > 0:
        if arr_a[i + 1] == 1 and item == 1:
            total_possibilities = 0
            break
        if arr_a[i + 1] == 1:
            total_possibilities *= item - 1
        elif arr_a[i - 1] <= item:
            total_possibilities *= item - 1
    elif i + 1 == len(arr_a):
        if arr_a[i - 1] == 1 and item == 1:
            total_possibilities = 0
            break
        elif i == 0:
            total_possibilities *= item
        elif arr_a[i - 1] <= item:
            total_possibilities *= item - 1
    else:
        total_possibilities *= item
    i += 1
print(total_possibilities % 998244353)

