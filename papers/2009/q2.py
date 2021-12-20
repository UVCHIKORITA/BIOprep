grid = []
for i in range(4):
    grid.append(list(input().strip()))

aboveGrid = []
for i in range(8):
    aboveGrid.append(list(grid[i % 4]))

def findBlock(coords, grid, val, visited, q):
    q.pop(0)
    visited.add(coords)
    if 0 < coords[0]:
        if grid[coords[0]-1][coords[1]] == val and (coords[0]-1, coords[1]) not in visited:
            q.insert(0, (coords[0]-1, coords[1]))
    if 0 < coords[1]:
        if grid[coords[0]][coords[1]-1] == val and (coords[0], coords[1]-1) not in visited:
            q.insert(0, (coords[0], coords[1]-1))
    if coords[0] < 3:
        if grid[coords[0]+1][coords[1]] == val and (coords[0]+1, coords[1]) not in visited:
            q.insert(0, (coords[0]+1, coords[1]))
    if coords[1] < 3:
        if grid[coords[0]][coords[1]+1] == val and (coords[0], coords[1]+1) not in visited:
            q.insert(0, (coords[0], coords[1]+1))
    if len(q) == 0:
        return list(visited)
    return findBlock(q[0], grid, val, visited, q)

def findallblocks(grid):
    q = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
    blocks = []
    while len(q) > 0:
        v = findBlock(q[0], grid, grid[q[0][0]][q[0][1]], set(), [q[0]])
        for item in v:
            q.remove(item)
        if len(v) > 1:
            blocks.append(v)
    return blocks

def removeblocks(blocks, grid, score, abovegrid):
    tempscore = 1
    for block in blocks:
        tempscore *= len(block)
        for val in block:
            grid[val[0]][val[1]] = ''
    score += tempscore
    while True:
        i = 3
        isChanged = False
        while i > 0:
            k = 3
            while k >= 0:
                if grid[i][k] == '' and grid[i-1][k] != '':
                    grid[i][k] = grid[i-1][k]
                    grid[i-1][k] = ''
                    isChanged = True
                k -= 1
            i -= 1
        if not isChanged:
            break
    while True:
        i = 3
        isChanged = False
        while i >= 0:
            k = 3
            while k >= 0:
                if grid[i][k] == '' and abovegrid[7][k] != '':
                    grid[i][k] = abovegrid[7][k]
                    abovegrid[7][k] = abovegrid[6][k]
                    abovegrid[6][k] = abovegrid[5][k]
                    abovegrid[5][k] = abovegrid[4][k]
                    abovegrid[4][k] = abovegrid[3][k]
                    abovegrid[3][k] = abovegrid[2][k]
                    abovegrid[2][k] = abovegrid[1][k]
                    abovegrid[1][k] = abovegrid[0][k]
                    abovegrid[0][k] = ''
                    isChanged = True
                k -= 1
            i -= 1
        if not isChanged:
            break
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            abovegrid[i][j] = abovegrid[i+4][j]
            j += 1
        i += 1
    return [grid, abovegrid, score]

score = 0
while True:
    n = int(input().strip())
    isValid = True
    if n == 0:
        break
    for k in range(n):
        blocks = findallblocks(grid)
        if len(blocks) == 0:
            if isValid:
                print("GAME OVER")
                print("SCORE: ", score)
                isValid = False
        else:
            grid_abovegrid_score = removeblocks(blocks, grid, score, aboveGrid)
            grid = grid_abovegrid_score[0]
            aboveGrid = grid_abovegrid_score[1]
            score = grid_abovegrid_score[2]
    if not isValid:
        break
    for line in grid:
        print("".join(line))
    print()
    print(score)