"""palindromes
Sachin Murugan
9/5/2014"""
string=input("Enter a string:\n")
def Palindrome(string):
#testing for base case    
    if len(string)== 0 or len(string)==1: #check if word is only 1 or zero letters
        print("Palindrome!")
    else:
        if string[0]==string[-1]:#check first and last letter
            Palindrome(string[1:-1])#make problem smaller
        else:
            print("Not a palindrome!")  
Palindrome(string)            

