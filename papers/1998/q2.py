pig_cords = list(map(int, input().strip().split(" ")))
farmer_cords = list(map(int, input().strip().split(" ")))
grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
farmer_dir = 0
pig_dir = 0
dir_pos = ["UP", "RIGHT", "DOWN", "LEFT"]

pig_cords[0] = pig_cords[0] - 1
pig_cords[1] = pig_cords[1] - 1
farmer_cords[0] = farmer_cords[0] - 1
farmer_cords[1] = farmer_cords[1] - 1

grid[farmer_cords[1]][farmer_cords[0]] = "F"
if grid[pig_cords[1]][pig_cords[0]] == "F":
    grid[pig_cords[1]][pig_cords[0]] = "+"
else:
    grid[pig_cords[1]][pig_cords[0]] = "P"


def display_grid():
    for row in grid[::-1]:
        print("".join(row))


display_grid()


def move(direction, coords, c):
    if direction == 0:
        if coords[1] < 9 and grid[coords[1] + 1][coords[0]] != "*":
            coords[1] += 1
        else:
            return move(1, coords, c)
        grid[coords[1]][coords[0]] = c
        return [0, coords]
    elif direction == 1:
        if coords[0] < 9 and grid[coords[1]][coords[0] + 1] != "*":
            coords[0] += 1
        else:
            return move(2, coords, c)
        grid[coords[1]][coords[0]] = c
        return [1, coords]
    elif direction == 2:
        if coords[1] > 0 and grid[coords[1] - 1][coords[0]] != "*":
            coords[1] -= 1
        else:
            return move(3, coords, c)
        grid[coords[1]][coords[0]] = c
        return [2, coords]
    else:
        if coords[0] > 0 and grid[coords[1]][coords[0] - 1] != "*":
            coords[0] -= 1
        else:
            return move(0, coords, c)
        grid[coords[1]][coords[0]] = c
        return [3, coords]


while True:
    x = input().strip()
    if x == "X":
        break
    elif x[0] == "T":
        for i in range(int(x[2])):
            tree_cords = list(map(int, input().strip().split(" ")))
            tree_cords[0] -= 1
            tree_cords[1] -= 1
            grid[tree_cords[1]][tree_cords[0]] = "*"
        display_grid()
    elif x[0] == "M":
        for i in range(int(x[2])):
            grid[farmer_cords[1]][farmer_cords[0]] = "."
            grid[pig_cords[1]][pig_cords[0]] = "."
            outputs = move(farmer_dir, farmer_cords, "F")
            print(outputs)
            farmer_dir = outputs[0]
            farmer_coords = outputs[1]
            outputs = move(pig_dir, pig_cords, "P")
            print(outputs)
            pig_dir = outputs[0]
            pig_coords = outputs[1]
            if pig_coords == farmer_coords:
                print("MET AT MOVE", i)
                grid[pig_cords[1]][pig_cords[0]] = "+"
        display_grid()

# I'm understanding the program wrong i think |:(
