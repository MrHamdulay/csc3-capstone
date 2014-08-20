# Assignment 8
# 5 May 2014
# Richard van Gysen
# Question 1
# palindrom finder

# get sentence
sentence = input("Enter a string:\n")
# define the function palindrome  
def palindrome (sentence):
    # if nothing, return is a palindrome
    if sentence == '':
        return True
    # if palindrome, return palindrome
    elif sentence[0] == sentence[-1]:
        return palindrome(sentence[1:-1])
    # else, not a palindrome
    elif sentence[0] != sentence[-1]:
        return False
# print palindrom if true
if palindrome(sentence) is True:
    print("Palindrome!")
# else, print not a palindrome
else:
    print("Not a palindrome!")