def find_amount_repaid(interest, repayment):
    debt = 100
    amount_repaid = 0
    while debt > 0:
        debt += debt * (interest / 100)
        repaid = max(50, (debt * (repayment / 100)))
        repaid = min(repaid, debt)
        debt -= repaid
        amount_repaid += repaid
    print(amount_repaid)


print("Input interest: ")
i = float(input().strip())
print("Input repayment: ")
r = float(input().strip())
find_amount_repaid(i, r)
