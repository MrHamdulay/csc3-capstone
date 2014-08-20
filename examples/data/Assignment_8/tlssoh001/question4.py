'''Sohail Tulsi
TLSSOH001
find palindromic numbers'''

# increase recursion limit
import sys
sys.setrecursionlimit (30000)

x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n")) 


count=2      
#check to see if the number in palindromic 
def check(n):
                global count
                if(n<2):
                                return False
                else:
                                
                                if(n==2):
                                                return True
                                else:
                                                
                                                if count==((n//2)+1):
                                                                return True
                                                else: 
                                                                if(n%count==0):
                                                                                return False
                                                                else:
                                                                                count=count+1
                                                                                return check(n)
#find palindrone 
def palin(word):
   
    if word == '':
        return True
    else:
                    if word[0] == word[len(word)-1]:
                        return palin(word[1:len(word)-1])
                    else:
                        return False                                                             
#fetch the palindrones in the restriction
def get(x,y):
                global count
                count=2
                if x == y+1:
                                return True
                else:
                                if palin(str(x)):
                                    if check(x):
                                                    print(x)
                                    
                                x=x+1
                                get(x,y)


print("The palindromic primes are:")
get(x,y)                                
