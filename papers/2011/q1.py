# Fibonacci letters - DONE 13m 40s

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def find_fibonacci(a, b, count, current):
    current += 1
    if current == count - 1:
        return b % 26
    return find_fibonacci(b, a+b, count, current)


print("Input: ")
input_val = list(input().strip().split(" "))
print(letters[find_fibonacci(int(letters.index(input_val[0]))+1, int(letters.index(input_val[1]))+1, int(input_val[2]), 0)-1])


