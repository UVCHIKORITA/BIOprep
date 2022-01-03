inputs = input().strip().split(" ")
letters = inputs[0]
p = int(inputs[1])
q = int(inputs[2])

max_letters = list('ABCDEFGHIJ')
chosen_letters = []
letter_map = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
    "I": [],
    "J": []
}
max_letters = max_letters[:len(letters)+2]
unchosen = list(max_letters)
while letters:
    k = ""
    for l in max_letters:
        if l not in chosen_letters and l not in letters:
            k = l
            break
    letter_map[k].append(letters[0])
    letter_map[letters[0]].append(k)
    chosen_letters.append(k)
    unchosen.remove(k)
    letters = letters[1:]
letter_map[unchosen[0]].append(unchosen[1])
letter_map[unchosen[1]].append(unchosen[0])
for l in max_letters:
    letter_map[l] = sorted(letter_map[l])
    print("".join(letter_map[l]))

# After this point work only with letter map, max_letters and variables below

visited = {}
exit_count = {}
for letter in max_letters:
    visited[letter] = 0
    exit_count[letter] = []
    for l in letter_map[letter]:
        exit_count[letter].append(0)
q -= p
visited["A"] += 1

def move(room):
    if room not in max_letters:
        raise Exception("Wait. That's Illegal.")
    if visited[room] % 2 == 0:
        i = 0
        for k in exit_count[room]:
            if k % 2 == 1:
                i = exit_count[room].index(k)
                break
        if i != len(exit_count[room]) - 1:
            visited[letter_map[room][i + 1]] += 1
            exit_count[room][i + 1] += 1
            return letter_map[room][i + 1]
        else:
            visited[letter_map[room][i]] += 1
            exit_count[room][i] += 1
            return letter_map[room][i]
    else:
        visited[letter_map[room][0]] += 1
        exit_count[room][0] += 1
        return letter_map[room][0]

k = move("A")
for i in range(p - 1):
    k = move(k)
print(k, end="")
for i in range(p-1, q+3):
    k = move(k)
print(k)
