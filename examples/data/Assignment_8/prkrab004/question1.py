#Assignment 9
#Question 1
#Rabia Parker
#Due Date: 09/05/14

#using recursion to calculate if a string s a palindrome

string = input("Enter a string:\n") #input function to get a function

def palindromes(string): #defining the function
    if len(string)==1: 
        print("Palindrome!")
    elif string[0]!=string[-1]:
        print("Not a palindrome!")
    else:
        return palindromes(string[1:-1]) #iterate again by taking away the first and last letters to work out each letter in the string. 
    

palindromes(string)
