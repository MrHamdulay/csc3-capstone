#Check for a palindrome using recursion
#Devaksha Pillay
#4 May 2014

word = input("Enter a string:\n")

def is_palindrome(word):
    #check if a word is a palindrome
    if len(word) <= 1:
        print("Palindrome!")
    else:
        if word[0] == word[-1]:
            #remove first and last letter of the string
            return is_palindrome(word[1:-1])
        else:
            print("Not a palindrome!")
            
is_palindrome(word)