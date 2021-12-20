f = open('mixmilk.in')
fileLines = list(f.read().split("\n"))
bucket1 = list(map(int, fileLines[0].strip().split(" ")))
bucket2 = list(map(int, fileLines[1].strip().split(" ")))
bucket3 = list(map(int, fileLines[2].strip().split(" ")))
f.close()
for i in range(100):
    if i % 3 == 0:
        poured = min(bucket1[1], bucket2[0]-bucket2[1])
        bucket1[1] = bucket1[1] - poured
        bucket2[1] = bucket2[1] + poured
    if i % 3 == 1:
        poured = min(bucket2[1], bucket3[0]-bucket3[1])
        bucket2[1] = bucket2[1] - poured
        bucket3[1] = bucket3[1] + poured
    if i % 3 == 2:
        poured = min(bucket3[1], bucket1[0]-bucket1[1])
        bucket3[1] = bucket3[1] - poured
        bucket1[1] = bucket1[1] + poured

p = open('mixmilk.out', "x")
p.write(str(bucket1[1]) + "\n")
p.write(str(bucket2[1]) + "\n")
p.write(str(bucket3[1]))
p.close()
