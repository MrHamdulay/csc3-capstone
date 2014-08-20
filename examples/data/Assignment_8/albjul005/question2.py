'''Letter pairing - Assignment 8
Julian Albert
08-05-2014'''

message = input("Enter a message:\n")

def pairs (message):
    if len(message) == 1: #if one character, then there are no pairs
        return 0
    if len(message) == 2 and message[0] == message[1]: #if there are two characters, and if they are the same, then 1 pair
        return 1
    if message[0] == message[1]: #if the first two letters are equal, then run through the function again
        return 1 + pairs(message[2:])
    else:
        return pairs(message[1:])
print("Number of pairs:", pairs(message))
