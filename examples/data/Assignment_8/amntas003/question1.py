#AMNTAS003  #Tashfia Amin   #Due Date: 9 May 2014
#Question 1: Assignment 8   #Check palindromes using recursion

#Ask for input of string to be checked
string=input("Enter a string: \n")

#Use recursion to reverse the string
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:])+string[0]

#Create new variable for reversed string
new_string = reverse(string)

#Check if string and reversed string are the same
def palindrome(string):
    if string == new_string:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
palindrome(string)