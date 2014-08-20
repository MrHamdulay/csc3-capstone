#Ariel Rubin
#RBNARI001
#program to determine if a string is a pandrome using recursion
#9 May 2014

#function to determine if a string is/is not a palindrome
def isPalindrome (word):
    if len(word) == 1 or len (word) == 0:
        return True
    #check to see if 1st and last letters are equal
    #if yes then checks runs the function again for 2nd letter and 2nd last letter
    #will continue to run until each letter has beenchecked correctly
    if word[0] == word [-1]:
        if isPalindrome (word[1:-1]) == True:
            return True
        else:
            return False
    #1st and last letters are not equal    
    else:
        return False
#ask user to enter a string    
message = input ("Enter a string:\n")
#displays whether string is/is not a palindrome
if isPalindrome (message) == True:
    print ("Palindrome!")
if isPalindrome (message) == False:
    print ("Not a palindrome!")