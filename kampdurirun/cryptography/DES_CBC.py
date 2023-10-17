from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Generate a random 8-byte initialization vector (IV)
iv = get_random_bytes(8)


# Create a DES cipher object
key = get_random_bytes(8)  # DES keys are 8 bytes
cipher = DES.new(key, DES.MODE_CBC, iv)


# Message to be encrypted
message = "This is a secret message.".encode('utf-8')


# Padding the message to be a multiple of 8 bytes (DES block size)
padded_message = pad(message, DES.block_size)


# Encrypt the message
encrypted_message = cipher.encrypt(padded_message)


# Printing the IV and encrypted message
print("IV:", iv)
print("Encrypted message:", encrypted_message)


# Decryption
decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(encrypted_message), DES.block_size)


# Printing the decrypted message
print("Decrypted message:", decrypted_message.decode('utf-8'))