def vigenere_cipher(message, key, mode):
    # 初始化结果字符串
    result = ''

    # 将消息和密钥转换为大写以便处理
    message = message.upper()
    key = key.upper()

    # 确定密钥的长度
    key_length = len(key)

    # 遍历消息中的每个字符
    for i in range(len(message)):
        # 如果字符是字母，则进行加密/解密，否则直接添加到结果中
        if message[i].isalpha():
            # 根据模式选择加密或解密
            if mode == 'encrypt':
                shift = ord(key[i % key_length]) - 65
            elif mode == 'decrypt':
                shift = 26 - (ord(key[i % key_length]) - 65)

            # 使用移位来加密/解密
            result += chr((ord(message[i]) - 65 + shift) % 26 + 65)
        else:
            result += message[i]

    return result


# 测试加密和解密
message = "HELLO"
key = "KEY"
encrypted_message = vigenere_cipher(message, key, 'encrypt')
print("Encrypted message:", encrypted_message)
decrypted_message = vigenere_cipher(encrypted_message, key, 'decrypt')
print("Decrypted message:", decrypted_message)
