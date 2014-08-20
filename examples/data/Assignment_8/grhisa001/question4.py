""" Bella Gorham 
palindrome prime checker
06/05/14"""


import sys
sys.setrecursionlimit (30000)

def palindrome(string):
    #check if length too small to use splitting and do these explicitly
    if len(string) == 2 and string[0] == string[1]:
        return True
    if len(string) == 1:
        return True
   #if the beg = end run again testing one less from the front and back
    if string[0] == string[len(string)-1]:
        
        return palindrome(string[1:len(string)-1])
    
    return False

import math
#check if prime
def is_prime(n,div=2):
    # if divsor greater than 2 of number return number because the rest will not be factors therefor no more fctors and prime
    if div> math.sqrt(n): 
        return n
# if no rem ie. has a mutliple return 0
    if n% div == 0:
        return ""
 # add one to divsor       
    else:
        div+=1
# run again    
    return is_prime(n,div) 
        
def list_primes2(start,end):
    
    # check next number
    newstart=start+1
    
    
    listitem = is_prime(start)
    pal = str(listitem)
    
    # since is_prime returns "" for nonprimes we must not print these too and then we have tp check is palindrome 
    
    if listitem != "" and listitem !=1 and palindrome(pal) == True :
        print(listitem)
    # stop when get to end of range
        
    if start == end:
            return     
# run again with next number
    return list_primes2(newstart,end)
    



# function to get inputs and return values
def main():
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    list_primes2(start,end)


main()
    

    



