"""A program to count the number of repeated characters in a string
Author: Emiel Zyde
Date: 4 May 2014"""

def double_letters(word):
    if word == "" or len(word) == 1:   #base/ termination case 
        return 0
    elif word[0] == word[1]:   #if the first and second letters are the same, add one to the number of double letters and chop off the first and second letters (avoids overlaps)
        return 1 + double_letters(word[2:])
    else:
        return double_letters(word[1:])

#get input from user and print double letters 
message = input("Enter a message:\n")
print("Number of pairs:", double_letters(message))