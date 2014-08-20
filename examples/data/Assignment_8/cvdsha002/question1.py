"""Shahrain Coovadia"""
import string

def main():
    string=input("Enter a string:\n")      #prompts to enter input
    reverse(string)                         #reverses string from reverse function
    rev=reverse(string)                  #assigns reverse string to a variable
    if rev.lower()==string.lower():          #checks if a reverse of the string is equal to the original string
        print("Palindrome!")                #print outputs palindrome or not a palindrome 
    else:
        print ("Not a palindrome!")
        
def reverse(str):              
    if str=="":                     #checks if string is empty
        return str                        
    else:
        return reverse (str[1:])+str[0]           #returns sum of first letter and string from second letter onwards 
    

main()
           