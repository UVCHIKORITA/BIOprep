inputs = list(map(int, input().strip().split()))
start_a = inputs[0]
mod_a = inputs[1]
start_b = inputs[2]
mod_b = inputs[3]
turns = inputs[4]


# GRID
#      01 02 03 04 05 06
#      07 08 09 10 11 12
#      13 14 15 16 17 18
#      19 20 21 22 23 24
#      25 26 27 28 29 30
#      31 32 33 34 35 36
#
gridList = {
    1: [2, 7],
    2: [3, 8, 1],
    3: [4, 9, 2],
    4: [5, 10, 3],
    5: [6, 11, 4],
    6: [12, 5],
    7: [1, 8, 13],
    8: [2, 9, 14, 7],
    9: [3, 10, 15, 8],
    10: [4, 11, 16, 9],
    11: [5, 12, 17, 10],
    12: [6, 18, 11],
    13: [7, 14, 19],
    14: [8, 15, 20, 13],
    15: [9, 16, 21, 14],
    16: [10, 17, 22, 15],
    17: [11, 18, 23, 16],
    18: [12, 24, 17],
    19: [13, 20, 25],
    20: [14, 21, 26, 19],
    21: [15, 22, 27, 20],
    22: [16, 23, 28, 21],
    23: [17, 24, 29, 22],
    24: [18, 30, 23],
    25: [19, 26, 31],
    26: [20, 27, 32, 25],
    27: [21, 28, 33, 26],
    28: [22, 29, 34, 27],
    29: [23, 30, 35, 28],
    30: [24, 36, 29],
    31: [25, 32],
    32: [26, 33, 31],
    33: [27, 34, 32],
    34: [28, 35, 33],
    35: [29, 36, 34],
    36: [30, 35]
}
grid = [["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*"]]
moves = []

def findSquares(line , c):
    found = False
    min_line = min(line)
    max_line = max(line)
    line = [min_line, max_line]
    if line[0] + 1 == line[1] or line[0] - 1 == line[1]:
        if line[0] > 6:
            if [line[0], line[0] - 6] in moves or [line[0] - 6, line[0]] in moves:
                if [line[1], line[1] - 6] in moves or [line[1] - 6, line[1]] in moves:
                    if [line[0] - 6, line[1] - 6] in moves or [line[1] - 6, line[0] - 6] in moves:
                        found = True
                        grid[(line[0] - 6) // 6][(line[0]) % 6 - 1] = c
        if line[0] < 31:
            if [line[0], line[0] + 6] in moves or [line[0] + 6, line[0]] in moves:
                if [line[1], line[1] + 6] in moves or [line[1] + 6, line[1]] in moves:
                    if [line[0] + 6, line[1] + 6] in moves or [line[1] + 6, line[0] + 6] in moves:
                        found = True
                        grid[line[0] // 6][(line[0]) % 6 - 1] = c
        return found
    else:
        if line[0] % 6 != 1:
            if [line[0], line[0] + 1] in moves or [line[0] + 1, line[0]] in moves:
                if [line[1], line[1] + 1] in moves or [line[1] + 1, line[1]] in moves:
                    if [line[0] + 1, line[1] + 1] in moves or [line[1] + 1, line[0] + 1] in moves:
                        found = True
                        grid[line[0] // 6][line[0] % 6 - 2] = c
        if line[0] % 6 > 0:
            if [line[0], line[0] - 1] in moves or [line[0] - 1, line[0]] in moves:
                if [line[1], line[1] - 1] in moves or [line[1] - 1, line[1]] in moves:
                    if [line[0] - 1, line[1] - 1] in moves or [line[1] - 1, line[0] - 1] in moves:
                        found = True
                        grid[line[0] // 6][line[0] % 6 - 1] = c
        return found

def findValidMove(pos, c):
    if c == "X":
        for item in gridList[pos]:
            if [pos, item] in moves or [item, pos] in moves:
                pass
            else:
                moves.append([pos, item])
                if findSquares([pos, item], c):
                    return [True, True]
                return [True, False]
        return [False, False]
    else:
        for item in gridList[pos][::-1]:
            if [pos, item] in moves or [item, pos] in moves:
                pass
            else:
                moves.append([pos, item])
                if findSquares([pos, item], c):
                    return [True, True]
                return [True, False]
        return [False, False]


for turn in range(turns):
    if turn % 2 == 0:
        start_a += mod_a
        start_a %= 36
        if start_a == 0:
            start_a = 36
        while not findValidMove(start_a, "X"):
            start_a += 1
            start_a %= 36
            if start_a == 0:
                start_a = 36

    else:
        start_b += mod_b
        start_b %= 36
        if start_b == 0:
            start_b = 36

