'''program to encrypt a message
Luke Naude
7 May 2014'''

message_=input('Enter a message:\n')
message=message_.lower()
alphabet='abcdefghijklmnopqrstuvwxyz'#string containing the alphabet
encrypted='' #empty string for encrypted message
letter_no=0 #letter number to encrypt
def encrypt(letter_no):
    global encrypted
    if letter_no<len(message) and message[letter_no] == ' ':
        '''skip encryption on an empty space and add a space'''
        encrypted+=' '
        return encrypt(letter_no+1)#perform recursion on next letter
    
    elif letter_no<len(message):#encrypt if within list length
        encrypted+=(alphabet[alphabet.find(message[letter_no])+1])#add encryption to encryption string
        return encrypt(letter_no+1) #perform encryption on next letter
    
encrypt(letter_no)
print('Encrypted message:\n',encrypted,sep='') #print output