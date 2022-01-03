rotorA = [[0, 0], [1, 3], [2, 1], [3, 2]]
rotorB = [[0, 0], [1, 2], [2, 1], [3, 3]]

# 3 - rotorB will give thing to go back by

n = int(input())
na = n % 4
nb = (n // 4) % 4

for i in range(na):
    for arr in rotorA:
        arr[0] -= 1
        arr[1] -= 1
        arr[0] %= 4
        arr[1] %= 4

rotorA = sorted(rotorA, key=lambda x:x[0])

for i in range(nb):
    for arr in rotorB:
        arr[0] -= 1
        arr[1] -= 1
        arr[0] %= 4
        arr[1] %= 4

rotorB = sorted(rotorB, key=lambda x:x[0])

word = input()
out = ""

for char in word:
    k = ord(char) - ord("A")
    print(rotorA)
    print(rotorB)
    pathTo = 3 - rotorB[rotorA[k][1]][1]
    rotorA = sorted(rotorA, key=lambda x: x[1])
    rotorB = sorted(rotorB, key=lambda x: x[1])
    out += chr(rotorA[rotorB[pathTo][0]][0] + ord("A"))
    nb += 1
    nb %= 4
    if nb == 3:
        for arr in rotorB:
            arr[0] -= 1
            arr[1] -= 1
            arr[0] %= 4
            arr[1] %= 4
    for arr in rotorA:
        arr[0] -= 1
        arr[1] -= 1
        arr[0] %= 4
        arr[1] %= 4
    rotorA = sorted(rotorA, key=lambda x: x[0])
    rotorB = sorted(rotorB, key=lambda x: x[0])

print(out)