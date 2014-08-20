#Program with a recursive function to calculate whether or not a string is a palindrome
#Saul Bloch
#6 April 2014

user_string = input ("Enter a string:\n")

def isPalindrome (word):
    if len(word) == 0 or len (word) == 1:
        return True
    elif word[0] == word [-1]:
        if isPalindrome (word[1:-1]) == True:
            return True
        else:
            return False
    else:
        return False
   
if isPalindrome (user_string) == True:
    print ("Palindrome!")
else: print ("Not a palindrome!")