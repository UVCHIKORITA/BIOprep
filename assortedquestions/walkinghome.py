def findpaths(b, p):
    if p == 1:
        if b[0][len(b[0])-1] == 'X' and b[len(b[0])-1][0] == 'X':
            return 0
        elif b[0][len(b[0])-1] == 'X' or b[len(b[0])-1][0] == 'X':
            return 1
        else:
            return 2
    else:
        return 0






cases = int(input())
for i in range(cases):
    n_k = list(map(int, input().strip().split(" ")))
    barn = []
    for q in range(n_k[0]):
        line = []
        for char in input().strip():
            if char == ".":
                line.append("")
            else:
                line.append("X")
        barn.append(line)
    print(findpaths(barn, n_k[1]))