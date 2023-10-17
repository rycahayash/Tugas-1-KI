from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Generate a random 16-byte nonce (counter)
nonce = get_random_bytes(8)


# Create an AES cipher object
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)


# Message to be encrypted
message = "This is a secret message.".encode('utf-8')


# Encrypt the message
encrypted_message = cipher.encrypt(message)


# Printing the nonce and encrypted message
print("Nonce:", nonce)
print("Encrypted message:", encrypted_message)


# Decryption
decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
decrypted_message = decipher.decrypt(encrypted_message)


# Printing the decrypted message
print("Decrypted message:", decrypted_message.decode('utf-8'))