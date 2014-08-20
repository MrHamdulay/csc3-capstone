'''Encrypion programme 
Siphesihle Zwane 
05/09/14'''
def encrypt(word):
    if word=="":
        return ""
    elif word[0]== " ":
        return " " +  encrypt(word[1:])
    elif word[0] != word[0].lower():
        return word[0] + encrypt(word[1:])
    elif word[0]=='z':
        return 'a' + encrypt(word[1:])
    elif word[0]== '.':
        return '.'
    else:
        asci= ord(word[0])+1
        return chr(asci) + encrypt(word[1:])
secret=input("Enter a message:\n")
print("Encrypted message:\n",encrypt(secret),sep='')