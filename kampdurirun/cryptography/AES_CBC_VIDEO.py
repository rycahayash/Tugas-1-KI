from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import io

# Generate a random 16-byte initialization vector (IV)
iv = get_random_bytes(16)

# Create an AES cipher object
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Read a video file (e.g., replace 'input_video.mp4' with your video file)
with open('AhTong.mp4', 'rb') as video_file:
    video_data = video_file.read()

# Calculate the length of the input video
input_video_length = len(video_data)

# Encrypt the video data
padded_video_data = pad(video_data, AES.block_size)
encrypted_video_data = cipher.encrypt(padded_video_data)

# Calculate the length of the encrypted video
encrypted_video_length = len(encrypted_video_data)

# Save the encrypted video to a file
with open('encrypted_video.mp4', 'wb') as encrypted_video_file:
    encrypted_video_file.write(iv + encrypted_video_data)

# Decryption
with open('encrypted_video.mp4', 'rb') as encrypted_video_file:
    encrypted_video = encrypted_video_file.read()
    iv = encrypted_video[:16]  # Extract the IV
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_video_data = unpad(decipher.decrypt(encrypted_video[16:]), AES.block_size)

# Calculate the length of the decrypted video
decrypted_video_length = len(decrypted_video_data)

# Save the decrypted video as 'decrypted_video.mp4'
with open('decrypted_video.mp4', 'wb') as decrypted_video_file:
    decrypted_video_file.write(decrypted_video_data)

# Display the lengths of the input, encrypted, and decrypted videos
print("Input video length:", input_video_length, "bytes")
print("Encrypted video length:", encrypted_video_length, "bytes")
print("Decrypted video length:", decrypted_video_length, "bytes")
