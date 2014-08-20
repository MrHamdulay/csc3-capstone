"""Ailsa Mackay MCKAIL001
Assignment 8 Question 1 
2014-05-06"""

def palindrome(word):
    if word == "":
        print("Palindrome!")
    else:
        if word[0] == word[-1]: #check if first character is equal to last character
            return palindrome(word[1:-1])
        else:
            print("Not a palindrome!")
            
def main():
    word = input("Enter a string:\n")
    palindrome(word)

main()
            


