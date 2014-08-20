j = input('Enter a string:\n')
def palindrome (j):  
    
    if len(j)<=2 and j[0]==j[-1]:    
        return 'Palindrome!'
    elif j[0]!=j[-1]:
        return 'Not a palindrome!'
    else:
        return palindrome (j[1:-1])   
print (palindrome (j))   