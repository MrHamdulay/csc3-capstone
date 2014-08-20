"""Question 2: Looks for identical letters next to each other
Galya Wolov
9 May 2014"""

message= input("Enter a message:\n") #asks 4 message

def pairs(x):
    if len(x) == 0 or len(x) ==1: 
        return 0
        #sees the length of the string if too small wont have a pair
    if x[0] == x[1]:
        return 1 + pairs(x[2:]) #sees if there is a pair in the first two next to eachother
    #recursive step above if pair exists
    else:
        return pairs(x[1:])#recursive step if pair does not exist



print("Number of pairs:", pairs(message))

#print statement of how many pairs
