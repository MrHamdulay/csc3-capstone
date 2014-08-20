#program to calculate a palindrome
#F.J.Chigwaza
#06 May 2014

n=input('Enter a string:\n')

def palindrome(n):
    
    s=str(n)
    if len(s)<2:
        return 'Palindrome!'

    
        
    elif s[0] == s[-1]:
        
        return palindrome(n[1:-1])
        
     
    else:
        return 'Not a palindrome!'
    
print(palindrome(n))    

         

        
            
        

        
    
    
    
    