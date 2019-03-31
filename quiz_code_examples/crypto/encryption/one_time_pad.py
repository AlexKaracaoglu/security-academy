"""
Security Academy
Group 9
2019
Cryptography
One Time Pad Encryption Implementation
"""

def encrypt_one_time_pad(plaintext, pad):
    if len(plaintext) != len(pad):
        raise Exception("The plaintext message and pad must be the same length to run the encryption method")
    length = len(pad)
    plaintext = plaintext.lower()
    pad = pad.lower()
    cipher = ""
    for i in range(0, length):
        cipher = cipher + calculate_cipher_letter(plaintext[i], pad[i])
    return cipher

def calculate_cipher_letter(plaintext_letter, pad_letter):
    offset = ord(pad_letter) - 97
    cipher_letter = ((ord(plaintext_letter) - 97) + offset) % 26
    return chr(cipher_letter + 97)
