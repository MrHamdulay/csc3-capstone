def checkpalindrome (word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return checkpalindrome(word[1:-1])    
    

word = input("Enter a string:\n")

if checkpalindrome (word) == True: print("Palindrome!")
else: print("Not a palindrome!")
    