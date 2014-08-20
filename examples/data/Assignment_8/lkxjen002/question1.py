#A program to determine whether a string is a palindrome
#created by: Jenna Lake 
#Date: 4/5/2014

def palindrome(full_string): 
    if len(full_string)>1: #when string length is less than 1, it is already prooved to be a palendrome
        if full_string[0]==full_string[len(full_string)-1]: #checks if first and last characters are the same
            return palindrome(full_string[1:len(full_string)-1])# Cuts of the first and last characters for each recursion, calls itself and inputs the shortened string as a parameter 
        else:
            check="Not a palindrome!"
    if len(full_string)==1 or len(full_string)==0:#if string has length 1 or 0 then that character is a palendrome, as all other value pairs have been found to be palendromes of eachother, 
        check="Palindrome!"
    return check

def main():
    full_string=input("Enter a string:\n")
    print(palindrome(full_string)) #prints what check returns(either that its a palindrome or that its not)
main()

                             