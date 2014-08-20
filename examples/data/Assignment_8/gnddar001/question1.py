#Darryl Gounden
#Checks if a string is a palindrome


def palindrome(word):
    
    if len(word) > 1:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        
        else:
            return "Not a palindrome!"
        
    elif len(str(word)) <= 1:
        return "Palindrome!"
    
#print(palindrome(word))

if __name__ == "__main__":
    word = input("Enter a string:\n")
    print(palindrome(word))
    
    