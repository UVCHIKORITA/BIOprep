num_tests = int(input())
n_values = []
watered = []
for i in range(num_tests):
    temp_n = int(input())
    n_values.append(temp_n)
    temp_watered = list(map(int, input().strip().split(" ")))
    watered.append(temp_watered)


def find_flower_state(water_schedule):
    j = 0
    height = 1
    while j < len(water_schedule):
        if j > 0 and water_schedule[j] == 0 and water_schedule[j-1] == 0:
            height = -1
            break
        elif j == 0:
            if water_schedule[j] == 1:
                height += 1
        else:
            if water_schedule[j] == 1 and water_schedule[j-1] == 1:
                height += 5
            elif water_schedule[j] == 1:
                height += 1
        j += 1
    print(height)


for w in watered:
    find_flower_state(w)
