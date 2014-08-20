#Naadirah Ismail
#recursion palindrome
#6 may 2014

strg=input('Enter a string:\n')
def palindrome(strg):
    
    if len(strg)<=1:
        print('Palindrome!')
        return
    elif len(strg)>1:
        if strg[0]==strg[-1]:
            new_strg=strg[1:-1]
            return palindrome(new_strg)
        else:
            print('Not a palindrome!')
            return
            
palindrome(strg)
        
        