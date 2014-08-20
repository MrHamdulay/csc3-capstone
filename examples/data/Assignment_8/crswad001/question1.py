'''Wade Cresswell
Question 1'''
def checkpalindrome(x): #function to check if input string is a palindrome
    if len(x) == 1 or len(x) ==0:
        print ('Palindrome!') #if recursion succeeds in getting to the point where the length of the string is 0 or 1, then string is palindrome.
    elif x[0]==x[len(x)-1]:
        return checkpalindrome(x[1:len(x)-1]) #if first character equal to last, splice and return cut string
    else:
        print('Not a palindrome!')  #if it doesnt succeed, is not palindrome
print('Enter a string:')
x = input()
checkpalindrome(x)