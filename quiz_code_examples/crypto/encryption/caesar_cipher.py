"""
Security Academy
Group 9
2019
Cryptography
Caesar Cipher Encryption Implementation
"""

def encrypt_caesar(plaintext, offset):
    plaintext = plaintext.lower()
    cipher = ""
    for letter in plaintext:
        cipher = cipher + calculate_cipher_letter(letter, offset)
    return cipher

def calculate_cipher_letter(letter, offset):
    cipher_letter = ((ord(letter) - 97) + offset) % 26
    return chr(cipher_letter + 97)
