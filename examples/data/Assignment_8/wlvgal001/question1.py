"""Question 1: checking if a string is a palindrome
Galya Wolov
9 May 2014"""

testingstring= input("Enter a string:\n")#asks 4 the string we are testing

def palindrome (x):
    
    
    if len(x) == 0 or len(x) ==1:#checks the length because if 0 or 1 at the end once recursion has occured
        #it will stop iterating
        return True
    
    if x[0] == x[len(x)-1]: #tis is the checking step so if 1 and the last letter match etc
        return  palindrome(x[1:(len(x)-1)]) #recursive step returns what we neeed to continue

    else:
        False

if palindrome(testingstring) == True:#just the print statements- YEs palindrome
    print("Palindrome!")

else:
    print("Not a palindrome!") #no not palindrome #aligns with true and false
    

            
                                           
