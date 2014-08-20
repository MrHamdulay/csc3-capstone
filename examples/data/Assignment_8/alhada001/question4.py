import sys
import math
sys.setrecursionlimit(30000)
beginning = input("Enter the starting point N:\n")

def palindrome(k,l,palin):
    k=str(k)
    l=str(l)
    if(k!=""):
        if(k[len(k)-1:] == l[:1]):
            return palindrome(k[:len(k)-1] ,l[1:len(l)],palin)
        else:
            return False
    return True

if(beginning != ""):
    beginning=eval(beginning)
    end=input("Enter the ending point M:\n")
    end=eval(end)
        
    palinp=True

def palinprime(current,end,denom,palinp):
    if(palindrome(current,current,True)):
        if(current == end):
            if(denom < current):
                if(palinp):
                    if(current%denom != 0):
                        denom+=1
                        return palinprime(current,end,denom,palinp)
                    else:
                        palinp = False
                        return palinprime(current,end,2,palinp)
                else:
                    return palinprime(current+1,end,2,True)
                    
            else:
                if(palinp):
                    if(current!=1):
                        print(current)
                        return palinprime(current+1,end,2,palinp)
                else:
                    return palinprime(current+1,end,2,True)
    else: 
        return palinprime(current+1,end,2,True)

print("The palindromic primes are:")
palinprime(beginning,end,2,palinp)
                                          
                