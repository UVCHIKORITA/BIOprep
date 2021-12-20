def is_square(s):
    if len(s) % 2 == 1:
        return "NO"
    half = int(len(s)/2)
    if s[0:half] == s[half:]:
        return "YES"
    return "NO"

t = int(input().strip())
for i in range(t):
    print(is_square(input().strip()))