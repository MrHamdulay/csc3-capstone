#Kiuran Naidoo
#Assignment 8
#Question 4
#5 May

import math
import sys
sys.setrecursionlimit(30000)

def palindrome(word): #Check if word is palindrome
    if len(word) < 2: #Base Case. If length is less than two there must be a single letter or none at all
        return True
    elif word[0] == word[-1]: #Check first and last characters are equal
        return palindrome(word[1:-1]) #Call function with string that is truncated 1 character on either side
    else:
        return False
 
def prime(onum,num=2): #Prime checking function
    if onum == 1:#Special case for 1
        return False
    if num > int(math.sqrt(onum)):#Base Case 
        return True
    else:
        if onum%num == 0:#Check divisibility
            return False
        else:
            return prime(onum,num+1)#Recall function

def outputNums(current,end):#Function for output
    if current > end:
        return None
    elif palindrome(str(current)) and prime(current):#Check if prime and palindrome
        print(current)
    return outputNums(current+1,end)
        
startPoint = eval(input("Enter the starting point N:\n"))
endPoint = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
outputNums(startPoint,endPoint)

