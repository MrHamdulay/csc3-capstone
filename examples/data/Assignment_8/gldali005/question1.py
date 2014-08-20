#Ali Goldstein
#program with a recursive function to calculate whether or not a string is a palindrome
#8 May 2014

def isPalindrome(string):
    if len(string) == 1 or len (string) == 0:
        return True
    #seeing if the first and last character of the string is the same
    #if it is, doing it again
    if string[0]==string[-1]:
        if isPalindrome(string[1:-1]) == True:
            return True
        else:
            return False
    else:
        return False

#prompt user to enter a string and then print out if its a palindrome or not
string=input("Enter a string: \n")
if isPalindrome(string) == True:
    print("Palindrome!")
if isPalindrome (string) == False:
    print("Not a palindrome!")


        
        
    