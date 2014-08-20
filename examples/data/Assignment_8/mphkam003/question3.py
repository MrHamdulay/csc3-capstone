"""convert all lowercase characters to the next character
kamogelo mphela
06 may 2012"""


def encrypt(s):
    """shift alphabets by 1"""
    if len(s) == 0:
        return ""
    
    elif s[0] == " ":
        return  " " + encrypt(s[1:])
    elif s[0] == '.':
        return "." + encrypt(s[1:])
    elif s[0]== "z":
        return "a" + encrypt(s[1:])
    
    else:
        return chr(ord(s[0])+1) + encrypt(s[1:])
    
string = input("Enter a message:\n")
encrypt(string)
print("Encrypted message:")
if string == string.upper():
    print(string)
else:
     print(encrypt(string))