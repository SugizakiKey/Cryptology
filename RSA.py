import random
import sympy


def generate_rsa_keypair(bits):
    # 生成两个大质数 p 和 q
    p = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
    q = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))

    # 计算 n = p * q
    n = p * q

    # 计算欧拉函数 φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)

    # 选择一个小于 φ(n) 的公钥指数 e，通常选择 65537
    e = 65537
    # 确保 e 与 φ(n) 互质
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # 计算私钥指数 d，使得 d ≡ e^(-1) (mod φ(n))
    d = sympy.mod_inverse(e, phi_n)

    return n, e, d
def encrypt(plaintext, e, n):
    # 将每个字符转换为其ASCII码值并加密
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(ciphertext, d, n):
    # 将每个加密后的ASCII码值解密并转换回字符
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)


# 测试
bits = 2048  # 密钥长度
n, e, d = generate_rsa_keypair(bits)
print("Public key (n, e):", (n, e))
print("Private key (d):", d)

message = "我是王奕涵!"
print("Original message:", message)

encrypted_msg = encrypt(message, e, n)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, d, n)
print("Decrypted message:", decrypted_msg)