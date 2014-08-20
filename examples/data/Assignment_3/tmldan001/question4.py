
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print ('The palindromic primes are:')
for i in range(x+1,y):
        k=str(i)[::-1]
        q=int(k)
        if q==i:
                d=0
                for j in range (1,q+1):
                        if q%j==0:
                                d+=1
                        if d>2:
                                        break
                if d==2:
                                print (q)
                