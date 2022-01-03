from math import factorial

inputs = list(map(int, input().strip().split(" ")))


def findStr(inputs, ans=""):
    if inputs[0] == inputs[1] == inputs[2] == inputs[3] == 0:
        return ans
    totalPos = factorial(inputs[0] + inputs[1] + inputs[2] + inputs[3]) / (
                factorial(inputs[0]) * factorial(inputs[1]) * factorial(inputs[2]) * factorial(inputs[3]))

    totalstarta = totalPos * (inputs[0] / (inputs[0] + inputs[1] + inputs[2] + inputs[3]))
    totalstartb = totalPos * (inputs[1] / (inputs[0] + inputs[1] + inputs[2] + inputs[3]))
    totalstartc = totalPos * (inputs[2] / (inputs[0] + inputs[1] + inputs[2] + inputs[3]))
    o = ""
    if inputs[4] <= totalstarta:
        inputs[0] -= 1
        o = "A"
    elif inputs[4] <= (totalstartb + totalstarta):
        inputs[1] -= 1
        inputs[4] -= totalstarta
        o = "B"
    elif inputs[4] <= (totalstartb + totalstarta + totalstartc):
        inputs[2] -= 1
        inputs[4] -= (totalstarta + totalstartb)
        o = "C"
    else:
        inputs[3] -= 1
        inputs[4] -= (totalstarta + totalstartb + totalstartc)
        o = "D"
    return o + findStr([inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]])

print(findStr(inputs))