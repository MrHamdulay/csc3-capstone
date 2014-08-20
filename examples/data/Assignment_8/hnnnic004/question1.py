'''program to find palindromes using recusrion
nicole henning
due 9 may 2014'''

string = input("Enter a string:\n")

def palindrome(string):
     if len(string) < 2: #if word contains only one or no letters/characters,true
          print("Palindrome!")
     elif string[0] == string[-1]: #if end and beginning character are the same, true
          #make string now without first and last character, if they were equal
          return palindrome(string[1:-1]) #recursion - continue until not the same, or until length < 2
     else:
          print("Not a palindrome!")

        
palindrome(string)

