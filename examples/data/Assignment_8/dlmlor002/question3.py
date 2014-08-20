"""Program to encrypt a message by changing the letters in the message to the next one in the alphabet
Lorena Dal Maso
10 May 2014"""

#get message from the user
message = input("Enter a message:\n")
#create a new string which will be the encrypted message
new_message = ""

def secret (message):
    global new_message
    #base case
    if message == "":
        return new_message
    #look if letter in string is lower case
    elif 96<ord(message[0])<122:
        new_message = new_message + chr(ord(message[0])+1)
        return secret (message[1:])
    #sort out the problem if the user types in "z"
    elif message[0]=="z":
        new_message = new_message + "a"
        return secret (message[1:])
    else:
        new_message = new_message + message[0]
        return secret (message[1:])
            
#print out encrypted message for the user to see            
print("Encrypted message:\n",secret(message),sep="")