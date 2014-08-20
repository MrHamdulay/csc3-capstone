# Najeeb Sirkhoth
# SRKMOH002
# question1.py
# Assignment 8 

# Program to check if string is a Palindrome

# Recursive Function to Reverse string
def reversestring(string):
    if string == "":
        return string                                 # Empty String as Base Case
    else:
        return reversestring(string[1:]) + string[0]  # Recursion concatenation


# Checking if input is Palindrome
x = input("Enter a string:\n") 
reverse = reversestring(x)                    # Get reverse of input
if x == reverse:                              # Check if input is Palindrome
    print("Palindrome!")
else:                                         
    print("Not a palindrome!") 
    



