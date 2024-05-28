def extended_gcd(a, b):
    """
    扩展欧几里得算法，返回 (gcd, x, y)，使得 ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

# 示例用法
a = 30
b = 20
gcd, x, y = extended_gcd(a, b)
print(f"gcd({a}, {b}) = {gcd}, x = {x}, y = {y}")
