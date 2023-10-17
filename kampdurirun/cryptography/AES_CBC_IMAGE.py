from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import io

# Generate a random 16-byte initialization vector (IV)
iv = get_random_bytes(16)

# Create an AES cipher object
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Read an image file (e.g., replace 'ahtong.png' with your image file)
with open('ahtong.png', 'rb') as image_file:
    image_data = image_file.read()

# Calculate the length of the input image
input_image_length = len(image_data)

# Encrypt the image data
padded_image_data = pad(image_data, AES.block_size)
encrypted_image_data = cipher.encrypt(padded_image_data)

# Calculate the length of the encrypted image
encrypted_image_length = len(encrypted_image_data)

# Save the encrypted image to a file
with open('encrypted_image.jpg', 'wb') as encrypted_image_file:
    encrypted_image_file.write(iv + encrypted_image_data)

# Decryption
with open('encrypted_image.jpg', 'rb') as encrypted_image_file:
    encrypted_image = encrypted_image_file.read()
    iv = encrypted_image[:16]  # Extract the IV
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_image_data = unpad(decipher.decrypt(encrypted_image[16:]), AES.block_size)

# Calculate the length of the decrypted image
decrypted_image_length = len(decrypted_image_data)

# Save the decrypted image as 'decrypted_image.jpg'
with open('decrypted_image.jpg', 'wb') as decrypted_image_file:
    decrypted_image_file.write(decrypted_image_data)

# Display the lengths of the input, encrypted, and decrypted images
print("Input image length:", input_image_length, "bytes")
print("Encrypted image length:", encrypted_image_length, "bytes")
print("Decrypted image length:", decrypted_image_length, "bytes")

# You can also display the decrypted image using PIL
decrypted_image = Image.open(io.BytesIO(decrypted_image_data))
decrypted_image.show()
