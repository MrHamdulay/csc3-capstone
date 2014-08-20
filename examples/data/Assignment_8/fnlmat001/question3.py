# Mathew Finlayson - FNLMAT001
# Assignment 8 - Question 3
# 04/05/2014

def encode(s):
    if s == "": # end case
        return ""
    if s[0] == " " or s[0] == ".": # doesn't change spaces or fullstops
        return s[0] + encode(s[1:])
    elif s[0].islower():
        if (s[0] == "z"): # character 'z' gets changed to character 'a'
            return "a" + encode(s[1:])
        else:
            return chr(ord(s[0])+1) + encode(s[1:]) # each other character is converted to the next character
    else:
        return s[0] + encode(s[1:])

# prompts user for input and prints the encrypted message
print("Encrypted message:\n" + encode(input("Enter a message:\n")))