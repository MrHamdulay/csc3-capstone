'''This program checks whether a string is a palindrome or not
Sandile Christopher Mahlangu
4 May 2014'''

def palindrome(string):
    
    '''This function checks if a string is a palindrome or not using recursion'''
    if len (string)<=1:#if one word or no words are left in the string and it is a palindrome print this
        
        return True
    
    elif string[0]==string[len(string)-1]:#checking if the letter at the back is equal to the one infront
        return palindrome(string[1:len(string)-1])
    else:
        return False
if __name__=='__main__':
    string=input('Enter a string:\n')
    check=palindrome(string)
    if check:
        print('Palindrome!')
    else:
        print('Not a palindrome!')

        