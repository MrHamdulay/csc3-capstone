"""
Serayen Govender 
prime palindrome numbers
"""

import sys
sys.setrecursionlimit (40000)
#error handling: set recursion limit to 40000

def palindromic(stri):
   
    if stri == '':
        return True
    #is palindromic
    
    else:
        a=stri[len(stri)-1]
        if stri[0] == a:
            # last letter equal first letter
            
            return palindromic(stri[1:len(stri)-1])
        #recuresion step
        else:
            
            
            return False
        # Not palindrome
c=2      

def check(k):
                global c
                if(k<2):
                                return False
                else:
                                
                                if(k==2):
                                                return True
                                else:
                                                
                                                if c==(k//2):
                                                                return True
                                                else: 
                                                                if(k%c==0):
                                                                                return False
                                                                else:
                                                                                c=c+1
                                                                                return check(k)
              #check prime if i.e. checks if any number from 2 to half way to the number is divisible 
                      
def search(r,l):
                global c
                c=2
                if r == l:
                                return True
                else:
                                if palindromic(str(r)):
                                    if check(r):
                                        print(r)
                                    
                                r+=1
                                search(r,l)
                        #checks if both methods return true        


                                


m=input("Enter the starting point N:\n")

x=eval(m)
p=input("Enter the ending point M:\n")
y=eval(p)
print("The palindromic primes are:")
search(x,y)                               
