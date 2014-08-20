#Program with a recursive function to calculate whether or not a string is a palindrome
#KNNSAD001
#Assignment 8

#inserting word-(string)- to be evaluated by function
insert_string = input('Enter a string:\n')

def palindrome (insert_string):
    
    if len(insert_string)<1:
        print ('Palindrome!')
        
    else:
        
        #if statement to evaluate if the first and last letters are the same 
        if insert_string[0]==insert_string[-1]:
            
            #the recursive process that will decrease the length of a word by initiating previous step with subsequent characters 
            return palindrome(insert_string[1:-1])
        else:
            print ('Not a palindrome!')
            
palindrome(insert_string)