def isItAPalindrome(theStringInQuestion):
    if len(theStringInQuestion) == 1 or len(theStringInQuestion) == 0:
        return True
    if theStringInQuestion[0] == theStringInQuestion[-1]:
        if isItAPalindrome(theStringInQuestion[1:-1]):
            return True
    else:
        return False

theString = input("Enter a string:\n")
if isItAPalindrome(theString):
    print("Palindrome!")
else:
    print("Not a palindrome!")
