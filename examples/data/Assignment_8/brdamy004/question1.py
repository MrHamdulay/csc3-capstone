# Assignment 8 question 1
# Amy Brodie
# 8/05/2014


# recursion function to see if a string is a palindrome
def palindrome(s,length):
   if length == 0:
      return ""
   else:
      return s[length-1] + palindrome(s,length-1)

# get input from user and output if a string is a palindrome or not
if __name__ == "__main__":
   original = input("Enter a string:\n")
   palin_str = palindrome(original,len(original))
   if palin_str == original:
      print("Palindrome!")
   else:
      print("Not a palindrome!")