#A program to encrypt a mssages
#F.J.Chigwaza
#08 May 2014

msg=input('Enter a message:\n')
blank=''
def encrypt(msg,blank):
    
    if msg=='':
        return 'Encrypted message:\n'+blank
    else:
        if msg[0].islower() and msg[0]!='z':
            blank+=chr(ord(msg[0])+1)
            return encrypt(msg[1:],blank)
        elif msg[0]=='z':
            blank+='a'
            return encrypt(msg[1:],blank)        
        elif msg[0].isupper():
            blank=blank + msg[0]
            return encrypt(msg[1:],blank)
        else:
            blank=blank+msg[0]
            return encrypt(msg[1:],blank)
print (encrypt(msg,blank))            
            
        


