def romanify(val):
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    powOfTen = len(str(val)) - 1
    val_array = list(map(int, str(val).split()))
    val_array.reverse()
    i = 0
    output = ""
    for digit in val_array:
        if digit == 4:
            output += roman_numerals[2 * (powOfTen - i)]
            output += roman_numerals[2 * (powOfTen - i) + 1]
        elif digit == 9:
            output += roman_numerals[2 * (powOfTen - i)]
            output += roman_numerals[2 * (powOfTen - i) + 2]
        elif digit == 5:
            output += roman_numerals[2 * (powOfTen - i) + 1]
        elif digit < 5:
            output += (roman_numerals[2 * (powOfTen - i)]) * digit
        else:
            output += roman_numerals[2 * (powOfTen - i) + 1]
            output += (roman_numerals[2 * (powOfTen - i)]) * (digit - 5)
        i += 1
    return output


def look_and_say(numeral, n):
    i = 0
    while i < n:
        output = ""
        current_char = ''
        char_list = []
        char_count = []
        current_char_count = 0
        for char in numeral:
            if char != current_char:
                if current_char != '':
                    char_list.append(current_char)
                    char_count.append(current_char_count)
                current_char = char
                current_char_count = 1
            else:
                current_char_count += 1
        char_list.append(current_char)
        char_count.append(current_char_count)
        j = 0
        for val in char_count:
            output += romanify(val)
            output += char_list[j]
            j += 1
        numeral = output
        i += 1
    i_count = 0
    v_count = 0
    for char in numeral:
        if char == "I":
            i_count += 1
        elif char == "V":
            v_count += 1
    print(str(i_count)+" "+str(v_count))


print("Input numeral: ")
inputNo = input().strip()
print("Input n: ")
inputN = int(input().strip())
look_and_say(inputNo, inputN)
