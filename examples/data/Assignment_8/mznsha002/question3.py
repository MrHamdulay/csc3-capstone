# 8 May 2014
# Shaun Muzenda
# program that uses a recursive function to encrypt a string by converting all lowercase characters to the next character (with z transformed to a)

string = input("Enter a message:\n")
    
def Encrypt(string):
    
    if string == "":  #base case where empty string returns empty string
        return ""
        
    elif string[0] == " ":      #is character is a space, prints a space and not {
        return " " + Encrypt(string[1:])   
    
    elif (ord(string[0]) < 97):  #checks whether character unicode value is greater than 97
        return string[0] + Encrypt(string[1:])   
    
    elif string[0] == "z": #if character is a z, prints an a
        return "a" + Encrypt(string[1:])
    
    elif not string[0].isalpha():   #if characters are not alphanumeric
        return string[0] + Encrypt(string[1:])
    
    else:
        return chr(ord(string[0])+1) + Encrypt(string[1:])
    
print_string = Encrypt(string)
print("Encrypted message:\n" + print_string)    #prints the encrypted message