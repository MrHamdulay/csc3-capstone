'''a recursive function to count the number of pairs of repeated characters in a string
sankara mallane
5 may 2014
'''

#a function to count the number of pairs
def numberofpairs(message):
    # check the length of message
    if len (message) > 1 :
        # check the letters next to each other if they match and if they do add one
        if message[0] == message[1]:
            return 1 + numberofpairs(message[2:])
        else:
            return 0 + numberofpairs(message[1:])
    else:
        return 0
# user input    
message = input("Enter a message:\n")

print("Number of pairs:",numberofpairs(message))