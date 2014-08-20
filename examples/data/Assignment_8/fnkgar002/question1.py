"""Program to to calculate whether or not a string is a palindrome
Gary Finkelstein
6 May 2014"""

def isPalindrome (word):
    if len(word) == 1 or len (word) == 0:  #if the word length is 1 or 0, then the word is a palindrome
        return True
    if word[0] == word [-1]:               #if the first and last letters of the word are the same, then call the function again to repeat the process
        if isPalindrome (word[1:-1]) == True:   
            return True
        else:
            return False
    else:
        return False                       #otherwise, the word is not a palindrome

#allows user to enter message   
message = input ("Enter a string:\n")
#calls the isPalindrome method and displays output accordingly
if isPalindrome (message) == True:
    print ("Palindrome!")
else:
    print ("Not a palindrome!")