#Assignment 8.3
#Michael Gant
#05/05/2014

import string

def Encrypt(sText):
    if len(sText) == 1:
        if sText.isalpha() == True and sText != "z" and sText.islower():
            return chr(ord(sText)+1)
        elif sText == "z":
            return chr(ord(sText)-25)
        else:
            return sText
    elif sText[0].isalpha() == True and sText[0] != "z" and sText[0].islower():
        return chr(ord(sText[0])+1) + Encrypt(sText[1:])
    elif sText[0] == "z":
        return chr(ord(sText[0])-25) + Encrypt(sText[1:])
    else:
        return sText[0] + Encrypt(sText[1:])

sInput = input("Enter a message:\n")
print("Encrypted message:\n" + Encrypt(sInput))
        
        