'''Program that used recursion to determine whether a string is a palindrome
Frans van Hoek
8 May 2014'''

def palincheck(word):
    if len(word) < 2: return 'Palindrome!'
    if word[0] != word[-1]: return 'Not a palindrome!'
    return palincheck(word[1:-1])

word = input("Enter a string:\n")
print(palincheck(word))
