'''program to reverse and check if a string is a palindrome
Simangaliso Mlangeni
MLNSIM014
07 May 2014
Assignment 8, question 1'''

def reverse(s):
    '''Function to reverse a string'''
    if s=="":#base case to check whether the string is empty or not. if it is, returns it and and stops the recursion
        return s
    else:#reverses string string by taking the string and placing it towards the end
        return reverse(s[1:]) + s[0]
     
def printRevStr(s):
    if s == reverse(s):#if word is a palindrome
        print("Palindrome!")
    else:#Prints this if the word is not a palindrome
        print("Not a palindrome!")
        
s = input("Enter a string:\n")
s = s.lower()
printRevStr(s)