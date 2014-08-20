#Mbongeni Mazibuko
#MZBMBO002
#Assignment 8

def palindrome(s,count):
    ''' recursive function to calculate whether or not a string is a palindrome'''
    if len(s)//2<=count:
        '''base statement'''
        return 'Palindrome!'
    elif s[count]==s[-1-count]:
        count+=1
        return palindrome(s, count)
    else: 
        return 'Not a palindrome!'

if __name__=='__main__':
    '''so that function can be used in future'''
    s= input('Enter a string:\n')
    count=0
    palindrome(s,count)
    print(palindrome(s,count))
    '''count used as index'''