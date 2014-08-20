'''program to check palindromes using recursion
Tinotenda Chemvura CHMTIN004
03 May 2014'''

#____________________________Program Starts Here________________________________

def check_palindrome(word):
    word = word.lower()
    #the smallest case: check if the word is one letter and return palindrome
    if len(word) == 1 or len(word) == 0:
        return "Palindrome!"
    #the recursive step, if the 1st letter of the word == last letter, return the word with the 1st and last letter sliced off
    elif word[0] == word[-1]:
            return check_palindrome(word[1:-1])
    #if the word does not meet the above conditions, return not palindrome
    else:
        return "Not a palindrome!"

word = input("Enter a string:\n")
print(check_palindrome(word))
#___________________________Program Ends Here___________________________________