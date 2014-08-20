"""assignment 9 question 2
shannon clacey
8 may 2014"""

string = input ("Enter a message: \n") #gets the input message from the user

def pair(parameter):
    length = len(parameter) #establishes the length of the given parameter
    if length == 1: #sees if the length is equal to 1 and if so returns 1
        return 0
    if length != 1 and length != 2: #checks if the length is greater than 2 (i.e. not equal to one or two 
        if parameter[1] == parameter[0]: #sees if teh letter in position 1 is equal to that in position two
            parameter = parameter[2:]
            return 1 + pair (parameter) #if so it returns 1 plus the given parameter
        else:
            return pair(parameter[1:]) #if not, it returns the position only after the first two positions, so that the process can continue to search for new pairs
    else:
        if parameter[0] == parameter[1]:
            return 1
        else:
            return 0 

print ("Number of pairs:", pair(string))