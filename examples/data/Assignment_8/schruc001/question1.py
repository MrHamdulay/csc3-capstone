'''Recursive palindromic string program
Ruchaan Schmidt
May 2014'''

string = input ('Enter a string:\n')

def ispal(string):
    
# base case:
    if len(string)==0: #empty string
        print ('Palindrome!')

# len string odd    
    elif len(string)==1:
        print ('Palindrome!')

# len string even    
    elif len(string)==2:
        if string[0]==string[1]:
            print ('Palindrome!')
        else:
            print ('Not a palindrome!')
    elif len(string)>2:
        
        if string[0]==string[len(string)-1]:

# temporary variable            
            temp = string [1:len(string)-1]
            ispal (temp)
        
        else:
            print ('Not a palindrome!')
    
    
ispal(string)