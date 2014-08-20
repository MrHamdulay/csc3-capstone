#GLNRUS002
#ASSIGNMENT 8
#QUESTION 4
#Chech palendromic and prime
import sys
sys.setrecursionlimit (30000)
count=0#used for counting through nuymbers

def findprime(f):#main function in program
    global count
    if count<=f:
        singleprime="13579"#used for singlr digitt primes
        
        if(str(count) in singleprime)and len(str(count))==1:# single digit primes
            print(count)
            
        else:
            test=palendrome(str(count))#used to check if palindromic 
            
            if test==True:
                check=prime(count,0)#counts number of divsors
                
                if check==False:
                    print(count)#final cehck of criteria
            
    count+=1#iertares global
    findprime(f)

def palendrome(s):#tests if palendromic
    if len(s) < 2: 
        return True
    if s[0] != s[-1]: 
        return False
    return palendrome(s[1:-1])  
####################################
#count number of divisors

def prime(n,i):
    nums="23456789"
    flag=False
    if i==8:
        return flag
    if n%eval(nums[i])!=0 and n!=eval(nums[i]):
        prime(n,i+1)
    else:
        return True
###################################
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
count=n
findprime(m)