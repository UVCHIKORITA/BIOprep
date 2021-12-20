from math import exp, log


def calcPower(val, power, currentVal = 1):
    if 0 < power < 1:
        return exp(log(val)/power)
    if power % 1 != power:
        frac = power.as_integer_ratio()
        return calcPower(calcPower(val, frac[0]), 1/frac[1])
    if power == 0:
        return 1
    if power < 0:
        return calcPower(1/val, -1 * power, currentVal)
    if power == 1:
        return currentVal * val
    return calcPower(val, power-1, val * currentVal)