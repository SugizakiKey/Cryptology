import hashlib


def encrypt_mac_address(mac_address):
    # 将MAC地址转换为小写并去除冒号
    mac_address = mac_address.lower().replace(':', '')

    # 使用SHA-256哈希算法进行加密
    hash_object = hashlib.sha256(mac_address.encode())
    encrypted_mac_address = hash_object.hexdigest()

    return encrypted_mac_address


mac_address = "00:11:22:33:44:55"
encrypted_mac_address = encrypt_mac_address(mac_address)
print("original：", mac_address)
print("decrypt：", encrypted_mac_address)
