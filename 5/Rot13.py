# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

import string

def rot13(message):
    alphabet = string.ascii_lowercase
    encrypted = ""
    for ch in message:
        if ch.isalpha():
            index = alphabet.index(ch.lower())
            if index <= 12:
                new_index = index + 13
                encrypted = encrypted + alphabet[new_index]
            else:
                new_index = (index+13) % 26
                encrypted = encrypted + alphabet[new_index]
        else:
            encrypted = encrypted + ch
    
    encrypted_list = [x for x in encrypted]
    for i in range(len(encrypted_list)):
        if message[i].isupper():
            encrypted_list[i] = encrypted_list[i].upper()

    return "".join(encrypted_list)

print(rot13("Test"))

# "grfg"