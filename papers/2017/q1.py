row = list(input().strip())
for i in range(len(row) - 1):
    temp_row = []
    for k in range(len(row) - 1):
        rgb = ['R', 'G', 'B']
        if row[k] == row[k+1]:
            temp_row.append(row[k])
        else:
            rgb.remove(row[k])
            rgb.remove(row[k+1])
            temp_row.append(rgb[0])
    row = temp_row
print(row[0])