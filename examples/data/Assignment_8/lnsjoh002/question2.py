"""Program to count the number of repeated characters in a string, using recursion
JP Lanser
3 May 2014"""


#Create a function and use recursion to count the number of repeated characters in a string


def count(string):
    
    if len(string) < 2: #If there is only one letter in the string, return 0, because obviously there can't be any repeated characters
        return 0
    
    if string[0] == string[1]: #If the strings first two letters are the same, return the rest of the string to the count function, excluding those two letters. And there is now one repeated pair so return '1 +'
        return 1 + count(string[2:])
    
    else: return count(string[1:]) #If the first two letters aren't the same return  the string (exluding the first letter) to the count function and continue to check for repeated letters through recursion.
    
message = input("Enter a message: \n")  #prompt user for input 
print("Number of pairs:",count(message))