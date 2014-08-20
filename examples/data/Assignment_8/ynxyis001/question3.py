# Encryts message (all letters to lowercase and the letter following it in alphabet)
#Jennifer Yuan
#7 May 2014

s = input("Enter a message:\n") #asks for input from user

def encrypt(s):
    if len(s)<2: #checks to see that length of string is larger than one character
        if s == "z": #"z" becomes "a"
            return "a"
        if s == " ": #a space stays a space in the after encryption
            return " "
        if s[0].isupper(): #a capital letter stays that same capital letter after the encrytion
                return s[0] 
        if s[0] ==".": #a fullstop stays a fullstop after the encrytion
            return "."
        else:
            return chr(ord(s[0]) +1) #if the character is none of the things mentioned above then it becomes the letter proceeding it in the alphabet. 
    else:
        if s[0] == "z": #same as above, but this is in a string longer than one character
            s[0] == "a"
            return encrypt(s[0]) + encrypt(s[1:]) #continues to recurse through string
        if s[0] == " ": #same as above
            s[0] == " "
            return encrypt(s[0]) + encrypt(s[1:])
        if s[0].isupper(): #same as above
            return encrypt(s[0]) + encrypt(s[1:])       
        else:
            s[0] == chr(ord(s[0]) +1) #same as above
            return encrypt(s[0]) + encrypt(s[1:])
        
    
print("Encrypted message:") #prints encrypted message
print(encrypt(s))