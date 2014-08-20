"""nasha somoina meoli
4th may 2014
program to encrypt stuff"""

def encrypt(string):
    #when to stop recursing
    if string == "":
        return ""
    #check for punctuation and characters outside the alphabet
    elif 65 > ord(string[0]) or 122 < ord(string[0]):
        return string[0] + encrypt(string[1:])
    #retain spacing
    elif string[0] == " ":
        return " " + encrypt(string[1:])
    #special case for z
    elif string[0] == "z":
        return "a" + encrypt(string[1:])
    #check whether character is lower case and returns the value of one up
    elif string[0].islower():
        return chr(ord(string[0])+1) + encrypt(string[1:])
    
    else: 
        return string[0] + encrypt(string[1:])
    
string = input("Enter a message:\n")
print("Encrypted message:\n"+encrypt(string))