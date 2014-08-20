# Program to check if string is a palindrome using recursion
# Budeli Rendani
# BDLREN001
# 06/05/2014

def palindrome(string): # Creating a function to reverse words
    if string==""  :# setting the base case
        return string
    elif string==1:
        return string
    else:
        return  string[-1] + palindrome(string[:-1]) #reversing the words


string=input("Enter a string:\n")# Obtaining input from the user

new_word=palindrome(string) # The new reversed word
if new_word!=string: # Checking if new_word is not equal to the original word and print that its not a palindrome
    print("Not a palindrome!")
elif new_word==1 or new_word=="": # if new word is an empty string or a single digit it should print palindrome
    print("Palindrome!")
else: # else printing that its not a palindrome
    print("Palindrome!")
    