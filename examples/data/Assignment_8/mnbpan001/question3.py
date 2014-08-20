"""Program to encrypt a message
Pankaj Munbodh
7 May 2014"""

get_str=input("Enter a message:\n")
def encrypt(string):
    if string[0].isalpha()==False and len(string)==1:
        return string[0]                       #stopping case when string ends in non-alphabetic character
    #If there is a space, proceed to next recursive step
    elif string[0].isalpha()==False:
        return string[0]+encrypt(string[1:])       #do not change non-alphabetic character. Continue recursion.
    elif len(string)==1:
        if string[0]=='z':             #stooping case when last character is 'z'. caters for exception when string[0]=='z', gives 'a'
            encrypt_z='a'
            return encrypt_z        
        return chr(ord(string)+1)   #stopping case
    else:
        if string[0]=='z':             #caters for exception when string[0]=='z', gives 'a'
            encrypt_z='a'+encrypt(string[1:])
            return encrypt_z
        else:
            encrypted_string= chr(ord(string[0])+1)+encrypt(string[1:])      # convert character to unicode representation, add 1 and convert back to string representation.
            return encrypted_string

if get_str.islower():                      #check if string is lowercase before encrypting
    print("Encrypted message:")
    print(encrypt(get_str))
else :
    print("Encrypted message:")
    print(get_str)