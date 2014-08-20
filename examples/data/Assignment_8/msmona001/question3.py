"""recursive function that encrypts a message
Onalerona Mosimege
04 May 2014"""

#initialize string
global new_s
new_s = ""

def Encrypt(s):
    """encrypts a message by converting all lowercase characters to the next character (with z transformed to a)"""
    #base case- if string is empty
    if s == "":
        return ""
    #recursion statement1- not a lower case alphabet
    elif (s[0] <'a') or (s[0] > 'z'):
        return new_s + s[0] + Encrypt(s[1:len(s)])
    #recursive statement2 - if alphabet is a z
    elif s[0] == 'z':
        return new_s + 'a' + Encrypt(s[1:])
    #recursion statement3- convert alphabet to the next in line
    else:
        return  new_s + (chr(ord(s[0])+1)) + Encrypt(s[1:len(s)])
    

    
s= input('Enter a message:\n')
string= Encrypt(s)
print("Encrypted message:")
print(string)