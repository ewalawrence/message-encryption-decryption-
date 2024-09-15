# Encrypting and Decrypting Program

import string
import random

encryptionCharacters = " " + string.punctuation + string.digits + string.ascii_letters

encryptionCharacters = list(encryptionCharacters)
keys = encryptionCharacters.copy()
random.shuffle(keys)

while True:
    options = input("Chose what to do, encrypt or decrypt( e or d ), or q to quit: ").lower()
    if options == "e":
        #ENCRYPT
        message = input("Enter your texts for encryption: ")
        cipherText = ""
        for letter in message:
            index = encryptionCharacters.index(letter)
            cipherText += keys[index]
        print(f"Original message: {message}")
        print(f"Encrypted message: {cipherText} 🔒")

    elif options == "d":
        #DECRYPT
        cipherText = input("Enter your Cipher Text for decryption: ")
        message = ""
        for letter in cipherText:
            index = keys.index(letter)
            message += encryptionCharacters[index]
        print(f"Encrypted message: {cipherText} 🔒")
        print(f"Translated message: {message}")

    elif options == "q":
        print("Program Closed🛄.")
        break

    else:
        print("Select a choice, encrypt or decrypt(e or d): ")