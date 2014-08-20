#Jono Field
#May 7 
#Question 1



def palindrome(x):   #base case created
    if len(x) == 1: 
        return x
    else:
        return x[-1] + palindrome(x[:-1])   #return function used, as opposed to iteration loops

Str = input("Enter a string:\n")
if palindrome(Str) == Str:
    print("Palindrome!")
else:
    print("Not a palindrome!")