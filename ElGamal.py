import random
from sympy import isprime, mod_inverse


def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p


def generate_keypair(bits):
    # 选择一个大素数 p 和生成元 g
    p = generate_prime(bits)
    g = random.randint(2, p - 1)

    # 私钥 x 是一个随机数
    x = random.randint(1, p - 2)

    # 公钥 y = g^x mod p
    y = pow(g, x, p)

    return (p, g, y), x


def encrypt(plaintext, public_key):
    p, g, y = public_key

    # 将明文转换为整数
    m = int.from_bytes(plaintext.encode(), 'big')

    # 选择一个随机数 k
    k = random.randint(1, p - 2)

    # 计算 c1 = g^k mod p 和 c2 = m * y^k mod p
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p

    return (c1, c2)


def decrypt(ciphertext, private_key, public_key):
    c1, c2 = ciphertext
    p, g, y = public_key
    x = private_key

    # 计算 s = c1^x mod p
    s = pow(c1, x, p)

    # 计算 s 的模逆
    s_inv = mod_inverse(s, p)

    # 计算 m = c2 * s^(-1) mod p
    m = (c2 * s_inv) % p

    # 将整数转换回字符串
    plaintext = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

    return plaintext


# 示例用法
bits = 256  # 密钥长度
public_key, private_key = generate_keypair(bits)
print("Public key (p, g, y):", public_key)
print("Private key (x):", private_key)

message = "我是王奕涵"
print("Original message:", message)

encrypted_msg = encrypt(message, public_key)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, private_key, public_key)
print("Decrypted message:", decrypted_msg)
