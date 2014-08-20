word=input("Enter a string:\n")

def is_palindrome(word):
    if len(word) < 2: return ("Palindrome!")
    if word[0] != word[-1]: return ("Not a palindrome!")
    return is_palindrome(word[1:-1])

print(is_palindrome(word))