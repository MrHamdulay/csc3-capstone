#program for counting pairs that are repeated
#aphiwe baleni
#9 may 2014
def pairs(message):
    if len(message)<2:
        return 0
    elif message[0] == message[1]:
        return 1 + pairs(message[2:])
    else:
        return pairs(message[1:])
message=input("Enter a message:\n")
print("Number of pairs:",pairs(message))