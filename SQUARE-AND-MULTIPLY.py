def square_and_multiply(a, b, m):
   
    result = 1
    a = a % m

    while b > 0:
        if (b % 2) == 1:
            result = (result * a) % m
        b = b >> 1  # Equivalent to b // 2
        a = (a * a) % m  # Square the a

    return result

a = 3
b = 12
m = 497
print(square_and_multiply(a, b, m))
