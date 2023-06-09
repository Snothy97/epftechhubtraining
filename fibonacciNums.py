def calculate_fibonacci_sum(limit):
    sum = 0
    a = 1
    b = 0
    fnum = 0

    while fnum < limit:
        a, b = b, a + b
        if b % 2 == 0:
            fnum += b

    return fnum

result = calculate_fibonacci_sum(4000000)
print(result)