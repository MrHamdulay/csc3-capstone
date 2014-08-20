'''this programm checks the palindrome
Nxumalo Goodman
09 May 2014'''

#this function reverses the string
def rev(w):
    #base case
    if w == '':
        return w #returns nothing if there is nothing in the string
    #recursive step
    else:
        return  rev(w[1:]) + w[0] 

#this function checks if the string is the palindrome    
def chck(w):
    #if the original string is the same as the reversed string then prints palindrome
    if w == rev(w):
        print('Palindrome!')
    #if the original string is not the same as the reversed string then prints not a palindrome
    else:
        print('Not a palindrome!')

#prompt a user to enter a string        
w = input('Enter a string:\n')
chck(rev(w))