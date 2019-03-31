"""
Security Academy
Group 9
2019
Cryptography
Caesar Cipher Decryption Implementation
"""

def decrypt_caesar(cipher, offset):
    cipher = cipher.lower()
    plaintext = ""
    for letter in cipher:
        plaintext = plaintext + calculate_plaintext_letter(letter, offset)
    return plaintext

def calculate_plaintext_letter(letter, offset):
    plaintext_letter = ((ord(letter) - 97) - offset) % 26
    return chr(plaintext_letter + 97)
