# Program to identify a palindromic string
# Nomsa Gamedze
# 7 May 2014

def reverse_word(word, word2):
    if len(word2) < len(word):
        x = len(word) - len(word2) - 1
        word2.append(word[x])
        reverse_word(word, word2)
        return word2

def check_equal(wordA, wordB):
    if wordA == wordB:
        return True
    else:
        return False
    
    
def is_palindrome(word):
    word2 = []
    word = list(word)
    word3 = reverse_word(word, word2)
    answer = check_equal(word3, word)
    if answer:
       print("Palindrome!") 
    else:
        print("Not a palindrome!")
        
def main():
    word = input("Enter a string:"'\n')
    is_palindrome(word)
    
main()

