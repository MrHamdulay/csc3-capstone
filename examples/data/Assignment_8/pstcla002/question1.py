"""palindrome checker
Claudia Pastellides
08 may 2014"""

def palindromecheck(string):
    if len(string) < 2: return True #if only two then it is palindrome
    if string[0] != string[-1]: return False #checks if not palindrome
    return palindromecheck(string[1:-1])

if __name__=="__main__":
    mystring = input("Enter a string:\n") #run in main 
    if palindromecheck(mystring) == False: #checks if not right
        print("Not a palindrome!")
    else:
        print("Palindrome!") #if right print palindrome