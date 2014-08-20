'''Palindrome
Author:Raees Eland
Date:05 May 2014'''


def pal(string):
    if string=='': 
        return string
    else:
        return string[-1] + pal(string[:-1]) #reverses string
    
if __name__=='__main__':
    string=input('Enter a string:\n')
    reverse_str=string
    if string==pal(reverse_str):
        print('Palindrome!')
    else:
        print('Not a palindrome!')
    
    

    
        
  
  
  
    
