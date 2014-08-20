def pairs (userInput):

    if len(userInput) == 1 or len(userInput) == 0:

        return 0

    if userInput[0] == userInput[1]:

        return 1 + pairs(userInput [2:])

    else:

        return 0 + pairs(userInput[1:])

    

userinput = input ("Enter a message:\n")

print ("Number of pairs:",pairs(userinput))


