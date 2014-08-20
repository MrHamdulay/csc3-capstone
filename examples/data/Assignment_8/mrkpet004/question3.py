"""program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
peter m muriuki
9/5/14"""
 
string=input("Enter a message:\n")

#replace all occurrences of lower case letters with the next character
def encrypt (string):
    # base case - empty string
    if len (string)==0:
        return string
    # first recursive step - replace "z" if found
    elif string[0]=="z":
        return chr(97) + encrypt (string[1:])
    # second recursive step - replace all other lower letters which are not z 
    elif string[0].isalpha() and string[0].islower():
        return chr(ord(string[0])+1) + encrypt (string[1:])
    # third recursive step - alphabetic and lower case not found
    else:
        return string[0] + encrypt (string[1:])
    
print ("Encrypted message:")
print (encrypt(string))