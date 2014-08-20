import math
import sys
sys.setrecursionlimit (30000)

def pali(num,new_num,answ):
    if (new_num==0):
        if num==answ:
            return True
        else:
            return False
    else:
        length=len(str(new_num))-1
        mod= new_num%10
        div=new_num//10
        return pali(num,div,answ+(mod*(10**length)))

def palindrome(num):
    new_num=num
    div=1
    return pali(num,new_num,0)


def prime_check(num,div):
    if num==0:
        return False
    elif num==1:
        return False
    elif div>=2 and div<= round(math.sqrt(num)):
        if num%div==0:
            return False
        else:
            return prime_check(num,div+1)
    else:
        return True
    
palis=[]   
def palindromic_primes(num,m):
    if not (num> m):
        if palindrome(num)==True and prime_check(num,2)==True:
            palis.append(num)
            return palindromic_primes(num+1,m)
        else:
            return palindromic_primes(num+1,m)
    else:
        return palis
            
      
def printed_list (l):
    if len(l) > 0:
        print (l[0])
        return printed_list (l[1:])
    else:
        return

num=eval(input('Enter the starting point N:\n'))
m=eval(input('Enter the ending point M:\n'))
print("The palindromic primes are:")
palindromic_primes(num,m)
printed_list(palis)