def pali():
    N = int(input('Enter the starting point N:\n'))
    M = int(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    for i in range(N+1,M):
        N = str(N)
        M = str(M)
        i = str(i)
        a = i[::-1]
        if a == i:
            a = int(a)
            for i in range(2,a):
                if a%i==0:
                    break
            if i == a-1 or a==2:
                #if i==2:
                   # print(i)
                print(a)
pali()    