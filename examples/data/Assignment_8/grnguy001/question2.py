#It tells you how many pairs there are in a given string 
#Done By Guy Green
#Question 2 Assigment 8

def PairsOfCharacters(g):
    #base case
    if len(g)<2:
        return 0
    
    elif g[0]==g[1]:
        return 1 + PairsOfCharacters(g[2:]) #recursion
    
    else:
        return 0 + PairsOfCharacters(g[1:]) #recursion



message=input("Enter a message:\n")

print("Number of pairs:", PairsOfCharacters(message))