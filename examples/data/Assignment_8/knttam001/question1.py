"""Program to Test Whether a String is a Palindrome Using Recursion
Tamsin Kantor
May 2014"""

string = input ("Enter a string:\n")

def palindrome(s):
    if s == "": # base case to end recursion
        return True 
    else:
        if s[0] == s[len(s) -1]: # if the first and last character are the same
            return palindrome(s[1:len(s)-1]) # return the string with first and last characters removed
        else:
            return False
            
if palindrome(string) == False: #running the function and printing the output
    print("Not a palindrome!")
if palindrome(string) == True:
    print("Palindrome!")
    