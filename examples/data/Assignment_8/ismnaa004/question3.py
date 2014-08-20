#Naadirah Ismail
#8 May 2014
#encrypt message in ascii code
message=input('Enter a message:\n')
def incrypt(message):    
    lenmsg=len(message)
    new=''
    if lenmsg==0:
        return new
    elif message[0]==' ':
        return ' '+incrypt(message[1:])      
   
    elif lenmsg>0 and message[0]!='z' and message[0].islower() and message[0].isalpha():
        new=chr(ord(message[0])+1)

        return new+incrypt(message[1:])
    if message[0]=='.':
        return message[0]                   
    if message[0]=='z':
        new=chr(ord(message[0])-25)
        return new +incrypt(message[1:])
    
    elif message[0].isupper():
        return message[0]+incrypt(message[1:])
    else:
        return
    
print('Encrypted message:\n',incrypt(message),sep='')    

incrypt(message)














