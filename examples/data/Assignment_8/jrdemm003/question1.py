"""ASSIGNMENT 8 QUESTION 1- FIND PALINDROMES RECURSIVELY
EMMA JORDI
8 MAY 2014"""

string= input("Enter a string:\n")
def palindrome(string):
    
    #base case
    if len(string) < 1:
        global ans
        ans= True
       
    
    #recursive step
    #if first letter = last letter, check next two letters in
    else:
        if string[0] == string[-1]:
            return ( palindrome (string[1:-1]))
        else:
            ans= False
           
palindrome(string)
#print answer
if ans:
    print("Palindrome!")
else: 
    print("Not a palindrome!")