"""encrypter
clare walker
5 may 2014"""

def encrypt(string):
    if len(string) ==1: #reached end, just return encrypted value
        if string[0] == 'z': #exception for z
            return 'a'
        elif 97<=ord(string[0]) <= 122: #ensure lowercase
            
            return chr(ord(string[0])+1) #return encrypted
        else:
            return string[0] #return upper case unchanged
    elif string[0] ==' ':
        return ' ' + encrypt(string[1:])
    elif string[0] == 'z':  #exception for z
        return 'a' + encrypt(string[1:])
    else:
        if 97 <= ord(string[0]) <= 122: #ensure lowercase
            return chr(ord(string[0])+1)  + encrypt(string[1:]) #return encrypted and carry on
        else:
            return string[0] + encrypt(string[1:]) #return upper case unchanged and carry on

# use functions with input    
string=input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))