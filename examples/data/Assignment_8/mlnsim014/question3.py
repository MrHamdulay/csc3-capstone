'''program to encrypt a message entered by a user by changing lowercase characters
Simangaliso Mlangeni
MLNSIM014
04 May 2014
Assignment 8, question 3'''


def encrypt(s):
    '''function that will encrypt the message'''
    if len(s)==1:#Base case to make sure that program does not index out of range when length of word is 1
        if s[0]==s[0].upper():
            return s[0]
        elif s[0]== 'z':
            return 'a'
        else:
            return chr(ord(s[0])+1)
    elif s[0]=="z": #special case, changes z to a since next numeric character after z is not an alphabet
        return chr(97) + encrypt(s[1:])
    elif 97<=ord(s[0])<=121: #checks whether the character is an alphabet or not and if it is a lowercase character
        return chr(ord(s[0])+1) + encrypt(s[1:]) #encrypt the character if the conditions above are true
    else:
        return s[0] + encrypt(s[1:]) #if character is not an alphabet or isn't in lowercase, returns as it is and recurses


#requests message to encrypt from user
s = input("Enter a message:\n")
#invokes function while printing encrypted message
print("Encrypted message:\n",encrypt(s),sep="")