dial_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inputs = list(input().strip().split(" "))
N = int(inputs[0])
dial_2 = []
dial_1_cp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
currentletter = ''
for k in range(26):
    if currentletter != '':
        index = dial_1_cp.index(currentletter)
        dial_1_cp.remove(currentletter)
        if len(dial_1_cp) > 1:
            currentletter = dial_1_cp[(index+N-1)%(len(dial_1_cp))]
        else:
            break
    else:
        currentletter = dial_1_cp[(dial_1_cp.index('A') + N - 1) % (len(dial_1_cp))]
    dial_2.append(currentletter)

output = ""
for p in range(6):
    output += dial_2[p]

print(output)

buffer = 0
output = ""
for char in inputs[1]:
    output += dial_2[(dial_1.index(char) + buffer) % 25]
    buffer += 1

print(output)