"""Name: Sibulele Hlongwane
Date: 06 May 2014
Assignment: Counting number of pairs in a string"""

message= input("Enter a message:\n")
count=0
def CountPairs(message):
    #checks to see if message is less than 2 words
    if len(message)<2:
        return 0
    else:
        #checks to see if first character of word matches second character of word and increases the counter if the condition is satisfied, and a "new" string is then returned from the 2nd position
        if (message[0])==(message[1]):
            return (count+1)+ CountPairs(message[2:])
        else:
            #else if the first character doesnt match the second character, just return the counter and "new" string from the first position
            return  count+CountPairs(message[1:])
#displays the number of pairs
print("Number of pairs: " +str(CountPairs(message)))