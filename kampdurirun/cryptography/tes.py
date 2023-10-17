import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"secret"
# key = get_random_bytes(16)
# print(key)
key = b'\x1e\x94\xcc\xe8)\xfa\xdf\xf0F\xbc `\xab&s\xed'
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(data)
nonce = b64encode(cipher.nonce).decode('utf-8')
print(nonce)
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
print(result)