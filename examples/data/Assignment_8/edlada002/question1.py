"""Recursion Palindrome
Adam Edelberg
2014/05/09"""

word = input("Enter a string:\n")

def palindrome(word):
    
    if len(word) <2:
        return True
        
    if word[0] != word[-1]: 
        return False
    
    return palindrome(word[1:-1])


if palindrome(word) == True:
    print ("Palindrome!")
else:
    print ("Not a palindrome!")