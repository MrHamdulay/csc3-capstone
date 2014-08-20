#Aniq Hartle
#Count number of character pairs
#09/05/2014

'''count the number of paired characters in the input string'''
def countPairs(userI):
    if userI == userI[len(userI)-1]:   #if there is only 1 character left, stop checking
        return 0
    elif userI[0]==userI[1]:
        if len(userI)>2:
            return 1+countPairs(userI[2:])#if a match exists, add 1 and continue
        else:
            return 1+countPairs(userI[1:])
    else:       #continue if no match found
        return countPairs(userI[1:])

#take in input from user and apply method to check number of pairs, produce output    
userInput = input("Enter a message:\n")
print("Number of pairs:",countPairs(userInput))