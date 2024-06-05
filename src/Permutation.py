import random

def generate_key(length):
    """生成一个长度为length的排列密钥"""
    key = list(range(length))
    random.shuffle(key)
    return key

def permutation_encrypt(plaintext, key):
    """使用排列密钥加密明文"""
    ciphertext = [''] * len(plaintext)
    for i, char in enumerate(plaintext):
        ciphertext[key[i]] = char
    return ''.join(ciphertext)

def permutation_decrypt(ciphertext, key):
    """使用排列密钥解密密文"""
    plaintext = [''] * len(ciphertext)
    for i, char in enumerate(ciphertext):
        plaintext[key[i]] = char
    return ''.join(plaintext)

# 示例用法
plaintext = "WOSHIWYH"
print("Original:", plaintext)

# 生成密钥
key = generate_key(len(plaintext))
print("key:", key)

# 加密
encrypted_msg = permutation_encrypt(plaintext, key)
print("Encrypted:", encrypted_msg)

# 解密
decrypted_msg = permutation_decrypt(encrypted_msg, key)
print("Decrypted:", decrypted_msg)
