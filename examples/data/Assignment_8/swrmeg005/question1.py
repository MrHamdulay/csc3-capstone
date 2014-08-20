#Program to check for palindromes
#Megan Swartz
#12th May 2014

#Checking if palindrome true or false
def palindrome(string):
    if len(string)<=1:
        return True
    elif string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

#ask for input, run check, and print correct output
string=input("Enter a string:\n")
if palindrome(string)==False:
    print("Not a palindrome!")
if palindrome(string)==True:
    print("Palindrome!")