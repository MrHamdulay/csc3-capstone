#Ariel Rubin
#RBNARI001
#program that finds the number of pairs of letters in a sentence using recursion
#9 May 2014

#function to determine number of pairs in a sentence
def pairs (sentence):
    if len(sentence) == 1 or len(sentence) == 0:
        return 0
    if sentence[0] == sentence[1]:
        return 1 + pairs(sentence [2:])
    else:
        return 0 + pairs(sentence[1:])
#ask user to enter a message    
message = input ("Enter a message:\n")
#displays number of pairs in that message
print ("Number of pairs:",pairs(message))
    