"""Michael Odhiambo
ODHMIC003
Assignment 8_Question 3
Program to encrypt a given message"""
message= input("Enter a message:\n")#Prompt user for input of message
array=[]
"""Convert each letter in message to the next letter in the alphabet and convert z to a. Append each converted letter to an array""" 
def encrypt(message):
        if len(message)>=1:
                if message.islower() == False:
                        array.append(message)
                else:
                        if message[0]=="z":
                                array.append("a")
                                encrypt(message[1:])                
                        elif message[0]==" ":
                                array.append(" ")
                                encrypt(message[1:]) 
                        elif message[0]==".":
                                array.append(".")
                                encrypt(message[1:])                         
                        else: 
                                x= chr(ord(message[0])+1)
                                array.append(x)
                                encrypt(message[1:])                
encrypt(message)    
x= "".join(array)#Convert array containing converted letters to a string
print("Encrypted message:")
print(x)
