#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 2

def countPairs(string): #function to count the number of pairs of a single letter
    if string==string[len(string)-1]:
        return 0 #if there is only one character left of the string
    
    elif string[0]==string[1]:
        if len(string)>2:
            return 1+countPairs(string[2:]) #incrementing the counter of consecutive letters then continuing to recurse through the word
        else:
            return 1+countPairs(string[1:]) 
    else:
        return countPairs(string[1:])
    
stringInput = input("Enter a message:\n") #asking for a string to be input

print("Number of pairs:",str(countPairs(stringInput))) #calling the recursive function
