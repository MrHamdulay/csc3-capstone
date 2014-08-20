#Mbongeni Mazibuko
#MZBMBO002
#Assignment 3

def prime():
    N= eval(input('Enter the starting point N:\n'))
    M= eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    for i in range(N+1,M):
        n=0
        if str(i)[::1]==str(i)[::-1]:
            for j in range(2,i):
                if (i%j)==0:
                    n+= 1
            if n==0:
                print(i)
                
prime()