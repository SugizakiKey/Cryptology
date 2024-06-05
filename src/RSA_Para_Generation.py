import sympy
import random
def generate_rsa_keypair(bits):
    # 生成质数 p 和 q
    p = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
    q = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))

    n = p * q
    ora = (p - 1) * (q - 1)

    # 一个小于ora 的公钥指数 e
    e = 17
    # 确保 e 与 φ(n) 互质
    while sympy.gcd(e, ora) != 1:
        e = random.randint(2, ora - 1)

    # 计算私钥指数 d
    d = sympy.mod_inverse(e, ora)

    return n, e, d

bits = 32
n, e, d = generate_rsa_keypair(bits)
print(f"RSA:\nn = {n}\ne = {e}\nd = {d}")