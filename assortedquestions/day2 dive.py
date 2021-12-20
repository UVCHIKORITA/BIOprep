array = []
while True:
    val = input()
    if val == '':
        break
    else:
        array.append(list(val.strip().split(" ")))

depth = 0
h_pos = 0
aim = 0
for item in array:
    if item[0] == "forward":
        h_pos  += int(item[1])
        depth += aim * int(item[1])
    if item[0] == "down":
        aim += int(item[1])
    if item[0] == "up":
        aim -= int(item[1])

print(depth * h_pos)