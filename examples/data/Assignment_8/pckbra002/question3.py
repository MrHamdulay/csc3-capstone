"""Brandon Pickup"""
"""3 May 2014"""
"""Assignment 8 Question 3"""
sent = input("Enter a message:\n")
def encrypt(s):
    """function to encrypt a message by converting all lowercase characters to the next character"""
    if s == "":
        return ""
    elif s[0].isupper():
        return s[0] + encrypt(s[1::])
    elif s[0].isalpha()==False:
        return s[0] + encrypt(s[1::])
    elif s[0]==" ":
        return " " + encrypt(s[1::])#if the character is a space, it keeps the space and runs encrypt on the rest of the string
    else:
        if s[0] == "z":#if the letter is z, it is changed to the next letter of the alphabet -a
            return "a" + encrypt(s[1::])
        else:
            x = ord(s[0]) + 1#gets the ASCII value of the character and adds 1 to it
            ch = chr(x)
            return str(ch) + encrypt(s[1::])#returns the shifted number, now in character form with the encryption runnin on what is left of the string
print("Encrypted message:\n",encrypt(sent),sep="")