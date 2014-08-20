#GWGTHE001
#Thembekani Gwegwana
#
def prime():
    n=eval(input('Enter the starting point N:\n'))
    m=eval(input('Enter the ending point M:\n'))
    m+=1
    print('The palindromic primes are:')
    for i in range(n+1,m-1):
        for j in range(2,i):
            if (i%j==0):
                break
            
                
               
        else :
            if str(i)==str(i)[::-1]:
                print(i)
prime()     
