def ispalindrome():
    word=input("Enter a string:\n")
    if len(word) < 2: 
        print("Palindrome!")
    elif word[0] != word[-1]: 
        print("Not a palindrome!")
    else:
        print("Palindrome!")


ispalindrome()