'''a recursive function to count the number of pairs of repeated characters in a string
kimley
5 may 2014
'''

#define function message
def numberofpairs(message):
    if len (message) > 1 :
        if message[0] == message[1]:
            return 1 + numberofpairs(message[2:])
        else:
            return 0 + numberofpairs(message[1:])
    else:
        return 0
    
message = input("Enter a message:\n")

print("Number of pairs:",numberofpairs(message))