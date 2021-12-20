up = [6, 2, 1, 5]
left = [6, 3, 1, 4]
face_down = 6

# 0 --> up
# 1 --> right
# 2 --> down
# 3 --> left
head = 0

up_ptr = 0
left_ptr = 0
pos = [5, 5]


middle_grid = []
for i in range(3):
    middle_grid.append(list(map(int, input().strip().split(" "))))

grid = []
for k in range(11):
    grid.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

grid[4][4] = middle_grid[0][0]
grid[4][5] = middle_grid[0][1]
grid[4][6] = middle_grid[0][2]
grid[5][4] = middle_grid[1][0]
grid[5][5] = middle_grid[1][1]
grid[5][6] = middle_grid[1][2]
grid[6][4] = middle_grid[2][0]
grid[6][5] = middle_grid[2][1]
grid[6][6] = middle_grid[2][2]

def move():
    global up_ptr, left_ptr, pos, head, face_down
    if head == 0:
        up_ptr += 1
        up_ptr %= 4
        pos[0] -= 1
        pos[0] %= 11
        face_down = up[up_ptr]
    if head == 1:
        left_ptr -= 1
        left_ptr %= 4
        pos[1] += 1
        pos[1] %= 11
        face_down = left[left_ptr]
    if head == 2:
        up_ptr -= 1
        up_ptr %= 4
        pos[0] += 1
        pos[0] %= 11
        face_down = up[up_ptr]
    if head == 3:
        left_ptr += 1
        left_ptr %= 4
        pos[1] -= 1
        pos[1] %= 11
        face_down = left[left_ptr]

def print_curr_pos():
    global pos, grid
    coords = [[pos[0]-1,pos[1]-1], [pos[0]-1,pos[1]], [pos[0]-1,pos[1]+1],
              [pos[0],pos[1]-1], [pos[0],pos[1]], [pos[0],pos[1]+1],
              [pos[0]+1,pos[1]-1], [pos[0]+1,pos[1]], [pos[0]+1,pos[1]+1]]
    i = 1
    output = ""
    for coord in coords:
        if -1 in coord or 11 in coord:
            output += "x"
        else:
            output += str(grid[coord[0]][coord[1]])
        if i % 3 == 0:
            output += "\n"
        i += 1
    return output

def set_new_val():
    global pos, head, grid, face_down
    curr_val = grid[pos[0]][pos[1]]
    print(curr_val)
    curr_val += (7-face_down)
    print(face_down)
    print(head)
    if curr_val > 6:
        curr_val -= 6
    print(curr_val)
    print("-----")
    grid[pos[0]][pos[1]] = curr_val
    if curr_val == 1 or curr_val == 6:
        pass
    elif curr_val == 2:
        head += 1
        head %= 4
    elif curr_val == 3 or curr_val == 4:
        head += 2
        head %= 4
    else:
        head -= 1
        head %= 4
    print(head)
    print("-----")



while True:
    moves = int(input())
    if moves == 0:
        break
    for k in range(moves):
        set_new_val()
        move()
        print(print_curr_pos())