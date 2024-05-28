import hashlib
import hmac

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    file_hash = hashlib.sha256(file_data).hexdigest()
    return file_hash


def generate_mac(message, key):
    mac = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    return mac

message = "woshiWangYihan"
key = "WYHkey"
mac = generate_mac(message, key)
print(mac)