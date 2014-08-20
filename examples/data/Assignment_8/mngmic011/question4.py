"""Assignment 8
Question 4
Micaela Menegaldo"""

import math
import sys
sys.setrecursionlimit(30000)

def checkpalindrome(number,numunchanged,end):
    if int(number)>int(end):
        return False
    if number=="" or len(number)==1:
        div=round(math.sqrt(eval(numunchanged)))
        checkprime(numunchanged,div)
        checkpalindrome(str(int(numunchanged)+1), str(int(numunchanged)+1),end)
    elif number[0]==number[len(number)-1]:
        if len(number)==2:
            div=round(math.sqrt(eval(numunchanged)))
            checkprime(numunchanged,div)
            checkpalindrome(str(int(numunchanged)+1), str(int(numunchanged)+1),end)            
        else:
            checkpalindrome(number[1:len(number)-1],numunchanged,end)
    else:
        checkpalindrome(str(int(numunchanged)+1), str(int(numunchanged)+1),end)
             
def checkprime(number,div):
    if number=="1":
        return False
    if div<2:
        print(number)
    elif eval(number)%int(div)!=0:
        checkprime(number,int(div)-1)
    else:
        return False
    
    

if __name__=='__main__':
    start=input("Enter the starting point N:\n")
    end=input("Enter the ending point M:\n")
    print("The palindromic primes are:")
    checkpalindrome(start,start,end)