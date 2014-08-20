"""Friday 9th May 2014
Itumeleng Nqoko
Assignment 8 question 3"""
#Program to encrypt a message by changing all lowercase letters to the next one

message=input("Enter a message:\n")
print("Encrypted message:")
def encrypted(message):
    if message.islower():
        if len(message)!=0:
            
            if message[0]=="z":
                print(chr(ord(message[0])-25),end="")
            elif message[0]==" ":
                print(" ",end="")
            elif message[0]==".":
                print(".",end="")
            else:
                print(chr(ord(message[0])+1),end="")
            encrypted(message[1:])
    else:
        print(message)
                
                

encrypted(message)
        

