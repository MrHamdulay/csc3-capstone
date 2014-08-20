N=eval(input("Enter the starting point N:\n"))+1
M=eval(input("Enter the ending point M:\n"))-1
print("The palindromic primes are:")
while N<=M:
        y = str(N)
        x = y[::-1]
        if y == x :
                a=N-1
                while a >=2:
                        div=N%a
                        if div == 0 or N==1 : break
                        a-= 1
                else:
                        print(N)
        N+=1
        
                                