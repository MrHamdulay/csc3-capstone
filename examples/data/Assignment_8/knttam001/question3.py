"""Program to Convert Lowercase Characters to Next Character Using Recursion
Tamsin Kantor
May 2014"""

message = input("Enter a message:\n")

def encode(m):
    if m == "": # base case to end recursion
        return m
    elif m[0] == " ": # if the character is a space, return a space
        return " " + encode(m[1:])
    elif m[0] == ".": # if the character is full stop, return a full stop
        return "." + encode(m[1:])
    elif m[0] == "z": # if the character is a z, return a
        return "a" + encode(m[1:])
    else: # all other characters - return next character
        return chr(ord(m[0])+1) + encode(m[1:])

if message.islower(): # if the message is in lowercase
    x = encode(message) # run function
    print("Encrypted message:")
    print(x) #print output
else:
    print("Encrypted message:") # if the message is NOT lowercase, print the message
    print(message)    