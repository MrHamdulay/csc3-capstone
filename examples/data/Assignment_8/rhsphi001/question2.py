'''Phillip Ruhesi
05/05/2014
program to count the number of repeated characters in a string'''


def repeated_char(x):    
        if len(x)<2:                                
                return 0
        elif x[0]==x[1]:                            
                return 1 + repeated_char(x[2:])             #check first two letters for equality and return 1 + new string
        else:
                return 0 + repeated_char(x[1:])             #return zero + new string when first two characters are not equal

x=input('Enter a message:\n')
print('Number of pairs:',end=' ')
print(repeated_char(x))        