# Question 1 - Assignment 8
# Oliver Harrison
# 6 May 2014


def palindrome(string):
    if string == "":
        return True
    if string[:1] == string[len(string)-1:]:
        return palindrome(string[1:len(string)-1])
    else:
        return False
    
    

    
string=input("Enter a string:\n")
count = 0
palindrome(string)
if palindrome(string):
    print("Palindrome!")
else:
    print("Not a palindrome!")