"""Ailsa Mackay MCKAIL001
Assignment 8 Question 3
2014-05-06"""

def encrypt(message):
    if len(message)==1:   #characters are passed through encrypt one by one
        if message.islower():  #checks if lower case
            if message=="z":  #if the character is z, return a, don't shift one character in unicode. Instead loop round alphabet
                return "a"
            else:
                return chr(ord(message)+1)  #this is the heart of the program, this shifts the characters along 1 in unicode.
        else:
            return message #if the character is not lower case, leave unchanged.
    else:
        return encrypt(message[0]) + encrypt(message[1:]) #splits first letter from the rest of the text so that it can be interpretted by encript function
def main():
    message = input("Enter a message:\n")
    print("Encrypted message:", encrypt(message), sep="\n")
    
main()