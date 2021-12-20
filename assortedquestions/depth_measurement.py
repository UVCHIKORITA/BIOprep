"""i = 0
prevVal = 0
increase_count = 0
while True:
    if i == 0:
        i += 1
        in_val = int(input())
        prevVal = in_val
        continue
    else:
        val = input()
        if val == '':
            break
        in_val = int(val)
        if prevVal < in_val:
            increase_count += 1
        i += 1
        prevVal = in_val

print(increase_count)"""

array = []
while True:
    val = input()
    if val == '':
        break
    else:
        array.append(int(val))

print("A")
numIncrease = 0
i = 3
while i < len(array):
    print(i)
    if array[i] + array[i-1] + array[i-2] > array[i-1] + array[i-2] + array[i-3]:
        numIncrease += 1
    i += 1

print(numIncrease)