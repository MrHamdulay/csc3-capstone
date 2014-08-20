""" Assignment 8 
Question1 - Palindrome
THNSIK001"""

def rev(word):
    #reverses word
    if word =="":
        return word
    return rev(word[1:]) + word[0]
    

word = str(input("Enter a string:\n"))
word2 = rev(word)
if word == word2:
    print("Palindrome!")
else:
    print("Not a palindrome!")