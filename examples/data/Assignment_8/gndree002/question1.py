"""Recursive function to calculate whether or not a string is a palindrome with recursive algorithm 
Reece Gounden
7 May 2014"""

string = input("Enter a string:\n")
x=0 #count variable from left
y=len(string) # from right
def isPalindrome(string):
    global x #define global for function to be able to modify counts
    global y
    if (y-x)<=3 and string[0]==string[-1]: #if string less than 3 and 1st = last then its a palindrome
        print("Palindrome!")
    elif (y-x)>=3 and string[x]==string[y-1]:#checks if index x = index y, if they are equal and the differance between indexes is great than 3 it moves x one fwd and y one back (indexes of next 2 chars)
        x=x+1
        y=y-1
        return isPalindrome(string)
    else:
        print("Not a palindrome!")
        
isPalindrome(string)