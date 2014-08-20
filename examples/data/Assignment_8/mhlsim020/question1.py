"""A program to check whether or not a string is a palindrome
Simlindile Mahlaba
09 May 2014"""
def main():
  
  a=input("Enter a string:\n")
  b = is_palindrome(a[1:]) + a[0]
  if a == b:
    print("Palindrome!")
  else :
      print("Not a palindrome!")   
    
def is_palindrome(a):
  
  if a == "":
    return a
  else:
    return is_palindrome(a[1:]) + a[0]

main()
    

    