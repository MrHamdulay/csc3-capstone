""" Sphiwe Muthembi
MTHSPH007
Assignment 8 - Question 1"""

# Recuscive function to reverse a word and check whether it is  a palindrome.
# palindrome: word from lft = word from right.


#input 
word= input('Enter a string:\n')

#=================

def reverse(word):
    
    if word == '':
        
        return ''
    else:
        return word[-1] + reverse(word[:-1]) 
#print(word)    
#print(reverse(word)) 

def check_palin(word1,word2):
    
    if word1 == word2:
        print('Palindrome!')
        
    else:
        print('Not a palindrome!')
        
#print(reverse(word))        
check_palin(word,reverse(word))        