'''Program to check whether a sentence is a palindrome
Mahnoor Ahmed
10 May 2014'''

def ispalindrome(word):
    #0 or 1 letter long sentences are palindromes hence form the base case
    if len(word) == 0 or len(word) == 1:
        print("Palindrome!")
        
    #checks to see if first and last character are the same
    else:
        if word[0] == word[-1]:
            #carries out recursive step on a smaller sentence which excludes the previous 1st and last characters
            return ispalindrome(word[1:-1])
        else:
            print("Not a palindrome!")
        
ispalindrome(word=input("Enter a string:\n"))