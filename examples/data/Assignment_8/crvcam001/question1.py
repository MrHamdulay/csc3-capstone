# question1.py
# program to find palindromes using recursion
# camilla craven
# 9 may 2014

# prompt user for word
string = input("Enter a string:\n")

# defining function
def palindrome_tester(string):
    
    # no word returns nothing
    if len(string) == 0:
        print("Not a palindrome!")
    
    # if word is only one letter, must be palindrome
    elif len(string) == 1:
            print("Palindrome!")   
    
    # when word has only two letters (left), compare the two        
    elif len(string) == 2:
        if string[0] == string[-1]:
            print("Palindrome!")
        # if not the same, not a palindrome
        else: 
            print("Not a palindrome!")
    
    # word that is bigger than two letters    
    elif len(string) > 2:
        # if first and last letter the same
        if string[0] == string[-1]:
            # test for same word without the first and last letter
            if palindrome_tester(string[1:-1]):
                return("Palindrome!")
        else:
            print("Not a palindrome!")
            
        
    
palindrome_tester(string)