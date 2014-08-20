# 8 May 2014
# Sarayn Subroyen
# program that uses a recursive function to encrypt a string by converting all lowercase characters to the next character (with z transformed to a)

string = input("Enter a message:\n")
    
def encrypt(string):
    
    if string == "":  
        return ""
        
    elif string[0] == " ":  
        return " " + encrypt(string[1:])   
    
    elif (ord(string[0]) < 97):  
        return string[0] + encrypt(string[1:])   
    
    elif string[0] == "z": 
        return "a" + encrypt(string[1:])
    
    elif not string[0].isalpha():
        return string[0] + encrypt(string[1:])
    
    else:
        return chr(ord(string[0])+1) + encrypt(string[1:])
    
print_string = encrypt(string)
print("Encrypted message:\n" + print_string)