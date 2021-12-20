def gen_cards(values):
    suits = ['C', 'H', 'S', 'D']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    row = []
    order = []
    for q in range(4):
        for i in range(13):
            order.append(numbers[i]+suits[q])
    count = values[0] - 1
    val = 0
    while len(order) > 0:
        row.append([order[count], 1])
        order.pop(count)
        if len(order) == 0:
            break
        val += 1
        val %= 6
        count += values[val] - 1
        count %= len(order)
    return row

def strategy_1(values):
    i = len(values) - 1
    foundMove = False
    while i >= 1:
        foundMove = False
        if values[i-1][0][1] == values[i][0][1] or values[i-1][0][0] == values[i][0][0]:
            foundMove = True
            values[i - 1] = [values[i][0], values[i - 1][1] + values[i][1]]
            values.pop(i)
        if i >= 3:
            if foundMove == False and (values[i-3][0][0] == values[i][0][0] or values[i-3][0][1] == values[i][0][1]):
                foundMove = True
                values[i-3] = [values[i][0], values[i-3][1] + values[i][1]]
                values.pop(i)
        if foundMove:
            break
        i -= 1
    if not foundMove:
        return str(str(len(values)) + " " + values[0][0])
    return strategy_1(values)

def strategy_2(values):
    i = len(values) - 1
    foundMove = False
    maxPile = 0
    maxPileIndexes = [] # LEFT, RIGHT
    while i >= 1:
        if values[i - 1][0][1] == values[i][0][1] or values[i - 1][0][0] == values[i][0][0]:
            foundMove = True
            if values[i - 1][1] + values[i][1] > maxPile:
                maxPile = values[i - 1][1] + values[i][1]
                maxPileIndexes = [i-1, i]
        if i >= 3:
            if values[i - 3][0][0] == values[i][0][0] or values[i - 3][0][1] == values[i][0][1]:
                foundMove = True
                if values[i - 3][1] + values[i][1] > maxPile:
                    maxPile = values[i - 3][1] + values[i][1]
                    maxPileIndexes = [i - 3, i]
        i -= 1
    if foundMove:
        values[maxPileIndexes[0]] = [values[maxPileIndexes[1]][0], values[maxPileIndexes[0]][1] + values[maxPileIndexes[1]][1]]
        values.pop(maxPileIndexes[1])
    else:
        return str(str(len(values)) + " " + values[0][0])
    return strategy_2(values)

def find_valid_moves(values):
    i = len(values) - 1
    possibilities = 0
    while i >= 1:
        if values[i-1][0][1] == values[i][0][1] or values[i-1][0][0] == values[i][0][0]:
            possibilities += 1
        if i >= 3:
            if (values[i-3][0][0] == values[i][0][0] or values[i-3][0][1] == values[i][0][1]):
                possibilities += 1
        i -= 1
    return possibilities




# IS BROKEN :(
def strategy_3(values):
    i = len(values) - 1
    foundMove = False
    maxMoves = -1
    maxMovesSwap = []  # LEFT, RIGHT
    while i >= 1:
        if values[i - 1][0][1] == values[i][0][1] or values[i - 1][0][0] == values[i][0][0]:
            foundMove = True
            tempvalues = list(values)
            tempvalues[i - 1] = [tempvalues[i][0], 1]
            k = find_valid_moves(tempvalues)
            if k > maxMoves:
                maxMoves = k
                maxMovesSwap = [i - 1, i]
        if i >= 3:
            if values[i - 3][0][0] == values[i][0][0] or values[i - 3][0][1] == values[i][0][1]:
                foundMove = True
                tempvalues = list(values)
                tempvalues[i - 3] = [tempvalues[i][0], 1]
                k = find_valid_moves(tempvalues)
                if k > maxMoves:
                    maxMoves = k
                    maxMovesSwap = [i - 3, i]
        i -= 1
    if foundMove:
        values[maxMovesSwap[0]] = [values[maxMovesSwap[1]][0], 1]
        values.pop(maxMovesSwap[1])
    else:
        return str(str(len(values)) + " " + values[0][0])
    return strategy_3(values)


inputs = list(map(int, input().strip().split(" ")))
piles = gen_cards(inputs)
piles1 = list(piles)
piles2 = list(piles)
print(piles[0][0] + " " + piles[-1][0])
print(strategy_1(piles))
print(strategy_2(piles1))
print(strategy_3(piles2))