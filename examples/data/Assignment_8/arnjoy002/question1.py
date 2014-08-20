#Joy Arendse-Gorvalla

def Palindrome (word): #defining a funtion that determines whether a string is/is not a palindrome
    if len(word) == 1 or len (word) == 0: 
        return True
    if word[0] == word [-1]: #checks to see if the 1st and last letters of string are the same, and if it is it will run until every letter has been checked correctly
        if Palindrome (word[1:-1]) == True:
            return True
        else:
            return False  
#not a palindrome if 1st and last letters aren't the same                     
    else:
        return False
message = input ("Enter a string:\n") #asking user for input to enter a string
if Palindrome (message) == True:
    print ("Palindrome!") 
if Palindrome (message) == False: #then it will display whether the string is or is not a palindrome
    print ("Not a palindrome!")
    
