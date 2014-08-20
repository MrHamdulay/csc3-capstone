#This program checks whether a string is a palindrome or not
#dario pillay"
#5 May 2014

def palindrome(x):
    
    #function checks if a string is a palindrome or not using recursion'''
    if len (x)<=1:#if one word or no words are left in the string and it is a palindrome print this
        
        print('Palindrome!')
    
    elif x[0]==x[len(x)-1]:#checking if the letter at the back is equal to the one infront
        return palindrome(x[1:len(x)-1])
    else:
        print('Not a palindrome!')

if __name__=='__main__':
    x=input('Enter a string:\n')
    palindrome(x)