digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
digitValues = [1, 5, 10, 50, 100, 500, 1000]


def repr_digit(log10, val):
    if val == 5:
        return digits[2*log10-1]
    if val == 4:
        returnval = digits[2*log10-2]
        returnval += digits[2*log10-1]
        return returnval
    if val == 9:
        returnval = digits[2 * log10]
        returnval += digits[2 * log10 + 2]
        return returnval
    elif val == 0 or val == 1 or val == 2 or val == 3:
        i = 0
        returnval = ''
        while i < val:
            returnval += digits[2 * log10]
            i += 1
        return returnval
    else:
        returnval = ''
        returnval += digits[2 * log10 + 1]
        val -= 5
        i = 0
        while i < val:
            returnval += digits[2 * log10]
            i += 1
        return returnval


print("Please enter number to be converted to roman numeral: ")
num = list(map(int, input().strip()))[::-1]
log10array = []
log10 = 0
for val in num:
    log10array.append(log10)
    log10 += 1
log10array = log10array[::-1]
num = num[::-1]
pos = 0
numeral = ''
for val in num:
    numeral += repr_digit(log10array[pos], val)
    pos += 1
print(numeral)

# For 1b, convert to normal numbers, add, then input into above

# For 1c, loop through and check

j = 1
sumAccNumSmall = 0
sumAccNumBig = 0
while j <= 3999:
    string_j = str(j)
    j_arr = list(map(int, string_j))[::-1]
    log10array = []
    log10 = 0
    for val in j_arr:
        log10array.append(log10)
        log10 += 1
    log10array = log10array[::-1]
    j_arr = j_arr[::-1]
    pos = 0
    numeral = ''
    for val in j_arr:
        numeral += repr_digit(log10array[pos], val)
        pos += 1
    if len(string_j) > len(numeral):
        sumAccNumBig += 1
    if len(string_j) < len(numeral):
        sumAccNumSmall += 1
    j += 1

print("Number of numbers with fewer characters in roman numeral form: "+str(sumAccNumBig))
print("Number of numbers with more characters in roman numeral form: "+str(sumAccNumSmall))
