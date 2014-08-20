#Author: NLXALE001
#Date: 6 May 2014
#Assignment8

global message
message = input("Enter a message:\n")
global newmessage
newmessage = ""
global index
index = 0

def encrypt(message, index, newmessage):
    if index == len(message):
        print ("Encrypted message:\n", newmessage, sep="")
    elif message[index] == " ":
        newmessage += " "
        encrypt(message, index+1, newmessage)
    else:
        #if letter is z then return a
        if (ord(message[index])) == 122:
            letter = 97
        #else return the next letter
        elif (ord(message[index]))>=97 and ord(message[index])<122:
            letter = ord(message[index]) +1
        #letter is capital so return same letter
        else:
            letter = ord(message[index])
        newmessage += chr(letter)
        encrypt(message, index+1, newmessage)


encrypt(message, index, newmessage)



