#Shaylan Lalloo
#LLLSHA008
#Checks if a sentence is a palindrome

myin = input('Enter a string:\n')

def ispalin(x):
    if len(x) == 0 or len(x) == 1:
        #if it only has 0 or 1 letters, then it's a palindrome
        return True
    else:
        if x[0] == x[-1]:
            #if the first letter equals the last, it can still be a palindrome
            return ispalin(x[1:len(x) - 1])
            #output check if the middle part is a palindrome then it will be a palindrom
        else:
            return False
            #won't be a palindrome

if ispalin(myin):
    print('Palindrome!')
else:
    print('Not a palindrome!')

#output appropriate answer
