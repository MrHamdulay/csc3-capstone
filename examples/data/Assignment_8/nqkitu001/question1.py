"""Tuesday 06th May 2014
Itumeleng Nqoko
Assignment 8-Question1"""
#program to see wether string is a palindrome
string=input("Enter a string:\n")
def palindrome(string):
    if len(string)==0 or len(string)==1:
        print("Palindrome!")
    else:
        if string[0]==string[(len(string)-1)]:
            return palindrome(string[1:(len(string)-1)])
        else:
            print("Not a palindrome!")
        
palindrome(string)        
        

    