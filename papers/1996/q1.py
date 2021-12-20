"""


Two numbers are said to be 'amicable' if they are different and the sum of the divisors of each number (including 1 but
excluding the number itself) equals the other number.
For example: 2620 is divisible by 1, 2, 4, 5, 10, 20, 131, 262, 524, 655 and 1310; these add up to 2924. 2924 is
divisible by 1, 2, 4, 17, 34, 43, 68, 86, 172, 731 and 1462; these add up to 2620. Therefore 2620 and 2924 are amicable.

1 (a)
[20 marks]	Write a program which inputs two numbers (which will be less than 10,000) and then prints "Amicable" if they
are amicable, or "Not amicable" otherwise. Your program should then terminate.

"""


def factor_sum(n):
    limit = int(n**0.5 // 1)
    iter = 1
    sum = 0
    while iter <= limit:
        if n % iter == 0:
            sum += iter
            sum += n/iter
        iter += 1
    sum -= n
    return sum


print("Input both numbers separated by a space: ")
numbers = list(map(int, input().strip().split(" ")))
if(factor_sum(numbers[0]) == numbers[1]) and (factor_sum(numbers[1]) == numbers[0]):
    print("Amicable")
else:
    print("Not amicable")

# 1b

k = 1
while True:
    j = factor_sum(k)
    if(factor_sum(j) == k) and (j != k):
        print("The first amicable numbers are " + str(k) + " and " + str(int(j)))
        break
    k += 1
