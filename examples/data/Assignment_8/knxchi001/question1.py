#Assignment 8
#Question 1

string=input("Enter a string:\n")
def palindrome(string):
    if len(string)<2:
        return "Palindrome!"
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return "Not a palindrome!" 

print(palindrome(string))







