#kairav soni 
#09/05/14
#q3 ASS 7


message=input("Enter a message:\n")
list1=[]

def shift(message):
    
    if (97)<=(ord(message[0]))<((122)):
        ch=(ord(message[0]))+1
        list1.append(chr(ch))
        
        if len(message)>1:
            shift(message[1:])
            x=("").join(list1)
            return (x)
        
        
        else:
            y=("").join(list1)
            return (y)
        
    
    elif (ord(message[0])==122):
        ch=97
        list1.append(chr(ch))
        
        
        if len(message)>1:
            shift(message[1:])
            z=("").join(list1)
            return (z)  
        
        
        else:
            a=("").join(list1)
            return (a)         
        
        
    else:
        ch=ord(message[0])
        list1.append(chr(ch))
        
        
        if len(message)>1:
            shift(message[1:])
            b=("").join(list1)
            return (b)
        
        
        else:
            c=("").join(list1)
            return (c) 
        

newmsg=shift(message)

print("Encrypted message:")
print(newmsg)
 

    

