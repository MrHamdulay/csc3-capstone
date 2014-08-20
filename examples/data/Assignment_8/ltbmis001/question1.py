"""Checks if input is a Palindrome or not
Mishka Latib
06 May 2014"""

#function to check for palindrome

def Palindrome(string):
    if len(string)==1:
        print("Palindrome!")
    if len(string)==2:
        if string[0]==string[1]:
            print("Palindrome!")
    if len(string)>2:
        if string[0]==string[-1]:
            #starts from either end of string, works towards centre to check if characters match to produce palindrome
            return Palindrome(string[1:-1])
        if string[0]!=string[-1]:
            print("Not a palindrome!")

        
string = str(input("Enter a string:\n"))
#takes user input and calls function
Palindrome(string)