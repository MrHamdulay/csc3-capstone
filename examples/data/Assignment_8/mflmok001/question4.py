'''a program that uses recursive functions to find all palindromic primes between two integers supplied as input
Mokoena M
10 May '14'''
import question1
import sys
sys.setrecursionlimit (30000)
import math
N=0
M=0
try:
    N=eval(input("Enter the starting point N:\n"))
except:
    print(end="")
try:
    M=eval(input("Enter the ending point M:\n"))
except:
    print(end="")
def Palindrome(Start,End,pal):
    if(Start>End):
        return pal[1::]
    Stri=str(Start)  
    if(question1.Palindrome(Stri,0)=="Palindrome!" and eval(Stri)!=1):
        var=eval(Stri)
        cnt=0
        y=math.sqrt(var)
        re=round(y)
        v=1
        cnt=0
        cnt=question1.alt(re,var,v,cnt)
        if(cnt==1):
                pal=pal+"\n"+str(var)           
        return Palindrome(Start+1,End,pal)
    else:
        return Palindrome(Start+1,End,pal)
if M!=0 or N!=0:  
    print("The palindromic primes are:\n",Palindrome(N,M,""),sep="")
