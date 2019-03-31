"""
Security Academy
Group 9
2019
Cryptography
One Time Pad Decryption Implementation
"""

def decrypt_one_time_pad(cipher, pad):
    if len(cipher) != len(pad):
        raise Exception("The message and pad must be the same length to run the encryption method")
    length = len(pad)
    cipher = cipher.lower()
    pad = pad.lower()
    plaintext = ""
    for i in range(0, length):
        plaintext = plaintext + calculate_plaintext_letter(cipher[i], pad[i])
    return plaintext

def calculate_plaintext_letter(cipher_letter, pad_letter):
    offset = ord(pad_letter) - 97
    plaintext_letter = ((ord(cipher_letter) - 97) - offset) % 26
    return chr(plaintext_letter + 97)
