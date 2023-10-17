def key_scheduling(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def stream_generation(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def encrypt_image(input_image_path, key):
    with open(input_image_path, 'rb') as image_file:
        image_data = image_file.read()

    key = bytes(key, 'utf-8')
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)

    encrypted_data = bytes((byte ^ next(key_stream)) for byte in image_data)
    return encrypted_data

def decrypt_image(input_image_path, key):
    with open(input_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()

    key = bytes(key, 'utf-8')
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)

    decrypted_data = bytes((byte ^ next(key_stream)) for byte in encrypted_data)
    return decrypted_data

# if __name__ == '__main__':
#     input_image = "ahtong.png"
#     encrypted_image = "encrypted_image.png"
#     decrypted_image = "decrypted_image_ahtong.png"
#     key = "your_key_here"

#     # Encrypt the image
#     encrypt_image(input_image, encrypted_image, key)

#     # Decrypt the image
#     decrypt_image(encrypted_image, decrypted_image, key)
