"""Assignment 8 Question 1
06 May 2014
Jordan Kadish, Recursive Palindrome"""

def PalinCheck(word):
    word=str(word)
    if len(word)==0 or len(word)==1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return PalinCheck(word[1:-1]) #Taking off the first and last equal letter

if __name__=='__main__':
    CheckWord=input('Enter a string:\n')
    CheckWord=CheckWord.lower() #To make sure the characters are the same
    if PalinCheck(CheckWord):
        print('Palindrome!')
    else:
        print('Not a palindrome!')