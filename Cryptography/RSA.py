import random

e = 8009
d = 10609
n = 14017

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_large_prime():
    while True:
        p = random.randrange(100, 500)
        if is_prime(p):
            return p

def generate_keypair():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, phi_n)
        if gcd(e, phi_n) == 1:
            break

    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n))

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    # Convert list of integers to a comma-separated string
    ciphertext_str = ','.join(map(str, ciphertext))
    return ciphertext_str

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Convert the comma-separated string back to a list of integers
    ciphertext_list = list(map(int, ciphertext.split(',')))
    plaintext = [chr(pow(char, d, n)) for char in ciphertext_list]
    return ''.join(plaintext)


