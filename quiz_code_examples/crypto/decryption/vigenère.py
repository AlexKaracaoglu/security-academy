"""
Security Academy
Group 9
2019
Cryptography
Vigenère Cipher Decryption Implementation
"""

def decrypt_vigenere(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    cipher_length = len(cipher)
    key = calculate_key(key, cipher_length)
    plaintext = ""
    for i in range(0, cipher_length):
        plaintext = plaintext + calculate_plaintext_letter(cipher[i], key[i])
    return plaintext

def calculate_key(key, cipher_length):
    if len(key) < cipher_length:
        return extend_key(key, cipher_length)
    else:
        return key[0: cipher_length]

def extend_key(key, cipher_length):
    key_length = len(key)
    key = key * int(cipher_length / key_length)
    additional_length= cipher_length - len(key)
    for i in range(0, additional_length):
        key = key + key[i]
    return key

def calculate_plaintext_letter(cipher_letter, key):
    offset = ord(key) - 96
    plaintext_letter = ord(cipher_letter) - offset
    if plaintext_letter < 97:
        plaintext_letter += 26
    return chr(plaintext_letter)
