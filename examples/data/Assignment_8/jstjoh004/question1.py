# Recursion
# checking palindromes
# Hendrik Joosten
# JSJOH004
# 04 May 2014


# recursive function to check palindrome
def checkPalindrome(s):
      # base case when the string len is == to 1 OR 0 and checking cannot be done:
      if len(s) <= 1:
            print("Palindrome!")
      #check if the first and the last char of the string is ==
      # If they are, return a string with first and last character sliced away
      elif s[0] == s[len(s)-1]:
            return checkPalindrome(s[1:len(s)-1])
      # as soon as the firt and last chars are not == the recursion stops and 
      # the string is declared not a palindrome
      else:
            print("Not a palindrome!")

# gets input from the user
user_str_in = input("Enter a string:\n")
#sends the user input into the recusrsive function
checkPalindrome(user_str_in)