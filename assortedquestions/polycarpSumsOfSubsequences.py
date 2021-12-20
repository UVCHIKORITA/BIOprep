testCases = int(input())
for i in range(testCases):
    case = list(map(int, input().strip().split(" ")))
    ABC = case[-1]
    BC = case[-2]
    AC = case[-3]
    A = ABC - BC
    C = AC - A
    B = BC - C
    print(A, " ", B, " ", C, " ")
