'''Assignment8q2, character pairing counter
Kieran Reilly, RLLKIE001
06/05/14'''

def charPair(userString, count):
    '''returns a count of pairs in a string'''
    #basecase - does nothing if length is less than 2
    if len(userString) >= 2:
        #recursive case and step - checks the current two pairs, and then goes to the next two characters
        if userString[0] == userString[1]:
            count += 1
            count = charPair(userString[2:], count)
        #recursive step - steps to the next character
        else:
            count = charPair(userString[1:], count)
    return count

def main():
    userString = input("Enter a message: \n")
    numPairs = charPair(userString, 0)
    print("Number of pairs: "+str(numPairs))
    
    
main()