#Assignment 8
#Question 1
#Barry SU
#8 May 2014
#Program to check if a string is a palindrome using recursion

#get the string
string=input("Enter a string:\n")

def palindrome(string):
    if len(string)<2:   #string that has length 1 is also a palindrome
        return "Palindrome!"
    if string[0]==string[-1]:   #check if first character is equal to last 
        return palindrome(string[1:-1]) #cut first and last charac if they are equal each time until charac <2
    else:
        return "Not a palindrome!"
    
print(palindrome(string))

    