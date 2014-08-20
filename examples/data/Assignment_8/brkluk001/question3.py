'''Program to encrypt strings using recursion
8 May 2014
Luke Barker'''

def encrypt(x):
    if x=='':      #if its starts with an empty string, return an empty string
        return ''
    if not x[0].isalpha() or x[0].isupper(): #if string is not letters or is upper case it will return the same character and move on 
        return x[0] + encrypt(x[1:])
    else: 
        num= ord(x[0])   #otherwise will change first letter by one postion
        num +=1
        if x[0] =='z':   #if the letter is z it will become 'a'  
            num-=26
        return chr(num) + encrypt(x[1:])   #will recursively go through the the rest of the string to convert it
    
x = input('Enter a message: \n')
print('Encrypted message:')
print(encrypt(x))

        
    