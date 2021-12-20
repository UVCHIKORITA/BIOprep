N = input()
flowers = list(map(int, input().strip().split(" ")))
count = 0
for i in range(len(flowers)):
    k = i
    while k < len(flowers):
        if sum(flowers[i:k+1]) / (k - i + 1) in flowers[i:k+1]:
            count += 1
        k += 1
print(count)
