from numpy import double

n, col = [int(x) for x in input().split()]


 

li = []

for i in range(n):

    temp = list(map(float, input().split()))

    li.append(temp)

k = double(input())

mn = -float('inf')

for i in range(n):

    if -1*li[i][1] > mn:

        mn = -1*li[i][1]


 

hi = 1e7

lo= 1e-7 + mn


 

while lo <= hi:

    mid = (lo+hi)/2.0

    ans = 0

    for i in range(n):

        if li[i][1]+mid != 0:

            ans += (li[i][0] / (li[i][1]+mid+0.0))

        if ans < k:

            hi = mid - (1e-7)

        else:

            lo = mid + (1e-7)


 

print(double(lo))