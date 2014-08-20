#A program to count the number of pairs of repeated characters in a string.
#BRXCAI001
#09 May 2014

message = input("Enter a message:\n")

def checkrepeats (message):
    #If the messsage has only no or 1 character, there can be no repitions.
    if len(message) == 0 or len(message) == 1:
        return 0
    #If the first character equals the second then you add to the number of repeated pairs.
    elif message[0] == message [1]:
        return 1 + checkrepeats(message[2:])
    #If the first character does not equal the second then you do not add to the number of repeated pairs and check the next letter.
    else:
        return 0 + checkrepeats(message[1:])
        
print("Number of pairs:", checkrepeats(message), end= "")

        
    
    