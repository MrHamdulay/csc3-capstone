"""Mphuthi Mamorena
assignment 8
question 1"""

string=input("Enter a string:\n")

n=len(string)-1
 
def palindrome(string):
    if len(string)==0 or len(string)==1:# base case 
        print("Palindrome!")
    else:
        if string[0]==string[-1]:
            return palindrome(string[1:-1])# recursive step where the function calls itsself again it will eventually get to len==1
        else:
            print("Not a palindrome!")
        
palindrome(string)