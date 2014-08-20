
N=eval(input('Enter the starting point N:\n'))
M=eval(input('Enter the ending point M:\n'))
def Prime(N,M):
    for i in range(N+1,M,1):
        num = str(i)
        rev =num[::-1]
        if num == rev:
            factor=0    
            for j in range(2,(i),1):
                if i%j==0:
                    factor+=1
            if factor==0:
                print(i)
                
            




print('The palindromic primes are:')
Prime(N,M)
    