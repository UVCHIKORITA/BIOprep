start_end_times = []
times = []
cowbuckets = []
using_buckets = []

f = open('blist.in')
N = int(f.read().strip())
for k in range(N):
    vals = list(map(int, f.read().strip().split(" ")))
    cowbuckets.append(vals[2])
    start_end_times.append([vals[0], vals[1]])
    times.append(vals[0])
    times.append(vals[1])

times.sort()

for time in times:
    pass
    # lol will do eventually