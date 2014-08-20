"""Program to encrypt characters by shifting to next character, where z shifts to a
joshua gullan
8 may 2014"""
def encrypt(x):
    if len(x)==1:   #characters are passed through encrypt one by one
        if x.islower():  #checks if lower case
            if x=="z":  #if the character is z, return a, don't shift one character in unicode, that won't become "a"
                return "a"
            else:
                return chr(ord(x)+1)  #this is the heart of the program, this shifts the characters along 1 in unicode.
        else:
            return x #if the character is not lower case, just return character.
    else:
        return encrypt(x[0]) + encrypt(x[1:])  #this splits up the string and passes the first letter to encrypt to deal with the next character. 

text=input("Enter a message:\n")
print("Encrypted message:", encrypt(text), sep="\n")