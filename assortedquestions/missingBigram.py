testCases = int(input())
for i in range(testCases):
    val = input()
    case = list(input().strip().split(" "))
    bigramUsed = False

    for j in range(len(case) - 1):
        if case[j][1] != case[j+1][0] and not bigramUsed:
            bigramUsed = True
            case.insert(j+1, case[j][1] + case[j+1][0])
            break
    if not bigramUsed:
        output = case[0]
        k = 1
        while k < len(case):
            output += case[k][1]
            k += 1
        output += 'a'
        print(output)
    else:
        output = case[0]
        k = 1
        while k < len(case):
            output += case[k][1]
            k += 1
        print(output)