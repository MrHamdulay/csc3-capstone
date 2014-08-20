# A program that changes all letters in a sentence/word to the next consequtive letter
# Martin Batek
# 5 May 2014

def encrypt(word):
    """A function that recursivly changes each lower case letter to the next consecutive letter"""
    if len(word) == 1:
        if (ord(word) >= 97) and ord(word)<=122: # Specify for lower case letters
            if word == "z":
                return "a"
            else:
                return chr(ord(word)+1)
        else:
            return word
    else:
        if ord(word[0]) >= 97 and ord(word[0])<=122:
            if word[0] == "z":
                return "a" + encrypt(word[1:])
            else:
                return chr(ord(word[0])+1) + encrypt(word[1:])
        else:
            return word[0] + encrypt(word[1:])

def encrypt_message():
    """A function that first asks for input then prints an encrypted version of the input""" 
    message = input("Enter a message:\n") # Gather input from user
    if message == "":
        encrypt_message() #In case user simply presses enter
    else:
        print("Encrypted message:")
        print(encrypt(message)) # Encrypt input
        
encrypt_message()