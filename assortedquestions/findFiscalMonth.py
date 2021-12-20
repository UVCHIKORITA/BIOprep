# To change delimeter edit line 6, replace default "/" with delimeter of choice


# input format "dd/MM"
def find_month(date):
    return list(map(int, date.split("/")))[1]


# input format "dd/MM"
def find_fiscal_month(date):
    fiscal_m = (find_month(date) - 2) % 12
    calc_m = lambda test: 12 if test == 0 else test
    return calc_m(fiscal_m)


dateInput = input().strip()
print(find_fiscal_month(dateInput))
