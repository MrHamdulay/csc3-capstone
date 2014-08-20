#deepak bhoojrajh
#question 3


a=""

def new(msg):
    global a
    
    if (msg==''):
        return a
    
    elif(ord(msg[0])>96 and ord(msg[0])<122):
        a=a+chr(ord(msg[0])+1)
        return new(msg[1:len(msg)])
   
    elif(ord(msg[0])==122):
        a=a+'a'
        return new(msg[1:len(msg)])  
   
    else:
        a=a+msg[0]
        return new(msg[1:len(msg)])  
        
x=input("Enter a message:\n")
print("Encrypted message:")
print(new(x))