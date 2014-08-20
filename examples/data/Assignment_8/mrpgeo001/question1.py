"""Program for checking is strings are palindromes
Geoff Murphy
MRPGEO001
6 May 2014"""

string = input("Enter a string:\n")

def pal_check(string):
    palindrome = 0                                                       #Initial value of a. If a = 0, not a palindrome. If a = 1, the string is a  palindrome.
    if len(string) == 1:                                        #If there is only one letter, it is automatically a palindrome.
        palindrome = 1
    elif len(string) == 2 and string[0] == string[1]:           #If there are only two letters and those letters are the same, it is a palindrome.
        palindrome = 1
    elif string[0] == string[-1]:                               #If the front and back letters are the same, it runs the recursive step, i.e. cuts the back and front letters and runs the function again. 
        palindrome = 1
        return pal_check(string[1:-1])
    else:                                                       #If all other conditions are not met, it makes 'a' equal to 0, i.e. it is not a palindrome.
        palindrome = 0
        
    if palindrome == 1:                                                  #Prints the respective message depending on the value of 'a'.
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
    
pal_check(string)