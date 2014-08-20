"""determine whether a string is a palindrome using recursion
Lauren Denny
8 May 2014"""

def palindrome(string):
    if len(string)==1 or len(string)==0:    #if the string is 1 character or the empty string, return "Palindrome!"
        return "Palindrome!"
    elif string[0]==string[-1]:             #if the first and last characters of the string are the same, checck and return whether the sring without the first and last letters is a palindrome
        return palindrome(string[1:-1])
    else:
        return "Not a palindrome!"          #otherwise, return "Not a palindrome!"

s=input("Enter a string:\n")                #get a string
print(palindrome(s))                        #print whether it is a palindrome or not

    