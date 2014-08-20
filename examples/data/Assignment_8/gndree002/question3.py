"""Recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a). 
Reece Gounden
7 May 2014"""
string = input("Enter a message:\n")
msg = ''

def encrypt(string):
    global msg
    if len(string)>1: 
        if string[0]=='z': #if z sets next letter to a
            msg+='a'
            string = string[1::]
        elif string[0]=='.':#if '.' sets next letter to '.'
            msg+='.'
            string = string[1::]        
        elif string[0]==' ':#if ' ' sets next letter to ' '
            msg+=' '
            string = string[1::]
        elif string[0].lower()==string[0]: #checks if letter is lowercase and if so changes letter to next ASCII char
            msg+=chr(ord(string[0])+1)
            string = string[1::]
        else: #if char is upper case then added to string straight
            msg+=string[0]
            string=string[1::]
        encrypt(string)
    elif len(string)==1: #same checks as before except this is for when the string has only 1 char left so it does not extract the char after it adds it to the encrpted message
        if string=='z':
            msg+='a'
        elif string[0]==' ':
            msg+=' '
        elif string[0]=='.':
            msg+='.'  
        elif string[0].lower()==string[0]:
            msg+=chr(ord(string[0])+1)
        else:
            msg+=string[0]
    
encrypt(string)
print("Encrypted message:\n"+msg)