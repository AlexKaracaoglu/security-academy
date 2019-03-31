"""
Security Academy
Group 9
2019
Cryptography
Caesar Cipher Brute Force Cryptanalysis Implementation
"""

def brute_force_solve(cipher):
    for offset in range(0,26):
        print("key = " + str(offset) + ": " + "message = " + decrypt_caesar(cipher, offset))

def decrypt_caesar(cipher, offset):
    cipher = cipher.lower()
    plaintext = ""
    for letter in cipher:
        plaintext = plaintext + calculate_plaintext_letter(letter, offset)
    return plaintext

def calculate_plaintext_letter(letter, offset):
    plaintext_letter = ((ord(letter) - 97) - offset) % 26
    return chr(plaintext_letter + 97)
