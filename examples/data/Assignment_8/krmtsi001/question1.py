string = input("Enter a string: \n") 

string.split()  #making the string into a list, easier manipulation to reverse the users input


def reverse(string):    
    
    if len(string) <=1:   #recursive base case, using a boolian where the string is either 1 word or no word at all return it as it is without change
        return string
    else: 
        return reverse(string[1:]) + string[0]   #here is the recursive step in each stack storing the 1st word so when it gets to the end off loading the stack will end up reversed
palin = reverse(string)    #this reversed string is made into a variable when the function is being called


if palin==string:    #here the variable is used to check if the reverse is the same as the string itself using a boolian as the character of a palindrome should satisfy this condition
    print("Palindrome!")  #the true condition in boolian the output 
    
else:
    print("Not a palindrome!")   #the false condition in boolian in output


        
    
    
    
    

