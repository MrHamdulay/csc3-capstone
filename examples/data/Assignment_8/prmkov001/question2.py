#Kovlin Perumal
#PRMKOV001
#09/05/2014
#Recursive Pairs Function

inputPhrase = input("Enter a message:\n")
 

def countPairs(dummy) :
    
    if len(dummy) == 0 or len(dummy) == 1 :
        return 0 #Account for input where it is impossible to have a pair
    elif dummy[0] == dummy[1] :
        return 1 + countPairs(dummy[2:]) #if first characters are equal add one and cut them out
    else :
        return 0 + countPairs(dummy[1:]) #else just cut first letter
    
print("Number of pairs:", countPairs(inputPhrase))