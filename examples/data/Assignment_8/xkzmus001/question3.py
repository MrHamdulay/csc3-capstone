"""question3.py :- encrypt a message by converting all lowercase characters to the next character
Author : Musa Xakaza
Date : 06/05/2014"""

def encrypt(s):
    if len(s) > 0:
        c = s[0]
        uniCode = ord(c)
        #take the first character of a string and get its unicode, increment it & converting to next character
        if 97 <= uniCode <= 121:
            c = chr(uniCode+1)
            return c + encrypt(s[1:])
        elif uniCode == 122:
            return chr(97) + encrypt(s[1:])
        else:
            return c + encrypt(s[1:])
    else:
        return ""

msg = input("Enter a message:\n")
if msg:
    print("Encrypted message:",encrypt(msg),sep='\n')