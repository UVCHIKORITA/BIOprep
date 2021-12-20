# SUCCESS!

import itertools
cars_inputs = list(input().strip().split(" "))
cars_array = [cars_inputs[0][i] for i in range(0,len(cars_inputs[0]))]
o = int(cars_inputs[1])


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def convert_index(index):
    return chr(index + ord('@') + 1)


max_letter = max(cars_array)
letter_pos = []
for c in char_range('a', max_letter):
    l_index = cars_array.index(c)
    if l_index == 0:
        letter_pos.append([convert_index(l_index)])
    elif c == 'a':
        letter_pos.append([convert_index(l_index)])
    else:
        i = l_index
        letter_pos.append([])
        while i >= 0 and cars_array[i] <= c:
            letter_pos[ord(c) - ord('a')].append(convert_index(i))
            i -= 1

cars_preferences = []

for tup in list(itertools.product(*letter_pos)):
    cars_preferences.append(''.join(list(tup)))

cars_preferences.sort()
print(cars_preferences[o])