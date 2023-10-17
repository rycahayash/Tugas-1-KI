from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Generate a random 16-byte initialization vector (IV)
iv = get_random_bytes(16)


# Create an AES cipher object
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)


# Message to be encrypted
message = "This is a secret message.".encode('utf-8')


# Padding the message to be multiple of 16 bytes
padded_message = pad(message, AES.block_size)


# Encrypt the message
encrypted_message = cipher.encrypt(padded_message)


# Printing the IV and encrypted message
print("IV:", iv)
print("Encrypted message:", encrypted_message)


# Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(encrypted_message), AES.block_size)


# Printing the decrypted message
print("Decrypted message:", decrypted_message.decode('utf-8'))