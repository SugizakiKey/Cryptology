import random
import sympy
def generate_rsa_keypair(bits):
    # 生成2个质数 
    p = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
    q = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))

    n = p * q
    ora = (p - 1) * (q - 1)
    e = 17
    # 确保 e 与 ora 互质
    while sympy.gcd(e, ora) != 1:
        e = random.randint(2, ora - 1)

    # 计算私钥指数 d，使得 d ≡ e^(-1) (mod ora)
    d = sympy.mod_inverse(e, ora)

    return n, e, d
def encrypt(plaintext, e, n):

    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(ciphertext, d, n):
    # 将每个加密后的ASCII码值解密并转换回字符
    result = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(result)

# 测试
bits = 1024  # 密钥长度
n, e, d = generate_rsa_keypair(bits)
print("Public key (n, e):", (n, e))
print("Private key (d):", d)

message = "我是王奕涵!"
print("first message:", message)

encrypted_msg = encrypt(message, e, n)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, d, n)
print("Decrypted message:", decrypted_msg)