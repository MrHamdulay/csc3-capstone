'''
Created on 06 May 2014
Recursive Caesar encryption 
@author: Yusuf Khan
KHNYUS005
'''
def encrypt(msg):
    if msg[0:1:]=='z':
        print('a',end='')#converts z to a
    elif msg[0:1:].islower():#main conversion, all lowercase to one up
        print(chr(ord(msg[0:1:])+1),end='')
    elif msg[0:1:]=='':#stops recursion if no letters left
        return ''
    else:#outputs punctuation marks and caps as normal
        print(msg[0:1:],end='')
        
    msg = msg[1::]#cuts first char off
    return encrypt(msg)

msg = input('Enter a message:\n')#input
print ('Encrypted message:')
print (encrypt(msg))#output