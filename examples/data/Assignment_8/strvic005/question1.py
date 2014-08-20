"""Program to see if a word is a palindrome using recursion
vicky stark
5 May 2014"""


def palindrome(words):
    if words=='':
        return 'a' #just to make sure a space doesn't get counted as a palindrome
    if len(words)==0:
        return ""
    if len(words)==1:
        return words
    else:
        return palindrome(words[1:]) + words[0]

words=input("Enter a string:\n")
reversed_words= palindrome(words)
if reversed_words==words:
    print("Palindrome!")
elif words=='a':
    print("")
else:
    print("Not a palindrome!")
    
   
    
    




