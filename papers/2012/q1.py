def find_prime_factors_product(n):
    i = 2
    distinct_factors = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n /= i
            distinct_factors.add(i)
    if n > 1:
        distinct_factors.add(n)
    product = 1
    for item in distinct_factors:
        product *= item
    return product

N = int(input())
print(find_prime_factors_product(N))

