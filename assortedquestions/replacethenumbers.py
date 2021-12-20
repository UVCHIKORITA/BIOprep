array = []
queries = int(input())
for i in range(queries):
    query = list(map(int, input().strip().split(" ")))
    if query[0] == 1:
        array.append(query[1])
    else:
        if query[1] != query[2]:
            array = [query[2] if x == query[1] else x for x in array]
output = ""
for item in array:
    output += str(item)
    output += " "
print(output[:-1])