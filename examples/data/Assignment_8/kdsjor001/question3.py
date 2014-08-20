"""Assignment 8 Question 3
06 May 2014
Jordan Kadish, CodeWord"""

def CodeWord(word):
    Coded=''
    if len(word)==1:
        if word[0].isupper():
            return word
        elif word[0]==' ':
            return word
        elif word[0]=='z':
            Coded='a'
            return Coded
        elif word[0].isalpha():
            return chr(ord(word[0])+1)
        else:
            return word
    elif word[0].isupper(): 
        return word[0]+CodeWord(word[1:])
    elif word[0]==' ':
        return word[0]+CodeWord(word[1:])    
    elif word[0].isalpha():    
        if word[0]=='z':
            Coded+='a'
            return Coded+CodeWord(word[1:])
        else:
            Coded+=chr(ord(word[0])+1)
            return Coded+CodeWord(word[1:])
    else:
        return word[0]+CodeWord(word[1:])
ChangeWord=input('Enter a message:\n')
print ('Encrypted message:')
print(CodeWord(ChangeWord))