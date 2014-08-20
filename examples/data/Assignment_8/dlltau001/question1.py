#Question1
#Assignment 8
#CSC1015F
#Tauriq Dolley

#Using Recursion, test whether a word is a Pallindrome


def pallindrome(word,reverse,count):
    if len(word) == len(reverse):
        if word == reverse:
            print("Palindrome!")
        else:
            print("Not a palindrome!")
    else:
        return pallindrome (word, reverse + (word[len(word)-count]), count+1)
        
word = input("Enter a string:\n")
pallindrome(word,"",1)