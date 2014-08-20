#mahdi marcus

s="" #empty string
m=input("Enter a message:\n") #get messsage frm user


def e(m): #encryption function
    global s
    
    if len(m)!=0: #has a length
        if m[0]=='z':
            s+= 'a'
            return e(m[1:])
        elif m[0]==" ":
            s+=' '
            return e(m[1:])
        else:
            n=ord(m[0]) #getting a number
            n+=1
            w=chr(n) #getting a word
            s+=w
            return e(m[1:])
    

    else:
        print("Encrypted message:\n",s,sep='')
        
e(m)
    



    