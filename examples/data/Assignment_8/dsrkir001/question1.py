#Program with a recursive function to calculate whether or not a string is a palindrome
#Kiran Desraj - DSRKIR001
#5 May 2014

#takes string input
word = input('Enter a string:\n')

def palindrome (word):
    #if length of word is 0 characters 
    
    if len(word)<1:
        print ('Palindrome!')
        
    else:
        
        # If last and first letters are exact
        if word[0]==word[-1]:
            
            #recursive process which initiates previous step with subsequent characters whilst decreasing the length of the word
            return palindrome(word[1:-1])
        else:
            print ('Not a palindrome!')
            
palindrome(word)