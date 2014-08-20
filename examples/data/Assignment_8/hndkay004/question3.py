#Program to encrypt a message
#Kayla Hendricks
#08 May 2014

new_string=""
def encrypt(message):
    if message[0:-1].islower():
        global new_string       #to call the empty string that is not in the function defined
        if len(message)!=0:
            if message[0]=='z':     #if letter is z, add an a to the empty string. This is the base case
                new_string+='a'
                return encrypt(message[1:])     #start again less the first letter
            elif message[0]==" ":
                new_string+=" "
                return encrypt(message[1:])
            else: 
                value=ord(message[0])   #getting a value for the letter
                value+=1                #adding one to the value
                letter=chr(value)       #getting a corresponding letter to the new value
                new_string+=letter      #adding the letter to empty string
                return encrypt(message[1:])
        else:
            print("Encrypted message:\n",new_string,sep="")
    else:
        new_string+=message
        print("Encrypted message:\n",message,sep="")
    
message=input("Enter a message:\n")
encrypt(message)