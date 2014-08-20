#Question 3 - Assignment 8
#Riya Desai
#8 May 2014


#ask the user to type in a message
message=input("Enter a message:\n")

#define the function "Encrypting"
def Encrypting(message):
    
    if message =="":
        return ""
       
    elif message[0]==" ":
        return " " + Encrypting(message[1:])
    
    elif(ord(message[0])<97):
        return message[0] +Encrypting(message[1:])
       
    elif(message[0]=='z'):
        return "a" + Encrypting(message[1:])
    
    elif not message[0].isalpha():
        
        return message[0] + Encrypting(message[1:])
       
    else:    
        
        return chr(ord(message[0])+1)+Encrypting(message[1:])
    
new_message=Encrypting(message)

#print the encrypted message
print("Encrypted message:\n"+str(new_message))