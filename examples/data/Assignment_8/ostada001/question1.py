'''palindrome program
Adam Oosthuizen'''

def checkPalindrome (s):
    '''returns a boolean value based on whether or not a string parameter is 
    a palindrome or not'''
    if s == "":
    #checks whether the string has been reduced to an empty string    
        return True
    
    elif s[0] != s[-1]:
    #compares the first character in a string to the last 
        
        return False
    else :
        #recurs the function if the characters thus far have supported a 
        #palindrome
        return checkPalindrome(s[1:-1])



#formatting according to question specifications
s = input("Enter a string:\n")
if checkPalindrome(s) == True:
    print('Palindrome!')
else:
    print('Not a palindrome!')