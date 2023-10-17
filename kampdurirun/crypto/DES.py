from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
import time
import binascii

def cut_to_8(original):
    return original[:8]

def des_cbc_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_content = pad(content, DES.block_size)
    encrypted_content = cipher.encrypt(padded_content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt

def des_cbc_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_content = unpad(decipher.decrypt(content), DES.block_size)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

def des_cfb_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    cipher = DES.new(key, DES.MODE_CFB, iv)
    encrypted_content = cipher.encrypt(content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt
    
def des_cfb_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    decipher = DES.new(key, DES.MODE_CFB, iv)
    decrypted_content = decipher.decrypt(content)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

def des_ofb_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    cipher = DES.new(key, DES.MODE_OFB, iv)
    encrypted_content = cipher.encrypt(content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt

def des_ofb_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_8(iv)
    key = cut_to_8(key)

    start_time = time.time()
    decipher = DES.new(key, DES.MODE_OFB, iv)
    decrypted_content = decipher.decrypt(content)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

# content = b"hello all"
# iv = bytes.fromhex("72c0c7aeaf0d4dec8a360768f4a3dc04")
# key = bytes.fromhex("72c0c7aeaf0d4dec8a360768f4a3dc04")

# encrypt, _, _, _ = des_ofb_en(content, iv, key)
# decrypt, _, _, _ = des_ofb_de(encrypt, iv, key)

# print(encrypt)
# print(decrypt)