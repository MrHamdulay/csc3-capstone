def encrypt(message):
    if message =='':# return empty string if message is an empty string
        return ''
    
    elif message == int:# return empty string if message is a number
        return ''
    
    a=ord(message[0])+1
    b=chr(a)
       
    if len(message)==1:
        if message[0]==message[0].upper():
            return message[0].upper()
        elif message[0]=="z":
            return "a"
        else:
            return b
    
    elif message[0]==message[0].upper():
        return message[0]+ encrypt(message[1:])
    
    elif (ord(message[0]) == 32):
            b = chr(a-1) 
            
    elif message[0]=="z":# Converting z to a
        return "a" + encrypt(message[1:])
    
    elif message[0] < chr(97):
        b = message[0]    
    
    else:
        return b + encrypt(message[1:])    
    
message=input("Enter a message:\n")
print('Encrypted message:')
y=encrypt(message)
print(y)

        