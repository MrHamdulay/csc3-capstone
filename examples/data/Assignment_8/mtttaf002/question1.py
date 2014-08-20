"""check if given string is a palindrome
tafara mtutu
6 may 2014"""

def check (sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + check(sentence[:-1])
    
x = input("Enter a string:\n")
if x:
    if x == check(x):
        print("Palindrome!")
    else: print("Not a palindrome!")
