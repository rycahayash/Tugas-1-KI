# Open the encrypted video file in binary mode
with open('encrypted_video.mp4', 'rb') as encrypted_video_file:
    encrypted_video_data = encrypted_video_file.read()

# Display or print the ciphertext (binary data)
print(encrypted_video_data)
