"""Finding palindromes using recursion
Joseph Preyer
6 May 2014"""

string = input("Enter a string:\n")


def palindrome (string):
    #x must be global to remain assigned through each recursion
    global x    

    #Base case: Only operate if string is longer than one character
    if len(string)>1:
        x=1
        #If first character of string is same as last character, call palindrome(string) without first and last characters of string
        if string[0]==string[-1]:
            x=2
            palindrome(string[1:-1])
        #If first and last characters of string not the same, string is not a palindrome
        else:
            print("Not a palindrome!")
    
    else:
        #If the first and last characters of string are the same for every recursion until the string is of length 1 or 0, string is a palindrome
        if x==2:
            print("Palindrome!")
        
palindrome(string)