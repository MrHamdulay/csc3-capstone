# Yudhi Moodley
# Assignment 8 - Palindrome evaluator
# 09/05/2014

# function that checks for palindrome
def palindrome(i):
    
    # base case 
    if i == "":
        print("Palindrome!")
    
    #checks the palindrome meets palindromic criteria
    else:
        if  i[0] == i[-1]:
            return palindrome(i[1:-1])
    
        # else not a palindrome
        else:
            print("Not a palindrome!")
    
string =input("Enter a string:\n")

palindrome(string)
