def gen_lucky():
    arr = []
    for i in range(7500):
        arr.append(2*(i + 1) - 1)
    ptr = 1
    while True:
        try:
            curr = arr[ptr]
            remVals = []
            for i in range(len(arr) - 1):
                if i % curr == curr - 1:
                    remVals.append(arr[i])
            for val in remVals:
                arr.remove(val)
            ptr += 1
        except:
            return arr

def findNearest(val):
    arr = gen_lucky()
    higher = 0
    lower = 0
    for k in arr:
        if k > val:
            higher = k
            break
        lower = k
    print(lower, higher)

v = int(input())
findNearest(v)