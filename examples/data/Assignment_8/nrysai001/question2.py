#question2
#saiheal narayan
#09 may 2014
 
def y():
    string=input('Enter a message:\n') # gets input from user
    print ('Number of pairs:' ,x(string)) 

def x(word):
    #gets the number of pairs
    if len(word)<=1:
        return 0 
    elif word[0]==word[1]: # checks if first equal second
        return 1 + x(word[2:]) # if so it returns 1 and adds a smaller number
    else:
        return 0 + x(word[1:])# it returns 0 and adds a smaller string into the fuction from the second letter



y()