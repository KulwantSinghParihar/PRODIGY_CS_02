import cv2
import numpy as np

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found. Check the path.")

    # Convert to int16 to prevent overflow
    encrypted = (image.astype(np.int16) + key) % 256
    return encrypted.astype(np.uint8)

def decrypt_image(encrypted_image, key):
    decrypted = (encrypted_image.astype(np.int16) - key) % 256
    return decrypted.astype(np.uint8)

# Set image path and key
image_path = r"C:\Users\KULWANTSINGH PARIHAR\OneDrive\Pictures\logo.jpg"
key = 50

# Encrypt and save
encrypted = encrypt_image(image_path, key)
cv2.imwrite("encrypted_image.jpg", encrypted)

# Decrypt and save
decrypted = decrypt_image(encrypted, key)
cv2.imwrite("decrypted_image.jpg", decrypted)

print("✅ Encryption and Decryption completed.")
