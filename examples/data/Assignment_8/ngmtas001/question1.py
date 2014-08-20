#Tase Ngambi
#Question1
#Assignment 8
def isPallindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    elif word[0] == word[-1]:
        return isPallindrome(word[1:len(word)-1])
    else:
        return False
    
word = input("Enter a string:\n")
if isPallindrome(word):
    print("Palindrome!")
else:
    print("Not a palindrome!")
    