#Taahirah achmat
import math
import sys
sys.setrecursionlimit (30000)

def test(t,r,count):
    
    if t == r+1 :
        return False
    elif t==2 or t==3:
        answer(t)
        return test(t+1,r,2)
    elif t<2:
        return test(t+1,r,2)
    elif t>3:
        #print('',t)
        if t % count !=0:
            if count<=math.sqrt(t):
                return test(t,r,count+1)
            else:
#redo test(t+1,r,2) + palindrome(t) 
                answer(t)
                return test(t+1,r,2)
        
        elif t%count==0:
            return test(t+1,r,2)
    
def answer(val):
    #if type(val)!='string':
    #    val=string(val)
    a=pal(val)
    if a:
        print(val)
    
    
    
def pal(p):
    p=str(p)
    
    if len(p)%2!=0:
        if len(p) == 1:
            return True
        elif p[0] == p[len(p)-1]: 
            return pal(p[1:len(p)-1])
        else:
            return False
    else:
        if len(p) == 0:
            return True
        elif p[0] == p[len(p)-1]: 
            return pal(p[1:len(p)-1])
        else:
            return False

t = eval(input("Enter the starting point N:\n"))        
r = eval(input("Enter the ending point M:\n"))


        
print("The palindromic primes are:")
test(t,r,2)