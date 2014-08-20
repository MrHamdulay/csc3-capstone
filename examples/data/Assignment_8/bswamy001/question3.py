"""Amy Bosworth
Assignment 8
Question 3
6 May 2014"""

x=input("Enter a message:\n")

def letters(x):
    #recursive base case
    if len(x)==0:
        return ''
    #not transforming uppercase letters
    elif x[0]==x[0].upper():
        return x[0] + letters(x[1:])
    
    #character z must change to a
    elif x[0]=='z':
        return chr(97) + letters(x[1:])
    
    else:
        return chr(ord(x[0])+1) + letters(x[1:])


print("Encrypted message:\n",letters(x),sep='')


    
    
        
        
        

