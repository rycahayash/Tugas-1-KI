from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
import time
import binascii

def cut_to_16(original):
    return original[:16]

def aes_cbc_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_content = pad(content, AES.block_size)
    encrypted_content = cipher.encrypt(padded_content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt

def aes_cbc_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_content = unpad(decipher.decrypt(content), AES.block_size)
    end_time = time.time()

    length_decrypt = len(decrypted_content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

def aes_cfb_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_content = cipher.encrypt(content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt
    
def aes_cfb_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    decipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_content = decipher.decrypt(content)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

def aes_ofb_en(content, iv, key):
    length_input = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    cipher = AES.new(key, AES.MODE_OFB, iv)
    encrypted_content = cipher.encrypt(content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt

def aes_ofb_de(content, iv, key):
    length_encrypt = len(content)

    iv = cut_to_16(iv)
    key = cut_to_16(key)

    start_time = time.time()
    decipher = AES.new(key, AES.MODE_OFB, iv)
    decrypted_content = decipher.decrypt(content)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

def aes_ctr_en(content, nonce, key):
    length_input = len(content)

    nonce = cut_to_16(nonce)
    key = cut_to_16(key)
    counter = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))

    start_time = time.time()
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    encrypted_content = cipher.encrypt(content)
    end_time = time.time()

    length_encrypt = len(encrypted_content)
    return encrypted_content, end_time - start_time, length_input, length_encrypt

def aes_ctr_de(content, nonce, key):
    length_encrypt = len(content)

    nonce = cut_to_16(nonce)
    key = cut_to_16(key)
    counter = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))

    start_time = time.time()
    decipher = AES.new(key, AES.MODE_CTR,counter=counter)
    decrypted_content = decipher.decrypt(content)
    end_time = time.time()

    length_decrypt = len(content)
    return decrypted_content, end_time - start_time, length_encrypt, length_decrypt

# content = b"hello all"
# iv = bytes.fromhex("72c0c7aeaf0d4dec8a360768f4a3dc04")
# nonce = iv
# key = bytes.fromhex("72c0c7aeaf0d4dec8a360768f4a3dc04")

# encrypt, _, _, _ = aes_ctr_en(content, iv, key)
# decrypt, _, _, _ = aes_ctr_de(encrypt, iv, key)

# print(encrypt)
# print(decrypt)