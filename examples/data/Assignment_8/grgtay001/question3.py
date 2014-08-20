"""Encryption using recursive functions
tayla george
9 may 2014"""

string = input("Enter a message:\n")
    
def Encryption(string):
    
    if string == "":  
        return ""
        
    elif string[0] == " ":  
        return " " + Encryption(string[1:])   
    
    elif (ord(string[0]) < 97):  
        return string[0] + Encryption(string[1:])   
    
    elif string[0] == "z": 
        return "a" + Encryption(string[1:])
    
    elif not string[0].isalpha():
        return string[0] + Encryption(string[1:])
    
    else:
        return chr(ord(string[0])+1) + Encryption(string[1:])
    
print_string = Encryption(string)
print("Encrypted message:\n" + print_string)