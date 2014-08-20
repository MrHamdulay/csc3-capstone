#Saijil Nemchund 
#NMCSAI001
#Question 4 


import math
import sys
sys.setrecursionlimit (30000)



def p(word):
   
    if word == '':  #checking if the data is a palindrome 
        return True
    else:
        if word[0] == word[len(word)-1]:
            
            return p(word[1:len(word)-1])
        else:
            return False
count=2      

def check_prime(n):
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
                                                                                return check_prime(n)
                                                             
def sort(x,y):
                global count
                count=2
                if x == y+1:
                                return True
                else:
                                if p(str(x)):
                                    if check_prime(x):
                                        print(x)
                                    
                                x=x+1
                                sort(x,y) #Finding the primes in the list entered 
                                
                                

x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")

sort(x,y)                                
