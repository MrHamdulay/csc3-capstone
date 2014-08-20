'''Encript a message
Othniel KONAN
KNNOTH001
2014/05/04'''

def encript(st):
    if len(st)>0:                               #set the break point to when the string is empty
        if (ord('a') <= ord(st[0]) < ord('z')):   #check if the letter is between a and y (ncluding both)
            print(chr(1+ord(st[0])),end='')     #change the letter to its next
        elif (ord(st[0])==ord('z')):              #if the letter is 'z'
            print('a',end='')                   #we change it manually to 'a'
        else:
            print(st[0],end='')                 #if it's not a lowercase character we keep it
        return encript(st[1:])                  #we continue to encript with the rest of the word

st=input('Enter a message:\n')
print('Encrypted message:')
encript(st)