#assignment 8 Q1 recursion - palindromes
#Kavir Ranchod
#05/05/2014

#Acquire input
s=input("Enter a string:\n")
def palindrome(s):
    #Base case, when the string is definitely a palindrome
    if len(s) == 0 or len(s) == 1:
        return ("Palindrome!")
    #If first and last characters don't match, its not a palindrome
    elif s[0] != s[-1]:
        return ("Not a palindrome!")
    #Test the second and second last characters of the string
    else:
        return palindrome(s[1:-1])
print(palindrome(s))