""""this program converts any small letters in a phrase or sentence and encrypts it by converting it to the letter that follows
quincy cele
9 may 2014"""

encrypt=input("Enter a message:\n")

def encrypted(string):
    """this function encrypts a string by converting all lower case letters to the letter that follows in the alphabet"""
    if len(string)==0:
        return ""
    else:
        char=string[0]
        if char.islower() and char.isalpha():
            if char=="z":
                char="a"
            else:
                char=chr(ord(char)+1)
               
                
        return char+encrypted(string[1:])
#display encrypted message
x=encrypted(encrypt)
print("Encrypted message:")
print(x)

               
        
                             
                             
    
    