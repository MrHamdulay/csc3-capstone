# Python program with a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed). 
# Mulisa Badugela
# BDGMUL001
# 08 MAY 2014
string=input("Enter a string:\n") # user inputs a string

def palindrome(string):
    
    if string =='':
        return True
    if len(string) == 1:
        return True
    
    else:
        if string[0] == string[len(string)-1]:
            string = string[1:-1]
            
            if palindrome(string):
                print("Palindrome!")
        else:
            print("Not a palindrome!")


palindrome(string)