print("Input lines: ")
line1 = input().strip().upper()
line2 = input().strip().upper()

alphabet = []
for i in range(26):
    alphabet.append(chr(ord('A') + i))
alphabet.remove('Q')

matrix1 = [[],[],[],[],[]]
matrix2 = [[],[],[],[],[]]
matrix1needtovisit = alphabet
matrix2needtovisit = alphabet
matrix1visited = []
matrix2visited = []

if 'Q' not in line1 and 'Q' not in line2:
    charcount = 0
    while len(matrix1needtovisit) > 0:
        if len(line1) > 0:
            try:
                print(matrix1needtovisit)
                print(charcount // 5)
                char_to_add = line1[0]
                if char_to_add not in matrix1visited:
                    matrix1needtovisit.remove(char_to_add)
                    matrix1[charcount // 5].append(char_to_add)
                    matrix1visited.append(char_to_add)
            except Exception as e:
                print(e)
                charcount -= 1
            line1 = line1[1:]
        else:
            print(matrix1needtovisit)
            print(charcount // 5)
            char_to_add = matrix1needtovisit[0]
            if char_to_add not in matrix1visited:
                matrix1[charcount // 5].append(char_to_add)
                matrix1needtovisit = matrix1needtovisit[1:]
                matrix1visited.append(char_to_add)
        charcount += 1
    charcount = 0
    while len(matrix2needtovisit) > 0:
        if len(line2) > 0:
            try:
                char_to_add = line2[0]
                if char_to_add not in matrix2visited:
                    matrix2needtovisit.remove(char_to_add)
                    matrix2[4 - (charcount // 5)].insert(0, char_to_add)
                    matrix2visited.append(char_to_add)
            except:
                charcount -= 1
            line2 = line2[1:]
        else:
            char_to_add = matrix2needtovisit[0]
            if char_to_add not in matrix2visited:
                matrix2[4 - (charcount // 5)].insert(0, matrix2needtovisit[0])
                matrix2needtovisit = matrix2needtovisit[1:]
                matrix2visited.append(char_to_add)
        charcount += 1
    for p in range(5):
        print(p)

        print(matrix1[p][0], " ", matrix1[p][1], " ", matrix1[p][2], " ", matrix1[p][3], " ", matrix1[p][4], "    ", matrix2[p][0], " ", matrix2[p][1], " ", matrix2[p][2], " ", matrix2[p][3], " ", matrix2[p][4])