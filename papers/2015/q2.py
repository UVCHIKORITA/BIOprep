inputs = list(map(int, input().strip().split(" ")))
a = inputs[0]
c = inputs[1]
m = inputs[2]
r = 0

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
currentSquares = set()
ptr = 0
while True:
    if ptr == len(ships):
        break
    r = a * r + c
    r %= m
    if len(str(r)) == 0:
        x_cord = 0
        y_cord = 0
    elif len(str(r)) == 1:
        x_cord = int(str(r)[-1])
        y_cord = 0
    else:
        x_cord = int(str(r)[-1])
        y_cord = int(str(r)[-2])
    r = a * r + c
    r %= m
    if r % 2 == 0:
        isValid = True
        for i in range(ships[ptr]):
            if x_cord+i >= 10:
                isValid = False
                break
            elif (x_cord+i, y_cord) in currentSquares:
                isValid = False
                break
        if isValid:
            for i in range(ships[ptr]):
                currentSquares.add((x_cord + i, y_cord))
                currentSquares.add((x_cord + i - 1, y_cord))
                currentSquares.add((x_cord + i + 1, y_cord))
                currentSquares.add((x_cord + i, y_cord + 1))
                currentSquares.add((x_cord + i, y_cord - 1))
                currentSquares.add((x_cord + i - 1, y_cord - 1))
                currentSquares.add((x_cord + i - 1, y_cord + 1))
                currentSquares.add((x_cord + i + 1, y_cord - 1))
                currentSquares.add((x_cord + i + 1, y_cord + 1))
            print(x_cord, y_cord, "H")
            ptr += 1

    else:
        # r is odd
        isValid = True
        for i in range(ships[ptr]):
            if y_cord + i >= 10:
                isValid = False
                break
            elif (x_cord, y_cord + i) in currentSquares:
                isValid = False
                break
        if isValid:
            for i in range(ships[ptr]):
                currentSquares.add((x_cord, y_cord + i))
                currentSquares.add((x_cord, y_cord + i - 1))
                currentSquares.add((x_cord, y_cord + i + 1))
                currentSquares.add((x_cord + 1, y_cord + i))
                currentSquares.add((x_cord + 1, y_cord - i))
                currentSquares.add((x_cord - 1, y_cord + i - 1))
                currentSquares.add((x_cord + 1, y_cord + i - 1))
                currentSquares.add((x_cord - 1, y_cord + i + 1))
                currentSquares.add((x_cord + 1, y_cord + i + 1))
            print(x_cord, y_cord, "V")
            ptr += 1
