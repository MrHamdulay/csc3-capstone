"""Assignment 8 Question 2
James Lloyd
4 May 2014"""

#Retrieving message
message = input ("Enter a message:\n")

def repeat (message):
    """Function to count the number of double characters"""
    #Setting the base case
    if len (message) == 1:
        return 0
    if len (message) == 2:
        if message [0] == message [1]:
            return 1
        else:
            return 0
    #Checking the first two characters. If same add one, else slice string
    else:
        if message [0] == message [1] and message [0] != ' ' and message [1] != ' ':
            return 1 + repeat (message [2:])
        else:
            return 0 + repeat (message [1:])

#Printing the number of pairs
print ("Number of pairs: " + str (repeat (message)))
