"""program that uses a recursive function to encrypt a string by converting all lowercase characters to the next character
Jade Petersen 
7 may 2014"""

string = input("Enter a message:\n")
    
def Encrypt(string):
    
    if string == "":  
        return ""
        
    elif string[0] == " ":  
        return " " + Encrypt(string[1:])   
    
    elif (ord(string[0]) < 97):  
        return string[0] + Encrypt(string[1:])   
    
    elif string[0] == "z": 
        return "a" + Encrypt(string[1:])
    
    elif not string[0].isalpha():
        return string[0] + Encrypt(string[1:])
    
    else:
        return chr(ord(string[0])+1) + Encrypt(string[1:])
    
print_string = Encrypt(string)
print("Encrypted message:\n" + print_string)