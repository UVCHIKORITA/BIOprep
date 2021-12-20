tests = int(input().strip())

for k in range(tests):
    inp = list(map(int, input().strip().split(" ")))
    w = inp[0]
    h = inp[1]
    hlineA = list(map(int, input().strip().split(" ")))[1:]
    hlineB = list(map(int, input().strip().split(" ")))[1:]
    horizontalmax = max(max(hlineA) - min(hlineA), max(hlineB) - min(hlineB))
    hmax = horizontalmax * h
    vlineA = list(map(int, input().strip().split(" ")))[1:]
    vlineB = list(map(int, input().strip().split(" ")))[1:]
    verticalmax = max(max(vlineA) - min(vlineA), max(vlineB) - min(vlineB))
    vmax = verticalmax * w
    area = max(hmax, vmax)
    print(area)