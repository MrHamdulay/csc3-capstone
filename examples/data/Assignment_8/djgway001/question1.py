#recursion to determine a palindrome string
#wayne de jager
#6 may 2014

def palindrome(x):
    if len(x) < 2: #a single character is a palindrome
        print("Palindrome!")
    elif x[0] != x[-1]: #not equal to the reverse index in that string
        print("Not a palindrome!")
    else:
        return palindrome(x[1:-1]) #is equal to reverse index in string
x=input("Enter a string:\n")
palindrome(x)