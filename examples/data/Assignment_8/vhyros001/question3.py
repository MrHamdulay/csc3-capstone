"""Assignment 8 question 3 encrpyt a string by moving letters 1 forward
Ross van der Heyde VHYROS001
7 May 2014"""

def encrypt(word):
    """encrpyt a string by moving letters 1 forward"""
    if len(word) == 1:
            if word.islower() and word !='z':#only encode lower case letters
                return chr(ord(word) + 1)
            elif word.isupper and word != 'z':
                return word
            elif word == 'z': # special case: z
                return chr(ord(word) -25)
    else:
        myChar = word[0] #first get first chararacter in the word
        if myChar.islower() and myChar != 'z':
            myChar = chr(ord(word[0])+1)
        elif myChar == 'z': # special case: z
            myChar = chr(ord(word[0])-25)
        elif myChar.isupper:
            pass    
        return  myChar + encrypt(word[1:])
    
mess = str(input("Enter a message:\n"))
crypt = encrypt(mess)
print("Encrypted message:")
print(crypt)
