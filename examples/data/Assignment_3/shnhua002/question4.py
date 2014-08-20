#Assignment 3 Q4
#Charlie Shang  
#SHNHUA002

N=eval(input("Enter the starting point N: \n"))
M=eval(input("Enter the ending point M: \n"))
test=0
print("The palindromic primes are:")
for i in range(N+1,M):
    x=2
    sNum=str(i)
    check=sNum[len(sNum):0:-1]+sNum[0]
    if sNum==check:
        while x<(i):
            test=i%x
            x+=1
            if test==0: break
        if test!=0:
            print(i)
        if i==2:
            print(i)
            