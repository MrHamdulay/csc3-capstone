# tarisai stephen kalinde
# klntar002
# palindrome using recursion


string=input('Enter a string:\n')  
#string=string.replace(' ','')


def palindrome(string):
    
    if len(string)==0 or len(string)==1:
        return 'Palindrome!'

    else:
        if string[0]==string[-1]:
            
            return palindrome(string[1:-1])
            
            #return palindrome(string)
        else:
            return 'Not a palindrome!'
    

print(palindrome(string))
