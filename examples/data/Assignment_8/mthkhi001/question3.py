#Recursion
#MTHKHI001
#Assignment 8
#question 3
"""program uses recursion to encrypt a message by shifting all lowercase values to the next letter in the alphabet"""

#test = "a"
#position = ord(test)
#newletter = chr(position+1)
#print(newletter)
#print(str(position))



def encryption(message,length,position,encrypted):
    
    if position == length :
        return encrypted
    
    else:
        if message[position].isupper() or message[position].isalpha() == False:
            encrypted = encrypted + message[position]

            return encryption(message,length,(position+1), encrypted)
        
        else:
            if message[position] == "z":
                encrypted = encrypted + "a"
                return encryption(message,length,(position+1),encrypted)
            else:
                next_letter = chr(ord(message[position])+1)
            
                encrypted = encrypted + next_letter
            
                return encryption(message,length,(position+1),encrypted)

message = input("Enter a message:\n")
length = len(message)
position = 0
encrypted = ""

encrypted_message = encryption(message,length,position,encrypted)
print("Encrypted message:")
print(encrypted_message)
