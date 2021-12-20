number = input()
count1 = number.count('1')
count2 = number.count('2')
count3 = number.count('3')
count4 = number.count('4')
count5 = number.count('5')
count6 = number.count('6')
count7 = number.count('7')
count8 = number.count('8')
count9 = number.count('9')
count0 = number.count('0')

isP = False
for i in range(9):
    new = str(int(number)*(i+1))
    if i != 0 and new.count('1') == count1 and new.count('2') == count2 and new.count('3') == count3 and new.count('4') == count4 and new.count('5') == count5 and new.count('6') == count6 and new.count('7') == count7 and new.count('8') == count8 and new.count('9') == count9 and new.count('0') == count0:
        print(str(i+1), end=" ")
        isP = True

if not isP:
    print("NO")

