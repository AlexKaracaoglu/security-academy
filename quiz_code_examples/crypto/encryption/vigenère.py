"""
Security Academy
Group 9
2019
Cryptography
Vigenère Cipher Encryption Implementation
"""

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()
    plaintext_length = len(plaintext)
    key = calculate_key(key, plaintext_length)
    cipher = ""
    for i in range(0, plaintext_length):
        cipher = cipher + calculate_cipher_letter(plaintext[i], key[i])
    return cipher

def calculate_key(key, plaintext_length):
    if len(key) < plaintext_length:
        return extend_key(key, plaintext_length)
    else:
        return key[0: plaintext_length]

def extend_key(key, plaintext_length):
    key_length = len(key)
    key = key * int(plaintext_length / key_length)
    additional_length= plaintext_length - len(key)
    for i in range(0, additional_length):
        key = key + key[i]
    return key

def calculate_cipher_letter(plaintext_letter, key):
    offset = ord(key) - 96
    cipher_letter = ord(plaintext_letter) + offset
    if cipher_letter > 122:
        cipher_letter -= 26
    return chr(cipher_letter)
