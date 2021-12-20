def find_next_palindrome(value):
    if len(str(value)) % 2 == 0:
        length = int((len(str(value))/2))
        half_string = str(value)[:length]
        half_val = int(half_string)
        half_val += 1
        new_half_string = str(half_val)
        if len(new_half_string) > len(half_string):
            output = new_half_string
            output += new_half_string[:-1][::-1]
            print(output)
        else:
            output = new_half_string
            output += new_half_string[::-1]
            print(output)
    else:
        length = int(((len(str(value)) - 1) / 2) + 1)
        half_string = str(value)[:length]
        half_val = int(half_string)
        half_val += 1
        new_half_string = str(half_val)
        if len(new_half_string) == len(half_string):
            output = new_half_string
            output += new_half_string[:-1][::-1]
            print(output)
        else:
            output = new_half_string
            output += new_half_string[::-1]
            print(output)


print("Input value: ")
v = int(input().strip())
find_next_palindrome(v)
