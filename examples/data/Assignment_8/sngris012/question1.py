"""Rishen Singh
Assignment 8
Question 1"""
input_word=input("Enter a string:\n")

def check(input_word):
    if input_word == '':
        return True #returns true if empty character
    else:
        if (ord(input_word[0]) == ord(input_word[len(input_word)-1])): # checks if the first and last character are the same
            return check(input_word[1:len(input_word)-1]) #checks if letters are the same for each corresponding position. 
        else:
            return False
if(check(input_word)==True):
    print("Palindrome!")
else:
    print("Not a palindrome!") 