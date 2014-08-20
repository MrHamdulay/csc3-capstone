'''Python program with a recursive function to calculate whether or not a string is a palindrome
Telisha Ramlall
4 May 2014'''

def palindrome(string):
    #if one or no words left 
    if len(string) <= 1:
        print('Palindrome!')
    
    #compare whether front and back characters are equal
    elif string[0] == string[len(string)-1]:
        return palindrome(string[1:len(string)-1])
    
    #not a palindrome if above conditions not met
    else:
        print('Not a palindrome!')

string=input('Enter a string:\n')
palindrome(string)
    