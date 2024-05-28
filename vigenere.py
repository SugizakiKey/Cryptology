def vigenere(message, key, mode):
    # 转换为大写
    message = message.upper()
    key = key.upper()
    key_length = len(key)
    result = ''
    # 遍历
    for i in range(len(message)):
        if message[i].isalpha():
            if mode == '0': #加密
                shift = ord(key[i % key_length]) - 65
            elif mode == '1':#解密
                shift = 27 - (ord(key[i % key_length]) - 65)
            # 使用移位来加密/解密
            result += chr((ord(message[i]) - 65 + shift) % 27 + 65)
        else:
            result += message[i]
    return result

message = "IamWyh"
print("message: ",message)
key = "KEY"
encrypt = vigenere(message, key, '0')
print("Encrypted:", encrypt)
decrypt = vigenere(encrypt, key, '1')
print("Decrypted:", decrypt)
