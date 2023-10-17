from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Function to encrypt a file
def encrypt_file(input_file, output_file, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as file_in:
        file_data = file_in.read()
        padded_data = pad(file_data, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

    with open(output_file, 'wb') as file_out:
        file_out.write(iv + encrypted_data)

# Function to decrypt a file
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in:
        file_data = file_in.read()
        iv = file_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(file_data[16:]), AES.block_size)

    with open(output_file, 'wb') as file_out:
        file_out.write(decrypted_data)

# Encryption
key = get_random_bytes(16)  # Use the same key for encryption and decryption
input_file = 'hmm.docx'  # Replace with your document file
encrypted_file = 'encrypted_document.docx'
encrypt_file(input_file, encrypted_file, key)

# Decryption
decrypted_file = 'decrypted_document.docx'
decrypt_file(encrypted_file, decrypted_file, key)
