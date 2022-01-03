tiles = [{"g": [1, 3], "r": [2, 4]}, {"r": [1, 3], "g": [2, 4]}, {"g": [2, 3], "r": [1, 4]}, {"g": [3, 4], "r": [1, 2]}, {"g": [1, 4], "r": [2, 3]}, {"g": [1, 2], "r": [3, 4]}]


n = int(input())
board = []

for i in range(n):
    row = list(map(int, input().strip().split(" ")))
    board.append(row)
