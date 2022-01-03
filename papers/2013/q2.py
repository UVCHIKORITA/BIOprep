from time import sleep

grid = [['S1','S2','S3','S4','S5'],
        ['.', '.', '.', '.', '.' ],
        ['.', '.', '*', '.', '.' ],
        ['.', '.', '.', '.', '.' ],
        ['F1','F2','F3','F4','F5']]

curr_neutron_pos = [2, 2]
curr_second_poss = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
curr_first_poss = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
player_winning_pos = [0, 4]

first_player_order = list(map(int, input().strip().split(" ")))
second_player_order = list(map(int, input().strip().split(" ")))
first_player_ptr = 0
second_player_ptr = 0


def find_surround(point):
    surrounding = []
    if point[0] > 0:
        if grid[point[0] - 1][point[1]] == ".":
            surrounding.append([point[0] - 1, point[1]])
        if point[1] < 4:
            if grid[point[0] - 1][point[1] + 1] == ".":
                surrounding.append([point[0] - 1, point[1] + 1])
        if point[1] > 0:
            if grid[point[0] - 1][point[1] - 1] == ".":
                surrounding.append([point[0] - 1, point[1] + 1])
    if point[1] > 0:
        if grid[point[0]][point[1] - 1] == ".":
            surrounding.append([point[0], point[1] - 1])
    if point[1] < 4:
        if grid[point[0]][point[1] + 1] == ".":
            surrounding.append([point[0], point[1] + 1])
    if point[0] < 4:
        if grid[point[0] + 1][point[1]] == ".":
            surrounding.append([point[0] + 1, point[1]])
        if point[1] < 4:
            if grid[point[0] + 1][point[1] + 1] == ".":
                surrounding.append([point[0] + 1, point[1] + 1])
        if point[1] > 0:
            if grid[point[0] + 1][point[1] - 1] == ".":
                surrounding.append([point[0] + 1, point[1] + 1])
    return surrounding


def neutron_move(player):
    global curr_neutron_pos, player_winning_pos

    # player 1 -----> player = 0
    # player 2 -----> player = 1

    # direction 1
    all_moves = []
    other_winning_moves = []


    i = curr_neutron_pos[0]
    end_dir_1 = []
    while i > 0:
        if grid[i-1][curr_neutron_pos[1]] != '.':
            break
        if i == 0:
            break
        end_dir_1 = [i-1, curr_neutron_pos[1]]
        i -= 1
    print(end_dir_1)
    print(player_winning_pos[player])
    if end_dir_1[0] == player_winning_pos[player]:
        grid[end_dir_1[0]][end_dir_1[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_1
        return "ENDGAME"
    elif end_dir_1[0] == player_winning_pos[(player+1)%2]:
        other_winning_moves.append(end_dir_1)
    all_moves.append(end_dir_1)

    # direction 2
    i = curr_neutron_pos[0]
    j = curr_neutron_pos[1]
    end_dir_2 = []
    while i > 0 and j < 4:
        if grid[i-1][j+1] != '.':
            break
        end_dir_2 = [i - 1, j + 1]
        i -= 1
        j += 1
    if end_dir_2[0] == player_winning_pos[player]:
        grid[end_dir_2[0]][end_dir_2[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_2
        return "ENDGAME"
    elif end_dir_2[0] == player_winning_pos[(player+1)%2]:
        other_winning_moves.append(end_dir_2)
    all_moves.append(end_dir_2)

    # direction 3
    j = curr_neutron_pos[1]
    end_dir_3 = []
    while j < 4:
        if grid[curr_neutron_pos[0]][j + 1] != '.':
            break
        end_dir_3 = [curr_neutron_pos[0], j + 1]
        j += 1
    all_moves.append(end_dir_3)

    # direction 4
    j = curr_neutron_pos[1]
    i = curr_neutron_pos[0]
    end_dir_4 = []
    while j < 4 and i < 4:
        if grid[i + 1][j + 1] != '.':
            break
        end_dir_4 = [i + 1, j + 1]
        i += 1
        j += 1
    if end_dir_4[0] == player_winning_pos[player]:
        grid[end_dir_4[0]][end_dir_4[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_4
        return "ENDGAME"
    elif end_dir_4[0] == player_winning_pos[(player + 1) % 2]:
        other_winning_moves.append(end_dir_4)
    all_moves.append(end_dir_4)

    # direction 5
    i = curr_neutron_pos[0]
    end_dir_5 = []
    while i < 4:
        if grid[i + 1][curr_neutron_pos[1]] != '.':
            break
        end_dir_5 = [i + 1, curr_neutron_pos[1]]
        i += 1
    if end_dir_5[0] == player_winning_pos[player]:
        grid[end_dir_5[0]][end_dir_5[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_5
        return "ENDGAME"
    elif end_dir_5[0] == player_winning_pos[(player + 1) % 2]:
        other_winning_moves.append(end_dir_5)
    all_moves.append(end_dir_5)

    # direction 6
    i = curr_neutron_pos[0]
    j = curr_neutron_pos[1]
    end_dir_6 = []
    while i < 4 and j > 0:
        if grid[i + 1][j - 1] != '.':
            break
        end_dir_6 = [i + 1, j - 1]
        i += 1
        j -= 1
    if end_dir_6[0] == player_winning_pos[player]:
        grid[end_dir_6[0]][end_dir_6[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_6
        return "ENDGAME"
    elif end_dir_6[0] == player_winning_pos[(player + 1) % 2]:
        other_winning_moves.append(end_dir_6)
    all_moves.append(end_dir_6)

    # direction 7
    j = curr_neutron_pos[1]
    end_dir_7 = []
    while j > 0:
        if grid[curr_neutron_pos[0]][j - 1] != '.':
            break
        end_dir_7 = [curr_neutron_pos[0], j - 1]
        j -= 1
    all_moves.append(end_dir_7)

    # direction 8
    j = curr_neutron_pos[1]
    i = curr_neutron_pos[0]
    end_dir_8 = []
    while j > 0 and i > 0:
        if grid[i - 1][j - 1] != '.':
            break
        end_dir_8 = [i - 1, j - 1]
        i -= 1
        j -= 1
    if end_dir_8[0] == player_winning_pos[player]:
        grid[end_dir_8[0]][end_dir_8[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = end_dir_8
        return "ENDGAME"
    elif end_dir_8[0] == player_winning_pos[(player + 1) % 2]:
        other_winning_moves.append(end_dir_8)
    all_moves.append(end_dir_8)

    # Cover case where no winning move is found but a win for opponent exists
    if len(other_winning_moves) > 0:
        moveToMake = other_winning_moves[0]
        grid[moveToMake[0]][moveToMake[1]] = "*"
        grid[curr_neutron_pos[0]][curr_neutron_pos[1]] = "."
        curr_neutron_pos = moveToMake
        return "ENDGAME"

    # Cover other case, allow move next player ptr
    print("HELLO")
    global chosenMove
    chosenMove = []
    print(all_moves)
    for move in all_moves:
        print(move)
        if len(move) == 0:
            continue
        else:
            if player == 0:
                print(find_surround(curr_first_poss[first_player_ptr]))
                if [move[0], move[1]] in find_surround(curr_first_poss[first_player_ptr]):
                    arr = find_surround(curr_first_poss[first_player_ptr])
                    arr.remove([move[0], move[1]])
                    if len(arr) != 0:
                        chosenMove = move
                        break
                else:
                    chosenMove = move
                    break
            else:
                if [move[0], move[1]] in find_surround(curr_second_poss[second_player_ptr]):
                    arr = find_surround(curr_second_poss[second_player_ptr])
                    arr.remove([move[0], move[1]])
                    if len(arr) != 0:
                        chosenMove = move
                        break
                else:
                    chosenMove = move
                    break
    if len(chosenMove) == 0:
        return "ENDGAME"
    else:
        grid[chosenMove[0]][chosenMove[1]] = "*"
        grid[chosenMove[0]][chosenMove[1]] = "."
        curr_neutron_pos = chosenMove
        return "C"







moveCounter = 1
while True:
    if moveCounter % 2 == 1:
        # Time for the first player!
        print(neutron_move(0))
        for line in grid:
            print(" ".join(line))
        sleep(1)
        first_player_ptr += 1
        first_player_ptr %= 5
    else:
        # Time for the second player!
        print(neutron_move(1))
        for line in grid:
            print(" ".join(line))
        sleep(1)
        second_player_ptr += 1
        second_player_ptr %= 5
    moveCounter += 1
    if curr_neutron_pos[0] == 0 or curr_neutron_pos[0] == 4:
        break
    if moveCounter == 1 or moveCounter == 2:
        pass