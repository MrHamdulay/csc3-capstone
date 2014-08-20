#Assignment 9
#Question 3
#Rabia Parker
#Due Date: 09/05/14

#using recursion to encrypt a message

space=''
message=input("Enter a message:\n")

def encryption(message):
    global space
    if len(message)!=0:
        if message[0]=='z':
            space+= 'a'
            return encryption(message[1:])
        elif message[0]==" ":
            space+=' '
            return encryption(message[1:])
        else:
            value=ord(message[0])
            value+=1
            letter=chr(value)
            space+=letter
            return encryption(message[1:])

    else:
        print("Encrypted message:\n",space,sep='')
    

encryption(message)

    