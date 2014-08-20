#Stephanie Latchmanan
#5 May 2014
#Assignment 8 (Finding palindromes using recursion)

#create a recursive function
def palindrome (string):
    #check if string is empty
    if len(string) == 0:
        return "Palindrome!"
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return "Not a palindrome!"

#Input a string
string = input("Enter a string:\n")
print(palindrome(string))