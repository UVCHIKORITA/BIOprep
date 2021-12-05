"""


In Roman times, numbers were represented using letters. The way of doing this, known as Roman
Numerals, is often seen depicting the copyright date on films and television.
Roman numerals are conventionally defined to represent numbers using seven letters: I=1, V=5,
X=10, L=50, C=100, D=500 and M=1000. Numbers other than these are formed by placing letters
together from left to right, in descending order of size, and adding their values. The basic rule is to
always use the biggest numeral possible (e.g. 15 is represented as XV, but never as VVV, VX or XIIIII).
Letters may not appear more than three times in a row, so there are six exceptions to these rules – the
combinations IV, IX, XL, XC, CD and CM. In these cases a letter is placed before one of greater value,
and the smaller value is subtracted from the larger, e.g. CD = 400.
1 (a)
[20 marks]
Write a program which accepts a number, between 1 and 3999 inclusive, and outputs
the same number in Roman numerals


"""
digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
digitValues = [1, 5, 10, 50, 100, 500, 1000]  # Just so i can build algorithm


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
