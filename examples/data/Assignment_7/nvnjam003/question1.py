#Assignment 7, Question 1
#James Nevin
#01/05/2014

print ("Enter strings (end with DONE):")
userStrings = [] #List for user's entries
userInput = ""
while (userInput != "DONE"): #Getting user's entries
    userInput = input()
    userStrings.append(userInput)

alreadyPrinted = [] #List for what's been printed
print ("\nUnique list:")
for item in userStrings:
    if (item not in alreadyPrinted and item != "DONE"): #Mustn't be DONE or already printed
        print (item)
        alreadyPrinted.append(item) #Add to list of printed