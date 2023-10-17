from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
data = b'My plain text'
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CTR)
ct_bytes = cipher.encrypt(data)
nonce = cipher.nonce
cipher = DES.new(key, DES.MODE_CTR, nonce=nonce)
pt = cipher.decrypt(ct_bytes)
print("The message was: ", pt)