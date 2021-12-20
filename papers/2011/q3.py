# Upside-down : (

def find_upside_down(k):
    isMiddleDigit = False
    if k == 1:
        return 5
    if k <= 19: # 2-3 digits
        base_val = "19"
        if k > 10:
            isMiddleDigit = True
            k -= 9
        k -= 2
        while k > 0:
            base_val = str(int(base_val[0] + 1)) + str(int(base_val[1] - 1))
            k -= 1
        if isMiddleDigit:
            base_val = base_val[0] + "5" + base_val[1]
        return base_val
    if k <= 181: # 4-5 digits
        base_val = "1199"
        if k > 10:
            isMiddleDigit = True
            k -= 9
        k -= 2
        itera = 0
        while k > 0:
            itera += 1
            base_val = str(int(base_val[0] + 1)) + str(int(base_val[1] - 1))
            k -= 1
        if isMiddleDigit:
            base_val = base_val[0] + "5" + base_val[1]
        return base_val
    if k <= 13303: # 6-7 digits
        pass
    if k <= 86106745: # 8-9 digits
        pass
    else: # 10 digits (max)



print("Input: ")
n = input().strip()
print(int(find_upside_down(n)))

