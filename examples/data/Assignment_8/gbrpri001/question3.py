"""PRIYANKA GOBERDHAN
08/05/2014
ASSIGNMENT 8 - QUESTION THREE"""


message = ""

def encrypt_wrd(word):
    global message
    if (word==''):
        return message

    elif(ord(word[0])>96 and ord(word[0])<122):
        message = message+chr(ord(word[0])+1)
        return encrypt_wrd(word[1:len(word)])

    elif(ord(word[0]) == 122):
        message=message+'a'
        return encrypt_wrd(word[1:len(word)])  

    else:
        message = message+word[0]
        return encrypt_wrd(word[1:len(word)])  

a = input("Enter a message:\n")

print("Encrypted message:")

print(encrypt_wrd(a))
























 
 
 
  




 
