# Aaron Krishna
# 5 may 2014
# A program that counts the number of pairs of repeated characters in a string

def count_pair(message): #function that counts number of pairs
    if len(message) == 2:
        if message[0] != message[1]: #base case
            return 0
        else:
            return 1
    elif len(message) < 2:
        return 0
    elif message[0] == message[1]:
        return 1 + count_pair(message[2:]) #makes sure there are no overlapping pairs
    else:
        return count_pair(message[1:])

message = input("Enter a message:\n")

print("Number of pairs:", count_pair(message)) #print number of pairs