"""recursive function to calculate whether or not a string is a palindrome
joshua wort
5 May 2014"""

def palindrome(string):
    #base case
    if string=="":
        return True
    
    elif string[0] == " ":
        return palindrome(string[1:len(string)-1])
    
    #checks if the first and last characters of the string are the same and if so will discard them and create a new string and continue the process of checking if the first and last characters are the same    
    else:
        if string[0]==string[len(string)-1]:
            return palindrome(string[1:len(string)-1])
        
    return False

string=input("Enter a string:\n")
if string!="":
    if palindrome(string) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        