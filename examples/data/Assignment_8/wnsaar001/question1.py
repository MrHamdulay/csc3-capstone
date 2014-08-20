"""program to say if input is a palindrome 
Aaron Weinstein
9 May 2014"""

def isPalindrome (word):
    if len(word) == 1 or len (word) == 0:
        return True
    if word[0] == word [-1]:
        if isPalindrome (word[1:-1]) == True:
            return True
        else:
            return False
    else:
        return False
msg = input ("Enter a string:\n")
if isPalindrome (msg) == True:
    print ("Palindrome!")
if isPalindrome (msg) == False:
    print ("Not a palindrome!")
 