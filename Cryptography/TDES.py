import base64
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def tdes_encrypt(plaintext, key):
    # Convert key to bytes if it is a string
    if isinstance(key, str):
        key = key.encode()

    # Ensure the key length is 24 bytes (192 bits) for 3DES
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long")

    # Generate a random IV (initialization vector)
    iv = get_random_bytes(8)

    # Create a Triple DES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Pad the plaintext to be a multiple of the block size (8 bytes)
    padded_text = pad(plaintext.encode(), DES3.block_size)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)

    # Return the IV and ciphertext, encoded as base64
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def tdes_decrypt(ciphertext, key):
    # Convert key to bytes if it is a string
    if isinstance(key, str):
        key = key.encode()

    # Ensure the key length is 24 bytes (192 bits) for 3DES
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long")

    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(ciphertext.encode('utf-8'))

    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:8]
    actual_ciphertext = ciphertext[8:]

    # Create a Triple DES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Decrypt the ciphertext
    padded_text = cipher.decrypt(actual_ciphertext)

    # Unpad the plaintext
    plaintext = unpad(padded_text, DES3.block_size)

    return plaintext.decode()

