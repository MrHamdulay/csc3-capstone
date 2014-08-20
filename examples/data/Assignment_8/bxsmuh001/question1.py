#Assignment 8, Question 1
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 08/05/2014

#This program is designed to check whether a string is a palindrome or not.
#Pre-condition: Input string.
#Post-condition: Output whether string is a palindrome or not.

#Creating a function to check if a string is a palindrome.
def isPalindrome(userInput):
    if(len(userInput) == 1 or len(userInput) == 0 or userInput == " "): #If length of string is one or blank, it automatically is a palindrome.
        return True
    else:
        if(userInput[0] == userInput[-1]): #Checks if first and last characters are the same.
            return isPalindrome(userInput[1:-1]) #Runs loop again but without checking first and last character of userInput.
        else:
            return False

#Checking if this file is being run as a standalone.
if __name__ == '__main__':
    userInput = input("Enter a string:\n")
   
    if(isPalindrome(userInput)):
        print("Palindrome!")
    else:
        print("Not a palindrome!")