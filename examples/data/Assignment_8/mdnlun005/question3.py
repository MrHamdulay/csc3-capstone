#-------------------------------------------------------------------------------
# Name:        question3
# Purpose:     program that uses a recursive function to encrypt a message by
#              converting all lowercase characters to the next character
#              (with z transformed to a)
#
# Author:      Lungelo Mdunge
#
# Created:     04/05/2014
# Copyright:   (c) Lungelo 2014
#
#-------------------------------------------------------------------------------

message=input('Enter a message:\n')

def encrypt(message):
    if not message.islower():
        return message
    if message=='':
        return ''

    elif message[0]=='z':
        return chr(ord(message[0])+1-26) + encrypt(message[1::])

    elif message[0]==' ':
        return ' ' + encrypt(message[1::])
    elif not 97<=ord(message[0])<=122:
        return message[0] + encrypt(message[1::])
    else:
        return chr(ord(message[0])+1) + encrypt(message[1::])

encrypted=encrypt(message)
print("Encrypted message:\n",encrypted,sep='')




