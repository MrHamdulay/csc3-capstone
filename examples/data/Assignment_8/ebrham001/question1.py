'''Recursive function checking a palindrome
HAMZA EBRAHIM
09/05/2014'''

# Assignment 8 - Question 1


import string

# recursive function that checks for a palindrome

def reverse (str):
   if str[0] == str[-1]:
      return str
   else:
      return 0
    
# main function prompting for a string and invoking the reverse function above to check if the user input is a palindrome

def main():
   s = input("Enter a string:\n")
   reverse(s)
   x = reverse(s)
   if x == s:
      
      print("Palindrome!")
   else:
      print("Not a palindrome!")

main()

# program ends
