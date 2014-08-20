"""YONELA FORD
FRDYON001
04 MAY 2014"""

# get an input message from the user
message=input("Enter a message:\n")

def count_pairs(message):
    #check if there are no pairs and return 0
    if len(message)<2:
        return 0
    #if there is a pair return 1 and look at the rest of the string without this pair
    elif message[0]==message[1]:
        return 1+ count_pairs(message[2:])
    else:
        #if there is no pair found before, continue checking without checking the last pair
        return count_pairs(message[1:])
#print result    
print("Number of pairs: ", end="")
print(count_pairs(message))
        
    
    