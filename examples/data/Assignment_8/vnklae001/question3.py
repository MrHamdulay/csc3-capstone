# Assignment 8 (Q3)
# A program that encrypts a message by converting all lowercase characters to the next character (with z transformed to a)
# Written by: Laene van Niekerk
# VNKLAE001

def encrypt(s):
    if s == "":     # If empty string
        return s
    elif s[0] == " ":   # If there is a space, print the space and then move on to next character
        return s[0] + encrypt(s[1:])
    elif s[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # If uppercase, print the character as is and move on
        return s[0] + encrypt(s[1:])
    elif s[0] == ".":           # If ".", print this character and move on
        return s[0] + encrypt(s[1:])
    elif s[0] == "z":
        return "a" + encrypt(s[1:])
    elif len(s) >= 1:       # If there is a word and it is lowercase, change it and move on
        wrd = s[0]
        num = ord(wrd)
        new_letter = chr(num+1)
        return new_letter + encrypt(s[1:])
    
x = input("Enter a message:\n")
print("Encrypted message:\n", encrypt(x), sep="")