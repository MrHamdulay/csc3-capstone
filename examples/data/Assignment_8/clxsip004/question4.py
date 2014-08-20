import math 

def prime(n,y):
    if y<=math.sqrt(n):
        x=n%y
        if x!=0:
            y=y+1
            prime(n,y)

        else:
            m=0
    else:
        print(n)
def palindrome(num,x):
    numm=int(num)
    xx=int(x)
    if (numm<xx):
        if num[::-1] == num:
           
            prime(numm,2)
           
            numm=numm+1
            num=str(numm)
            palindrome(num,x)
        else:

            numm=numm+1
            num=str(numm)
            palindrome(num,x)
m = int(input("Enter the starting point N:\n"))

n=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

m=str(m)

n=str(n)
palindrome(m,n)
