"""program to determine whether a string is a palindrome, using recursion
JP Lanser
3 May 2014"""

#Create a function and use recursion to determine whether a string is a palindrome or not (return True if it is)

def palindrome(string):
    
    
    
    
    if len(string)<2:  #If the string is empty or has one letter return True, If the string is a palindrome it will eventually get to this stage through recursion (through using the algorithm below)
        return True
    
 
    
    elif string[0] == string[len(string)-1]: #If the first and last character are the same, return the string excluding these letters to the palindrome function.
        return palindrome(string[1 : len(string)-1])
    
    else: return False #The string is not a palindrome if one of the above 'if' statements aren't executed. Therefore return false.
    
    
    
string = input("Enter a string:\n").lower()  #prompt user for input and convert string to lower case, so that the palindrome function can work properly

if palindrome(string):
    print("Palindrome!")
    
else: print("Not a palindrome!")

    
    
    
    
    

    
