hours1 = 0
minutes1 = 0
hours2 = 0
minutes2 = 0

def timeformat(hours, minutes):
    output = ""
    if 0 <= hours < 10:
        output += f'0{hours}:'
    else:
        output += f'{hours}:'
    if 0 <= minutes < 10:
        output += f'0{minutes}'
    else:
        output += f'{minutes}'
    return output

vals = list(map(int, input().strip().split(" ")))
while True:
    hours1 += 1
    hours2 += 1
    minutes1 += vals[0]
    minutes2 += vals[1]
    while minutes1 >= 60:
        hours1 += 1
        minutes1 -= 60
    while minutes2 >= 60:
        hours2 += 1
        minutes2 -= 60
    while hours1 >= 24:
        hours1 -= 24
    while hours2 >= 24:
        hours2 -= 24
    if  hours1 == hours2 and minutes1 == minutes2:
        break
print(timeformat(hours1, minutes2))