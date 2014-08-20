"""Tevin Chetty
8 May 2014
Program to encrypt message"""

def encrypt(message,final):
    if message=="": #if empty string print empty string
        return print(final)
    else:
        position=ord(message[0]) #converts to unicode
        if 97<=position<122: #checks if it is lowercase
            position+=1 #moves one letter up
            new=chr(position) #converts back to normal letters
            final=final+new
            return encrypt(message[1:],final) #moves on to next letter
        elif position==122: #statement to make z a
            exception="a"
            final=final+exception
            return encrypt(message[1:],final)
        else:
            final+=chr(position)
            return encrypt(message[1:],final) #if not lowercase alphabet simple print it out
    print(final)
message=input("Enter a message: \n")
print("Encrypted message:")
encrypt(message,"")
    
    
    