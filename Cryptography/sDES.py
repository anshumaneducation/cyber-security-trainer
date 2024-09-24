P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # Permutation P10
P8 = [6, 3, 7, 4, 8, 5, 10, 9]        # Permutation P8
P4 = [2, 4, 3, 1]                      # Permutation P4

IP = [2, 6, 3, 1, 4, 8, 5, 7]          # Initial Permutation IP
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]      # Inverse Initial Permutation IP^(-1)

EP = [4, 1, 2, 3, 2, 3, 4, 1]          # Expansion Permutation EP

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]                     # S-Box S0

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]                     # S-Box S1

def permutate(original, permutation):
    """Permute the bits according to the given permutation."""
    return [original[i - 1] for i in permutation]

def left_shift(bits, shifts):
    """Left shift the bits by the specified number of shifts."""
    return bits[shifts:] + bits[:shifts]

def xor(bits1, bits2):
    """Perform bitwise XOR between two bit lists."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox_lookup(bits, sbox):
    """Lookup the value in the specified S-Box."""
    row = (bits[0] << 1) | bits[3]
    col = (bits[1] << 1) | bits[2]
    return [int(x) for x in format(sbox[row][col], '02b')]

def generate_keys(key):
    """Generate the two subkeys from the main key."""
    key = permutate(key, P10)
    left, right = key[:5], key[5:]
    
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    k1 = permutate(left + right, P8)
    
    left = left_shift(left, 2)
    right = left_shift(right, 2)
    k2 = permutate(left + right, P8)
    
    return k1, k2

def fk(bits, key):
    """Feistel function used in the encryption and decryption."""
    left, right = bits[:4], bits[4:]
    temp = permutate(right, EP)
    temp = xor(temp, key)
    left_half = sbox_lookup(temp[:4], S0)
    right_half = sbox_lookup(temp[4:], S1)
    temp = permutate(left_half + right_half, P4)
    return xor(left, temp) + right

def sdes_encrypt_block(block, k1, k2):
    """Encrypt an 8-bit block using the two subkeys."""
    bits = permutate(block, IP)
    bits = fk(bits, k1)
    bits = bits[4:] + bits[:4]  # Switch the left and right halves
    bits = fk(bits, k2)
    ciphertext = permutate(bits, IP_INV)
    return ciphertext

def sdes_decrypt_block(block, k1, k2):
    """Decrypt an 8-bit block using the two subkeys."""
    bits = permutate(block, IP)
    bits = fk(bits, k2)
    bits = bits[4:] + bits[:4]  # Switch the left and right halves
    bits = fk(bits, k1)
    plaintext = permutate(bits, IP_INV)
    return plaintext

def string_to_bits(s):
    """Convert a string to a list of bits."""
    return [int(bit) for char in s for bit in format(ord(char), '08b')]

def bits_to_string(bits):
    """Convert a list of bits to a string."""
    return ''.join(chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8))

def sdes_encrypt(plaintext, key):
    """Encrypt a plaintext string using the given key."""
    key_bits = string_to_bits(key)
    plaintext_bits = string_to_bits(plaintext)
    k1, k2 = generate_keys(key_bits[:10])

    ciphertext_bits = []
    for i in range(0, len(plaintext_bits), 8):
        block = plaintext_bits[i:i+8]
        if len(block) < 8:
            block += [0] * (8 - len(block))
        ciphertext_bits.extend(sdes_encrypt_block(block, k1, k2))
    return bits_to_string(ciphertext_bits)

def sdes_decrypt(ciphertext, key):
    """Decrypt a ciphertext string using the given key."""
    key_bits = string_to_bits(key)
    ciphertext_bits = string_to_bits(ciphertext)
    k1, k2 = generate_keys(key_bits[:10])

    plaintext_bits = []
    for i in range(0, len(ciphertext_bits), 8):
        block = ciphertext_bits[i:i+8]
        plaintext_bits.extend(sdes_decrypt_block(block, k1, k2))
    return bits_to_string(plaintext_bits)


