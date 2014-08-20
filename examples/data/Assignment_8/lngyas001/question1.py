"""program to check if a given string is a palindrome
yasha longstaff 
6 may 2014"""

def palin(s,x):
    if len(s)/2 >= x: #only work up to the middle
        if s[x] == s[-1-x] and palin(s, x+1) == 'Palindrome!': #check first and last then do the rest of the word
            return 'Palindrome!'
        else: #first and last values not =
            return 'Not a palindrome!'
    else:
        return 'Palindrome!'
        
s = input('Enter a string:\n')
x = 0
    
print(palin(s,x))        
        
        
