"""CHRIS BOLTON
11/05/2014"""

def pairCounter(string): 
    if string==string[len(string)-1]:
        return 0 
    
    elif string[0]==string[1]:
        if len(string)>2:
            return 1+pairCounter(string[2:]) 
        else:
            return 1+pairCounter(string[1:]) 
    else:
        return pairCounter(string[1:])
    
userInput = input("Enter a message:\n") 

print("Number of pairs:",str(pairCounter(userInput)))