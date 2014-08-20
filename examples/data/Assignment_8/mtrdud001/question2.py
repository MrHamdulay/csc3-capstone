""" using recursion to count repeated strings
Dudley Mutero
9 may 2014"""

def numberofpairs(message):
    """characters in a string with repitition"""
    if len (message) > 1 :
        if message[0] == message[1]:
            return 1 + numberofpairs(message[2:])
        else:
            return 0 + numberofpairs(message[1:])
    else:
        return 0
    
#main input from user
message = input("Enter a message:\n")
print("Number of pairs:",numberofpairs(message))