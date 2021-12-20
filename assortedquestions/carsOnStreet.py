# This is sad and broken

cars_array = list(input().strip().split(" "))
cars = []
numpos = 1
i = 0

while i < len(cars_array):
    cars.append(chr(ord('a') + i))
    i += 1

last_letter = max(cars_array)
print(cars_array)
cars_array_new = []
orig_postions = []
for car in cars_array:
    cars_array_new.append("")
    orig_postions.append([])

i = 0

while i < len(cars_array):
    letter = cars[i]
    letter_index = cars_array.index(letter)
    if letter_index == 0:
        cars_array_new[letter_index] = letter
        print(letter)
        print(ord(letter) - ord('a'))
        orig_postions[ord(letter) - ord('a')].append(chr(ord("@") + ord(letter) - ord('a') - 1))
    elif cars_array_new[letter_index - 1] == "":
        print(letter)
        print(ord(letter) - ord('a'))
        cars_array_new[letter_index] = letter
        orig_postions[ord(letter) - ord('a')].append(chr(ord("@") + ord(letter) - ord('a') + letter_index + 1))
    else:
        cars_array_new[letter_index] = "0"
        print(letter)
        print(ord(letter) - ord('a'))
        print(ord("@") + ord(letter) - ord('a') + letter_index)
        j = letter_index - 1
        orig_postions[ord(letter) - ord('a')].append(chr(ord("@") + ord(letter) - ord('a') + letter_index))
        while cars_array_new[j] != '' and j >= 0:
            orig_postions[ord(letter) - ord('a')].append(chr(ord("@") + ord(letter) - ord('a') + j))
            j -= 1
    i += 1


print(orig_postions)