import sys
sys.setrecursionlimit (30000)

#check if the number is prime and add to a list
def prime(n,m,List):
    if n==1:
        return prime(n+1,m,List)
    elif n==2:
        List.append(n)
        return prime(n+1,m,List)
    elif n == m:
        if primecheck(m,2) ==True and palin(n)==True:
            List.append(m)
        return List
    elif primecheck(n,2) == True and palin(n)==True:
        List.append(n)
        return prime(n+1,m,List)
    else:
        return prime(n+1,m,List)
    

#check if number is palindrominc
def palin(x):
    if str(x) ==reverse(str(x)):
        return True
    else:
        return False
    
#function to reverse the number
def reverse(x):
    if x=='':
        return x
    else:
        return reverse(x[1:])+x[0]

#checks if a number is prime    
def primecheck(n,dev):
    prime= True
    if dev==(n-1):
        if n%dev == 0:
            prime=False
    elif dev==n**0.5:
        if n%dev==0:
            prime=False
    elif n%dev==0:
        prime=False
    elif n%dev!=0:
        return primecheck(n,dev+1)
    else:
        prime=True
    return prime
#prints the list of palindromic primes
def PrintList(x):
    if len(x)==1:
        print(x[0])
    else:
        print(x[0])
        return PrintList(x[1:])
    

#take inputs and run through checks, output a list of palindromic primes
def main():
    
    n=eval(input('Enter the starting point N:\n'))
    m=eval(input('Enter the ending point M:\n'))
    List=[]
    pos=0
    prime(n,m,List)
    print('The palindromic primes are:')
    PrintList(List)

main()

