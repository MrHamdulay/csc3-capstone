""" Reverse a string
Kumaran Reddy
8 May 2014"""

word=input("Enter a string:\n")
def reverse(word):
    if len(word)==0: #Base test
        return False
    else:
        if word[0]==word[-1]:  #Checks if first letter is equal to last
            return reverse(word[1:-1]) #Keeps calling function if condition is true

if reverse(word) != False:
    print("Not a palindrome!")
else:
    print("Palindrome!")