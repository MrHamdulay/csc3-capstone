"""Program to determine whether a given string is a palindrome
Lorena Dal Maso
10 May 2014"""

#get input from user
string = input("Enter a string:\n") 

#create a function to determine whether the above string is a palindrome
def palindrome (string):
    #base case
    if len(string) == 0:
        return False
    #if the first character equals the last character
    elif string[-1]==string[0]:
        palindrome (string[1:-1])
        return True

#tell the user if their string is a palindrome or not
if palindrome(string) == True:
    print("Palindrome!", end="")
else:
    print("Not a palidrome!",end="")