import math

n = input()
p_list = list(map(int, input().strip().split(" ")))
t_list = list(map(int, input().strip().split(" ")))
difflist = []
i = 0
mindiff = math.inf
while i < len(p_list):
    if abs(p_list[i]-t_list[i]) < mindiff and p_list[i]-t_list[i] != 0 and mindiff == math.inf:
        mindiff = abs(p_list[i] - t_list[i])
    difflist.append(p_list[i] - t_list[i])
    i += 1

while difflist[0] == 0:
    difflist.pop(0)
while difflist[-1] == 0:
    difflist.pop(-1)

k = 0
count = 0
if len(difflist) % 2 == 0:
    while k <= math.ceil(len(difflist)/2):
        count += abs(int(difflist[k]) - int(difflist[-k]))
        p = k
        for q in difflist[k:-k]:
            difflist[p] -= int(difflist[k]) - int(difflist[-k])
            difflist[-p] -= int(difflist[k]) - int(difflist[-k])
            p += 1
        k += 1
else:
    while k <= math.ceil(len(difflist) / 2):
        count += abs(int(difflist[k]) - int(difflist[-k - 1]))
        p = k
        for q in difflist[k:-k]:
            difflist[p] -= int(difflist[k]) - int(difflist[-k])
            difflist[-p] -= int(difflist[k]) - int(difflist[-k])
            p += 1
        k += 1
print(count + mindiff)