# Message Encryption
# Khwezi Majola
# MJLKHW001
# 04 May 2014

def encrypt(string):
    if len(string) == 0: #If the end of the string is reached it returns nothing
        return ''
    else:
        if string[0] == ' ':
            return string[0] + encrypt(string[1:])
        elif string[0].isupper(): #Checks if capital letter and excludes from encryption
            return string[0] + encrypt(string[1:])
        elif not string[0].isalpha(): #Checks if it is not an alphabetic character and excludes it from encryption
            return string[0] + encrypt(string[1:])
        elif (ord(string[0]) + 1) > ord('z'): #Checks if the shifted value is beyond z
            return chr(ord(string[0])+1-26) + encrypt(string[1:]) #Shifts it to a and beyond. Recursion occurs 
        else: return chr(ord(string[0])+1) + encrypt(string[1:]) #Shifts the value. Recursion occurs
    
def main():
    string = input('Enter a message:\n')
    print('Encrypted message:', encrypt(string), sep = '\n')

main()