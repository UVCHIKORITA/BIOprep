"""


The Roman look-and-say description of a string (of Is, Vs, Xs, Ls, Cs, Ds and Ms) is made by taking each
block of adjacent identical letters and replacing it with the number of occurrences of that letter, given in
Roman numerals (*), followed by the letter itself. A block of adjacent identical letters is never broken
into smaller pieces before describing it.
For example:
• MMXX is described as “two Ms followed by two Xs”. Since two is II in Roman numerals, this is
written as IIMIIX;
• IIMIIX is described as IIIIMIIIIX, which is “two Is, one M, two Is, one X”;
• IIIIMIIIIX is described as IVIIMIVIIX;
• It is not valid to describe III as, “two Is, one I” IIIII.
Note that Roman look-and-say descriptions are not necessarily Roman numerals.

1(a) [ 25 marks ]
Write a program that reads in a Roman numeral representing a number between 1
and 3999 inclusive, followed by n (1 ≤ n ≤ 50).
You should apply the Roman look-and-say description n times and then output the
number of Is in the final description, followed by the number of Vs.


"""
digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
digitValues = [1, 5, 10, 50, 100, 500, 1000]


def digit_to_rom(log10, val):
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


def look_and_say(value, n):
    if n == 0:
        isum = 0
        vsum = 0
        for v in value:
            if v == 'I':
                isum += 1
            elif v == 'V':
                vsum += 1
        print(str(isum) + " " + str(vsum))
    else:
        new_value = ""
        digit_order = []
        digit_count = []
        current_char = ""
        current_count = 0
        for char in value:
            if char != current_char:

                if current_char != "":
                    digit_order.append(current_char)
                    digit_count.append(current_count)
                current_char = char
                current_count = 0
            current_count += 1
        digit_order.append(current_char)
        digit_count.append(current_count)
        pos = 0
        for d in digit_count:
            num = list(map(int, str(d)))[::-1]
            log10array = []
            log10 = 0
            for val in num:
                log10array.append(log10)
                log10 += 1
            log10array = log10array[::-1]
            num = num[::-1]
            i = 0
            for b in num:
                new_value += digit_to_rom(log10array[i], b)
                i += 1
            new_value += digit_order[pos]
            pos += 1
        look_and_say(new_value, n-1)


print("Input roman number and n on same line separated by space:")
obtainedValues = list(input().strip().split(' '))
lookandsay = look_and_say(obtainedValues[0], int(obtainedValues[1]))

