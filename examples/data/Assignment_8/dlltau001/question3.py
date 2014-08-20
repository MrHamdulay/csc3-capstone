'''Question 3
Assignment 8
Tauriq Dolley

Write a program that, using recursion, encrypts a sentence to the next letter character in the alphabet'''

message = input("Enter a message:\n")
#message = message.lower()

def encode(message,encryption):
     
    if message == '':
        print("Encrypted message:\n",encryption,sep='')
    elif message[0:1] == 'z':
        return encode(message[1:],encryption + 'a')
    elif message[0:1] == ' ':
        return encode(message[1:],encryption + ' ')
    elif message[0:1].islower(): 
        num = 1 + ord(message[0:1])
        letter = chr(num)
        return encode(message[1:],encryption + letter)
    else:
        return encode(message[1:],encryption + message[0:1])
        
        
encode(message,"")