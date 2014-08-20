'''Assignment 8 question 3 Encryption
Adam Smith
5 May 2014'''


def Encryption(text): #encyrpts the string by shifting the letters one to the right
    if text == "":
        return ""
    
    if text[0] == "z":
        return "a" + (Encryption(text[1:]))
    
    elif text[0].islower():
        return chr(ord(text[0])+1) + (Encryption(text[1:]))
    
    else:
        return text[0] + (Encryption(text[1:]))
 

print ("Encrypted message:\n" + Encryption(input("Enter a message:\n"))) 