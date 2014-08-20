#USING RECURSSION TO CHECK FOR PALINDROMES
#MDLCAR002
#6 MAY 2014

def palindrome(word):
    """Function to check if a string is palindromic"""
    #ARE OUTER LETTERS EQUAL TO ONE AND OTHER
    if word[:1] == word[-1:]:
        #CHECKS IF STRING HAS ANY CHARACERS IN IT
        if word == "":
            return "Palindrome!"
        #DETERMINING IF THERE ARE LETTERS LEFT
        else:
            return palindrome(word[1:-1])
    #NOT PALINDROMIC IF OUTER LETTERS ARE NOT EMPTY   
    else:
        return "Not a palindrome!"
     
def main():
    word = input("Enter a string:\n")
    print(palindrome(word))
    
if __name__ == "__main__":
    main()
