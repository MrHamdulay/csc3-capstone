#HLNCEC001
#Question4
#Assignment8
#program that uses recursive functions to find all palindromic primes between two integers
import sys
sys.setrecursionlimit (30000)

nv = 0
nv_2 = 0

def palindrom(s, e):
    global nv
    if s!=e:
        if str(s)[::1] == str(s)[::-1]:
            nv = s
            s+=1
            return palindrom(s, e)
        else:
            s+=1    
            return palindrom(s, e)

c = 2
def prime(a,b):
    global nv_2
    global c
    if a<=b:
        if a%c == 0 and a!=c:
            a+=1
            return prime(a,b) 
        elif a%c != 0:
            c+=1
            return prime(a,b)
        elif a%c==0 and a == c:
            nv_2 = a
            #print(a)
            a+=1
            c = 2
            return prime(a,b) and True
        return False


def main():
    s= eval(input('Enter the starting point N:\n'))
    e= eval(input('Enter the ending point M:\n'))    
    if palindrom(s,e) == nv :
        a=s
        b=e
        #print(a)
        if prime(a,b) == nv_2 :
            print(nv_2,"c")
main()