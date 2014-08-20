'''Dumisani Ngwenza
NGWDUM005
06/05/2014
Assignment 8 Question 3'''


#Enter a string
string = input ('Enter a message:\n')
space = ord (' ')

#Encrypt Message using recursion
def EncryptMes(string):
    lowercase = string.lower()
    if string == '':
        return (' ')
    if string[0].istitle():
        return string[0] + EncryptMes(string[1:])
    if string[0] == 'z':
        return 'a' + EncryptMes(string[1:]) 
    if string[0] == '.':
        return string[0] + EncryptMes(string[1:])
    if string[0] == ':':
        return string[0] + EncrpytMes(string[1:])    
    if string[0]!= ' ':
        character = chr(ord(string[0])+1)
        return character + EncryptMes(string[1:])
    if string[0] == ' ':
        return string[0] + EncryptMes(string[1:])
    
    
print ('Encrypted message:')
print (EncryptMes(string))
