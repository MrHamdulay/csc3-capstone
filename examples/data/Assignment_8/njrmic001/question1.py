#A program to calculate whether a string is a palindrom
#Author: Michelle Njoroge
#Date: 9 May 2014

word=input("Enter a string:\n")
def palindrome(word):
    if word!=" ":
        if word[0]==word[-1]:
            word=word[0:-1]
            return word
        else: return False
    return True

if palindrome(word):
    print("Palindrome!")
else:
    print("Not a palindrome!")
    