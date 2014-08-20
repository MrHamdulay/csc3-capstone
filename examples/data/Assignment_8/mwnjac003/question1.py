# program to check if input string is a palindrome
# by Jacob Mwanza
# 04/05/2014


# reverse string
def reverse(word):
    if len(word) == 0 or len(word) == 1:
        return(word)
    else:
        return word[len(word) - 1] + reverse(word[1:len(word) - 1]) + word[0]
    
# input string
def palin():
    word = input("Enter a string:\n")
    
    # compare input string to reversed string
    if reverse(word) == word:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        

palin()