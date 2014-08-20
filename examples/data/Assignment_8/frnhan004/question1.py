"""Question1-Assignment8
FRNHAN004
3 May 2014"""

word=input("Enter a string:\n") #user input
def check_palindrome(word):
    if len(word)<1: #base case
        print("Palindrome!")
    else:
        if word[0]==word[len(word)-1]:
            return check_palindrome(word[1:len(word)-1]) #if first and last letter match, move inwards
        else:
            print("Not a palindrome!") #if first letter and last letter dont match
check_palindrome(word)




