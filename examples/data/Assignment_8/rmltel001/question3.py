"""Program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
Telisha Ramlall
5 May 2014"""

def encrypt(string): 
    if len(string) < 1:
        return string
    
    #Check if each letter is a alphabetical letter, that it's lowercase and not z
    elif string[0].isalpha() and string[0]==string[0].lower() and string[0] != "z": 
        return chr(ord(string[0])+1) + encrypt(string[1:])
   
   #if z
    elif string[0].isalpha() and string[0]==string[0].lower():
        return "a" + encrypt(string[1:])
    
    else: 
        return string[0] + encrypt(string[1:])


string=input("Enter a message:\n")
print("Encrypted message:\n"+encrypt(string))