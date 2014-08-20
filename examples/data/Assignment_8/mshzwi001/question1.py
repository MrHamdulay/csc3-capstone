# a program with a recursive function to calculate whether or not a string is a palindrome
# mashau zwivhuya
# 5 may 2014
# get input
s=input("Enter a string:\n")
def isPal(s):
    # check length
    if (len(s) < 2):  
        #is true
        x="Palindrome!"
        return x 
    if (s[0] != s[-1]):
        y="Not a palindrome!"
        return y
    # do reccursion
    return isPal(s[1:-1]) 
print(isPal(s))