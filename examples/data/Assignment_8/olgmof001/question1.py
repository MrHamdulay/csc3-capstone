"""Tofunmi Olagoke
5 May 2014
Programme on finding palindromes"""

def palin(word):
    #if word is odd it goes through this recursion
    if len(word)%2!=0:
        if len(word) == 1:
            return True
        elif word[0] == word[len(word)-1]: 
            return palin(word[1:len(word)-1])
        else:
            return False
    else:
        #if word is even it goes through this recursion
        if len(word) == 0:
            return True
        elif word[0] == word[len(word)-1]: 
            return palin(word[1:len(word)-1])
        else:
            return False        
    

word = input("Enter a string:\n")
inpalin=palin(word)

if inpalin:
    print("Palindrome!")
else:
    print("Not a palindrome!")