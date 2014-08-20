''' Recursion to identify a palindrome
Siphesihle Zwane
09/05/14'''
def palidrome(word):
    if word=="":
        return ""
    else:
        return word[-1] + palidrome(word[:-1])

strng= input("Enter a string:\n")
if strng ==palidrome(strng) :
    print("Palindrome!")
else:
    print("Not a palindrome!")
