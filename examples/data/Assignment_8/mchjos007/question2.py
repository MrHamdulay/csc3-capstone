def theNumberOfPairsOfCharactersiInAString(theStringInQuestion):
    if len(theStringInQuestion) == 1 or len(theStringInQuestion) == 0:
        return 0
    if theStringInQuestion[0] == theStringInQuestion[1]:
        return 1 +theNumberOfPairsOfCharactersiInAString(theStringInQuestion[2:])
    else:
        return theNumberOfPairsOfCharactersiInAString(theStringInQuestion[1:])    
    
thestring = input("Enter a message: \n")
print ("Number of pairs: "+ str(theNumberOfPairsOfCharactersiInAString(thestring)))