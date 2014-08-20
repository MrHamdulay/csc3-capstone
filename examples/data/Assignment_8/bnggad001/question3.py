# Assignment 8: Question 3 
# Gadziraiushe Bangure: BNGGAD001
# May 9, 2014

# ----------------------------------------------------------------------
# A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a). You MUST NOT use any form of loop in your program!
# ----------------------------------------------------------------------



s = input('Enter a message:\n')

def conv(s):
    if s == "":
        return ""
    if s == s.upper:   #Check if whole string is upper case
        print("Encrypted message: ")
        return s
    
    elif s[0] == " ":
        return " " + conv(s[1:])   #ensures space character is not scrambled 
    
    elif s[0] == "z":
            return "a" + conv(s[1:])   #move z to a
    
    elif s[0].isupper():
        return s[0] + conv(s[1:])   #ensures all upper case letters are not scrambled
    
    
    elif s[0] == ".":
        return "." + conv(s[1:])  #ensures . is not scrambled
    
    else:
        return chr(ord(s[0])+1) + conv(s[1:])   #uses ordered numbers to shift each character 1 position up
    
print("Encrypted message: ")    
print(conv(s))

        