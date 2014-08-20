""" A program with a recursive function to calculate whether or not a string is a palindrome (reads the sa me if reversed)
Author: Afika Nyati
Date: 5th May 2014 """



def palindrome(string):  # A recursive function that checks whether in inputted string is a palindrome. It returns True or False.
    
    if len(string) <= 1: # The stopping condition occurs when there are ony one letter left in the string.
        
        return True # True is always returned once the stack reaches this point.
    
    else: # This is is where the main part of the function occurs. The return statement makes use of Boolean.
       
        return string[:1] == string[len(string)-1:len(string)-2:-1] and palindrome(string[1:len(string)-1]) 
    
    # This section of the function returns back a Boolean result depending on the condition. The condition check whether the first letter of the string is equal to the last letter. If they are equal, it evaluates True, and the rest of the string is sliced and placed in the function. Once all the conditions of the end letters of the string are evaluated, there will be a long Boolean operation of Boolean results, using 'and'. AND is equivalent to multiplication, therefore if there is one False (equivalent to zero) in the operation, the final Boolean will return False, but if all the letters matched, it will return True.
        

def main():
    
    string = input("Enter a string:\n") # Asks user for a string.
    
    if palindrome(string) == False: # If the palinrome recursive function returns False, print "Not a palindrome!"
        
        print("Not a palindrome!")
        
    else: # If the palinrome recursive function returns True, print "Palindrome!"
        print("Palindrome!")
    
main()