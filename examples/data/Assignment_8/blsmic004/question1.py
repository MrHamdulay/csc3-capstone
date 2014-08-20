# program with a recursive function to calculate whether or not 
# a string is a palindrome using recursion
# Michele Balestra  BLSMIC004
# 5 May 2014

def palindrome(string):
    ''' function checks if string is a palindrome'''
    if len(string)<1:
        return "Palindrome!"
    else:
        # condition if first and last index of string is identicle
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else: return "Not a palindrome!"
   
        
if __name__=='__main__':
    sent = input('Enter a string:\n')
    print(palindrome(sent))