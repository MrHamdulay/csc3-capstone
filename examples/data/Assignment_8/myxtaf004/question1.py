"""Checks if a string is a palindrome
Tafadzwa Moyo 
4 May 2014"""


#Recurvise function
def palindrome(string):
    #reverses string
    if len(string):
        rvrse=palindrome(string[1:])+string[0]
        return rvrse
    else:
        return string

#get input
string=input("Enter a string:\n")
#checks is the reverse string is equal to the string
if palindrome(string)==string:
    print ("Palindrome!")
else:
    print ("Not a palindrome!")