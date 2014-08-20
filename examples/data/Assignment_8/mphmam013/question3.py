"""Mphuthi Mamorena
assignment 8
question 3"""

message=input("Enter a message:\n")
print("Encrypted message:")

def nextletter(s):
    if s=='z':
        s='a'
        print(s,sep='',end='')
    elif s==' ':
        s=' '
        print(' ',sep='',end='')
    elif s=='.':
        s='.'
        print('.',sep='',end='')    
    else:
        a=ord(s)
        nextord=a+1
        B=chr(nextord)
        print(B,sep='',end='')
        
def Uppercase(message):
    if message==message.upper():
        print(message)
        
        
def encript(message):
    if message==message.lower():
        if message=='':
            return message
        else:
            return str(nextletter(message[0])) + encript(message[1:])
        
encript(message)
Uppercase(message)