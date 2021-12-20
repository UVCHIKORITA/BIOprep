cases = int(input())
for i in range(cases):
    n_k = list(map(int, input().strip().split(" ")))
    barn = []
    itera = 0
    for q in range(n_k[0]):
        line = []
        for char in input().strip():
            if char == "." and line != [] and line[-1] != [""]:
                line.append([itera-1, itera, "A"])
            else:
                line.append([""])
            itera += 1
        barn.append(line)
