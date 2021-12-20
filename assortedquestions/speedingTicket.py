f = open("speeding.in")
N_M = list(map(int, f.readline().strip().split(" ")))
limits = []
speed = []
maxAboveLimit = 0
for i in range(N_M[0]):
    segment = list(map(int, f.readline().strip().split(" ")))
    for k in range(segment[0]):
        limits.append(segment[1])
for i in range(N_M[1]):
    segment = list(map(int, f.readline().strip().split(" ")))
    for k in range(segment[0]):
        speed.append(segment[1])
f.close()
p = 0
while p < len(limits):
    maxAboveLimit = max(maxAboveLimit, speed[p] - limits[p])
    p += 1

q = open("speeding.out", "w")
q.write(str(maxAboveLimit))
q.close()