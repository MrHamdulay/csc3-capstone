#Program to check for palindromes using recursion
#Nevarr Pillay - PLLNEV006
#4 May 2014

def palindrome(word):
    """Function to check if a string is palindromic"""
    #If the outer letters are equal to one another
    if word[:1] == word[-1:]:
        #Check if the string is empty
        if word == "":
            return "Palindrome!"
        #Check if there are letters left
        else:
            return palindrome(word[1:-1])
    #If the outer letters are not equal - Not palindromic    
    else:
        return "Not a palindrome!"
     
def main():
    word = input("Enter a string:\n")
    print(palindrome(word))
    
if __name__ == "__main__":
    main()