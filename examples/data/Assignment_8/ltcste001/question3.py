#Stephanie Latchmanan
#5 May 2014
#Assignment 8 (encrypting a message)

#create a recursive function
def encrypt(msg):
    if len(msg) == 0:  #stop recursion when no more characters left
        return ""
    if msg.islower() == False:
        return msg
    if msg[0] == "z":  #wrap around z to become a
        return "a" + encrypt(msg[1:])
    if msg[0] == " ":  #place a space when there is a space for return
        return " " + encrypt(msg[1:])   
    if msg[0] == ".":
        return "." + encrypt(msg[1:])
    else:  #convert original character to next lowercase character when not z
            return chr((ord(msg[0]))+1) + encrypt(msg[1:])
    
    
#input a message:
msg = input("Enter a message:\n")
#return encrypted message
print("Encrypted message:\n", encrypt(msg), sep="")