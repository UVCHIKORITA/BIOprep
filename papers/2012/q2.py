import sys
sys.setrecursionlimit(10001)
# Train station format
# 0 <---- Train station letter
# 1 <---- Train station on straight edge <--------- Pointer to position
# 2 <---- Train stations on curved edges <--------- Pointers to positions
# 3 <---- LAZY = 0, FLIP-FLOP = 1
# 4 <---- Direction of orientation <--------------- LEFT = 0, RIGHT = 1

stations = [['A', 3, [4, 5], 0, 0],     # 0
            ['B', 2, [6, 7], 0, 0],     # 1
            ['C', 1, [8, 9], 0, 0],     # 2
            ['D', 0, [10, 11], 0, 0],   # 3
            ['E', 0, [12, 13], 0, 0],   # 4
            ['F', 0, [13, 14], 0, 0],   # 5
            ['G', 1, [14, 15], 0, 0],   # 6
            ['H', 1, [15, 16], 0, 0],   # 7
            ['I', 2, [16, 17], 0, 0],   # 8
            ['J', 2, [17, 18], 0, 0],   # 9
            ['K', 3, [18, 19], 0, 0],   # 10
            ['L', 3, [19, 12], 0, 0],   # 11
            ['M', 20, [11, 4], 0, 0],   # 12
            ['N', 20, [4, 5], 0, 0],    # 13
            ['O', 21, [5, 6], 0, 0],    # 14
            ['P', 21, [6, 7], 0, 0],    # 15
            ['Q', 22, [7, 8], 0, 0],    # 16
            ['R', 22, [8, 9], 0, 0],    # 17
            ['S', 23, [9, 10], 0, 0],   # 18
            ['T', 23, [10, 11], 0, 0],  # 19
            ['U', 21, [12, 13], 0, 0],  # 20
            ['V', 20, [14, 15], 0, 0],  # 21
            ['W', 23, [16, 17], 0, 0],  # 22
            ['X', 22, [18, 19], 0, 0]]  # 23

# Can use the integer representation of letters by ord(letter) - ord('A')
# to get array position of station [0-indexed]

# In similar way can also retrieve info abt which station train is coming from
# without having to use .index() method by looking at where the index of the train is
# in indexes 2 and 3.


# Keep track of which stations visited, use -1 and -2 indexes to get last 2 after
curr_visited = ""

def moveTrain(movesToMake):
    global curr_visited, stations
    if movesToMake == 0:
        return curr_visited[-2:]
    curr_index = ord(curr_visited[-1]) - ord('A')
    if ord(curr_visited[-2]) - ord('A') == stations[curr_index][1]:
        # Means is coming from a straight edge
        curr_visited += chr(stations[curr_index][2][stations[curr_index][4]] + ord('A'))
        if stations[curr_index][3] == 1:
            stations[curr_index][4] += 1
            stations[curr_index][4] %= 2
    else:
        # Means is coming from a curved edge
        curr_visited += chr(stations[curr_index][1] + ord('A'))
        """
        if stations[curr_index][3] == 0:    
            if stations[curr_index][2].index(ord(curr_visited[-2])-ord('A')) != stations[curr_index][4]:
                    stations[curr_index][4] += 1
                    stations[curr_index][4] %= 2
        """
    return moveTrain(movesToMake-1)


high_stations = list(input().strip())
for letter in high_stations:
    stations[ord(letter)-ord('A')][3] = 1

curr_visited += input().strip()

N = int(input().strip())

print(moveTrain(N))