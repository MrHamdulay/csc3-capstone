#Pairs
#Sofia Palmer
#5 May 2014

message = input("Enter a message: \n")
def pairs(position, message, count):
    #recurse through message if position is less than len of message
    if (position < len(message)-1):
        #if two letters next to each other are the same, that is a pair
        if message[position] == message[position + 1]:
            return pairs(position+2, message, count+1)
        else:
            return pairs(position+1, message, count)
    else:
        print("Number of pairs:", count)
pairs(0, message, 0)
    
