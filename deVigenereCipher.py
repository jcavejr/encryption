#!/usr/bin/env python3.6

import random

def encryption():
    """Asks user for a message and key, prints out a cipher created through
    De Vigenere function."""
    print("Start encryption by entering key. The key can only contain letters, numbers, a space, '.', ',', '!', '?', \"'\", '\"'. If you'd prefer a blank key, press enter.")
    key = input("Enter desired key or hit enter for one to be generated: ")
    print("Next enter the message. The message can only contain letters, numbers, and/or a space.")
    message = input("Enter message to encrypt: ")
    if key == '':
        key = get_generated_key(len(message))
        print("Key: \n", key, sep='')
    encrypted_message = get_encrypted_message(key, message)
    print("-"*30, "\nThe message is:\n", encrypted_message, end="\n", sep="")

def decryption():
    """Asks user for cipher and key, prints out decrypted message."""
    print("Start decryption by entering the encryption key.")
    key = input("Enter decryption key: ")
    print("Next enter the encrypted message.")
    cipher = input("Encrypted message: ")
    decrypted_message = get_decrypted_message(key, cipher)
    print("-"*30, "\nThe message is:\n", decrypted_message, end="\n", sep="")

def get_generated_key(key_len):
    """Generates a key with the same length as the message"""
    key = ""
    for i in range(key_len):
        key += get_char(random.randint(0, 42))
    return key

def get_decrypted_message(key, cipher):
    """Decrypts an encrypted message with a key using De Vigenere function"""
    key_pos = 0
    message = ""
    for ch in cipher:
        if key_pos < len(key):
            message += get_char(get_value(ch) - get_value(key[key_pos]))
            key_pos += 1
        else:
            message += get_char(get_value(ch) - get_value(key[0]))
            key_pos = 1
    return message

def get_encrypted_message(key, message):
    """Turns a key and a message into a cipher using De Vigenere function"""
    key_pos = 0
    cipher = ""
    for ch in message:
        if key_pos < len(key):
            cipher += get_char(get_value(ch) + get_value(key[key_pos]))
            key_pos += 1
        else:
            cipher += get_char(get_value(ch) + get_value(key[0]))
            key_pos = 1
    return cipher
                
def get_char(value):
    """Returns the character associated with the given value in this program"""
    if value == 0:
        return ' '
    elif value > 26 and value < 37:
        return chr(value + 21)
    elif value > 0 and value < 27:
        return chr(value + 96)
    elif value == 37:
        return '.'
    elif value == 38:
        return ','
    elif value == 39:
        return '!'
    elif value == 40:
        return '?'
    elif value == 41:
        return "'"
    elif value == 42:
        return '"'
    elif value > 42:
        return get_char(value - 40)
    elif value < 0:
        return get_char(value + 40)
    else:
        raise Exception("Only acceptable chars are a-z, 0-9, ' ', '.', '!', and '?'")


def get_value(char):
    """Returns the value of a character with respect to this program."""
    if char == ' ':
        return 0
    elif ord(char) >= 48 and ord(char) <= 57:
        return ord(char) - 21
    elif ord(char.lower()) >= 97 and ord(char.lower()) <= 122:
        return ord(char.lower()) - 96
    elif char == '.':
        return 37
    elif char == ',':
        return 38
    elif char == '!':
        return 39
    elif char == '?':
        return 40
    elif char == "'":
        return 41
    elif char == '"':
        return 42
    else:
        raise Exception("Only acceptable chars are a-z, 0-9, ' ', '.', ',', '!', and '?'")


if __name__ == "__main__":
    print("=+=Welcome to De Vigenere Encryption=+=")
    ans = input("To begin, enter (1) for encryption or (2) for decryption: ")
    if ans == '1':
        encryption()
    elif ans == '2':
        decryption()
    else:
        raise Exception("Invalid input.")
