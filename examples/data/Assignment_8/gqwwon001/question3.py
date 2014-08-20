# A program to shift characters one place forward
# Wongwa Giqwa
# 06 May 2014

s = input("Enter a message:\n")
#function to encrypt message
def message(s):
    
    if s == "":  
        return ""
            
    elif s[0] == " ":  
        return " " + message(s[1:])   
        
    elif (ord(s[0]) < 97): #check if character if less than z 
        return s[0] + message(s[1:])   
        
    elif s[0] == "z": #if character is z
        return "a" + message(s[1:])
        
    elif not s[0].isalpha(): #checks if character is an alphabet or not
        return s[0] + message(s[1:])
        
    else:
        return chr(ord(s[0])+1) + message(s[1:])
        
print_string = message(s)
print("Encrypted message:\n" + print_string)    
    