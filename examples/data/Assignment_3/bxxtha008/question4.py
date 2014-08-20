def Pal_Prime():
    begin_pt=eval(input('Enter the starting point N: \n'))
    endpoint=eval(input('Enter the ending point M: \n'))
    print('The palindromic primes are: ')
    
    for i in range(begin_pt+1, endpoint):
        if(i==2):
            print(i)
        if(i%2!=0):
            x=str(i)
            if (x==x[::-1]):
                y=2
                while (y<i-1):
                    y+=1
                    if i%y==0:
                        break
                else:
                    print(i)

Pal_Prime()