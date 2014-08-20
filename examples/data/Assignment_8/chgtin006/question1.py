""" Program to check if string is a palindrome using recursion
By Tinashe Choga 
5/4/2014"""

#function to reverse the string
def reverse(string):
    if string=="":
        return string
    else:
        return  string[-1] + reverse(string[:-1])

# checking if the reverse is equal to the original string
string=input("Enter a string:\n")
rev=reverse(string)
if rev==string:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    