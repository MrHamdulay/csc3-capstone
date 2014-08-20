""" A program to determine whether a word is a palindrome
Author: Emiel Zyde
Date: 4 May 2014"""


def palindrome(word):
    
    if word == "":#base case 
        return True
    elif word[0] == " ":
        return palindrome(word[1:len(word)-1])
    elif word[0] == word[len(word)-1]:    #if the first and last characters of the word are the same, we "remove" them from the word and then check if the first and last characters of the new word are the same
        return palindrome (word[1:len(word)-1])
    
    return False 

#get input from user and print whether it is a palindrome or not 
word = input("Enter a string:\n")
if word != "":
    if palindrome(word) == True:
        print("Palindrome!")
    elif palindrome(word) == False:
        print("Not a palindrome!")
